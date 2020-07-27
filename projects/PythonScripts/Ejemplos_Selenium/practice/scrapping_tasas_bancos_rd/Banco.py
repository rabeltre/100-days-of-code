from datetime import datetime, date, time, timedelta

class Entidad:

    def __init__(self, id = 0,  name="", compra="", venta="", variacion="", spread="", moneda = "USD", ultima_actualizacion = datetime.now().strftime("%d-%m-%y %H:%M:%S")):
        self.id = id
        self.name = name
        self.compra = compra
        self.venta = venta
        self.variacion = variacion
        self.spread = spread
        self.moneda = moneda
        self.ultima_actualizacion = ultima_actualizacion