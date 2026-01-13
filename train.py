import os
import tensorflow as tf
from tensorflow.keras import layers, models

# --- CONFIGURATION ---
DATASET_DIR = 'dataset'  # Le dossier créé par l'étape précédente
IMG_SIZE = (128, 128)    # Taille des images (réduite pour aller vite sur CPU)
BATCH_SIZE = 32          # Nombre d'images traitées à la fois
EPOCHS = 10              # Nombre de "tours" d'apprentissage (augmenter pour plus de précision)

print("--- Chargement des données ---")

# 1. Chargement des données d'entraînement (80%)
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

# 2. Chargement des données de validation (20% pour tester l'IA)
val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
print(f"Classes détectées : {class_names}")

# Optimisation de la mémoire
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# --- CRÉATION DU MODÈLE (Cerveau) ---
print("--- Construction du modèle ---")
model = models.Sequential([
    # Entrée et standardisation (pixels de 0-255 vers 0-1)
    layers.Rescaling(1./255, input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
    
    # Couches de convolution (L'IA cherche les motifs: lignes, formes, textures)
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    
    # Classification
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(class_names), activation='softmax') # La couche finale de décision
])

# Compilation
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# --- ENTRAÎNEMENT ---
print("--- Démarrage de l'entraînement... (Patience !) ---")
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS
)

# --- SAUVEGARDE ---
print("--- Sauvegarde du modèle ---")
model.save('modele_tomates.keras')
print("SUCCÈS : Le modèle a été sauvegardé sous 'modele_tomates.keras'")