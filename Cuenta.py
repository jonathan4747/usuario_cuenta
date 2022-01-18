class Cuenta:
    def __init__(self, nombre="N/A",email="N/A",cuenta=0):
        self.nombre= nombre
        self.email = email
        self.cuenta=cuenta
    
    def hacer_retiro(self, monto):
        self.cuenta = self.cuenta - monto
        return self.cuenta
    def imprimir_estado_cuenta(self):
        print(self.nombre, str(self.cuenta))
        
    def tranferncia (self, usuario ,monto):
        self.cuenta = self.cuenta-monto
        usuario.cuenta = usuario.cuenta+monto
        print(usuario.nombre,str(usuario.cuenta))
        print(self.nombre,str(self.cuenta))
        
        
        
