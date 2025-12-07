# Aplicación de Arquitectura Cliente/Servidor en la Página Web LumiNoche

## Curso: Desarrollo de Aplicaciones para la Web - 202047916
## Etapa 1: Conceptos Previos

---

## 1. ¿Qué es la Arquitectura Cliente/Servidor?

La arquitectura Cliente/Servidor es un modelo de comunicación distribuida donde:
- **Cliente (Frontend):** Solicita servicios y recursos
- **Servidor (Backend):** Procesa solicitudes y proporciona respuestas

---

## 2. Estructura Cliente/Servidor en Nuestra Página Web

### 2.1. Componente CLIENTE (Frontend)

El cliente está compuesto por los archivos que se ejecutan en el navegador del usuario:

#### **HTML5 (`index.html`)**
```html
<!-- Estructura semántica que el navegador renderiza -->
<header>
    <nav class="navbar">
        <!-- Navegación del cliente -->
    </nav>
</header>

<main>
    <section id="productos">
        <!-- Contenido que el usuario ve -->
    </section>
</main>
```

**Responsabilidades del Cliente (HTML):**
- Presentar la interfaz de usuario
- Estructurar el contenido de manera semántica
- Definir formularios para capturar datos del usuario

#### **CSS3 (`css/styles.css`)**
```css
/* Estilos que el navegador aplica al HTML */
.product-card {
    background: rgba(26, 26, 26, 0.8);
    border-radius: 20px;
    /* Estilos visuales del cliente */
}
```

**Responsabilidades del Cliente (CSS):**
- Renderizar estilos visuales
- Crear diseño responsivo
- Aplicar animaciones y efectos

#### **JavaScript (`js/main.js`)**
```javascript
// Código que se ejecuta en el navegador (cliente)
const addCartButtons = document.querySelectorAll('.btn-add-cart');
addCartButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const productCard = this.closest('.product-card');
        const productName = productCard.querySelector('h3').textContent;
        
        // Aquí se implementaría la lógica Cliente/Servidor
        // En una aplicación real, esto enviaría una petición al servidor
        console.log('Producto agregado (simulación Cliente/Servidor):', productName);
    });
});
```

**Responsabilidades del Cliente (JavaScript):**
- Manejar interacciones del usuario
- Validar datos antes de enviarlos
- Enviar peticiones al servidor
- Procesar respuestas del servidor
- Actualizar la interfaz de usuario

---

### 2.2. Componente SERVIDOR (Backend - Simulado)

En nuestra página estática, el servidor está **simulado**, pero en una aplicación real sería:

#### **Servidor Real (Ejemplo con Node.js/Express)**
```javascript
// SERVIDOR (Backend) - No está en nuestro código actual
// Pero así se implementaría:

const express = require('express');
const app = express();

// Endpoint para agregar producto al carrito
app.post('/api/carrito/agregar', (req, res) => {
    const { productId, userId } = req.body;
    
    // Lógica del servidor:
    // 1. Validar datos
    // 2. Consultar base de datos
    // 3. Actualizar inventario
    // 4. Guardar en carrito del usuario
    
    res.json({ success: true, message: 'Producto agregado' });
});

// Endpoint para procesar formulario de contacto
app.post('/api/contacto', (req, res) => {
    const { nombre, email, mensaje } = req.body;
    
    // Lógica del servidor:
    // 1. Validar datos
    // 2. Guardar en base de datos
    // 3. Enviar email de confirmación
    
    res.json({ success: true, message: 'Mensaje enviado' });
});
```

**Responsabilidades del Servidor:**
- Procesar solicitudes del cliente
- Validar y sanitizar datos
- Acceder a bases de datos
- Ejecutar lógica de negocio
- Gestionar seguridad y autenticación
- Generar respuestas para el cliente

---

## 3. Comunicación Cliente/Servidor en Nuestro Código

### 3.1. Ejemplo 1: Agregar Producto al Carrito

