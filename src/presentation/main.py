from ManagerViewModel import ManagerViewModel
from StudentViewModel import StudentViewModel

#mensagem padrao do sistema
def default_options():
    while True:
        print("Escolha a opcao:\n[1] Listar estudantes.\n[2] Criar estudantes.\n[3] Sair.")
        option = int(input())
        if(option in range(1,4)):
            return option
        print("opcao invalida\n\n")


def main():

    newId = 0 # contador de ids 
    students = [] #armazena estudantes

    while True:
        #obtem opcao
        option = default_options()

        if option == 1:
            #lista usuarios
            for student in students:
               student.print()
        elif option == 2:
            #pega informacoes do estudante
            student = StudentViewModel()
            student.createAccount(newId)
            newId += 1
            #salva estudante
            students.append(student)
        else:
            break

    
main()