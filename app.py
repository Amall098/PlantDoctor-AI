# Configuration pour éviter les déconnexions intempestives
import streamlit as st
st.set_page_config(
    page_title="PlantDoctor AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st
import numpy as np
from PIL import Image
import os
import base64
import requests

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="PlantDoctor AI - Prof. Malloum",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FONCTION DE SÉCURITÉ POUR L'IMAGE ---
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

# --- CSS PERSONNALISÉ (Identique au vôtre) ---
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #2e7d32; color: white; }
    h1 { color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- GESTION DES LANGUES (Optimisée) ---
translations = {
    'Français': {
        'author_title': "Auteur & Supervision",
        'univ': "Université d'Ottawa",
        'main_title': "🌿 PlantDoctor AI",
        'subtitle': "Système de Diagnostic Végétal Intelligent",
        'upload_label': "Chargez une image de feuille (JPG/PNG)",
        'analyzing': "Analyse par intelligence artificielle en cours...",
        'diagnosis': "Diagnostic Expert",
        'confidence': "Indice de Fiabilité",
        'footer': "Développé sous la supervision du Prof. Abakar Malloum - Université d'Ottawa © 2026",
        'api_error': "Erreur de connexion à l'IA. Vérifiez votre clé API.",
        'prompt': "Tu es un expert en phytopathologie. Analyse cette image de plante. Donne le nom de la maladie et un conseil de traitement court."
    },
    'English': {
        'author_title': "Author & Supervision",
        'univ': "University of Ottawa",
        'main_title': "🌿 PlantDoctor AI",
        'subtitle': "Intelligent Plant Diagnostic System",
        'upload_label': "Upload a leaf image (JPG/PNG)",
        'analyzing': "AI Analysis in progress...",
        'diagnosis': "Expert Diagnosis",
        'confidence': "Reliability Index",
        'footer': "Developed under the supervision of Prof. Abakar Malloum - University of Ottawa © 2026",
        'api_error': "AI Connection Error. Check your API Key.",
        'prompt': "You are a plant pathology expert. Analyze this plant image. Provide the disease name and short treatment advice."
    }
}

# --- SIDEBAR ---
with st.sidebar:
    language = st.selectbox("Langue / Language", ["Français", "English"])
    t = translations[language]
    
    st.image("https://upload.wikimedia.org/wikipedia/fr/thumb/5/5f/Universit%C3%A9_d%27Ottawa_logo.svg/1200px-Universit%C3%A9_d%27Ottawa_logo.svg.png", width=200)
    st.markdown("---")
    st.markdown(f"### 👤 {t['author_title']}")
    
    if os.path.exists("profil.jpg"):
        st.image("profil.jpg", width=150)
    
    st.markdown("**Prof. Abakar Malloum**")
    st.markdown(f"*{t['univ']}*")
    st.markdown("📧 amaloumm@uottawa.ca")

# --- CORPS PRINCIPAL ---
st.title(t['main_title'])
st.markdown(f"### {t['subtitle']}")

uploaded_file = st.file_uploader(t['upload_label'], type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

    with col2:
        st.markdown(f"#### 📊 {t['diagnosis']}")
        
        if st.button("Lancer le diagnostic" if language == "Français" else "Start Diagnosis"):
            with st.spinner(t['analyzing']):
                try:
                    # Récupération de la clé API sauvegardée dans Render
                    api_key = os.environ.get("OPENAI_API_KEY")
                    base64_image = encode_image(uploaded_file)

                    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
                        payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": """
                Tu es un expert phytopathologiste et agronome spécialisé dans les cultures africaines. 
                Ta mission est d'analyser les images de plantes pour identifier les maladies, ravageurs ou carences.
                
                RÈGLES STRICTES :
                1. NE DIS JAMAIS "Je ne peux pas diagnostiquer". Donne toujours ton MEILLEUR avis d'expert.
                2. Analyse les symptômes visibles (taches, jaunissement, flétrissement).
                3. Structure ta réponse en 4 parties claires :
                   - 🔍 Identification probable de la plante
                   - ⚠️ Symptômes observés
                   - 🦠 Diagnostic (Maladie / Ravageur / Carence / Stress hydrique)
                   - 💊 Traitement recommandé (Remèdes naturels locaux et solutions chimiques)
                4. Réponds toujours en FRANÇAIS.
                """
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyse cette plante et donne-moi un diagnostic précis et des solutions."
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
        "max_tokens": 800}

                    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                    response.raise_for_status()
                    full_response = response.json()['choices'][0]['message']['content']
                    
                    st.info(full_response)
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"{t['api_error']}")
                    st.caption(f"Détail : {e}")

    st.divider()
    st.caption(t['footer'])