#### **En el Cliente (JavaScript actual - Simulado):**
```javascript
// js/main.js - Líneas 82-101
const addCartButtons = document.querySelectorAll('.btn-add-cart');
addCartButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const productCard = this.closest('.product-card');
        const productName = productCard.querySelector('h3').textContent;
        
        // Feedback visual (solo cliente)
        this.textContent = '✓ Agregado';
        this.style.background = '#4caf50';
        
        // SIMULACIÓN: En una app real, aquí se enviaría al servidor:
        // fetch('/api/carrito/agregar', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({ productId: 'classic-001' })
        // })
        
        console.log('Producto agregado (simulación Cliente/Servidor):', productName);
    });
});
```

#### **Cómo sería con Servidor Real:**
```javascript
// CLIENTE - Enviando petición al servidor
button.addEventListener('click', async function(e) {
    e.preventDefault();
    
    // 1. CLIENTE: Prepara los datos
    const productId = this.dataset.productId;
    const userId = getCurrentUserId(); // Función que obtiene el usuario
    
    // 2. CLIENTE: Envía petición HTTP POST al servidor
    try {
        const response = await fetch('/api/carrito/agregar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getAuthToken()}`
            },
            body: JSON.stringify({
                productId: productId,
                userId: userId,
                quantity: 1
            })
        });
        
        // 3. CLIENTE: Recibe respuesta del servidor
        const data = await response.json();
        
        if (data.success) {
            // 4. CLIENTE: Actualiza la interfaz
            this.textContent = '✓ Agregado';
            updateCartCounter(data.cartItems);
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error('Error al comunicarse con el servidor:', error);
    }
});
```

#### **Flujo de Comunicación:**
```
1. Usuario hace clic en "Agregar" 
   ↓
2. CLIENTE (JavaScript) captura el evento
   ↓
3. CLIENTE prepara los datos (productId, userId)
   ↓
4. CLIENTE envía petición HTTP POST al servidor
   ↓
5. SERVIDOR recibe la petición
   ↓
6. SERVIDOR valida los datos
   ↓
7. SERVIDOR consulta base de datos
   ↓
8. SERVIDOR actualiza el carrito
   ↓
9. SERVIDOR envía respuesta JSON al cliente
   ↓
10. CLIENTE recibe la respuesta
   ↓
11. CLIENTE actualiza la interfaz de usuario
```

---

### 3.2. Ejemplo 2: Formulario de Contacto

#### **En el Cliente (HTML):**
```html
<!-- index.html - Líneas 199-207 -->
<form class="contact-form" id="contactForm">
    <input type="text" placeholder="Nombre completo" required>
    <input type="email" placeholder="Correo electrónico" required>
    <textarea placeholder="Mensaje" rows="5" required></textarea>
    <button type="submit" class="submit-btn">Enviar Mensaje</button>
