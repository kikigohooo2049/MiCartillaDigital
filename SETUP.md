##Guia de instalação
Requisitos. 
-Python 3.8 ou superior
-Git

abran una terminal bash.
y ejecuten esto 
git clone https://github.com/kikigohooo2049/MiCartillaDigital.git
cd MiCartillaDigital
 
 de ahi

cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno 
en terminal 

venv\Scripts\activate

pip install -r requirements.txt

# Preparar BD
python manage.py migrate
python manage.py createsuperuser

# Listo
python manage.py runserver
# Si subes cambios de código
git pull

# Si subes nuevas librerías (cambios en requirements.txt)
pip install -r requirements.txt

# Si hay cambios en modelos
python manage.py migrate