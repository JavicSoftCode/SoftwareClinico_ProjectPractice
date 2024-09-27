import os
from pathlib import Path

# pip install python-dotenv
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Definir el entorno actual (desarrollo o producción)
ENVIRONMENT = os.getenv('ENVIRONMENT', '')

VALID_ENVIRONMENT = os.getenv('VALID_ENVIRONMENT', '')  # Asegúrate de que esta variable esté bien definida

# Configuración de DEBUG: Activo solo en desarrollo
DEBUG = ENVIRONMENT == VALID_ENVIRONMENT and os.getenv('DEBUG', 'False').lower() == 'true'

# Configuración de seguridad: Clave secreta
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')

# Hosts permitidos
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # My Apps
  'BackEnd.Apps.core',
  'BackEnd.Apps.Crud_Doctor',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Config_SoftwareClinico.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'FrontEnd/templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'Config_SoftwareClinico.wsgi.application'

# Configuración de la base de datos
# pip install psycopg2-binary conector de base de datos Postgresql
DATABASES = {
  'default': {
    'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
    'NAME': os.getenv('DB_NAME_DATABASE', ''),
    'USER': os.getenv('DB_USERNAME_DATABASE', ''),
    'PASSWORD': os.getenv('DB_PASSWORD_DATABASE', ''),
    'HOST': os.getenv('DB_HOST_DATABASE', ''),
    'PORT': os.getenv('DB_PORT_DATABASE', '5432'),
  }
}

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]

# Configuración de localización
LANGUAGE_CODE = 'ES-EC'  # Cambiar a español de Ecuador
TIME_ZONE = 'America/Guayaquil'  # Zona horaria de Ecuador
USE_I18N = True  # Habilitar internacionalización
USE_TZ = True  # Usar zonas horarias

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'FrontEnd/static')]

# Configuración de archivos de medios
MEDIA_URL = '/public/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
