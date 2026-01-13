import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array

# --- CONFIGURATION ---
MODEL_PATH = 'modele_tomates.keras'
IMG_SIZE = (128, 128)

# Les noms des classes
CLASS_NAMES = [
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato_Target_Spot',
    'Tomato_Tomato_YellowLeaf__Curl_Virus',
    'Tomato_Tomato_mosaic_virus',
    'Tomato_healthy'
]

def predict_image(image_path):
    if not os.path.exists(image_path):
        print(f"ERREUR : L'image '{image_path}' n'existe pas !")
        return

    print(f"\n--- Analyse de l'image : {image_path} ---")
    
    # Chargement du modèle
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except:
        print("Erreur : Impossible de charger le modèle.")
        return

    # Préparation de l'image
    img = load_img(image_path, target_size=IMG_SIZE)
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Prédiction
    predictions = model.predict(img_array)
    
    # CORRECTION : On prend directement le résultat (plus de double Softmax)
    score = predictions[0]

    # Résultat
    class_index = np.argmax(score)
    confidence = 100 * np.max(score)
    
    print(f"\nRÉSULTAT : Cette image semble être : {CLASS_NAMES[class_index]}")
    print(f"CONFIANCE : {confidence:.2f}%")

# --- LE DÉCLENCHEUR (C'est cette partie qui manquait !) ---
if __name__ == "__main__":
    image_to_test = input("Glisse une image ici ou tape son nom (ex: test2.jpg) : ")
    image_to_test = image_to_test.replace('"', '').strip()
    predict_image(image_to_test)