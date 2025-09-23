README  # ☕️ Sendero de Café

**Sendero de Café** es un e-commerce desarrollado con **Django + Python** en el backend y **Bootstrap** en el frontend.  
El proyecto busca ofrecer una experiencia minimalista y de alta calidad para la venta de café colombiano.

---

## 📌 Project Title

**Sendero de Café** – Un e-commerce diseñado para ofrecer café de alta calidad proveniente de las mejores fincas de Colombia.  
Está pensado para usuarios que valoran una experiencia de compra intuitiva, rápida y moderna.

---

## 🙌 Acknowledgements

- Construido con **Django + Django REST Framework** para el backend.  
- Uso de **Bootstrap 5** en el frontend.  
- Gracias a la comunidad de **open source** por las librerías y soporte.  

---

## 🔌 API Reference

#### Get all products

http
  GET /api/products

⚙️ Installation

Clona el repositorio y configura el proyecto localmente:

# 1. Clonar el repositorio
git clone https://github.com/LinaR3/E-commerce_Sendero_de_cafe_LinaR3
cd E-commerce_Sendero_de_cafe_LinaR3

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt

# 3. Migrar la base de datos
python manage.py makemigrations
python manage.py migrate

# 4. Ejecutar el servidor
python manage.py runserver
