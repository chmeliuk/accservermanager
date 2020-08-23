"""
Django settings for accservermanager project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'material',
    'material.frontend',
    'django_bootstrap_breadcrumbs',
    'django_tables2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cfgs',
    'instances',
    'results',
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

ROOT_URLCONF = 'accservermanager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'accservermanager.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'


LOGIN_REDIRECT_URL = '/cfgs'
LOGOUT_REDIRECT_URL = '/cfgs'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv('DEBUG', 'False').lower() == 'true' else False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY'] \
    if 'SECRET_KEY' in os.environ else None  # create a key with eg 'openssl rand -base64 32', one may also put it directly here

ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS']) \
    if 'ALLOWED_HOSTS' in os.environ else []

ALLOW_SAME_PORTS = True if os.getenv('ALLOW_SAME_PORTS','False').lower() == 'true' else False

try:
    from accservermanager.local_settings import *
except ImportError:
    raise Exception("A local_settings.py file is required to run this project")

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

# list of acc server files that are copied to the instance, make sure they are found
SERVER_FILES = ['accServer.exe','cfg/configuration.json','cfg/settings.json']
for f in SERVER_FILES:
    if not os.path.isfile(os.path.join(ACCSERVER, f)):
        raise Exception('Cannot find required server file: %s.'%f)

# session template used in case no session is present
SESSION_TEMPLATE = {
    "hourOfDay": 14,
    "dayOfWeekend": 2,
    "timeMultiplier": 1,
    "sessionType": "R",
    "sessionDurationMinutes": 10
}


# list of available tracks
TRACKS = [
    ('misano', 'Misano'),
    ('paul_ricard', 'Paul Ricard'),
    ('nurburgring', 'Nurburgring GP'),
    ('hungaroring', 'Hungaroring'),
    ('zolder', 'Zolder'),
    ('monza', 'Monza'),
    ('brands_hatch', 'Brands Hatch'),
    ('barcelona', 'Catalunya (Barcelona)'),
    ('silverstone', 'Silverstone'),
    ('spa', 'Spa-Francorchamps'),
    ('zandvoort', 'Zandvoort'),
]
TRACKS.extend([('%s_2019'%t[0], '%s 2019'%t[1]) for t in TRACKS])
TRACKS.extend([
    ('kyalami_2019', 'Kyalami'),
    ('mount_panorama_2019', 'Mount Panaorama'),
    ('suzuka_2019', 'Suzuka'),
    ('laguna_seca_2019', 'Laguna Seca'),
])

CAR_MODEL_TYPES = (
    (0, 'Porsche 911 (991) GT3 R'),
    (1, 'Mercedes-AMG GT3'),
    (2, 'Ferrari 488 GT3'),
    (3, 'Audi R8 LMS'),
    (4, 'Lamborghini Huracán GT3'),
    (5, 'McLaren 650S GT3'),
    (6, 'Nissan GT-R Nismo GT3 (2018)'),
    (7, 'BMW M6 GT3'),
    (8, 'Bentley Continental GT3 (2018)'),
    (9, 'Porsche 911.2 GT3 Cup'),
    (10, 'Nissan GT-R Nismo GT3 (2017)'),
    (11, 'Bentley Continental GT3 (2016)'),
    (12, 'Aston Martin Racing V12 Vantage GT3'),
    (13, 'Lamborghini Gallardo R-EX'),
    (14, 'Jaguar G3'),
    (15, 'Lexus RC F GT3'),
    (16, 'Lamborghini Huracan Evo (2019)'),
    (17, 'Honda/Acura NSX GT3'),
    (18, 'Lamborghini Huracán Super Trofeo (2015)'),
    (19, 'Audi R8 LMS Evo (2019)'),
    (20, 'AMR V8 Vantage (2019)'),
    (21, 'Honda NSX Evo (2019)'),
    (22, 'McLaren 720S GT3 (Special)'),
    (23, 'Porsche 911 II GT3 R (2019)'),

    (50, 'Alpine A110 GT4'),
    (51, 'Aston Martin Vantage GT4'),
    (52, 'Audi R8 LMS GT4'),
    (53, 'BMW M4 GT4'),
    (55, 'Chevrolet Camaro GT4'),
    (56, 'Ginetta G55 GT4'),
    (57, 'KTM X-Bow GT4'),
    (58, 'Maserati MC GT4'),
    (59, 'McLaren 570S GT4'),
    (60, 'Mercedes AMG GT4'),
    (61, 'Porsche 718 Cayman GT4'),
)

CAR_GROUPS = (
    ("FreeForAll","FreeForAll"),
    ("GT3", "GT3"),
    ("GT4",  "GT4"),
    ("Cup", "Cup"),
    ("ST","ST")
)

SESSION_TYPES = (
    ("P",'Practice'),
    ("Q",'Qualify'),
    ("R",'Race'),
)

EVENT_TYPES = (
    ("E_3h",'Endurance - 3h'),
    ("E_6h",'Endurance - 6h'),
)

DRIVER_CATEGORY = {
    (3, "Platinum"),
    (2, "Gold"),
    (1, "Silver"),
    (0, "Bronze")
}

CUP_CATEGORY = {
    (0, "Overall"),
    (1, "ProAm"),
    (2, "Am"),
    (3, "Silver"),
    (4, "National")
}

MESSAGES = json.load(open(os.path.join(BASE_DIR, 'accservermanager/messages.json'), 'r'))
