import csv
import os
import sqlite3

if __name__ == "__main__":
    connection_string = os.path.join(os.getcwd(), "db_cursos.sqlite3")

    connection = sqlite3.connect(connection_string)

    cursor = connection.cursor()

    comando = "DROP TABLE IF EXISTS tb_cursos"
    cursor.execute(comando)

    comando = """
        CREATE TABLE tb_cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL,
            preco REAL NOT NULL
        );
"""
    cursor.execute(comando)

    with open("cursos.csv", mode="r", encoding="utf-8") as arquivo:
        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            comando = "INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES('{}', '{}', '{}')".format(   
                linha.get('curso'),
                int(linha.get('carga_horaria')),
                float(linha.get('preco').replace('.', ','))
            )
            cursor.execute(comando)
        connection.commit()
            
    comando = "DROP TABLE IF EXISTS tb_estatisticas_cursos"
    cursor.execute(comando)

    comando = """
        CREATE TABLE tb_estatisticas_cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            qtd_cursos INTEGER,
            curso_maior_carga_horaria TEXT,
            curso_com_maior_valor TEXT
        );
"""
    cursor.execute(comando)

    comando = "SELECT * FROM tb_cursos"
    result = cursor.execute(comando)

    qtd_cursos = len(result)
    curso_maior_carga_horaria = sorted(result, key=lambda x: x[2], reverse=True)
    
    print(f"Quantidade de cursos: {qtd_cursos}")
    print(f"Curso com a maior carga horária:")
