import sqlite3

#coneccion

conexion = sqlite3.connect('pruebas.db')

#crar cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion text,
    precio int(255)
);
""")


#guardar cambios
conexion.commit()

"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto','Descripción de mi producto', 550)")
conexion.commit()
"""

"""
#Borrar registros

cursor.execute("DELETE FROM productos")
conexion.commit()
"""
#insertar muchos registros de golpe
productos=[
    ("Telefono", "LG", 700),
    ("Ordenador portatil", "MSI", 140),
    ("Placa Base", "ASUS", 80),
    ("Tablet", "NOGA", 300),
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)",productos)
conexion.commit()

#Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#listar datos
cursor.execute("SELECT * FROM productos WHERE precio > 100")
conexion.commit()
productos = cursor.fetchall()

for producto in productos:
    print(producto)


cursor.execute("SELECT id FROM productos")
producto = cursor.fetchone()
print(producto)




#Cerrar conexión
conexion.close()
