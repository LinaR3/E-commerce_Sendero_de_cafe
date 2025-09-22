# E-commerce Sendero de Café

**Sendero de Café** es un e-commerce completo construido con Django para la venta de café premium colombiano. El proyecto integra una arquitectura backend robusta pensada para escalabilidad y futuras APIs REST, enfatizando buenas prácticas de desarrollo y un flujo de compra claro y eficiente.

![Homepage Screenshot](https://github.com/user-attachments/assets/0bc98295-04a0-4894-9d93-52f44e934a12)

## 🚀 Características Principales

### ✨ Funcionalidades del E-commerce
- **Catálogo de Productos**: Sistema completo de productos con categorías, filtros y búsqueda
- **Carrito de Compras**: Funcionalidad completa de carrito con sesiones
- **Sistema de Usuarios**: Registro, autenticación y perfiles de usuario
- **Gestión de Pedidos**: Sistema completo de órdenes y seguimiento
- **Panel de Administración**: Interface administrativa completa para gestionar productos, categorías y pedidos
- **API REST**: Endpoints API listos para integración con aplicaciones móviles o frontend separado

### 🎨 Diseño y UX
- **Responsive Design**: Completamente adaptable a dispositivos móviles y desktop
- **Tema Coffee**: Diseño personalizado con paleta de colores café
- **Bootstrap 5**: Interface moderna y profesional
- **Font Awesome**: Iconografía consistente y atractiva

### 🛠 Tecnologías Utilizadas
- **Backend**: Django 4.2.7
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción recomendada)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **API**: Django REST Framework
- **Formularios**: Django Crispy Forms con Bootstrap 5
- **Imágenes**: Pillow para procesamiento de imágenes
- **Pagos**: Estructura preparada para Stripe (configurable)

## 📦 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/LinaR3/E-commerce_Sendero_de_cafe.git
cd E-commerce_Sendero_de_cafe
```

2. **Crear y activar un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Aplicar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Cargar datos de ejemplo (opcional)**
```bash
python manage.py load_sample_data
```

8. **Iniciar el servidor de desarrollo**
```bash
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000`

## 🗂 Estructura del Proyecto

```
E-commerce_Sendero_de_cafe/
├── sendero_cafe/           # Configuración principal del proyecto
│   ├── settings.py         # Configuraciones de Django
│   ├── urls.py            # URLs principales
│   └── ...
├── products/              # App de productos
│   ├── models.py          # Modelos de productos y categorías
│   ├── views.py           # Vistas del catálogo
│   ├── admin.py           # Configuración del admin
│   └── ...
├── cart/                  # App del carrito de compras
│   ├── cart.py            # Lógica del carrito
│   ├── views.py           # Vistas del carrito
│   └── ...
├── orders/                # App de pedidos
│   ├── models.py          # Modelos de órdenes
│   ├── views.py           # Vistas de pedidos
│   └── ...
├── accounts/              # App de cuentas de usuario
│   ├── models.py          # Perfiles de usuario
│   ├── views.py           # Autenticación y perfiles
│   └── ...
├── templates/             # Plantillas HTML
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── media/                 # Archivos de medios subidos
└── requirements.txt       # Dependencias del proyecto
```

## 🎯 Funcionalidades Principales

### 1. Gestión de Productos
- **Categorías**: Sistema de categorización jerárquica
- **Productos**: Información detallada con imágenes, precios, stock
- **Filtros**: Por categoría, precio, tipo de café, nivel de tueste
- **Búsqueda**: Búsqueda de texto completo en nombre, descripción y origen

### 2. Carrito de Compras
- **Sesiones**: Persistencia del carrito sin necesidad de registro
- **Actualización**: Modificar cantidades en tiempo real
- **Cálculos**: Totales automáticos con IVA y envío

### 3. Sistema de Usuarios
- **Registro**: Formulario completo de registro
- **Autenticación**: Login/logout seguro
- **Perfiles**: Información personal y direcciones
- **Historial**: Visualización de pedidos anteriores

### 4. Gestión de Pedidos
- **Checkout**: Proceso de compra simplificado
- **Estados**: Seguimiento de estado del pedido
- **Confirmaciones**: Emails de confirmación y actualizaciones

### 5. Panel de Administración
- **Dashboard**: Interface intuitiva para administradores
- **CRUD Completo**: Gestión de productos, categorías, pedidos y usuarios
- **Reportes**: Estadísticas de ventas y productos

## 🔧 Configuración Avanzada

### Variables de Entorno (.env)
```env
DEBUG=True
SECRET_KEY=tu-secret-key-aqui
ALLOWED_HOSTS=localhost,127.0.0.1
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

### Base de Datos en Producción
Para usar PostgreSQL en producción:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sendero_cafe_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🌐 API REST

La aplicación incluye endpoints API REST para:

- **Productos**: `GET /api/products/`
- **Categorías**: `GET /api/categories/`
- **Filtros**: Soporte para filtrado y paginación
- **Búsqueda**: Endpoints de búsqueda avanzada

Ejemplo de uso:
```bash
curl http://localhost:8000/api/products/?category=arabica-premium
```

## 🧪 Testing

Ejecutar las pruebas:
```bash
python manage.py test
```

## 📱 Responsive Design

La aplicación está optimizada para:
- **Desktop**: Experiencia completa con todas las funcionalidades
- **Tablet**: Layout adaptado para pantallas medianas
- **Mobile**: Interface táctil optimizada para móviles

## 🎨 Personalización

### Colores del Tema
```css
:root {
    --coffee-primary: #8B4513;
    --coffee-secondary: #D2691E;
    --coffee-accent: #A0522D;
}
```

### Agregar Nuevas Categorías de Producto
1. Acceder al admin en `/admin/`
2. Ir a **Products > Categories**
3. Agregar nueva categoría con slug único

## 🔒 Seguridad

- **CSRF Protection**: Protección contra ataques CSRF
- **XSS Prevention**: Escape automático de contenido
- **SQL Injection**: ORM de Django previene inyecciones SQL
- **User Authentication**: Sistema robusto de autenticación
- **File Upload**: Validación segura de archivos subidos

## 🚀 Despliegue en Producción

### Checklist de Producción
- [ ] Configurar `DEBUG=False`
- [ ] Usar base de datos robusta (PostgreSQL)
- [ ] Configurar servidor web (Nginx + Gunicorn)
- [ ] Configurar archivos estáticos
- [ ] Configurar SSL/HTTPS
- [ ] Configurar email backend
- [ ] Configurar monitoreo y logs

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📞 Soporte

Para soporte técnico o preguntas:
- **Issues**: Crear un issue en GitHub
- **Email**: contacto@senderodecafe.com
- **Documentación**: Ver la wiki del proyecto

## 🙏 Agradecimientos

- **Django Community**: Por el excelente framework
- **Bootstrap Team**: Por el framework CSS
- **Font Awesome**: Por los iconos
- **Unsplash**: Por las imágenes de muestra

---

**Sendero de Café** - Llevando el mejor café colombiano desde las montañas hasta tu taza ☕
