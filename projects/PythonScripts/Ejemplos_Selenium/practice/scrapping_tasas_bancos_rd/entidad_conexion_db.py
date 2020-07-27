from Banco import Entidad
import sqlite3


def execute_query(query):
    con = None
    data = None
    try:
        con = sqlite3.connect('tasa_db.db')
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if not data:
            con.commit()
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in _query: %s" % e)
    finally:
        if con:
            con.close()
    return data



def agregar_entidad(entidad):
    query = f"INSERT INTO historical_rates (name, compra, venta, variacion, spread, moneda, ultima_actualizacion) VALUES ('{entidad.name}', '{entidad.compra}', '{entidad.venta}', '{entidad.variacion}', '{entidad.spread}', '{entidad.moneda}', '{entidad.ultima_actualizacion}')"
    execute_query(query)

def buscar_entidad_x_nombre(entidad):
    query = f"select * from historical_rates where name= '{entidad.name}'"
    return execute_query(query)

def buscar_todas_las_entidades():
    query = "select * from historical_rates"
    return execute_query(query)