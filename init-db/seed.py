from faker import Faker
import random

fake = Faker()

condominios = "INSERT INTO condominios (nome, endereco) VALUES\n"
moradores = "INSERT INTO moradores (nome, condominio_id, data_registro) VALUES\n"
imoveis = "INSERT INTO imoveis (tipo, condominio_id, valor) VALUES\n"
transacoes = "INSERT INTO transacoes (imovel_id, morador_id, data_transacao, valor_transacao) VALUES\n"

# Gerar 100 registros para condominios
for i in range(1, 101):
    nome = fake.company()
    endereco = fake.address().replace('\n', ', ')
    condominios += f"('{nome}', '{endereco}'),\n"

# Gerar 100 registros para moradores
for i in range(1, 101):
    nome = fake.name()
    condominio_id = random.randint(1, 100)
    data_registro = fake.date_this_decade()
    moradores += f"('{nome}', {condominio_id}, '{data_registro}'),\n"

# Gerar 100 registros para imoveis
for i in range(1, 101):
    tipo = random.choice(['Apartamento', 'Casa'])
    condominio_id = random.randint(1, 100)
    valor = round(random.uniform(100000, 1000000), 2)
    imoveis += f"('{tipo}', {condominio_id}, {valor}),\n"

# Gerar 100 registros para transacoes
for i in range(1, 101):
    imovel_id = random.randint(1, 100)
    morador_id = random.randint(1, 100)
    data_transacao = fake.date_this_year()
    valor_transacao = round(random.uniform(50000, 500000), 2)
    transacoes += f"({imovel_id}, {morador_id}, '{data_transacao}', {valor_transacao}),\n"

# Remover a última vírgula e adicionar ponto e vírgula para finalizar os comandos
condominios = condominios.rstrip(",\n") + ";\n"
moradores = moradores.rstrip(",\n") + ";\n"
imoveis = imoveis.rstrip(",\n") + ";\n"
transacoes = transacoes.rstrip(",\n") + ";\n"

# Imprimir os comandos SQL
print(condominios)
print(moradores)
print(imoveis)
print(transacoes)
