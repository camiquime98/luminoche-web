# Guía: Subir a GitHub Pages desde la Consola (PowerShell)

## Curso: Desarrollo de Aplicaciones para la Web - 202047916

---

## Requisitos Previos

### 1. Instalar Git

Si no tienes Git instalado:

1. Descarga desde: https://git-scm.com/download/win
2. Instala Git (siguiente, siguiente, siguiente...)
3. Durante la instalación, deja todas las opciones por defecto

### 2. Verificar que Git está instalado

Abre PowerShell y ejecuta:

```powershell
git --version
```

Si ves algo como `git version 2.40.0` o similar, ¡está instalado! ✅

---

## Paso 1: Crear Cuenta y Repositorio en GitHub

### 1.1. Crear cuenta (si no tienes)

1. Ve a https://github.com
2. Haz clic en **"Sign up"**
3. Completa el formulario
4. Verifica tu email

### 1.2. Crear repositorio en GitHub

1. En GitHub.com, haz clic en **"+"** (arriba derecha) → **"New repository"**
2. Completa:
   - **Repository name:** `luminoche-web`
   - **Description:** "Página web sobre luces estéticas - UNAD"
   - **Visibility:** ✅ Public (necesario para GitHub Pages gratis)
   - ❌ **NO marques** "Add a README file"
   - ❌ **NO marques** "Add .gitignore"
   - ❌ **NO marques** "Choose a license"
3. Haz clic en **"Create repository"**

**IMPORTANTE:** Copia la URL que aparece. Será algo como:
```
https://github.com/TU-USUARIO/luminoche-web.git
```

---

## Paso 2: Configurar Git (Solo la primera vez)

Abre PowerShell y ejecuta (reemplaza con tus datos):

```powershell
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email (el mismo de GitHub)
git config --global user.email "tu-email@ejemplo.com"
```

Ejemplo:
```powershell
git config --global user.name "Juan Pérez"
git config --global user.email "juan.perez@gmail.com"
```

---

## Paso 3: Inicializar Repositorio en tu Carpeta

Abre PowerShell y navega a tu carpeta del proyecto:

```powershell
# Navegar a tu carpeta
cd "C:\Users\decim\Documents\trabajo desarrollo de aplciaciones web"

# Verificar que estás en la carpeta correcta
ls
```

Deberías ver: `index.html`, `css`, `js`, `img`, `Documentacion`

### 3.1. Inicializar Git

```powershell
# Inicializar repositorio Git
git init
```

Verás: `Initialized empty Git repository in ...`

### 3.2. Agregar todos los archivos

```powershell
# Agregar todos los archivos al staging
git add .
```

### 3.3. Hacer el primer commit

```powershell
# Crear el primer commit
git commit -m "Primera versión de la página web LumiNoche"
```

---

## Paso 4: Conectar con GitHub

### 4.1. Agregar el repositorio remoto

Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub:

```powershell
# Agregar repositorio remoto
git remote add origin https://github.com/TU-USUARIO/luminoche-web.git
```

Ejemplo:
```powershell
git remote add origin https://github.com/juanperez/luminoche-web.git
```

### 4.2. Verificar que se agregó correctamente

```powershell
# Verificar repositorio remoto
git remote -v
```

Deberías ver:
```
origin  https://github.com/TU-USUARIO/luminoche-web.git (fetch)
origin  https://github.com/TU-USUARIO/luminoche-web.git (push)
```

### 4.3. Cambiar a rama main

```powershell
# Cambiar nombre de rama a main
git branch -M main
```

---

## Paso 5: Subir Archivos a GitHub

### 5.1. Subir archivos

```powershell
# Subir archivos a GitHub
git push -u origin main
```

### 5.2. Autenticación

Te pedirá credenciales:

**Opción A: Usuario y Contraseña (si tienes contraseña)**
- Username: Tu usuario de GitHub
- Password: Tu contraseña de GitHub

**Opción B: Personal Access Token (Recomendado)**

Si te pide token en lugar de contraseña:

1. Ve a GitHub.com → **Settings** (tu perfil) → **Developer settings**
2. **Personal access tokens** → **Tokens (classic)**
3. **Generate new token (classic)**
4. Nombre: `GitHub Pages`
5. Marca: ✅ `repo` (todos los permisos de repo)
6. **Generate token**
7. **COPIA EL TOKEN** (solo se muestra una vez)
8. Úsalo como contraseña cuando Git lo pida

**Nota:** Si usas Windows, Git puede abrir una ventana de autenticación. Usa tu token ahí.

### 5.3. Verificar que se subió

```powershell
# Verificar estado
git status
```

Debería decir: `Your branch is up to date with 'origin/main'`

---

## Paso 6: Activar GitHub Pages

### 6.1. Desde la Consola (con GitHub CLI)

Si tienes GitHub CLI instalado:

