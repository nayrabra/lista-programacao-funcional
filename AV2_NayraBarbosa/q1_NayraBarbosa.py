var = 140

check_account = lambda estado : "check_account" if estado == "start" else "not found"

withdrawal = lambda estado, valor : teste_withdraw(valor) if estado == "check_account" else "not found"

teste_withdraw = lambda valor : "withdraw amount" if var - valor >= 0 else "withdraw not allowed"

deposito = lambda estado : "deposito" if estado == "check_account" else "not found"

update_account_balance = lambda estado, valor: (var - valor) if estado == "withdrawal" else (var + valor) if estado == "deposito" else var

var = update_account_balance(deposito(check_account("start")),360)

print(var)
