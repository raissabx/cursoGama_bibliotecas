import receitas
import receitas.brasileira
import receitas.italianas
import receitas.asiatias

menu = '''
1. ovo
2. miojo
3. feijoada
4.sushi
5.carbonara
'''
print(menu)
opcao = int(input('Qual prato você quer? '))


if opcao == 1:
    receitas.fritar_ovo()

elif opcao == 2:
    receitas.fazer_miojo()

elif opcao == 3:
    receitas.brasileira.feijoada()

elif opcao == 4:
    receitas.asiatias.sushi()

elif opcao == 5:
    receitas.italianas.carbonara('ovo', 'bacon', 'queijo', 'macarrao')
