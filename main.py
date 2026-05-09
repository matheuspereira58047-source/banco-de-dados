import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("""create table if not exists contas_bancarias (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Titular TEXT NOT NULL,
               Saldo FLOAT NOT NULL,
               Cpf TEXT NOT NULL
               
               
               )""")

cursor.execute("""INSERT INTO  contas_bancarias (
              Titular, Saldo, Cpf)values 
               ('joao', -1000 , 10000000000)""")

cursor.execute("""SELECT * FROM contas_bancarias""")
contas = cursor.fetchall()
print(contas)
for contas in contas:
    id, nome, saldo, cpf = contas
    print( f'id: {id}, nome: {nome}, saldo: {saldo}, cpf: {cpf}')
conexao.commit()