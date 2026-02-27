from enemigo import *
from zombie import *
from ogro import *

zombie = zombie(10, 1)
ogro = ogro(20, 3) 

print(f"{zombie.get_tipo_enemigo()} tiene {zombie.punto_energia} de energia y puede hacer ataque de {zombie.ataque}")
print(f"{zombie.habla()}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.punto_energia} de energia y puede hacer ataque de {ogro.ataque}")
print(f"{ogro.habla()}")