</form>
```

#### **En el Cliente (JavaScript actual - Simulado):**
```javascript
// js/main.js - Líneas 104-134
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // SIMULACIÓN: En una app real, aquí se enviaría al servidor
        const submitBtn = this.querySelector('.submit-btn');
        submitBtn.textContent = 'Enviando...';
        
        // Simular petición al servidor
        setTimeout(() => {
            submitBtn.textContent = '✓ Enviado';
            this.reset();
        }, 1500);
        
        console.log('Formulario enviado (simulación Cliente/Servidor)');
    });
}
```

#### **Cómo sería con Servidor Real:**
```javascript
// CLIENTE - Enviando formulario al servidor
contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // 1. CLIENTE: Obtiene datos del formulario
    const formData = {
        nombre: this.querySelector('input[type="text"]').value,
        email: this.querySelector('input[type="email"]').value,
        mensaje: this.querySelector('textarea').value
    };
    
    // 2. CLIENTE: Valida datos (validación del lado del cliente)
    if (!formData.nombre || !formData.email || !formData.mensaje) {
        alert('Por favor complete todos los campos');
        return;
    }
    
    // 3. CLIENTE: Envía petición HTTP POST al servidor
    const submitBtn = this.querySelector('.submit-btn');
    submitBtn.textContent = 'Enviando...';
    submitBtn.disabled = true;
    
    try {
        const response = await fetch('/api/contacto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        // 4. CLIENTE: Recibe respuesta del servidor
        const data = await response.json();
        
        if (data.success) {
            // 5. CLIENTE: Muestra confirmación
            submitBtn.textContent = '✓ Enviado';
            this.reset();
            showNotification('Mensaje enviado correctamente');
        } else {
            alert(data.message || 'Error al enviar mensaje');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error de conexión con el servidor');
    } finally {
        submitBtn.disabled = false;
    }
});
```

---

## 4. Separación de Responsabilidades

### 4.1. Cliente (Frontend) - ¿Qué hace?

| Responsabilidad | Ejemplo en Nuestro Código |
|----------------|---------------------------|
| **Presentación** | HTML estructura la página, CSS la estiliza |
| **Interacción** | JavaScript maneja clicks, hovers, scrolls |
| **Validación Básica** | Formularios con `required`, validación de email |
| **Feedback Visual** | Animaciones, cambios de estado en botones |
| **Envío de Datos** | Preparar y enviar peticiones HTTP al servidor |
| **Renderizado** | Mostrar datos recibidos del servidor |

### 4.2. Servidor (Backend) - ¿Qué haría?

| Responsabilidad | Ejemplo en Aplicación Real |
|----------------|----------------------------|
| **Procesamiento** | Validar datos, ejecutar lógica de negocio |
| **Base de Datos** | Guardar productos, carritos, mensajes |
| **Seguridad** | Autenticación, autorización, validación |
| **Lógica de Negocio** | Calcular precios, aplicar descuentos |
| **Comunicación Externa** | Enviar emails, conectar con APIs |
| **Respuestas** | Generar JSON/HTML para el cliente |

---

## 5. Protocolo de Comunicación HTTP/HTTPS

### 5.1. Métodos HTTP Utilizados

#### **GET** - Obtener datos
```javascript
// Cliente solicita productos al servidor
fetch('/api/productos')
    .then(response => response.json())
    .then(productos => {
        // Mostrar productos en la página
    });
```

#### **POST** - Enviar datos
```javascript
// Cliente envía formulario al servidor
fetch('/api/contacto', {
    method: 'POST',
    body: JSON.stringify({ nombre, email, mensaje })
});
```

#### **PUT** - Actualizar datos
```javascript
// Cliente actualiza cantidad en carrito
fetch('/api/carrito/actualizar', {
    method: 'PUT',
    body: JSON.stringify({ itemId: 123, quantity: 2 })
});
```

#### **DELETE** - Eliminar datos
```javascript
// Cliente elimina item del carrito
fetch('/api/carrito/eliminar/123', {
    method: 'DELETE'
});
```

---

## 6. Estructura de Archivos y Separación Cliente/Servidor

```
proyecto-web/
│
├── CLIENTE (Frontend) - Se ejecuta en el navegador
│   ├── index.html          → Estructura y contenido
│   ├── css/
│   │   └── styles.css      → Estilos visuales
│   └── js/
│       └── main.js         → Lógica del cliente
│
├── SERVIDOR (Backend) - Se ejecuta en el servidor
│   ├── server.js           → Servidor Node.js/Express
│   ├── routes/
│   │   ├── productos.js    → Rutas de productos
│   │   └── contacto.js     → Rutas de contacto
│   ├── controllers/
│   │   └── carritoController.js
│   └── models/
│       └── Producto.js     → Modelos de base de datos
│
└── Documentacion/
    └── Arquitectura_Cliente_Servidor.md (este archivo)
