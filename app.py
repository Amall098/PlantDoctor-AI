import streamlit as st
import requests
import base64
import os
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="PlantDoctor AI", page_icon="🌿", layout="wide")

# --- BARRE LATÉRALE (PROFIL & LANGUE) ---
with st.sidebar:
    # 1. Sélecteur de langue
    st.header("🌐 Language")
    language = st.radio("Choisissez votre langue / Select language:", ("Français", "English"))

    st.markdown("---")

    # 2. Votre Profil (Photo et Bio)
    # Assurez-vous d'avoir un fichier 'profile.jpg' dans votre GitHub pour que cela fonctionne
    try:
        st.image("profile.jpg", width=150) 
    except:
        st.write("📷 (Ajoutez 'profile.jpg' sur GitHub pour voir votre photo)")

    st.markdown("### Dr. Abakar Malloum")
    st.markdown("**Chercheur & Professeur**")
    st.caption("Université d'Ottawa & Université Saint-Paul")
    
    st.markdown("---")
    st.markdown("📍 *Spécialiste en éthique du numérique et innovation.*")
    st.markdown("📧 *Contactez-moi pour toute collaboration.*")

# --- CONTENU PRINCIPAL ---

# Textes dynamiques selon la langue
if language == "Français":
    title = "🌿 PlantDoctor AI"
    subtitle = "Assistant intelligent pour le diagnostic des maladies des plantes"
    upload_text = "Téléchargez une photo de la plante malade (feuille, tige ou fruit)"
    button_text = "🔍 Lancer le diagnostic"
    loading_text = "Analyse en cours par l'expert..."
    success_text = "Diagnostic terminé !"
    error_key = "Erreur : Clé API manquante."
    
    # Prompt Système en Français
    system_prompt = """
    Tu es un expert phytopathologiste et agronome. 
    Ta mission est d'analyser les images pour identifier les maladies, ravageurs ou carences.
    RÈGLES :
    1. Ne dis jamais "Je ne peux pas". Donne ton meilleur avis d'expert.
    2. Structure ta réponse en 4 parties : Identification, Symptômes, Diagnostic, Traitement (Bio et Chimique).
    3. Réponds en FRANÇAIS.
    """
    user_prompt = "Analyse cette plante, identifie la maladie et donne des remèdes."

else: # English
    title = "🌿 PlantDoctor AI"
    subtitle = "Intelligent assistant for plant disease diagnosis"
    upload_text = "Upload a photo of the affected plant (leaf, stem, or fruit)"
    button_text = "🔍 Start Diagnosis"
    loading_text = "Analysis in progress by the expert..."
    success_text = "Diagnosis complete!"
    error_key = "Error: API Key missing."

    # Prompt Système en Anglais
    system_prompt = """
    You are an expert plant pathologist and agronomist.
    Your mission is to analyze images to identify diseases, pests, or deficiencies.
    RULES:
    1. Never say "I cannot diagnose". Give your best expert opinion.
    2. Structure your answer in 4 parts: Identification, Symptoms, Diagnosis, Treatment (Organic and Chemical).
    3. Answer in ENGLISH.
    """
    user_prompt = "Analyze this plant, identify the disease, and provide remedies."

# Affichage du titre
st.title(title)
st.subheader(subtitle)

# Fonction encodage image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Récupération clé API
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error(error_key)
    st.stop()

# Zone d'upload
uploaded_file = st.file_uploader(upload_text, type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption='Image', use_container_width=True)
    
    with col2:
        if st.button(button_text, type="primary"):
            with st.spinner(loading_text):
                try:
                    uploaded_file.seek(0)
                    base64_image = encode_image(uploaded_file)

                    headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {api_key}"
                    }

                    payload = {
                        "model": "gpt-4o",
                        "messages": [
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": user_prompt
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{base64_image}"
                                        }
                                    }
                                ]
                            }
                        ],
                        "max_tokens": 800
                    }

                    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                    
                    if response.status_code == 200:
                        result = response.json()
                        analysis = result['choices'][0]['message']['content']
                        st.success(success_text)
                        st.markdown(analysis)
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")

                except Exception as e:
                    st.error(f"Error: {e}")
