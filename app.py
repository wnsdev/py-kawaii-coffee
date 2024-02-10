import os
navegar = [{'nome': 'Adicionar ao pedido'}, 
           {'nome': 'Itens Adicionados'}, 
           {'nome': 'Remover do Pedido'}, 
           {'nome': 'Finalizar Pedido'},
           {'nome': 'Sair'}]
pedido = []
itens = [
    { 'nome': 'Omurice Shokugeki no Soma', 'valor': 199.9, 'categoria': 'Comida'},
    { 'nome': 'Parfait de Chocolate Gintama', 'valor': 19.9, 'categoria': 'Bebida'},
    { 'nome': 'Milkshake Neko 259 ml', 'valor': 17.9, 'categoria': 'Sobremesa '},
    { 'nome': 'Milkshake Neko 400 ml', 'valor': 19.9, 'categoria': 'Sobremesa '},
    { 'nome': 'Milkshake Neko 700 ml', 'valor': 23.9, 'categoria': 'Sobremesa '},
    { 'nome': 'Mitarashi Dango Demon Slayer', 'valor': 13.9, 'categoria': 'Sobremesa '},
    { 'nome': 'Love Love Power Coffee', 'valor': 19.9, 'categoria': 'Bebida '},
    { 'nome': 'Matinal Coffee Anteiku', 'valor': 14.9, 'categoria': 'Bebida '},
    { 'nome': 'Aishiteru Cake', 'valor': 14.9, 'categoria': 'Sobremesa '},
]
def exibir_nome_do_app():
    '''Exibe o nome da aplicação'''
    print("""
⣿⡇⣿⣿⣿⠛⠁⣴⣿⡿⠿⠧⠹⠿⠘⣿⣿⣿⡇⢸⡻⣿⣿⣿⣿⣿⣿⣿
⢹⡇⣿⣿⣿⠄⣞⣯⣷⣾⣿⣿⣧⡹⡆⡀⠉⢹⡌⠐⢿⣿⣿⣿⡞⣿⣿⣿
⣾⡇⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣦⡀⠁⢸⡌⠻⣿⣿⣿⡽⣿⣿
⡇⣿⠹⣿⡇⡟⠛⣉⠁⠉⠉⠻⡿⣿⣿⣿⣿⣿⣦⣄⡉⠂⠈⠙⢿⣿⣝⣿
⠤⢿⡄⠹⣧⣷⣸⡇⠄⠄⠲⢰⣌⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⡀⠄⠈⠻⢮    _      __    _        __    _   _     __   __   ___  ___  ___  ___ 
⠄⢸⣧⠄⢘⢻⣿⡇⢀⣀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⢀   | |_/  / /\  \ \    / / /\  | | | |   /  ` /  \ |__  |__  |__  |__  
⠄⠈⣿⡆⢸⣿⣿⣿⣬⣭⣴⣿⣿⣿⣿⣿⣿⣿⣯⠝⠛⠛⠙⢿⡿⠃⠄⢸   |_| \ /_/--\  \_\/\/ /_/--\ |_| |_|   \__, \__/ |    |    |___ |___ 
⠄⠄⢿⣿⡀⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡾⠁⢠⡇⢀
⠄⠄⢸⣿⡇⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣫⣻⡟⢀⠄⣿⣷⣾
⠄⠄⢸⣿⡇⠄⠈⠙⠿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠊⢀⡇⣿⣿
⠒⠤⠄⣿⡇⢀⡲⠄⠄⠈⠙⠻⢿⣿⣿⠿⠿⠟⠛⠋⠁⣰⠇⠄⢸⣿⣿⣿
""")
    
def limpar():
    '''Limpa o terminal'''
    os.system('cls')
    os.system('clear')
    
def desligar():
    '''Encerra a interação com o aplicativo'''
    limpar()
    print('\nAplicativo fechado!\n')
    
def pressione_para_voltar():
    '''Ao pressionar o enter volta ao menu principal
    Inputs:
        - Pressione o botão X
    '''
    input('\nPressione enter para voltar ao menu principal ')
    principal()
    
def opcao_invalida():
    '''Mostra uma mensagem ao selecionar uma opção invalida!'''
    limpar()
    print('\nOpção invalida!')
    pressione_para_voltar()
    
def listar_itens(itens):
    print(f'{"#".ljust(5)} {"Menu".ljust(40)} {"Categoria".ljust(20)} {"Valor(R$)".ljust(20)}')
    for indice, item in enumerate(itens, start=1):
        print(f'{str(indice).ljust(5)} {item["nome"].ljust(40)} {item["categoria"].ljust(20)} {item["valor"]:.2f}')
        
def adicionar_itens():
    try:
        itens_selecionados = input("\nDigite os numeros dos itens que deseja adicionar separando por espaço: ").split(' ')
        print("\n")
        for item in itens_selecionados:
            item = int(item)-1
            item_selecionado = itens[item]
            pedido.append(item_selecionado)
            print(item_selecionado["nome"])
        print(f'\nItens adicionados com sucesso!')
    except:
        principal()
    
def adicionar_ao_pedido():
    '''Essa função é a opção da navegação para montar o pedido
    Input: 
        - item
    Output: 
        - mensagem
    '''
    listar_itens(itens)
    adicionar_itens()
    
def itens_adicionados():
    '''Lista itens adicionados ao pedido'''
    listar_itens(pedido)
        
def remover_do_pedido():
    '''Remove itens do pedido
    Input: 
        - remover_item
    '''
    listar_itens(pedido)
    remover_item = int(input("\nDigite o numero do item que deseja remover? ")) - 1
    
    pedido.remove(pedido[remover_item])
    pressione_para_voltar()
    
        
def finalizar_pedido():
    '''Finaliza o pedido e Imprime os dados para pagamento'''
    listar_itens(pedido)
    valor = sum(item['valor'] for item in pedido)
    print(f'\n{"Total:".ljust(5)} {valor:.2f}')
    
def abrir_navegacao(opcao_selecionada):
    limpar()

    print('.' * (len(opcao_selecionada)))
    print(opcao_selecionada.capitalize())
    print('`' * (len(opcao_selecionada)))
    
    call = globals()[opcao_selecionada.lower().replace(' ', '_')]
    call()
    
    pressione_para_voltar()
    
def navegacao():
    '''Cria navegação da aplicação para a interação do usuario'''
    try:
        for indice, opcao in enumerate(navegar, start=1):
            name = opcao['nome']
            print(f'{indice}. {name}')
       
        opcao = int(input('\nEscolha uma opção: '))
        
        if opcao == len(navegar):
            desligar()
        elif opcao > len(navegar):
            opcao_invalida()
        else:
            abrir_navegacao(navegar[opcao-1]['nome'])
    except: 
        opcao_invalida()
        
def principal():
    limpar()
    exibir_nome_do_app()
    navegacao()
    
if __name__ == '__main__':
    principal()