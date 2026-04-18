import customtkinter as ctk
from tkinter import messagebox
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("500x400")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
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

        self.btnAjouter = ctk.CTkButton(
            self.cadreActions,
            text="Ajouter",
            command=self.ajouter_salle
        )
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(
            self.cadreActions,
            text="Modifier",
            command=self.modifier_salle
        )
        self.btnModifier.grid(row=0, column=1, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(
            self.cadreActions,
            text="Supprimer",
            command=self.supprimer_salle
        )
        self.btnSupprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(
            self.cadreActions,
            text="Rechercher",
            command=self.rechercher_salle
        )
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)

    def ajouter_salle(self):
        code = self.entryCode.get()
        libelle = self.entryLibelle.get()
        type_salle = self.entryType.get()
        capacite = self.entryCapacite.get()

        salle = Salle(code, libelle, type_salle, capacite)

        succes, message = self.service_salle.ajouter_salle(salle)

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def modifier_salle(self):
        code = self.entryCode.get()
        libelle = self.entryLibelle.get()
        type_salle = self.entryType.get()
        capacite = self.entryCapacite.get()

        salle = Salle(code, libelle, type_salle, capacite)

        succes, message = self.service_salle.modifier_salle(salle)

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def supprimer_salle(self):
        code = self.entryCode.get()

        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Succès", "Salle supprimée avec succès")

    def rechercher_salle(self):
        code = self.entryCode.get()

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entryLibelle.delete(0, "end")
            self.entryLibelle.insert(0, salle.libelle)

            self.entryType.delete(0, "end")
            self.entryType.insert(0, salle.type)

            self.entryCapacite.delete(0, "end")
            self.entryCapacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle introuvable")