# edco-python-basics

## Configuración ambiente desarrollo

1. Instalar dependencias:

```
python -m pip install -r requirements.txt
```

2. Crear copia de archivo variables de entorno:

```
cp .env.example .env
```

3. Ejecutar con Docker:

```
docker build -t biblioteca_backend .
docker run --name biblioteca_backend -d -p 8000:8000 biblioteca_backend
```

4. Correr migraciones y crear superuser:
```
docker exec -it biblioteca_backend bash
python manage.py migrate
python manage.py createsuperuser
```

4. Acceder al servidor:
http://localhost:8000/admin