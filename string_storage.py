# menu strings

prompt = "> "

menu_string = """Bem vindo ao sistema da Universidade. O que deseja acessar?
            [a] Dados dos Estudantes
            [b] Dados das Diciplinas
            [c] Dados dos Professores
            [d] Dados das Turmas
            [e] Dados das Matrículas
            [f] Sair do sistema
            """

data_menu_string = """O que você deseja fazer?
            [a] Inserir
            [b] Listar
            [c] Excluir
            [d] Alterar
            [e] Voltar ao menu principal"""

incorrect_option = "Opção Inválida. Por favor, selecione uma das opções abaixo\n"

confirmation_exit = """Tem certeza de que deseja sair?
            [a] Sim
            [b] Não, retornar ao menu"""


# json manipulation strings

blank_data = """
[
    
        
    
]

"""

estudante_object_blank = """
{
    "codigo": "",
    "nome": "",
    "cpf": "",
    "idade": "",
    "curso": "",
    "telefone": "",
    "e-mail": ""
}
"""

disciplina_object_blank = """
{
    "codigo": "",
    "nome": ""
}
"""

matricula_object_blank = """
{
    "codigo": "",
    "aluno": ""
}
"""

professor_object_blank = """
{
    "codigo": "",
    "nome": "",
    "cpf": "",
    "idade": "",
    "disciplina": "",
    "telefone": "",
    "e-mail": ""
}
"""

turma_object_blank = """
{
    "codigo": "",
    "professor": "",
    "disciplina": "",
    "alunos": ""
}
"""
