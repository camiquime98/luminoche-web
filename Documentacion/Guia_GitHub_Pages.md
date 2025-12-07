# Guía: Cómo Subir la Página Web a GitHub Pages

## Curso: Desarrollo de Aplicaciones para la Web - 202047916

---

## Opción 1: Usando GitHub Desktop (Más Fácil) 🎯

### Paso 1: Instalar GitHub Desktop

1. Descarga GitHub Desktop desde: https://desktop.github.com/
2. Instala la aplicación
3. Inicia sesión con tu cuenta de GitHub (o créala en github.com)

### Paso 2: Crear Repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en el botón **"+"** (arriba a la derecha) → **"New repository"**
3. Completa:
   - **Repository name:** `luminoche-web` (o el nombre que prefieras)
   - **Description:** "Página web sobre luces estéticas - UNAD"
   - **Visibility:** Public (necesario para GitHub Pages gratuito)
   - **NO marques** "Initialize with README"
4. Haz clic en **"Create repository"**

### Paso 3: Conectar Carpeta Local con GitHub

1. Abre GitHub Desktop
2. Haz clic en **"File"** → **"Add Local Repository"**
3. Haz clic en **"Choose..."** y selecciona tu carpeta del proyecto:
   ```
   C:\Users\decim\Documents\trabajo desarrollo de aplciaciones web
   ```
4. Si te pide crear un repositorio, haz clic en **"Create a Repository"**
5. En la ventana que aparece:
   - **Name:** `luminoche-web`
   - **Local path:** Ya debería estar seleccionado
   - Haz clic en **"Create Repository"**

### Paso 4: Subir Archivos a GitHub

1. En GitHub Desktop verás todos tus archivos listos para subir
2. En la parte inferior izquierda, escribe un mensaje:
   ```
   Primera versión de la página web LumiNoche
   ```
3. Haz clic en **"Commit to main"** (botón azul abajo)
4. Haz clic en **"Publish repository"** (botón azul arriba)
5. Asegúrate de que **"Keep this code private"** esté DESMARCADO
6. Haz clic en **"Publish Repository"**

### Paso 5: Activar GitHub Pages

1. Ve a tu repositorio en GitHub.com
2. Haz clic en **"Settings"** (arriba a la derecha)
3. En el menú lateral izquierdo, busca **"Pages"**
4. En **"Source"**, selecciona:
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Haz clic en **"Save"**
6. Espera 1-2 minutos
7. Tu página estará disponible en:
   ```
   https://TU-USUARIO.github.io/luminoche-web/
   ```

---

## Opción 2: Usando Git desde la Terminal (Avanzado) 💻

### Paso 1: Instalar Git

1. Descarga Git desde: https://git-scm.com/download/win
2. Instala Git (siguiente, siguiente, siguiente...)
3. Abre PowerShell o Terminal

### Paso 2: Inicializar Repositorio

Abre PowerShell en tu carpeta del proyecto y ejecuta:

```powershell
# Navegar a tu carpeta (si no estás ahí)
cd "C:\Users\decim\Documents\trabajo desarrollo de aplciaciones web"

# Inicializar repositorio Git
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "Primera versión de la página web LumiNoche"
```

### Paso 3: Crear Repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en **"+"** → **"New repository"**
3. Nombre: `luminoche-web`
4. **NO marques** "Initialize with README"
5. Haz clic en **"Create repository"**

### Paso 4: Conectar y Subir

En PowerShell, ejecuta (reemplaza TU-USUARIO):

```powershell
# Agregar el repositorio remoto
git remote add origin https://github.com/TU-USUARIO/luminoche-web.git

# Cambiar a rama main
git branch -M main

# Subir archivos
git push -u origin main
```

Te pedirá usuario y contraseña de GitHub.

### Paso 5: Activar GitHub Pages

1. Ve a tu repositorio en GitHub.com
2. **Settings** → **Pages**
3. **Source:** `main` → `/ (root)`
4. **Save**
5. Espera 1-2 minutos
6. Tu URL será: `https://TU-USUARIO.github.io/luminoche-web/`

---

## Opción 3: Arrastrar y Soltar (Más Simple) 🚀

### Paso 1: Crear Repositorio en GitHub

1. Ve a https://github.com
2. **"+"** → **"New repository"**
3. Nombre: `luminoche-web`
4. **Marca** "Initialize with README"
5. **Create repository**

