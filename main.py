from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

try:
    connexion = dao.get_connection()
    print("Connexion à la base de données réussie")
    connexion.close()
except Exception as e:
    print("Erreur de connexion :", e)

print("\n--- TEST INSERTION ---")
salle1 = Salle("A101", "Salle reseau", "Laboratoire", 25)
dao.insert_salle(salle1)
print("Salle ajoutée avec succès")

print("\n--- TEST RECHERCHE ---")
salle_trouvee = dao.get_salle("A101")
if salle_trouvee:
    salle_trouvee.afficher_infos()
else:
    print("Salle non trouvée")

print("\n--- TEST MODIFICATION ---")
salle1_modifiee = Salle("A101", "Salle informatique", "Laboratoire", 30)
dao.update_salle(salle1_modifiee)
print("Salle modifiée avec succès")

print("\n--- TEST LISTE DES SALLES ---")
liste = dao.get_salles()
for salle in liste:
    salle.afficher_infos()
    print("----------------------")

print("\n--- TEST SUPPRESSION ---")
dao.delete_salle("A101")
print("Salle supprimée avec succès")

print("\n--- TEST FINAL LISTE DES SALLES ---")
liste = dao.get_salles()
for salle in liste:
    salle.afficher_infos()
    print("----------------------")