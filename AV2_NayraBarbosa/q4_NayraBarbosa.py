import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nay.4349"
)

cursor = mydb.cursor()

execsqlcmd = lambda comando, cursor: cursor.execute(comando)

execusedatabase = lambda dbname, cursor: execsqlcmd("USE " + dbname + ";\n", cursor)
execcreatetable = lambda table, attrs, cursor: execsqlcmd("CREATE TABLE " + table + " (" + attrs + ");\n", cursor)
execinsertinto = lambda table, attrs, values, cursor: execsqlcmd("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ")" + ";\n", cursor)
execselectfrom = lambda attrs, table, cursor: execsqlcmd("SELECT " + attrs + " FROM " + table + ";\n", cursor)
execdroptable = lambda table, cursor: execsqlcmd("DROP TABLE " + table + ";\n", cursor)
execdropdatabase = lambda dbname, cursor: execsqlcmd("DROP DATABASE " + dbname + ";\n", cursor)

execsqlcmd("CREATE DATABASE IF NOT EXISTS mydatabase2;", cursor)

execusedatabase("mydatabase2", cursor)

execcreatetable("usuarios", "id INT, nome VARCHAR(255), console VARCHAR(255)", cursor)
execcreatetable("jogos", "id INT, nome VARCHAR(255), data_lancamento DATE", cursor)

execinsertinto("usuarios", "id, nome, console", "1, 'Nayra', 'console1'", cursor)
execinsertinto("jogos", "id, nome, data_lancamento", "2, 'Candy crush', '2012-04-12'", cursor)

execselectfrom("*", "usuarios", cursor)
result_usuarios = cursor.fetchall()

execselectfrom("*", "jogos", cursor)
result_jogos = cursor.fetchall()

for row in result_usuarios:
    print(row)

for row in result_jogos:
    print(row)

execdroptable("usuarios", cursor)
execdroptable("jogos", cursor)

execdropdatabase("mydatabase2", cursor)

mydb.commit()
mydb.close()
