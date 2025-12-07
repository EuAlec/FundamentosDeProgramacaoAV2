def catalogoDisponivel(biblioteca):
    print(f'''
          ================================================
                      Biblioteca da meia noite      
          ================================================
  ''')

    for livro in biblioteca:    
        print(f"ID:        {livro['id']}")
        print(f"Título:    {livro['titulo']}")
        print(f"Autor:     {livro['autor']}")
        print(f"Descrição: {livro['descricao']}")
        print(f"Preço:     R${livro['preco']:.2f}")
        print('-' * 30)

def livroID(biblioteca, id):
    for livro in biblioteca:
        if livro['id'] == id:
            return livro
    
    return None              

catalogoDeLivros = [
    {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "descricao": "Uma aventura fantástica na Terra Média.", "preco": 49.90},
    {"id": 2, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "descricao": "O clássico mistério de Bentinho e Capitu.", "preco": 39.90},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "descricao": "Uma distopia sobre vigilância e totalitarismo.", "preco": 59.90},
    {"id": 4, "titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "descricao": "A história de Liesel durante a Segunda Guerra.", "preco": 44.90},
    {"id": 5, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "descricao": "Uma fábula poética sobre amizade e amor.", "preco": 29.90}
]

if __name__ == "__main__":
    catalogoDisponivel(catalogoDeLivros)

    while True:
        IdLivro = (input(f'''
                    Busque o livro que deseja, indicando o ID:
                        (ou digite sair para encerrar)
        '''))
        if IdLivro.lower() == 'sair':
            print('\n Programa encerrado. Agradecemos por visitar a Biblioteca da Meia Noite!')
            break

        try:
            IdLivro = int(IdLivro)
            buscarLivro = livroID(catalogoDeLivros, IdLivro)

            if buscarLivro:
                print(f"ID:        {buscarLivro['id']}")
                print(f"Título:    {buscarLivro['titulo']}")
                print(f"Autor:     {buscarLivro['autor']}")
                print(f"Descrição: {buscarLivro['descricao']}")
                print(f"Preço:     R${buscarLivro['preco']:.2f}")
            else:
                print(f"\n❌ Erro: Não existe livro com o ID {IdLivro}.")
        except ValueError:
            print(f'\n ERRO: >>{IdLivro}<< não é um ID válido. Digite um número para buscar ou "sair" para encerrar.')