class studentPresentation():
    def getCreateData():
        print("Digite seu nome:")
        name = input()
        print("Digite sua idade:")
        age = int(input())
        print("Digite sua senha: (deve conter)")
        password = input()
        return name, age, password
    
    def selectStudent():
        print("Digite o nome:")
        name = input()
        return name
    
    def UpdateStudent(selection):
        if(selection == 1):
            print("Atualize o nome")
            name = input()
            return name
        elif(selection == 2):
            print("Atualize a idade")
            age = input()
            return age
        elif(selection == 3):
            print("Atualize a senha")
            password = input()
            return password