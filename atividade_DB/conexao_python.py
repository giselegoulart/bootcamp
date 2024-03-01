# Exercício banco de dados bootcamp data analytics womakerscode 2024

import sqlite3
# Criacao de conexao com o banco de dados
conexao = sqlite3.connect('C:/Users/Gisele Tavares/Documents/GitHub/bootcamp/atividade_DB/banco')
cursor = conexao.cursor()
# Insercao de dados de alunos
# 1 e 2
#consulta = 'CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));'
#cursor.execute(consulta)
#consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "joana", 27, "medicina")'
#cursor.execute(consulta)
'''
consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "claudio", 31, "história")'
cursor.execute(consulta)

consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "mariana", 28, "geografia")'
cursor.execute(consulta)

consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "marilia", 30, "medicina")'
cursor.execute(consulta)

consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "marcio", 40, "matematica")'
cursor.execute(consulta)

consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "janete", 33, "engenharia")'
cursor.execute(consulta)

consulta = 'INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "lucia", 39, "engenharia")'
cursor.execute(consulta)
'''
# 3
consulta = 'SELECT * FROM alunos'
visualizar = cursor.execute(consulta)
for aluno in visualizar:
    print(aluno)

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20;')
for aluno in dados:
    print(aluno)

dados = cursor.execute('SELECT * FROM alunos WHERE curso="engenharia" ORDER BY nome ASC;')
for aluno in dados:
    print(aluno)

dados = cursor.execute('SELECT id FROM alunos')
num_alunos = 0
for id_aluno in dados:
    num_alunos+=1

print("Total de alunos:", num_alunos)

# 4
cursor.execute('UPDATE alunos SET idade=45 WHERE id=3')
cursor.execute('DELETE FROM alunos WHERE id=2')
print('Aluno de id=2 deletado.')

# Insercao de dados de clientes
# 5 - Tabela de clientes
'''
consulta = 'CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT, PRIMARY KEY (id));'
cursor.execute(consulta)
consulta = 'INSERT INTO clientes(id, nome, idade, saldo)  VALUES(1, "julia", 21, 2003.65);' 
cursor.execute(consulta)
consulta = 'INSERT INTO clientes(id, nome, idade, saldo)  VALUES(2, "naldo", 40, 55003.65);' 
cursor.execute(consulta)
consulta = 'INSERT INTO clientes(id, nome, idade, saldo)  VALUES(3, "marcia", 26, 7008.65);' 
cursor.execute(consulta)
'''
# 6 -
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30;')
for cliente in dados:
    print(cliente)

dados = cursor.execute('SELECT saldo FROM clientes;')
saldo_total = 0
num_clientes = 0
for sal in dados:
    saldo_total+=sal[0]
    num_clientes+=1

print('Saldo médio: ', saldo_total/num_clientes)

dados = cursor.execute('SELECT nome, MAX(saldo) FROM clientes;')
for d in dados:
    print(d)

dados = cursor.execute('SELECT nome FROM clientes WHERE saldo>1000;')
print('Clientes com saldo>1000:')
for d in dados:
    print(d)

# 7 -
cursor.execute('UPDATE clientes SET saldo=6000 where id=3;')
cursor.execute('DELETE FROM clientes WHERE id=2')
print('Cliente id=2 deletado.')

#Criacao tabela de compras
# 8-
''''''
consulta = '''
CREATE TABLE compras(
id INT,
client_id INT,
produto VARCHAR(100),
valor REAL,
PRIMARY KEY (id),
FOREIGN KEY (client_id) REFERENCES clientes(id)
);
'''
'''
cursor.execute(consulta)
'''
# Insercao de dados de compras

#cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES(1, 3, "camiseta", 30);')
#cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES(2, 1, "jaqueta", 500);')
#cursor.execute('INSERT INTO compras(id, client_id, produto, valor) VALUES(3, 3, "calça", 150);')

# consulta das informacoes dos clientes
consulta = '''
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
INNER JOIN clientes ON compras.client_id=clientes.id;
'''
dados = cursor.execute(consulta)
print('\nCompras dos clientes: ')
for compras_c in dados:
    print(compras_c)

conexao.commit()
conexao.close
