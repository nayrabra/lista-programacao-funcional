from flask import Flask, request, render_template
app = Flask(__name__, template_folder = 'templates_folder')

login_data = {}

arquivo = "login_data.txt"

read_login_data = lambda: dict(line.strip().split(':') for line in open(arquivo))

save_login_data = lambda data: open(arquivo, "w").writelines([f"{k}:{v}\n" for k, v in data.items()])

login_data = read_login_data()

programa = lambda option : (
    lambda : "SUCESSO" if (lambda login, senha: login in login_data and login_data[login] == senha)(f'{request.form["username"]}', f'{request.form["password"]}') else "FRACASSO",
    lambda: login_data.update({f'{request.form["username"]}': f'{request.form["password"]}'}) or save_login_data(login_data) or "Usuário cadastrado com sucesso!")[int(option) - 1]

reqresp_login = lambda : programa(1)() if request.method == 'POST' else render_template('login.html')
reqresp_cadastro = lambda : programa(2)() if request.method == 'POST' else render_template('cadastro.html')

app.add_url_rule('/login/', 'login', reqresp_login, methods=['GET', 'POST'])
app.add_url_rule('/cadastro/', 'cadastro', reqresp_cadastro, methods=['GET', 'POST'])

app.run(host='0.0.0.0', port=5757)