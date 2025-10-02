# edco-python-basics

## Configuración ambiente desarrollo (Entorno Virtual)

1. Crear entorno virtual:

```
python -m venv .venv
```

2. Activar entorno virtual:

Linux:
```
source .venv/bin/activate
```

Windows:
```
./venv/Scripts/activate
```

3. Instalar dependencias:

```
python -m pip install -r requirements.txt
```

4. Crear copia de archivo variables de entorno:

```
cp .env.example .env
```

## Configuración ambiente desarrollo (Docker)
1. Crear copia de archivo variables de entorno:

```
cp .env.example .env
```

2. Ejecutar con Docker desde la carpeta donde está ubicado el `Dockerfile`:

```
docker build -t biblioteca_backend .
docker run --name biblioteca_backend_container -d -p 8000:8000 biblioteca_backend
```

3. Correr migraciones y crear superuser:
```
docker exec -it biblioteca_backend_container bash
python manage.py migrate
python manage.py createsuperuser
```


## Acceder Django Admin
http://localhost:8000/admin
