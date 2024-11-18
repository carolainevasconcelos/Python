import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Função para conectar ao banco de dados MySQL
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",           # Usuário do MySQL
            password="",           # Sem senha, conforme especificado
            database="LIA"         # Nome do banco de dados
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida.")
            return conexao
    except Error as e:
        print(f"Erro na conexão com o banco de dados: {e}")
        return None

# Carregar e formatar o arquivo CSV
try:
    passagem_df = pd.read_csv('C:/Users/Adriane/Documents/MeusProjetos/py/LIA/2024_Passagem.csv', encoding='ISO-8859-1', sep=';')
    passagem_df['Valor da passagem'] = pd.to_numeric(passagem_df['Valor da passagem'], errors='coerce')
    passagem_df['Taxa de serviço'] = pd.to_numeric(passagem_df['Taxa de serviço'], errors='coerce')
    passagem_df['Data da emissão/compra'] = pd.to_datetime(passagem_df['Data da emissão/compra'], errors='coerce', format='%d/%m/%Y')
    passagem_df['Hora da emissão/compra'] = pd.to_datetime(passagem_df['Hora da emissão/compra'], errors='coerce', format='%H:%M').dt.time
    print("Arquivo CSV carregado e formatado com sucesso.")
    print("Conteúdo do DataFrame:")
    print(passagem_df.head())  # Exibe as primeiras linhas do DataFrame para verificação
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")

# Query para criar a tabela se ela não existir
create_table_query = """
CREATE TABLE IF NOT EXISTS passagens (
    identificador_processo_viagem VARCHAR(255),
    numero_proposta VARCHAR(255),
    meio_transporte VARCHAR(255),
    pais_origem_ida VARCHAR(255),
    uf_origem_ida VARCHAR(255),
    cidade_origem_ida VARCHAR(255),
    pais_destino_ida VARCHAR(255),
    uf_destino_ida VARCHAR(255),
    cidade_destino_ida VARCHAR(255),
    pais_origem_volta VARCHAR(255),
    uf_origem_volta VARCHAR(255),
    cidade_origem_volta VARCHAR(255),
    pais_destino_volta VARCHAR(255),
    uf_destino_volta VARCHAR(255),
    cidade_destino_volta VARCHAR(255),
    valor_passagem DECIMAL(10, 2),
    taxa_servico DECIMAL(10, 2),
    data_emissao_compra DATE,
    hora_emissao_compra TIME
)
"""

# Query para inserir os dados
insert_query = """
INSERT INTO passagens (
    identificador_processo_viagem, numero_proposta, meio_transporte, pais_origem_ida, 
    uf_origem_ida, cidade_origem_ida, pais_destino_ida, uf_destino_ida, cidade_destino_ida,
    pais_origem_volta, uf_origem_volta, cidade_origem_volta, pais_destino_volta, 
    uf_destino_volta, cidade_destino_volta, valor_passagem, taxa_servico, data_emissao_compra, 
    hora_emissao_compra
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Conectar ao banco e executar instruções SQL
conexao = conectar_banco()
if conexao:
    try:
        cursor = conexao.cursor()
        
        # Cria a tabela 'passagens'
        cursor.execute(create_table_query)
        conexao.commit()
        print("Tabela 'passagens' criada ou já existe.")
        
        # Realizar uma inserção de teste
        cursor.execute("CREATE TABLE IF NOT EXISTS teste_conexao (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")
        cursor.execute("INSERT INTO teste_conexao (nome) VALUES ('teste')")
        conexao.commit()
        print("Inserção de teste bem-sucedida.")
        
        # Inserir dados na tabela 'passagens'
        registros_inseridos = 0
        for index, row in passagem_df.iterrows():
            data_to_insert = (
                row['Identificador do processo de viagem'],
                row['Número da Proposta (PCDP)'],
                row['Meio de transporte'],
                row['País - Origem ida'],
                row['UF - Origem ida'],
                row['Cidade - Origem ida'],
                row['País - Destino ida'],
                row['UF - Destino ida'],
                row['Cidade - Destino ida'],
                row['País - Origem volta'],
                row['UF - Origem volta'],
                row['Cidade - Origem volta'],
                row['País - Destino volta'],
                row['UF - Destino volta'],
                row['Cidade - Destino volta'],
                row['Valor da passagem'],
                row['Taxa de serviço'],
                row['Data da emissão/compra'],
                row['Hora da emissão/compra']
            )
            try:
                cursor.execute(insert_query, data_to_insert)
                registros_inseridos += 1
                if registros_inseridos % 10 == 0:  # Confirmar a cada 10 registros
                    conexao.commit()
            except Error as insert_err:
                print(f"Erro ao inserir o registro na linha {index}: {insert_err}")
                print("Dados do registro com erro:", data_to_insert)

        conexao.commit()  # Confirmar qualquer restante
        print(f"{registros_inseridos} registros inseridos com sucesso.")

        # Consultar e exibir os dados do banco de dados
        select_query = "SELECT * FROM passagens"
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        if results:
            print("Dados inseridos:")
            for row in results:
                print(row)
        else:
            print("Nenhum dado encontrado na tabela 'passagens'.")

    except Error as sql_err:
        print(f"Erro no SQL: {sql_err}")

    finally:
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados fechada.")
else:
    print("Falha na conexão.")