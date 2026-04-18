import mysql.connector
import json


class DataSalle:

    def get_connection(self):
        with open("Data/config.json", "r") as fichier:
            config = json.load(fichier)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connexion