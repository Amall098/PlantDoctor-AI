import urllib.request
import tarfile
import os
import shutil

# URL officielle des images de fleurs (Google)
url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
filename = "fleurs_temp.tgz"

print("--- ETAPE 1 : TELECHARGEMENT LOCAL ---")
print("Téléchargement en cours directement dans ce dossier...")
print("Patience, c'est environ 200 Mo...")
# On télécharge directement ICI (on évite le dossier .keras bloqué)
urllib.request.urlretrieve(url, filename)
print("Téléchargement terminé !")

print("\n--- ETAPE 2 : EXTRACTION ---")
# On nettoie si un dossier dataset cassé existe déjà
if os.path.exists("dataset"):
    print("Nettoyage de l'ancien dossier...")
    shutil.rmtree("dataset")

print("Extraction des images...")
with tarfile.open(filename, "r:gz") as tar:
    tar.extractall()

# Le dossier s'appelle 'flower_photos' par défaut, on le renomme 'dataset'
if os.path.exists("flower_photos"):
    os.rename("flower_photos", "dataset")

print("\n--- ETAPE 3 : NETTOYAGE ---")
# On supprime le fichier zip pour faire propre
if os.path.exists(filename):
    os.remove(filename)

print("--- SUCCES TOTAL ! ---")
print("Ton dossier 'dataset' est prêt.")
print("Lance maintenant : py -3.11 train_cnn.py")