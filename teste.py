from cyk import Gramatica

gramatica = Gramatica()

palavra1 = "aabb" # Pertence
palavra2 = "baaba" # Não pertence
palavra3 = "acca" # Não pertence


#gramatica.cyk(palavra1)
# gramatica.cyk(palavra2)
# gramatica.cyk(palavra3)
#
gramatica.cyk_passo_a_passo(palavra1)
