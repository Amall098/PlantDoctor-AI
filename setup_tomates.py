import os
import zipfile
import shutil

# Nom du fichier zip que tu as téléchargé
ZIP_FILE = "tomates.zip" 
DEST_DIR = "dataset"

print(f"--- TRAITEMENT DE {ZIP_FILE} ---")

if not os.path.exists(ZIP_FILE):
    print(f"ERREUR : Je ne trouve pas le fichier '{ZIP_FILE}' dans le dossier !")
    print("Assure-toi de l'avoir copié ici et renommé.")
    exit()

# 1. Extraction
print("Extraction en cours (cela peut prendre un moment)...")
temp_dir = "temp_extract"
with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)

# 2. Recherche et Filtrage des Tomates
print("Recherche des dossiers de tomates...")
if os.path.exists(DEST_DIR):
    shutil.rmtree(DEST_DIR)
os.makedirs(DEST_DIR)

found_count = 0

# On parcourt tous les dossiers extraits pour trouver ceux qui contiennent "Tomato"
for root, dirs, files in os.walk(temp_dir):
    for dir_name in dirs:
        # On ne garde que les dossiers qui parlent de Tomates
        if "Tomato" in dir_name:
            source_path = os.path.join(root, dir_name)
            # On nettoie le nom (ex: "PlantVillage_Tomato__Healthy" -> "Tomato_Healthy")
            clean_name = dir_name.split('/')[-1] 
            dest_path = os.path.join(DEST_DIR, clean_name)
            
            # Copie
            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            print(f" - Récupéré : {clean_name}")
            found_count += 1

# 3. Nettoyage
print("Nettoyage des fichiers temporaires...")
shutil.rmtree(temp_dir)

if found_count > 0:
    print(f"\n--- SUCCÈS ! ---")
    print(f"{found_count} catégories de tomates ont été installées dans 'dataset'.")
    print("Tu peux lancer l'entraînement !")
else:
    print("\n--- ATTENTION ---")
    print("Aucun dossier 'Tomato' n'a été trouvé dans le zip.")
    print("Vérifie que tu as téléchargé le bon fichier.")