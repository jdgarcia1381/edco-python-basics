# edco-python-basics
Taller Final: Heladería

## Configuración ambiente desarrollo (Docker)
1. Crear copia de archivo variables de entorno:

```
cp .env.example .env
```

2. Ejecutar con Docker Compose desde la carpeta donde está ubicado el `compose.yaml`:

```
docker compose up --build
```

3. Correr migraciones y crear superuser:
```
docker exec -it heladeria-web-1 bash
python manage.py migrate
python manage.py createsuperuser
```


## Acceder Django Admin
http://localhost:8000/admin