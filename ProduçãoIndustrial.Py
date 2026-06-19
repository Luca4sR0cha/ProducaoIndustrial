# =========================
# CLASSE PRODUTO
# =========================
class CadastrarProduto:
    def __init__(self, codigo, produto, setor, quant, custo):

        # Conversões de tipo
        codigo = int(codigo)
        quant = int(quant)
        custo = float(custo)

        # Validações
        if codigo < 0:
            raise ValueError("Código inválido")

        if not produto.strip():
            raise ValueError("Produto inválido")

        if not setor.strip():
            raise ValueError("Setor inválido")

        if quant < 0:
            raise ValueError("Quantidade inválida")

        if custo < 0:
            raise ValueError("Custo inválido")

        # Atributos
        self.codigo = codigo
        self.produto = produto
        self.setor = setor
        self.quant = quant
        self.custo = custo

    def __str__(self):
        return f"{self.codigo} - {self.produto} - {self.quant} - R${self.custo}"


# =========================
# LISTA DE PRODUTOS
# =========================
produtos = []


# =========================
# MENU
# =========================
def menuOpcoes():

    opcoes = [
        "Cadastrar produto",
        "Listar produtos",
        "Buscar produto",
        "Registrar produção",
        "Consultar estoque atual",
        "Encerrar programa"
    ]

    print(50 * "=")
    print("SISTEMA DE ESTOQUE")
    print(50 * "=")

    for i, opcao in enumerate(opcoes):
        print(i + 1, "-", opcao)

    print(50 * "=")

    escolha = int(input("Escolha uma opção: "))

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
                    codigo = input("Código: ")
                    produto = input("Produto: ")
                    setor = input("Setor: ")
                    quant = input("Quantidade: ")
                    custo = input("Custo: ")

                    produtos.append(CadastrarProduto(codigo, produto, setor, quant, custo))
                    print("Produto cadastrado!")

                except Exception as erro:
                    print("Erro:", erro)

            # -------------------------
            # 2 - LISTAR
            # -------------------------
            case 2:
                print("\n--- PRODUTOS ---")
                for p in produtos:
                    print(p)

            # -------------------------
            # 3 - BUSCAR
            # -------------------------
            case 3:
                busca = input("Código ou nome: ").lower().strip()

                encontrado = False

                for p in produtos:
                    if str(p.codigo) == busca or p.produto.lower() == busca:
                        print(p)
                        encontrado = True

                if not encontrado:
                    print("Produto não encontrado.")

            # -------------------------
            # 4 - REGISTRAR PRODUÇÃO
            # (aumenta estoque)
            # -------------------------
            case 4:
                codigo = input("Código do produto: ")

                for p in produtos:
                    if str(p.codigo) == codigo:
                        qtd = int(input("Quantidade produzida: "))
                        p.quant += qtd
                        print("Produção registrada!")
                        break
                else:
                    print("Produto não encontrado.")

            # -------------------------
            # 5 - CONSULTAR ESTOQUE
            # -------------------------
            case 5:
                print("\n--- ESTOQUE ATUAL ---")
                total = 0

                for p in produtos:
                    print(p)
                    total += p.quant

                print("Total geral:", total)

            # -------------------------
            # 6 - ENCERRAR
            # -------------------------
            case 6:
                print("Encerrando programa...")
                break


# =========================
# EXECUÇÃO
# =========================
try:
    inicio()

except Exception as erro:
    print("Erro:", erro)