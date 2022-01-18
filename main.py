from Cuenta import Cuenta

usuario = Cuenta("Jonathan","harold307lat@gmail.com",500)
#usuario.hacer_retiro(50)
#usuario.imprimir_estado_cuenta()
usuario.hacer_deposito(50).hacer_retiro(100).imprimir_estado_cuenta()

usuario1 = Cuenta("Isabel","isa25@gmail.com",700)
#usuario1.hacer_retiro(100)
#usuario1.imprimir_estado_cuenta()
usuario1.hacer_deposito(100).hacer_retiro(50).imprimir_estado_cuenta()

usuario1.tranferncia(usuario, 50)