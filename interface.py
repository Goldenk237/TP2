import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime

class FormulaireInscription:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Inscriptions - CRUD")
        self.root.geometry("1400x750")

        # Couleurs du thème moderne
        self.bg_main = "#f5f7fa"
        self.bg_card = "#ffffff"
        self.primary = "#4A90E2"
        self.success = "#2ecc71"
        self.warning = "#f39c12"
        self.danger = "#e74c3c"
        self.secondary = "#95a5a6"
        self.text_dark = "#2c3e50"
        self.text_light = "#7f8c8d"

        self.root.configure(bg=self.bg_main)

        # Initialiser la connexion MySQL
        self.init_database()
        self.selected_id = None

        # Créer l'interface
        self.create_widgets()
        self.charger_donnees()

    def init_database(self):
        """Initialise la connexion à la base de données"""
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="inscription"
            )
            self.cursor = self.conn.cursor()

            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS utilisateurs
                                (
                                    id
                                    INT
                                    AUTO_INCREMENT
                                    PRIMARY
                                    KEY,
                                    nom
                                    VARCHAR
                                (
                                    100
                                ),
                                    prenom VARCHAR
                                (
                                    100
                                ),
                                    anniversaire DATE,
                                    sexe VARCHAR
                                (
                                    10
                                ),
                                    contact VARCHAR
                                (
                                    100
                                ),
                                    mot_de_passe VARCHAR
                                (
                                    255
                                ),
                                    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )
                                """)
            self.conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur de connexion",
                                 f"Impossible de se connecter à MySQL:\n{err}\n\n"
                                 "Assurez-vous que MySQL est démarré.")

    def create_widgets(self):
        """Crée l'interface moderne"""

        # En-tête principal
        header = tk.Frame(self.root, bg=self.primary, height=80)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)

        title_label = tk.Label(header, text="🎯 GESTION DES INSCRIPTIONS",
                               font=("Segoe UI", 24, "bold"),
                               bg=self.primary, fg="white")
        title_label.pack(expand=True)

        # Conteneur principal
        container = tk.Frame(self.root, bg=self.bg_main)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # ========== PARTIE GAUCHE : FORMULAIRE ==========
        left_frame = tk.Frame(container, bg=self.bg_card, relief="flat", bd=0)
        left_frame.pack(side="left", fill="both", padx=(0, 10), ipadx=30, ipady=30)

        # Ajouter une ombre subtile avec un frame
        shadow_frame = tk.Frame(left_frame, bg="#e0e0e0")
        shadow_frame.place(x=2, y=2, relwidth=1, relheight=1)
        shadow_frame.lower()

        # En-tête du formulaire
        form_header = tk.Frame(left_frame, bg=self.primary, height=60)
        form_header.pack(fill="x", padx=0, pady=(0, 25))
        form_header.pack_propagate(False)

        tk.Label(form_header, text="📝 Formulaire d'Inscription",
                 font=("Segoe UI", 16, "bold"),
                 bg=self.primary, fg="white").pack(expand=True)

        # Frame pour les champs
        form_frame = tk.Frame(left_frame, bg=self.bg_card)
        form_frame.pack(fill="both", expand=True, padx=20)

        # Nom
        self.create_modern_field(form_frame, "👤 Nom", 0)
        self.nom_entry = self.create_modern_entry(form_frame, 0)

        # Prénom
        self.create_modern_field(form_frame, "👤 Prénom", 1)
        self.prenom_entry = self.create_modern_entry(form_frame, 1)

        # Anniversaire
        self.create_modern_field(form_frame, "🎂 Anniversaire", 2)
        self.date_entry = DateEntry(form_frame, font=("Segoe UI", 11), width=27,
                                    background=self.primary, foreground='white',
                                    borderwidth=2, date_pattern='dd/mm/yyyy',
                                    relief="flat")
        self.date_entry.grid(row=2, column=1, pady=12, sticky="w", padx=5)

        # Sexe
        self.create_modern_field(form_frame, "⚧ Sexe", 3)
        self.sexe_var = tk.StringVar(value="Homme")
        sexe_frame = tk.Frame(form_frame, bg=self.bg_card)
        sexe_frame.grid(row=3, column=1, pady=12, sticky="w", padx=5)

        rb_homme = tk.Radiobutton(sexe_frame, text="Homme", variable=self.sexe_var,
                                  value="Homme", font=("Segoe UI", 10),
                                  bg=self.bg_card, fg=self.text_dark,
                                  selectcolor=self.bg_card, cursor="hand2")
        rb_homme.pack(side="left", padx=(0, 15))

        rb_femme = tk.Radiobutton(sexe_frame, text="Femme", variable=self.sexe_var,
                                  value="Femme", font=("Segoe UI", 10),
                                  bg=self.bg_card, fg=self.text_dark,
                                  selectcolor=self.bg_card, cursor="hand2")
        rb_femme.pack(side="left")

        # Contact
        self.create_modern_field(form_frame, "📱 Contact", 4)
        self.contact_entry = self.create_modern_entry(form_frame, 4)

        # Mot de passe
        self.create_modern_field(form_frame, "🔒 Mot de passe", 5)
        self.password_entry = self.create_modern_entry(form_frame, 5, show="●")

        # Boutons CRUD
        button_frame = tk.Frame(left_frame, bg=self.bg_card)
        button_frame.pack(pady=25, padx=20)

        # Bouton Ajouter
        self.create_modern_button(button_frame, "✚ Ajouter", self.ajouter,
                                  self.success, 0, 0)

        # Bouton Modifier
        self.create_modern_button(button_frame, "✎ Modifier", self.modifier,
                                  self.warning, 0, 1)

        # Bouton Supprimer
        self.create_modern_button(button_frame, "🗑 Supprimer", self.supprimer,
                                  self.danger, 1, 0)

        # Bouton Désélectionner
        self.create_modern_button(button_frame, "↺ Réinitialiser", self.deselectionner,
                                  self.secondary, 1, 1)

        # ========== PARTIE DROITE : TABLEAU ==========
        right_frame = tk.Frame(container, bg=self.bg_card, relief="flat", bd=0)
        right_frame.pack(side="right", fill="both", expand=True, ipadx=20, ipady=20)

        # En-tête du tableau
        table_header = tk.Frame(right_frame, bg=self.primary, height=60)
        table_header.pack(fill="x", padx=0, pady=(0, 20))
        table_header.pack_propagate(False)

        tk.Label(table_header, text="📊 Liste des Utilisateurs",
                 font=("Segoe UI", 16, "bold"),
                 bg=self.primary, fg="white").pack(expand=True)

        # Frame pour le tableau
        table_frame = tk.Frame(right_frame, bg=self.bg_card)
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # Style du Treeview
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Custom.Treeview",
                        background=self.bg_card,
                        foreground=self.text_dark,
                        rowheight=35,
                        fieldbackground=self.bg_card,
                        font=("Segoe UI", 10),
                        borderwidth=0)

        style.configure("Custom.Treeview.Heading",
                        background=self.primary,
                        foreground="white",
                        font=("Segoe UI", 11, "bold"),
                        borderwidth=0)

        style.map("Custom.Treeview",
                  background=[("selected", self.primary)],
                  foreground=[("selected", "white")])

        # Treeview
        self.tree = ttk.Treeview(table_frame,
                                 columns=("ID", "Nom", "Prénom", "Anniversaire", "Sexe", "Contact"),
                                 show="headings",
                                 style="Custom.Treeview",
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set,
                                 height=18)

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        # Colonnes
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prénom", text="Prénom")
        self.tree.heading("Anniversaire", text="Anniversaire")
        self.tree.heading("Sexe", text="Sexe")
        self.tree.heading("Contact", text="Contact")

        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Nom", width=140)
        self.tree.column("Prénom", width=140)
        self.tree.column("Anniversaire", width=120, anchor="center")
        self.tree.column("Sexe", width=90, anchor="center")
        self.tree.column("Contact", width=160)

        self.tree.pack(fill="both", expand=True)

        # Alternance de couleurs pour les lignes
        self.tree.tag_configure("oddrow", background="#f8f9fa")
        self.tree.tag_configure("evenrow", background="white")

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def create_modern_field(self, parent, text, row):
        """Crée un label moderne"""
        label = tk.Label(parent, text=text, font=("Segoe UI", 11, "bold"),
                         bg=self.bg_card, fg=self.text_dark, anchor="w")
        label.grid(row=row, column=0, sticky="w", pady=12, padx=(5, 15))

    def create_modern_entry(self, parent, row, show=None):
        """Crée un champ de saisie moderne"""
        entry = tk.Entry(parent, font=("Segoe UI", 11), width=28,
                         relief="solid", bd=1, bg="white",
                         fg=self.text_dark, show=show)
        entry.grid(row=row, column=1, pady=12, sticky="w", padx=5)

        # Effet focus
        entry.bind("<FocusIn>", lambda e: entry.config(bd=2, relief="solid"))
        entry.bind("<FocusOut>", lambda e: entry.config(bd=1, relief="solid"))

        return entry

    def create_modern_button(self, parent, text, command, color, row, col):
        """Crée un bouton moderne avec effet hover"""
        btn = tk.Button(parent, text=text, command=command,
                        font=("Segoe UI", 10, "bold"),
                        bg=color, fg="white", width=16,
                        cursor="hand2", relief="flat",
                        bd=0, padx=10, pady=8)
        btn.grid(row=row, column=col, padx=8, pady=6)

        # Effet hover
        btn.bind("<Enter>", lambda e: btn.config(bg=self.darken_color(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

        return btn

    def darken_color(self, color):
        """Assombrit une couleur hexadécimale"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
        darker_rgb = tuple(max(0, int(c * 0.8)) for c in rgb)
        return '#%02x%02x%02x' % darker_rgb

    def charger_donnees(self):
        """Charge les données dans le tableau"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            self.cursor.execute("""
                                SELECT id, nom, prenom, anniversaire, sexe, contact
                                FROM utilisateurs
                                ORDER BY id DESC
                                """)
            rows = self.cursor.fetchall()

            for idx, row in enumerate(rows):
                date_format = row[3].strftime("%d/%m/%Y") if row[3] else ""
                tag = "evenrow" if idx % 2 == 0 else "oddrow"
                self.tree.insert("", "end", values=(row[0], row[1], row[2], date_format, row[4], row[5]), tags=(tag,))

        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors du chargement:\n{err}")

    def on_select(self, event):
        """Gère la sélection"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']

            self.selected_id = values[0]

            self.nom_entry.delete(0, tk.END)
            self.nom_entry.insert(0, values[1])

            self.prenom_entry.delete(0, tk.END)
            self.prenom_entry.insert(0, values[2])

            try:
                date_obj = datetime.strptime(values[3], "%d/%m/%Y")
                self.date_entry.set_date(date_obj)
            except:
                pass

            self.sexe_var.set(values[4])

            self.contact_entry.delete(0, tk.END)
            self.contact_entry.insert(0, values[5])

            self.password_entry.delete(0, tk.END)

    def ajouter(self):
        """Ajoute un utilisateur"""
        nom = self.nom_entry.get().strip()
        prenom = self.prenom_entry.get().strip()
        anniversaire = self.date_entry.get_date()
        sexe = self.sexe_var.get()
        contact = self.contact_entry.get().strip()
        mot_de_passe = self.password_entry.get()

        if not all([nom, prenom, contact, mot_de_passe]):
            messagebox.showwarning("⚠️ Champs manquants",
                                   "Veuillez remplir tous les champs obligatoires.")
            return

        try:
            sql = """INSERT INTO utilisateurs
                         (nom, prenom, anniversaire, sexe, contact, mot_de_passe)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (nom, prenom, anniversaire, sexe, contact, mot_de_passe)

            self.cursor.execute(sql, values)
            self.conn.commit()

            messagebox.showinfo("✅ Succès", f"Inscription réussie pour {prenom} {nom}!")
            self.deselectionner()
            self.charger_donnees()

        except mysql.connector.Error as err:
            messagebox.showerror("❌ Erreur", f"Erreur lors de l'ajout:\n{err}")

    def modifier(self):
        """Modifie un utilisateur"""
        if not self.selected_id:
            messagebox.showwarning("⚠️ Aucune sélection",
                                   "Veuillez sélectionner un utilisateur à modifier.")
            return

        nom = self.nom_entry.get().strip()
        prenom = self.prenom_entry.get().strip()
        anniversaire = self.date_entry.get_date()
        sexe = self.sexe_var.get()
        contact = self.contact_entry.get().strip()
        mot_de_passe = self.password_entry.get()

        if not all([nom, prenom, contact]):
            messagebox.showwarning("⚠️ Champs manquants",
                                   "Veuillez remplir tous les champs obligatoires.")
            return

        try:
            if mot_de_passe:
                sql = """UPDATE utilisateurs \
                         SET nom=%s, \
                             prenom=%s, \
                             anniversaire=%s, \
                             sexe=%s, \
                             contact=%s, \
                             mot_de_passe=%s \
                         WHERE id = %s"""
                values = (nom, prenom, anniversaire, sexe, contact, mot_de_passe, self.selected_id)
            else:
                sql = """UPDATE utilisateurs \
                         SET nom=%s, \
                             prenom=%s, \
                             anniversaire=%s, \
                             sexe=%s, \
                             contact=%s \
                         WHERE id = %s"""
                values = (nom, prenom, anniversaire, sexe, contact, self.selected_id)

            self.cursor.execute(sql, values)
            self.conn.commit()

            messagebox.showinfo("✅ Succès", "Utilisateur modifié avec succès!")
            self.deselectionner()
            self.charger_donnees()

        except mysql.connector.Error as err:
            messagebox.showerror("❌ Erreur", f"Erreur lors de la modification:\n{err}")

    def supprimer(self):
        """Supprime un utilisateur"""
        if not self.selected_id:
            messagebox.showwarning("⚠️ Aucune sélection",
                                   "Veuillez sélectionner un utilisateur à supprimer.")
            return

        nom = self.nom_entry.get().strip()
        prenom = self.prenom_entry.get().strip()

        reponse = messagebox.askyesno("⚠️ Confirmation",
                                      f"Voulez-vous vraiment supprimer:\n\n"
                                      f"{prenom} {nom} (ID: {self.selected_id})?\n\n"
                                      f"Cette action est irréversible.",
                                      icon='warning')

        if not reponse:
            return

        try:
            sql = "DELETE FROM utilisateurs WHERE id=%s"
            self.cursor.execute(sql, (self.selected_id,))
            self.conn.commit()

            messagebox.showinfo("✅ Succès", "Utilisateur supprimé avec succès!")
            self.deselectionner()
            self.charger_donnees()

        except mysql.connector.Error as err:
            messagebox.showerror("❌ Erreur", f"Erreur lors de la suppression:\n{err}")

    def deselectionner(self):
        """Réinitialise le formulaire"""
        self.nom_entry.delete(0, tk.END)
        self.prenom_entry.delete(0, tk.END)
        self.date_entry.set_date(datetime.now())
        self.sexe_var.set("Homme")
        self.contact_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        self.selected_id = None

        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def __del__(self):
        """Ferme la connexion"""
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = FormulaireInscription(root)
    root.mainloop()