```powershell
# Instalar GitHub CLI (si no lo tienes)
# Descarga desde: https://cli.github.com/

# Autenticarse
gh auth login

# Activar GitHub Pages
gh api repos/TU-USUARIO/luminoche-web/pages -X POST -f source[branch]=main -f source[path]=/
```

### 6.2. Desde el Navegador (Más Fácil)

1. Ve a tu repositorio en GitHub.com:
   ```
   https://github.com/TU-USUARIO/luminoche-web
   ```

2. Haz clic en **"Settings"** (arriba a la derecha)

3. En el menú lateral, busca **"Pages"**

4. En **"Source"**, selecciona:
   - **Branch:** `main`
   - **Folder:** `/ (root)`

5. Haz clic en **"Save"**

6. Espera 1-2 minutos

7. Tu página estará en:
   ```
   https://TU-USUARIO.github.io/luminoche-web/
   ```

---

## Paso 7: Verificar que Funciona

### 7.1. Abrir la página

Abre en tu navegador:
```
https://TU-USUARIO.github.io/luminoche-web/
```

### 7.2. Verificar que todo carga

- ✅ La página se ve correctamente
- ✅ Las imágenes se muestran
- ✅ El CSS funciona
- ✅ El JavaScript funciona

---

## Actualizar la Página Después de Cambios

Cuando hagas cambios en tus archivos:

```powershell
# 1. Ver qué archivos cambiaron
git status

# 2. Agregar los cambios
git add .

# 3. Hacer commit con descripción
git commit -m "Descripción de los cambios"

# 4. Subir cambios a GitHub
git push
```

Ejemplo:
```powershell
git add .
git commit -m "Actualizar precios de productos"
git push
```

GitHub Pages se actualiza automáticamente en 1-2 minutos.

---

## Comandos Útiles de Git

### Ver estado del repositorio
```powershell
git status
```

### Ver historial de commits
```powershell
git log
```

### Ver qué archivos están listos para commit
```powershell
git status
```

### Deshacer cambios en un archivo
```powershell
git checkout -- nombre-archivo.html
```

### Ver diferencias
```powershell
git diff
```

### Ver información del repositorio remoto
```powershell
git remote -v
```

---

## Solución de Problemas

### Error: "fatal: not a git repository"

**Solución:**
```powershell
# Asegúrate de estar en la carpeta correcta
cd "C:\Users\decim\Documents\trabajo desarrollo de aplciaciones web"
git init
```

### Error: "remote origin already exists"

**Solución:**
```powershell
# Eliminar el remoto existente
git remote remove origin

# Agregar de nuevo
git remote add origin https://github.com/TU-USUARIO/luminoche-web.git
```

### Error: "authentication failed"

**Solución:**
1. Usa Personal Access Token en lugar de contraseña
2. O configura SSH (más avanzado)

### Error: "failed to push some refs"

**Solución:**
```powershell
# Si el repositorio en GitHub tiene archivos (como README)
git pull origin main --allow-unrelated-histories

# Luego intenta push de nuevo
git push -u origin main
```

### Las imágenes no se ven en GitHub Pages

**Verifica:**
1. Las rutas son relativas: `img/nombre.jpg` (no absolutas)
2. Los nombres de archivo coinciden exactamente (mayúsculas/minúsculas)
3. Las imágenes están en la carpeta `img/`

---

## Script Completo (Todo en Uno)

Aquí está todo el proceso en un solo bloque (copia y pega, reemplazando TU-USUARIO):

```powershell
# 1. Navegar a la carpeta
cd "C:\Users\decim\Documents\trabajo desarrollo de aplciaciones web"

# 2. Inicializar Git
git init

# 3. Agregar todos los archivos
git add .

# 4. Primer commit
git commit -m "Primera versión de la página web LumiNoche"

# 5. Agregar repositorio remoto (REEMPLAZA TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/luminoche-web.git

# 6. Cambiar a rama main
git branch -M main

# 7. Subir a GitHub
git push -u origin main
```

Después ejecuta estos comandos, ve a GitHub.com y activa Pages manualmente (Settings → Pages).

---

## Resumen de Comandos Esenciales

```powershell
# Configurar Git (solo una vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Inicializar repositorio
git init
git add .
git commit -m "Mensaje descriptivo"

# Conectar con GitHub
git remote add origin https://github.com/TU-USUARIO/luminoche-web.git
git branch -M main
git push -u origin main

# Actualizar después de cambios
git add .
git commit -m "Descripción de cambios"
git push
```

---

## Checklist Final ✅

Antes de subir, verifica:

- [ ] Git está instalado (`git --version`)
- [ ] Estás en la carpeta correcta
- [ ] Todos los archivos están presentes
- [ ] Las rutas en HTML son relativas
- [ ] El repositorio en GitHub está creado y es **Public**
- [ ] GitHub Pages está activado (Settings → Pages)
- [ ] Tu URL funciona: `https://TU-USUARIO.github.io/luminoche-web/`

---

**¡Listo!** Tu página estará en línea usando solo la consola. 🚀

