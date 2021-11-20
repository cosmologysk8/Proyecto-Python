import mysql.connector as SkateTablas
import proyecto

def conectar_bbdd():

    conexion = SkateTablas.connect(host='localhost', port='3306', user='root', password='adrian123', database='TablasSkate', autocommit=True)

    return conexion


def consulta_skates():
    #Crear conexion
    conexion = conectar_bbdd()

    #Crear un cursor
    cursor = conexion.cursor()

    #Realizamos un script de consulta
    sql_script = 'SELECT * from TablasSkate'

    #Ejecutamos el Script del cursor
    cursor.execute(sql_script)

def insertar_tablas_bbdd():

    list_skates = proyecto.cargar_tablas()

    conexion = conectar_bbdd()

    cursor = conexion.cursor()

    sql_script = " insert into TablasSkate(url_imagen, nombre, marca, precio_original) "

    for tablas in list_skates:
        values = [SkateTablas["url_image"],SkateTablas["nombre"],SkateTablas["marca"],SkateTablas["precio_original"],SkateTablas['precio_rebajado'],SkateTablas['ahorro_porciento'],SkateTablas['precio_original_rebajado']]
        cursor.execute(sql_script,values)

    print("Se han cargado todas las tablas con exito")

def borrar_datos_tablas():
    conexion = conectar_bbdd()
    cursor = conexion.cursor()
    delete_script = "delete from TablasSkate where id is not null"
    cursor.execute(delete_script)


insertar_tablas_bbdd()