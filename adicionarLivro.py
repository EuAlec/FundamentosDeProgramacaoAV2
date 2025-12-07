def adicionarLivro(carrinho):
    print(f'''
          ==================================================
                      Biblioteca da Meia Noite     

                Adicione livros ao carrinho de compras 
          ==================================================
  ''')

    while True:
        livro = input('Digite o nome do livro ou "sair" para encerrar: ')
        if livro.lower() == 'sair':
            break

        if livro.strip():
            carrinho.append(livro)
            print(f'📘 Livro "<{livro}>" adicionado ao carrinho com sucesso!')

    print(f'''
          ==================================================
                      Biblioteca da Meia Noite     

                  Livros adicionados ao carrinho:
          ==================================================
    ''')

    if len(carrinho) > 0:
        for livro in carrinho:
            print(f'- {livro}')
    else:
        print('Nenhum livro adicionado ao carrinho de compras.')

if __name__ == '__main__':
    carrinhoDeCompras = []
    adicionarLivro(carrinhoDeCompras)

    print(f'''
          ==================================================
           Obrigado por utilizar a Biblioteca da Meia Noite
          ==================================================
  ''') 