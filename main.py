import json
import os

# Nome do arquivo para salvar os dados
ARQUIVO_DADOS = "usuarios.json"

def carregar_usuarios():
    """Carrega usuários do arquivo JSON"""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_usuarios(usuarios):
    """Salva usuários no arquivo JSON"""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)

def menu_principal():
    """Exibe o menu principal"""
    usuarios = carregar_usuarios()
    
    while True:
        print("\n=== SISTEMA DE CADASTRO ===")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por email")
        print("4. Remover usuário")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            buscar_usuario(usuarios)
        elif opcao == "4":
            remover_usuario(usuarios)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def cadastrar_usuario(usuarios):
    """Cadastra um novo usuário"""
    print("\n--- NOVO CADASTRO ---")
    
    nome = input("Nome: ").strip()
    email = input("Email: ").strip().lower()
    idade = input("Idade: ").strip()
    
    # Validação básica
    if not nome or not email or not idade:
        print("Erro: Todos os campos são obrigatórios!")
        return
    
    # Verifica se email já existe
    for usuario in usuarios:
        if usuario['email'] == email:
            print(f"Erro: O email {email} já está cadastrado!")
            return
    
    # Cria novo usuário
    novo_usuario = {
        'nome': nome,
        'email': email,
        'idade': idade
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print(f"✅ Usuário {nome} cadastrado com sucesso!")

def listar_usuarios(usuarios):
    """Lista todos os usuários cadastrados"""
    print("\n--- LISTA DE USUÁRIOS ---")
    
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return
    
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. {usuario['nome']} - {usuario['email']} - {usuario['idade']} anos")

def buscar_usuario(usuarios):
    """Busca usuário por email"""
    print("\n--- BUSCAR USUÁRIO ---")
    
    email_busca = input("Digite o email para buscar: ").strip().lower()
    
    for usuario in usuarios:
        if usuario['email'] == email_busca:
            print(f"\n✅ Usuário encontrado:")
            print(f"   Nome: {usuario['nome']}")
            print(f"   Email: {usuario['email']}")
            print(f"   Idade: {usuario['idade']}")
            return
    
    print(f"❌ Nenhum usuário encontrado com email: {email_busca}")

def remover_usuario(usuarios):
    """Remove usuário por email"""
    print("\n--- REMOVER USUÁRIO ---")
    
    email_remover = input("Digite o email do usuário a remover: ").strip().lower()
    
    for i, usuario in enumerate(usuarios):
        if usuario['email'] == email_remover:
            confirmacao = input(f"Tem certeza que deseja remover {usuario['nome']}? (s/n): ")
            if confirmacao.lower() == 's':
                usuario_removido = usuarios.pop(i)
                salvar_usuarios(usuarios)
                print(f"✅ Usuário {usuario_removido['nome']} removido com sucesso!")
            else:
                print("Operação cancelada.")
            return
    
    print(f"❌ Nenhum usuário encontrado com email: {email_remover}")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()