import mysql.connector
import json
from models.salle import Salle


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

    def insert_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()

    def update_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)

        curseur.execute(requete, valeurs)
        connexion.commit()

        curseur.close()
        connexion.close()

    def delete_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "DELETE FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        connexion.commit()

        curseur.close()
        connexion.close()

    def get_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "SELECT code, libelle, type, capacite FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        resultat = curseur.fetchone()

        curseur.close()
        connexion.close()

        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
        return None

    def get_salles(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()

        requete = "SELECT code, libelle, type, capacite FROM salle"
        curseur.execute(requete)
        resultats = curseur.fetchall()

        curseur.close()
        connexion.close()

        liste_salles = []
        for resultat in resultats:
            salle = Salle(resultat[0], resultat[1], resultat[2], resultat[3])
            liste_salles.append(salle)

        return liste_salles