import json
import os
import sqlite3

if __name__ == "__main__":
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    connection = sqlite3.connect(connection_string)

    cursor = connection.cursor()

    comando = "DROP TABLE IF EXISTS tb_estados"
    cursor.execute(comando)

    comando = """
CREATE TABLE tb_estados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla TEXT NOT NULL
);
"""
    cursor.execute(comando)

    with open("estados.json", mode="r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)

    estados = data.get("UF")

    for estado in estados:
        comando = "INSERT INTO tb_estados(nome, sigla) VALUES('{}', '{}');".format(
            estado.get("nome"), estado.get("sigla")
        )
        cursor.execute(comando)
    connection.commit()

    comando = "SELECT * FROM tb_estados;"
    result = cursor.execute(comando)

    print(result.fetchone())

    print(result.fetchmany(10))
    
    print(result.fetchall())

    comando = "DELETE FROM tb_estados WHERE sigla IN ('SP', 'RJ', 'RS');"
    cursor.execute(comando)
    connection.commit()

    dados = [
        ("São Paulo", "SP",),
        ("Rio de Janeiro", "RJ",),
        ("Rio Grande do Sul", "RS",)
    ]

    comando = "INSERT INTO tb_estados(nome, sigla) VALUES (?, ?);"
    cursor.executemany(comando, dados)
    connection.commit()

    connection.close()