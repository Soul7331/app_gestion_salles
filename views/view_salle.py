import customtkinter as ctk
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("500x400")

        self.service_salle = ServiceSalle()


        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.labelCode = ctk.CTkLabel(self.cadreInfo, text="Code :")
        self.labelCode.grid(row=0, column=0, padx=10, pady=10)
        self.entryCode = ctk.CTkEntry(self.cadreInfo)
        self.entryCode.grid(row=0, column=1, padx=10, pady=10)

        self.labelLibelle = ctk.CTkLabel(self.cadreInfo, text="Libellé :")
        self.labelLibelle.grid(row=1, column=0, padx=10, pady=10)
        self.entryLibelle = ctk.CTkEntry(self.cadreInfo)
        self.entryLibelle.grid(row=1, column=1, padx=10, pady=10)

        self.labelType = ctk.CTkLabel(self.cadreInfo, text="Type :")
        self.labelType.grid(row=2, column=0, padx=10, pady=10)
        self.entryType = ctk.CTkEntry(self.cadreInfo)
        self.entryType.grid(row=2, column=1, padx=10, pady=10)

        self.labelCapacite = ctk.CTkLabel(self.cadreInfo, text="Capacité :")
        self.labelCapacite.grid(row=3, column=0, padx=10, pady=10)
        self.entryCapacite = ctk.CTkEntry(self.cadreInfo)
        self.entryCapacite.grid(row=3, column=1, padx=10, pady=10)

        # Cadre Actions
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")

        self.btnAjouter = ctk.CTkButton(self.cadreActions, text="Ajouter")
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(self.cadreActions, text="Modifier")
        self.btnModifier.grid(row=0, column=1, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(self.cadreActions, text="Supprimer")
        self.btnSupprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(self.cadreActions, text="Rechercher")
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)