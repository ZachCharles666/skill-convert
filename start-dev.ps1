# Skill Converter MVP 启动脚本

Write-Host "Starting Skill Converter MVP..." -ForegroundColor Cyan

# 启动Backend
Write-Host "`nStarting Backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "F:\geo\mygeo\Scripts\Activate.ps1; cd E:\skill-convert\backend; python api/main.py"

# 等待2秒让backend启动
Start-Sleep -Seconds 2

# 启动Frontend
Write-Host "`nStarting Frontend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd E:\skill-convert\frontend; npm run dev"

# 等待3秒让frontend启动
Start-Sleep -Seconds 3

# 打开浏览器
Write-Host "`nOpening browser..." -ForegroundColor Green
Start-Process "http://localhost:3000"

Write-Host "`nMVP is running!" -ForegroundColor Green
Write-Host "   Backend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "   Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "`nPress any key to stop all services..." -ForegroundColor Yellow

$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# 停止所有进程
Get-Process | Where-Object {$_.MainWindowTitle -like "*skill-converter*"} | Stop-Process
Write-Host "`nStopped all services" -ForegroundColor Red
