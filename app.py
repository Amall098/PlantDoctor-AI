import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="PlantDoctor AI - Prof. Malloum",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stButton>button { width: 100%; border-radius: 5px; }
    h1 { color: #2e7d32; }
    .stProgress > div > div > div > div { background-color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- GESTION DES LANGUES (TRADUCTIONS) ---
translations = {
    'Français': {
        'sidebar_title': "PlantDoctor AI 🔬",
        'sidebar_info': "Système expert basé sur un Réseau de Neurones Convolutifs (CNN) pour l'agriculture de précision.",
        'author_title': "Auteur & Supervision",
        'univ': "Université d'Ottawa",
        'main_title': "🌿 PlantDoctor AI",
        'subtitle': "Système de Diagnostic Végétal Intelligent",
        'welcome': "Bienvenue dans l'interface de détection assistée par ordinateur.",
        'upload_label': "Chargez une image de feuille (JPG/PNG)",
        'col_image': "📸 Échantillon analysé",
        'col_result': "📊 Résultats de l'analyse",
        'analyzing': "Extraction des caractéristiques...",
        'diagnosis': "Diagnostic",
        'prob_diagnosis': "Diagnostic probable",
        'uncertain': "Résultat incertain",
        'confidence': "Indice de Confiance",
        'healthy_msg': "✅ Aucune pathologie détectée.",
        'warning_msg': "⚠️ Pathologie détectée. Veuillez consulter les protocoles de traitement.",
        'footer': "Développé sous la supervision du Prof. Abakar Malloum - Université d'Ottawa © 2026",
        'wait_msg': "👆 En attente d'une image pour commencer le diagnostic...",
        'photo_missing': "Photo 'profil.jpg' introuvable."
    },
    'English': {
        'sidebar_title': "PlantDoctor AI 🔬",
        'sidebar_info': "Expert system based on Convolutional Neural Networks (CNN) for precision agriculture.",
        'author_title': "Author & Supervision",
        'univ': "University of Ottawa",
        'main_title': "🌿 PlantDoctor AI",
        'subtitle': "Intelligent Plant Diagnostic System",
        'welcome': "Welcome to the computer-aided detection interface.",
        'upload_label': "Upload a leaf image (JPG/PNG)",
        'col_image': "📸 Analyzed Sample",
        'col_result': "📊 Analysis Results",
        'analyzing': "Feature extraction in progress...",
        'diagnosis': "Diagnosis",
        'prob_diagnosis': "Probable Diagnosis",
        'uncertain': "Uncertain Result",
        'confidence': "Confidence Index",
        'healthy_msg': "✅ No pathology detected.",
        'warning_msg': "⚠️ Pathology detected. Please consult treatment protocols.",
        'footer': "Developed under the supervision of Prof. Abakar Malloum - University of Ottawa © 2026",
        'wait_msg': "👆 Waiting for an image to start diagnosis...",
        'photo_missing': "Photo 'profil.jpg' not found."
    }
}

# Noms des maladies par langue
CLASS_NAMES_FR = [
    'Tache Bactérienne', 'Mildiou (Early Blight)', 'Mildiou (Late Blight)', 
    'Moisissure des feuilles', 'Septoriose', 'Araignées Rouges', 
    'Tache Cible', 'Virus des feuilles jaunes', 'Virus de la Mosaïque', 'Sain'
]

CLASS_NAMES_EN = [
    'Bacterial Spot', 'Early Blight', 'Late Blight', 
    'Leaf Mold', 'Septoria Leaf Spot', 'Spider Mites', 
    'Target Spot', 'Yellow Leaf Curl Virus', 'Mosaic Virus', 'Healthy'
]

# --- CHARGEMENT DU MODÈLE ---
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('modele_tomates.keras')
    return model

# --- SÉLECTION DE LA LANGUE ---
# On met le sélecteur tout en haut de la sidebar
with st.sidebar:
    language = st.selectbox("Langue / Language", ["Français", "English"])
    t = translations[language] # 't' contient maintenant tous les textes dans la bonne langue
    class_names = CLASS_NAMES_FR if language == "Français" else CLASS_NAMES_EN

    # Logo UOttawa
    st.image("https://upload.wikimedia.org/wikipedia/fr/thumb/5/5f/Universit%C3%A9_d%27Ottawa_logo.svg/1200px-Universit%C3%A9_d%27Ottawa_logo.svg.png", width=200)
    
    st.markdown("---")
    st.markdown(f"### 👤 {t['author_title']}")
    
    # Photo de profil
    if os.path.exists("profil.jpg"):
        st.image("profil.jpg", width=150)
    else:
        st.warning(t['photo_missing'])

    st.markdown("**Prof. Abakar Malloum**")
    st.markdown(f"*{t['univ']}*")
    st.markdown("📧 amaloumm@uottawa.ca")
    
    st.markdown("---")
    st.info(t['sidebar_info'])
    st.caption("Version 1.1.0 (Bilingual)")

# --- CORPS PRINCIPAL ---
st.title(t['main_title'])
st.markdown(f"### {t['subtitle']}")
st.write(t['welcome'])

# Zone de téléchargement
uploaded_file = st.file_uploader(t['upload_label'], type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"#### {t['col_image']}")
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, use_container_width=True)

    with col2:
        st.markdown(f"#### {t['col_result']}")
        
        with st.spinner(t['analyzing']):
            # Préparation
            img_resized = image.resize((128, 128))
            img_array = tf.keras.preprocessing.image.img_to_array(img_resized)
            img_array = tf.expand_dims(img_array, 0)

            # Prédiction
            model = load_model()
            predictions = model.predict(img_array)
            score = predictions[0]
            
            # On utilise la liste de noms correspondant à la langue choisie
            predicted_class = class_names[np.argmax(score)]
            confidence = 100 * np.max(score)

        # Affichage conditionnel
        if confidence > 80:
            st.success(f"**{t['diagnosis']} : {predicted_class}**")
        elif confidence > 50:
            st.warning(f"**{t['prob_diagnosis']} : {predicted_class}**")
        else:
            st.error(f"**{t['uncertain']} : {predicted_class}**")

        st.metric(label=t['confidence'], value=f"{confidence:.2f} %")
        st.progress(int(confidence))

        # Message de santé traduit
        # On vérifie si c'est "Sain" ou "Healthy"
        if predicted_class in ["Sain", "Healthy"]:
            st.info(t['healthy_msg'])
        else:
            st.warning(t['warning_msg'])

    st.divider()
    st.caption(t['footer'])

else:
    st.info(t['wait_msg'])