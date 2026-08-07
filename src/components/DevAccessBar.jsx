import { useMemo, useState } from "react";

function buildLinks() {
  const dev = window.__MUNDIALCARD_DEV_ACCESS__;
  const origin = window.location.origin;
  const hashPath = window.location.hash || "#/";
  const current = `${origin}${hashPath === "#" ? "" : hashPath}`;

  const links = [
    { label: "Este dispositivo", url: current },
    { label: "localhost", url: `http://localhost:5173/` },
    { label: "127.0.0.1", url: `http://127.0.0.1:5173/` },
  ];

  const ips = dev?.ips?.length ? dev.ips : [];
  const httpPort = dev?.httpPort ?? 5173;
  const httpsPort = dev?.httpsPort ?? 5174;

  for (const ip of ips) {
    links.push({ label: `Rede HTTP · ${ip}`, url: `http://${ip}:${httpPort}/` });
    links.push({
      label: `Rede HTTPS · ${ip} (câmera)`,
      url: `https://${ip}:${httpsPort}/#/consulta-digital`,
    });
  }

  if (dev?.externalUrl) {
    links.unshift({ label: "Internet (base de testes)", url: dev.externalUrl });
  }

  return [...new Map(links.map((item) => [item.url, item])).values()];
}

export default function DevAccessBar() {
  const [open, setOpen] = useState(false);
  const links = useMemo(() => buildLinks(), []);

  if (!import.meta.env.DEV) return null;

  return (
    <div className={`dev-access-bar${open ? " is-open" : ""}`}>
      <button
        type="button"
        className="dev-access-bar__toggle"
        onClick={() => setOpen((value) => !value)}
        aria-expanded={open}
      >
        🧪 Base de testes · localhost / rede / HTTPS
      </button>

      {open ? (
        <div className="dev-access-bar__panel">
          <p>
            Use <strong>HTTP</strong> para testar o site no celular. Use <strong>HTTPS (porta 5174)</strong>{" "}
            para a câmera do Dr. Digital. Para link na internet: <code>npm run dev:external</code>.
          </p>
          <ul className="dev-access-bar__links">
            {links.map((item) => (
              <li key={item.url}>
                <span>{item.label}</span>
                <a href={item.url} target="_blank" rel="noopener noreferrer">
                  {item.url}
                </a>
              </li>
            ))}
          </ul>
          <p className="dev-access-bar__hint">
            No PC: <code>npm run dev:test</code> sobe HTTP (5173) + HTTPS (5174) juntos.
          </p>
        </div>
      ) : null}
    </div>
  );
}