### Paso 2: Subir Archivos

1. En tu repositorio, haz clic en **"uploading an existing file"**
2. Arrastra TODA tu carpeta del proyecto (excepto node_modules si existe)
3. Escribe un mensaje: "Primera versión"
4. Haz clic en **"Commit changes"**

### Paso 3: Activar GitHub Pages

1. **Settings** → **Pages**
2. **Source:** `main` → `/ (root)`
3. **Save**
4. Espera y obtén tu URL

---

## Verificar que Todo Funcione ✅

### Checklist antes de subir:

- [ ] Todos los archivos están en la carpeta
- [ ] Las imágenes están en `img/` con nombres correctos
- [ ] `index.html` está en la raíz
- [ ] Las rutas en HTML son relativas (`img/...`, `css/...`, `js/...`)
- [ ] No hay errores en la consola del navegador

### Estructura que debe subirse:

```
luminoche-web/
├── index.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── img/
│   ├── lampara-luminoche-classic.jpg
│   ├── lampara-luminoche-pro.jpg
│   ├── lampara-luminoche-elite.jpg
│   ├── galeria-ambiente-moderno.jpg
│   ├── galeria-estilo-minimalista.jpg
│   ├── galeria-iluminacion-suave.jpg
│   └── galeria-diseno-elegante.jpg
└── Documentacion/
    └── (todos los archivos .md)
```

---

## Actualizar la Página Después de Cambios

### Con GitHub Desktop:
1. Haz tus cambios en los archivos
2. En GitHub Desktop verás los cambios
3. Escribe un mensaje de commit
4. Haz clic en **"Commit to main"**
5. Haz clic en **"Push origin"** (botón azul arriba)
6. GitHub Pages se actualiza automáticamente en 1-2 minutos

### Con Git Terminal:
```powershell
git add .
git commit -m "Descripción de los cambios"
git push
```

---

## Solución de Problemas 🔧

### La página no carga:
- Verifica que el repositorio sea **Public**
- Espera 2-3 minutos después de activar Pages
- Verifica que `index.html` esté en la raíz

### Las imágenes no se ven:
- Verifica que las rutas sean relativas: `img/nombre.jpg`
- No uses rutas absolutas: `C:\Users\...`
- Verifica que los nombres de archivo coincidan exactamente

### Error 404:
- Asegúrate de que el archivo se llame `index.html` (no `Index.html`)
- Verifica que esté en la raíz del repositorio

### La página tarda en actualizarse:
- GitHub Pages puede tardar 1-5 minutos en actualizar
- Haz un "hard refresh": Ctrl + F5

---

## Obtener el Enlace Final

Una vez activado GitHub Pages, tu enlace será:

```
https://TU-USUARIO.github.io/luminoche-web/
```

Reemplaza:
- `TU-USUARIO` → Tu nombre de usuario de GitHub
- `luminoche-web` → El nombre de tu repositorio

Ejemplo:
```
https://juanperez.github.io/luminoche-web/
```

---

## Actualizar el Anexo 1

Una vez tengas el enlace, actualiza:

`Documentacion/Anexo1_ConceptosPrevios.md`

Busca la sección:
```markdown
### Enlace del desarrollo de la página web

**Enlace público:** [COMPLETAR CON EL ENLACE]
```

Y reemplaza con:
```markdown
**Enlace público:** https://TU-USUARIO.github.io/luminoche-web/
```

---

## Alternativas a GitHub Pages

Si prefieres otra opción:

1. **Netlify** (https://netlify.com)
   - Arrastra y suelta tu carpeta
   - URL automática: `tu-proyecto.netlify.app`

2. **Vercel** (https://vercel.com)
   - Similar a Netlify
   - URL automática: `tu-proyecto.vercel.app`

3. **Firebase Hosting** (https://firebase.google.com)
   - Requiere cuenta de Google
   - URL: `tu-proyecto.web.app`

---

## Resumen Rápido 🎯

1. ✅ Crea cuenta en GitHub.com
2. ✅ Crea repositorio nuevo (público)
3. ✅ Sube tus archivos (GitHub Desktop o arrastrar)
4. ✅ Settings → Pages → Activar
5. ✅ Espera 1-2 minutos
6. ✅ Copia tu URL y úsala en el Anexo 1

---

**¡Listo!** Tu página estará en línea y accesible desde cualquier lugar. 🌐

