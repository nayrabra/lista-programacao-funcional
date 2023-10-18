login_data = {}

arquivo = "login_data.txt"

read_login_data = lambda: dict(line.strip().split(':') for line in open(r"/Users/nayrabraga/Desktop/adsS3/Programação Funcional/av2Python/AV2_NayraBarbosa/login_data.txt"))

save_login_data = lambda data: open(r"/Users/nayrabraga/Desktop/adsS3/Programação Funcional/av2Python/AV2_NayraBarbosa/login_data.txt", "w").writelines([f"{k}:{v}\n" for k, v in data.items()])

login_data = read_login_data()
        
menu = lambda : input("Escolha uma opção\n1 - Login\n2 - Cadastro")

app = lambda option : (
    (lambda : (print("SUCESSO") if (lambda login, senha: login in login_data and login_data[login] == senha)(input("Digite o nome de usuário: "), input("Digite a senha: ")) else print("FRACASSO"))),
(lambda: (login_data.update({input("Digite o nome de usuário: "): input("Digite a senha: ")}), save_login_data(login_data), print("Usuário cadastrado com sucesso!"))))[int(option) - 1]
    
app(menu())()