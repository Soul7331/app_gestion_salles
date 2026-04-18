from Data.dao_salle import DataSalle

dao = DataSalle()

try:
    connexion = dao.get_connection()
    print("Connexion à la base de données réussie")
    connexion.close()
except Exception as e:
    print("Erreur de connexion :", e)