from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

print("\n--- TEST AJOUT VIA SERVICE ---")
salle1 = Salle("B201", "Salle multimedia", "Laboratoire", 20)
succes, message = service.ajouter_salle(salle1)
print(message)

print("\n--- TEST AJOUT INVALIDE ---")
salle_invalide = Salle("B202", "Petite salle", "Bureau", 0)
succes, message = service.ajouter_salle(salle_invalide)
print(message)

print("\n--- TEST RECHERCHE VIA SERVICE ---")
salle_trouvee = service.rechercher_salle("B201")
if salle_trouvee:
    salle_trouvee.afficher_infos()
else:
    print("Salle non trouvée")

print("\n--- TEST MODIFICATION VIA SERVICE ---")
salle_modifiee = Salle("B201", "Salle multimedia avancee", "Laboratoire", 35)
succes, message = service.modifier_salle(salle_modifiee)
print(message)

print("\n--- TEST LISTE VIA SERVICE ---")
liste = service.recuperer_salles()
for salle in liste:
    salle.afficher_infos()
    print("----------------------")

print("\n--- TEST SUPPRESSION VIA SERVICE ---")
service.supprimer_salle("B201")
print("Salle supprimée avec succès")

print("\n--- TEST FINAL LISTE VIA SERVICE ---")
liste = service.recuperer_salles()
for salle in liste:
    salle.afficher_infos()
    print("----------------------")