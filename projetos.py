cadastros = {}
def cadastro_biblioteca():
    matricula = int(input("informe sua matriula para cadastro"))
    senha = int(input("informe sua senha para cadastro"))
    cadastros[matricula] = senha
    
def acesso_biblioteca():
    matricula = int(input("informe sua matricula"))
    senha = int(input("informe sua senha"))
    if matricula in cadastros and cadastros[matricula] == senha:
        print("bem vindo ao sistema")
    else:
        print("senha ou matricula invalidos")
        
while True:       
    print("Bem-vindo ao sistema da biblioteca, informe o que deseja fazer")
    print("1 - realizar cadastro")
    print("2 - acessar o sistema")
    print("3 - sair")
    op = input("informe sua operação")
    if op == '1':
        cadastro_biblioteca()
    elif (op == '2') and (len(cadastros) == 0):
        print("nenhum cadastro feito ainda")
        break
    elif (op == '2'):
        acesso_biblioteca()
   
    elif op == '3':
        break 
    else: 
        print("opção invalida")