```

---

## 7. Ventajas de la Arquitectura Cliente/Servidor

### ✅ **Escalabilidad**
- Un servidor puede atender múltiples clientes simultáneamente
- El servidor puede escalarse independientemente del cliente

### ✅ **Separación de Responsabilidades**
- Cliente se enfoca en presentación e interacción
- Servidor se enfoca en lógica de negocio y datos

### ✅ **Seguridad**
- Datos sensibles se procesan en el servidor
- Validación en ambos lados (cliente y servidor)

### ✅ **Mantenibilidad**
- Código organizado y separado
- Fácil de actualizar y modificar

### ✅ **Rendimiento**
- Cliente puede cachear recursos estáticos
- Servidor optimiza consultas a base de datos

---

## 8. Ejemplo Completo: Flujo Cliente/Servidor

### Escenario: Usuario agrega producto al carrito

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENTE (Navegador)                   │
├─────────────────────────────────────────────────────────┤
│ 1. Usuario hace clic en "Agregar"                        │
│ 2. JavaScript captura el evento                         │
│ 3. Prepara datos: { productId: "classic-001" }          │
│ 4. Envía petición HTTP POST                              │
│    POST /api/carrito/agregar                             │
│    Headers: Content-Type: application/json               │
│    Body: { "productId": "classic-001", "quantity": 1 }  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ HTTP Request
                        ↓
┌─────────────────────────────────────────────────────────┐
│                    SERVIDOR (Backend)                    │
├─────────────────────────────────────────────────────────┤
│ 1. Recibe petición HTTP POST                             │
│ 2. Valida datos recibidos                                │
│ 3. Verifica autenticación del usuario                    │
│ 4. Consulta base de datos:                               │
│    - Verifica existencia del producto                    │
│    - Verifica disponibilidad en inventario               │
│ 5. Actualiza carrito del usuario                         │
│ 6. Calcula total del carrito                            │
│ 7. Genera respuesta JSON:                               │
│    {                                                     │
│      "success": true,                                    │
│      "message": "Producto agregado",                     │
│      "cartItems": 3,                                     │
│      "total": 89900                                      │
│    }                                                     │
│ 8. Envía respuesta HTTP 200 OK                          │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ HTTP Response
                        ↓
┌─────────────────────────────────────────────────────────┐
│                    CLIENTE (Navegador)                   │
├─────────────────────────────────────────────────────────┤
│ 1. Recibe respuesta del servidor                        │
│ 2. Parsea JSON recibido                                  │
│ 3. Actualiza interfaz:                                   │
│    - Cambia botón a "✓ Agregado"                         │
│    - Actualiza contador del carrito                      │
│    - Muestra notificación                                │
│ 4. Usuario ve confirmación visual                        │
└─────────────────────────────────────────────────────────┘
```

---

## 9. Resumen

### En Nuestra Página Web Actual:

✅ **Cliente (Frontend) implementado:**
- HTML5 con estructura semántica
- CSS3 con diseño responsivo
- JavaScript con interactividad
- Simulación de comunicación con servidor

⚠️ **Servidor (Backend) simulado:**
- La lógica del servidor está comentada/simulada
- En una aplicación real, se implementaría con Node.js, PHP, Python, etc.

### Para Implementar Servidor Real:

1. **Elegir tecnología:** Node.js, PHP, Python (Django/Flask), etc.
2. **Crear API REST:** Endpoints para productos, carrito, contacto
3. **Base de datos:** MySQL, PostgreSQL, MongoDB, etc.
4. **Actualizar JavaScript:** Cambiar simulaciones por peticiones reales con `fetch()` o `axios`

---

## 10. Referencias en el Código

- **HTML:** `index.html` - Estructura del cliente
- **CSS:** `css/styles.css` - Estilos del cliente
- **JavaScript:** `js/main.js` - Lógica del cliente (líneas 82-134)
- **Documentación:** `Documentacion/Anexo1_ConceptosPrevios.md` - Explicación metodológica

---

**Nota:** Esta arquitectura Cliente/Servidor es la base de todas las aplicaciones web modernas. Aunque nuestra página es estática, la estructura y el código están preparados para integrarse fácilmente con un servidor real.

