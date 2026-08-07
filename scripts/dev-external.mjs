import { spawn } from "node:child_process";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { getLanAddresses } from "./network-access-help.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const port = Number(process.env.VITE_DEV_PORT || 5173);
const tunnelFile = path.join(root, ".dev-tunnel-url");
const viteBin = path.join(root, "node_modules", "vite", "bin", "vite.js");

const children = [];

function cleanup() {
  for (const child of children) {
    child.kill("SIGTERM");
  }
  try {
    fs.unlinkSync(tunnelFile);
  } catch {
    // ignore
  }
  process.exit(0);
}

process.on("SIGINT", cleanup);
process.on("SIGTERM", cleanup);

function waitForServer(targetPort, attempts = 40) {
  return new Promise((resolve, reject) => {
    let tries = 0;

    const tick = () => {
      const req = http.get(`http://127.0.0.1:${targetPort}/`, (res) => {
        res.resume();
        resolve();
      });

      req.on("error", () => {
        tries += 1;
        if (tries >= attempts) {
          reject(new Error(`Servidor local não respondeu na porta ${targetPort}.`));
          return;
        }
        setTimeout(tick, 500);
      });
    };

    tick();
  });
}

function printBanner({ tunnelUrl }) {
  const ips = getLanAddresses();

  console.log("\n  ═══ MundialCard — base de testes (acesso externo) ═══\n");
  console.log("  PC (este computador):");
  console.log(`     http://localhost:${port}/\n`);

  console.log("  Celular/tablet (mesma Wi-Fi):");
  if (ips.length === 0) {
    console.log(`     http://SEU-IP-LOCAL:${port}/`);
  } else {
    for (const ip of ips) {
      console.log(`     http://${ip}:${port}/`);
    }
  }

  if (tunnelUrl) {
    console.log("\n  Internet (qualquer rede — base de testes):");
    console.log(`     ${tunnelUrl}`);
    console.log(`     ${tunnelUrl}#/consulta-digital`);
  }

  console.log("\n  Mantenha este terminal aberto enquanto testa.\n");
}

function startVite() {
  const child = spawn(
    process.execPath,
    [viteBin, "--host", "0.0.0.0", "--port", String(port), "--strictPort"],
    {
      cwd: root,
      env: {
        ...process.env,
        VITE_DEV_HTTPS: "0",
        VITE_DEV_TUNNEL: "1",
        VITE_DEV_STRICT_PORT: "1",
      },
      stdio: "inherit",
      shell: false,
    }
  );

  children.push(child);
  return child;
}

function startTunnel() {
  return new Promise((resolve, reject) => {
    const child = spawn(
      process.platform === "win32" ? "npx.cmd" : "npx",
      ["--yes", "cloudflared", "tunnel", "--url", `http://127.0.0.1:${port}`, "--no-autoupdate"],
      {
        cwd: root,
        env: process.env,
        stdio: ["ignore", "pipe", "pipe"],
        shell: false,
      }
    );

    children.push(child);

    let tunnelUrl = "";
    const handleOutput = (chunk) => {
      const text = chunk.toString();
      process.stderr.write(text);

      const match = text.match(/https:\/\/[a-z0-9-]+\.trycloudflare\.com/);
      if (!match || tunnelUrl) return;

      tunnelUrl = match[0];
      fs.writeFileSync(tunnelFile, tunnelUrl, "utf8");
      printBanner({ tunnelUrl });
      resolve(tunnelUrl);
    };

    child.stdout.on("data", handleOutput);
    child.stderr.on("data", handleOutput);

    child.on("exit", (code) => {
      if (!tunnelUrl) {
        reject(new Error(`Túnel encerrou antes de gerar URL (código ${code ?? "?"})`));
      }
    });
  });
}

async function ensureFirewall() {
  const script = path.join(root, "scripts", "allow-firewall.ps1");
  await new Promise((resolve) => {
    const child = spawn(
      "powershell",
      ["-ExecutionPolicy", "Bypass", "-File", script],
      { cwd: root, stdio: "inherit", shell: false }
    );
    child.on("exit", () => resolve());
  });
}

console.log("\n  Preparando base de testes com acesso externo...\n");
await ensureFirewall();

startVite();

try {
  await waitForServer(port);
  await startTunnel();
} catch (error) {
  console.error(`\n  Erro: ${error.message}\n`);
  cleanup();
}
