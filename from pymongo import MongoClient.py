from pymongo import MongoClient

# Establecer la conexión con MongoDB Atlas
# Asegúrate de reemplazar "<CONNECTION_STRING>" con la cadena de conexión adecuada
client = MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos
db = client["veterinaria_linces"]

# Crear un registro único en la tabla "clientes"
clientes = db["clientes"]
cliente_data = {
    "nombre": "Juan Pérez",
    "telefono": "1234567890",
    "email": "juan@example.com",
    # Agrega otros campos según sea necesario
}
clientes.insert_one(cliente_data)

# Crear un registro único en la tabla "mascotas"
mascotas = db["mascotas"]
mascota_data = {
    "nombre": "Max",
    "especie": "Perro",
    "edad": 3,
    # Agrega otros campos según sea necesario
}
mascotas.insert_one(mascota_data)

# Crear un registro único en la tabla "consultas"
consultas = db["consultas"]
consulta_data = {
    "cliente": "Juan Pérez",
    "mascota": "Max",
    "fecha": "2023-05-30",
    "motivo": "Control de rutina",
    # Agrega otros campos según sea necesario
}
consultas.insert_one(consulta_data)

# Actualizar datos en la tabla "clientes"
clientes.update_one(
    {"nombre": "Juan Pérez"},
    {"$set": {"telefono": "9876543210"}}
)

# Actualizar datos en la tabla "mascotas"
mascotas.update_one(
    {"nombre": "Max"},
    {"$set": {"edad": 4}}
)

# Actualizar datos en la tabla "consultas"
consultas.update_one(
    {"mascota": "Max"},
    {"$set": {"motivo": "Vacunación"}}
)

# Cerrar la conexión con la base de datos
client.close()
