
from typing import Dict, Tuple

# -----------------------------
# "Base de dados" em memória
# -----------------------------
# Chave primária: RM (string)
Funcionario = Dict[str, object]
Database = Dict[str, Funcionario]

db_funcionarios: Database = {
    "565191": {"nome": "Gabriel Akira", "departamento": "TI", "id_hub": "HUB001", "consumo_kwh": 120.5},
    "561820": {"nome": "Gustavo Santos", "departamento": "RH", "id_hub": "HUB002", "consumo_kwh": 95.0},
    "556645": {"nome": "Mauro Carlos", "departamento": "Financeiro", "id_hub": "HUB003", "consumo_kwh": 110.0},
}

# -----------------------------
# Utilidades / Validações
# -----------------------------
def limpar_trailing(s: str) -> str:
    return s.strip()

def solicitar_opcao_int(msg: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            valor = int(input(msg).strip())
            if valor < minimo or valor > maximo:
                print(f"⚠️  Digite um número entre {minimo} e {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠️  Entrada inválida. Digite apenas números inteiros.")

def solicitar_float_positivo(msg: str) -> float:
    while True:
        try:
            valor = float(input(msg).replace(",", ".").strip())
            if valor < 0:
                print("⚠️  O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Valor inválido. Use apenas números (ex.: 123.45).")

def solicitar_rm(msg: str) -> str:
    while True:
        rm = limpar_trailing(input(msg))
        if not rm:
            print("⚠️  O RM não pode ser vazio.")
            continue
        return rm

# -----------------------------
# Funções de negócio
# -----------------------------
def exibir_menu() -> None:
    print("\n=== Sistema de Gestão EcoWork ===")
    print("1) Cadastrar novo funcionário")
    print("2) Listar funcionários")
    print("3) Registrar consumo de energia (kWh)")
    print("4) Gerar relatório de consumo")
    print("5) Sair")
    print("=================================")

def cadastrar_funcionario(database: Database) -> None:
    print("\n--- Cadastro de Funcionário ---")
    rm = solicitar_rm("RM (chave única): ")
    if rm in database:
        print("❌ Erro: este RM já está cadastrado.")
        return

    nome = limpar_trailing(input("Nome: "))
    if not nome:
        print("❌ Erro: nome não pode ser vazio.")
        return

    departamento = limpar_trailing(input("Departamento: "))
    if not departamento:
        print("❌ Erro: departamento não pode ser vazio.")
        return

    id_hub = limpar_trailing(input("ID do EcoWork Hub (ex.: HUB123): "))
    if not id_hub:
        print("❌ Erro: ID do Hub não pode ser vazio.")
        return

    database[rm] = {
        "nome": nome,
        "departamento": departamento,
        "id_hub": id_hub,
        "consumo_kwh": 0.0,
    }
    print(f"✅ Funcionário {nome} (RM {rm}) cadastrado com sucesso.")

def listar_funcionarios(database: Database) -> None:
    print("\n--- Lista de Funcionários ---")
    if not database:
        print("Nenhum funcionário cadastrado.")
        return
    for rm, dados in database.items():
        print(f"RM: {rm}")
        print(f"  Nome: {dados['nome']}")
        print(f"  Departamento: {dados['departamento']}")
        print(f"  ID Hub: {dados['id_hub']}")
        print(f"  Consumo acumulado: {dados['consumo_kwh']} kWh")
        print("-" * 28)

def registrar_consumo(database: Database) -> None:
    print("\n--- Registrar Consumo de Energia ---")
    rm = solicitar_rm("RM do funcionário: ")
    if rm not in database:
        print("❌ Erro: RM não encontrado.")
        return
    incremento = solicitar_float_positivo(f"Consumo a adicionar (kWh) para {database[rm]['nome']}: ")
    database[rm]["consumo_kwh"] += incremento
    print(f"✅ Consumo registrado. Total atual: {database[rm]['consumo_kwh']} kWh")

def calcular_totais(database: Database) -> Tuple[float, float, str, float]:
    if not database:
        return (0.0, 0.0, "", 0.0)
    total = sum(d["consumo_kwh"] for d in database.values())
    media = total / len(database)
    campeao_nome = ""
    campeao_valor = -1.0
    for _, d in database.items():
        if d["consumo_kwh"] > campeao_valor:
            campeao_valor = d["consumo_kwh"]
            campeao_nome = d["nome"]
    return (total, media, campeao_nome, campeao_valor)

def gerar_relatorio(database: Database) -> None:
    print("\n--- Relatório de Consumo EcoWork ---")
    if not database:
        print("Não há dados para relatório.")
        return
    total, media, vencedor, maior = calcular_totais(database)
    print(f"Total de funcionários: {len(database)}")
    print(f"Consumo TOTAL: {total:.2f} kWh")
    print(f"Média por funcionário: {media:.2f} kWh")
    print(f"Maior consumo: {vencedor} ({maior:.2f} kWh)")

# -----------------------------
# Ponto de entrada
# -----------------------------
def main() -> None:
    while True:
        exibir_menu()
        opcao = solicitar_opcao_int("Escolha uma opção (1-5): ", 1, 5)

        if opcao == 1:
            cadastrar_funcionario(db_funcionarios)
        elif opcao == 2:
            listar_funcionarios(db_funcionarios)
        elif opcao == 3:
            registrar_consumo(db_funcionarios)
        elif opcao == 4:
            gerar_relatorio(db_funcionarios)
        elif opcao == 5:
            print("👋 Saindo... Obrigado por usar o EcoWork!")
            break

if __name__ == "__main__":
    main()