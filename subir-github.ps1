# Script para subir la página web a GitHub Pages
# Ejecuta este script desde PowerShell en la carpeta del proyecto

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Subir Página Web a GitHub Pages" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que Git está instalado
Write-Host "Verificando Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git no está instalado. Descárgalo desde: https://git-scm.com/download/win" -ForegroundColor Red
    exit
}

Write-Host ""

# Verificar que estamos en la carpeta correcta
Write-Host "Verificando archivos del proyecto..." -ForegroundColor Yellow
if (Test-Path "index.html") {
    Write-Host "✓ index.html encontrado" -ForegroundColor Green
} else {
    Write-Host "✗ No se encontró index.html. Asegúrate de estar en la carpeta correcta." -ForegroundColor Red
    exit
}

Write-Host ""

# Solicitar información del usuario
Write-Host "Necesito algunos datos:" -ForegroundColor Cyan
$githubUser = Read-Host "Tu nombre de usuario de GitHub"
$repoName = Read-Host "Nombre del repositorio (ej: luminoche-web)"

Write-Host ""
Write-Host "¿Es la primera vez que subes este proyecto? (S/N)" -ForegroundColor Yellow
$primeraVez = Read-Host

if ($primeraVez -eq "S" -or $primeraVez -eq "s") {
    Write-Host ""
    Write-Host "Configurando Git (solo primera vez)..." -ForegroundColor Yellow
    
    $userName = Read-Host "Tu nombre completo"
    $userEmail = Read-Host "Tu email de GitHub"
    
    git config --global user.name "$userName"
    git config --global user.email "$userEmail"
    
    Write-Host "✓ Git configurado" -ForegroundColor Green
    Write-Host ""
    
    # Inicializar repositorio
    Write-Host "Inicializando repositorio Git..." -ForegroundColor Yellow
    if (Test-Path ".git") {
        Write-Host "⚠ Repositorio Git ya existe" -ForegroundColor Yellow
    } else {
        git init
        Write-Host "✓ Repositorio inicializado" -ForegroundColor Green
    }
    
    Write-Host ""
    Write-Host "Agregando archivos..." -ForegroundColor Yellow
    git add .
    Write-Host "✓ Archivos agregados" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "Creando primer commit..." -ForegroundColor Yellow
    git commit -m "Primera versión de la página web LumiNoche"
    Write-Host "✓ Commit creado" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "Conectando con GitHub..." -ForegroundColor Yellow
    
    # Verificar si el remoto ya existe
    $remoteExists = git remote -v 2>$null
    if ($remoteExists) {
        Write-Host "⚠ Repositorio remoto ya existe. ¿Deseas reemplazarlo? (S/N)" -ForegroundColor Yellow
        $reemplazar = Read-Host
        if ($reemplazar -eq "S" -or $reemplazar -eq "s") {
            git remote remove origin
            git remote add origin "https://github.com/$githubUser/$repoName.git"
            Write-Host "✓ Repositorio remoto actualizado" -ForegroundColor Green
        }
    } else {
        git remote add origin "https://github.com/$githubUser/$repoName.git"
        Write-Host "✓ Repositorio remoto agregado" -ForegroundColor Green
    }
    
    Write-Host ""
    Write-Host "Cambiando a rama main..." -ForegroundColor Yellow
    git branch -M main
    Write-Host "✓ Rama main configurada" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  Subiendo archivos a GitHub..." -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Te pedirá credenciales:" -ForegroundColor Yellow
    Write-Host "  - Username: $githubUser" -ForegroundColor White
    Write-Host "  - Password: Tu Personal Access Token (no tu contraseña)" -ForegroundColor White
    Write-Host ""
    Write-Host "Si no tienes token, créalo en:" -ForegroundColor Yellow
    Write-Host "  https://github.com/settings/tokens" -ForegroundColor Cyan
    Write-Host ""
    
    $continuar = Read-Host "Presiona Enter para continuar..."
    
    git push -u origin main
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  ¡Archivos subidos!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Ahora activa GitHub Pages:" -ForegroundColor Yellow
    Write-Host "  1. Ve a: https://github.com/$githubUser/$repoName/settings/pages" -ForegroundColor Cyan
    Write-Host "  2. En 'Source', selecciona: Branch 'main' → Folder '/' (root)" -ForegroundColor White
    Write-Host "  3. Haz clic en 'Save'" -ForegroundColor White
    Write-Host "  4. Espera 1-2 minutos" -ForegroundColor White
    Write-Host ""
    Write-Host "Tu página estará en:" -ForegroundColor Green
    Write-Host "  https://$githubUser.github.io/$repoName/" -ForegroundColor Cyan
    Write-Host ""
    
} else {
    Write-Host ""
    Write-Host "Actualizando repositorio existente..." -ForegroundColor Yellow
    
    Write-Host ""
    Write-Host "Verificando cambios..." -ForegroundColor Yellow
    git status
    
    Write-Host ""
    Write-Host "Agregando cambios..." -ForegroundColor Yellow
    git add .
    
    Write-Host ""
    $commitMessage = Read-Host "Mensaje del commit (ej: Actualizar precios)"
    git commit -m "$commitMessage"
    
    Write-Host ""
    Write-Host "Subiendo cambios..." -ForegroundColor Yellow
    git push
    
    Write-Host ""
    Write-Host "✓ Cambios subidos exitosamente" -ForegroundColor Green
    Write-Host ""
    Write-Host "Tu página se actualizará automáticamente en 1-2 minutos" -ForegroundColor Yellow
    Write-Host "URL: https://$githubUser.github.io/$repoName/" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

