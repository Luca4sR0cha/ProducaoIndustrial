# =========================
# CLASSE PRODUTO
# =========================
class CadastrarProduto:
    def __init__(self, codigo, produto, setor, quant, custo):

        # Validações
        if not str(codigo).strip().isdigit():
            raise ValueError("Código inválido")

        if not isinstance(produto, str) or not produto.strip():
            raise ValueError("Produto inválido")

        if not isinstance(setor, str) or not setor.strip():
            raise ValueError("Setor inválido")

        if not str(quant).strip().isdigit():
            raise ValueError("Quantidade inválida")

        try:
            custo_valor = float(custo)
        except (TypeError, ValueError):
            raise ValueError("Custo inválido")

        if custo_valor < 0:
            raise ValueError("Custo inválido")

        # Atributos
        self.codigo = codigo
        self.produto = produto
        self.setor = setor
        self.quant = quant
        self.custo = custo

    def __str__(self):
        return (
            f"{self.codigo:<8}| "
            f"{self.produto.capitalize():<18}| "
            f"{self.setor.capitalize():<14}| "
            f"{self.quant:<11}| "
            f"R$ {float(self.custo):.2f}"
        )


# =========================
# LISTA DE PRODUTOS
# =========================
produtos = []

# Cabeçalho usado nas listagens de produtos
CABECALHO_TABELA = f"{'Código':<8}| {'Produto':<18}| {'Setor':<14}| {'Quantidade':<11}| Custo"


# =========================
# MENU
# =========================
def menuOpcoes():

    opcoes = [
        "Cadastrar produto",
        "Listar produtos",
        "Buscar produto",
        "Registrar produção",
        "Registrar saída",
        "Consultar estoque atual",
        "Encerrar programa"

    ]

    print("\n" + "=" * 50)
    print("SISTEMA DE ESTOQUE".center(50))
    print("=" * 50)

    for i, opcao in enumerate(opcoes):
        print(f"  {i + 1} - {opcao}")

    print("=" * 50)

    escolha = int(input("Escolha uma opção: "))

    print("=" * 50)

    if escolha < 1 or escolha > len(opcoes):
        raise ValueError("Opção inválida")

    return escolha


# =========================
# FUNÇÃO PRINCIPAL
# =========================
def inicio():

    while True:

        opcao = menuOpcoes()

        match opcao:

            # -------------------------
            # 1 - CADASTRAR
            # -------------------------
            case 1:
                try:
                    print("CADASTRAR PRODUTO".center(50))
                    print("-" * 50)
                    codigo = input("Código: ")
                    produto = input("Produto: ")
                    setor = input("Setor: ")
                    quant = input("Quantidade: ")
                    custo = input("Custo: ")

                    produtos.append(CadastrarProduto(codigo, produto, setor, quant, custo))
                    print("-" * 50)
                    print("✔ Produto cadastrado com sucesso!")

                except Exception as erro:
                    print("-" * 50)
                    print("✘ Erro:", erro)

            # -------------------------
            # 2 - LISTAR
            # -------------------------
            case 2:
                print("\n" + "=" * 50)
                print("PRODUTOS CADASTRADOS".center(50))
                print("=" * 50)
                if not produtos:
                    print("Nenhum produto cadastrado.")
                else:
                    print(CABECALHO_TABELA)
                    print("-" * 60)
                    for p in produtos:
                        print(p)
                print("=" * 50)

            # -------------------------
            # 3 - BUSCAR
            # -------------------------
            case 3:
                busca = input("\nCódigo ou nome: ").lower().strip()

                encontrado = False

                print("-" * 50)
                for p in produtos:
                    if str(p.codigo) == busca or p.produto.lower() == busca:
                        if not encontrado:
                            print(CABECALHO_TABELA)
                            print("-" * 60)
                        print(p)
                        encontrado = True

                if not encontrado:
                    print("Produto não encontrado.")
                print("-" * 50)

            # -------------------------
            # 4 - REGISTRAR PRODUÇÃO
            # (aumenta estoque)
            # -------------------------
            case 4:
                print("\n" + "=" * 50)
                print("REGISTRAR PRODUÇÃO".center(50))
                print("=" * 50)
                try:
                    codigo = input("\nCódigo do produto: ").strip()
                    if not codigo.isdigit():
                        raise ValueError("Código inválido")

                    for p in produtos:
                        if str(p.codigo) == codigo:
                            qtd = input("Quantidade produzida: ").strip()
                            if not qtd.isdigit():
                                raise ValueError("Valor de registro inválido")
                            p.quant = str(int(p.quant) + int(qtd))
                            print("✔ Produção registrada!")
                            break
                    else:
                        print("Produto não encontrado.")

                except Exception as erro:
                    print("✘ Erro:", erro)

                print("=" * 50)

            # -------------------------
            # 5 - REGISTRAR SAÍDA
            # (diminuir estoque)
            # -------------------------
            case 5:
                print("\n" + "=" * 50)
                print("REGISTRAR SAÍDA".center(50))
                print("=" * 50)

                try:
                    codigo = input("Código do produto: ").strip()
                    if not codigo.isdigit():
                        raise ValueError("Código inválido")

                    for p in produtos:
                        if str(p.codigo) == codigo:
                            qtd = input("Quantidade de saída: ").strip()
                            if not qtd.isdigit():
                                raise ValueError("Valor de registro inválido")
                            if int(qtd) > int(p.quant):
                                raise ValueError("Quantidade de saída maior que o estoque disponível")
                            p.quant = str(int(p.quant) - int(qtd))
                            print("✔ Saída registrada!")
                            break
                    else:
                        print("Produto não encontrado.")

                except Exception as erro:
                    print("✘ Erro:", erro)

                print("=" * 50)
            # -------------------------
            # 6 - CONSULTAR ESTOQUE
            # -------------------------
            case 6:
                print("\n" + "=" * 50)
                print("ESTOQUE ATUAL".center(50))
                print("=" * 50)
                total = 0

                if not produtos:
                    print("Nenhum produto cadastrado.")
                else:
                    print(CABECALHO_TABELA)
                    print("-" * 60)
                    for p in produtos:
                        print(p)
                        total += int(p.quant)

                print("-" * 50)
                print("Total geral:", total)
                print("=" * 50)

            # -------------------------
            # 7 - ENCERRAR
            # -------------------------
            case 7:
                print("Encerrando programa...")
                break


# =========================
# EXECUÇÃO
# =========================
try:
    inicio()

except Exception as erro:
    print("\n" + "=" * 50)
    print("Erro:", erro)
    print("=" * 50)