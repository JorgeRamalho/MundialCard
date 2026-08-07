# Execute como Administrador no PowerShell:
#   Set-ExecutionPolicy -Scope Process Bypass; .\scripts\allow-firewall.ps1

$ports = @(5173, 5174, 5500)

foreach ($port in $ports) {
  $name = "MundialCard Dev Port $port"
  $existing = Get-NetFirewallRule -DisplayName $name -ErrorAction SilentlyContinue
  if ($existing) {
    Write-Host "Regra já existe: $name"
    continue
  }
  try {
    New-NetFirewallRule -DisplayName $name -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port -ErrorAction Stop | Out-Null
    Write-Host "Firewall liberado: porta $port"
  } catch {
    Write-Host "Não foi possível liberar a porta $port (execute o PowerShell como Administrador)."
  }
}

Write-Host "`nPronto. Reinicie npm run dev:network e acesse pelo IP exibido no terminal."
