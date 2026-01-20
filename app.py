import streamlit as st
import requests
import base64
import os
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="PlantDoctor AI", page_icon="🌿", layout="centered")

# Titre et description
st.title("🌿 PlantDoctor AI")
st.write("Téléchargez une photo de votre plante malade pour obtenir un diagnostic et un traitement.")

# Fonction pour encoder l'image en base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Récupération de la clé API depuis les variables d'environnement (Render)
api_key = os.environ.get("OPENAI_API_KEY")

# Vérification de la clé
if not api_key:
    st.error("Erreur : La clé API n'est pas configurée. Ajoutez OPENAI_API_KEY dans les variables d'environnement de Render.")
    st.stop()

# Zone de téléchargement de fichier
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Afficher l'image
    image = Image.open(uploaded_file)
    st.image(image, caption='Image téléchargée', use_container_width=True)
    
    # Bouton pour lancer l'analyse
    if st.button("🔍 Lancer le diagnostic"):
        with st.spinner('Analyse en cours par l\'expert agronome...'):
            try:
                # Encoder l'image pour l'envoyer à l'API (on rembobine le fichier avant)
                uploaded_file.seek(0)
                base64_image = encode_image(uploaded_file)

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }

                # LE COEUR DU SYSTÈME : Le Prompt Expert
                payload = {
                    "model": "gpt-4o",
                    "messages": [
                        {
                            "role": "system",
                            "content": """
                            Tu es un expert phytopathologiste et agronome spécialisé dans les cultures africaines. 
                            Ta mission est d'analyser les images de plantes pour identifier les maladies, ravageurs ou carences.
                            
                            RÈGLES STRICTES :
                            1. NE DIS JAMAIS "Je ne peux pas diagnostiquer". Donne toujours ton MEILLEUR avis d'expert basé sur les symptômes visibles.
                            2. Analyse les symptômes (taches, jaunissement, flétrissement, insectes).
                            3. Structure ta réponse en 4 parties claires avec des titres en GRAS :
                               - 🔍 **Identification probable** (Plante reconnue)
                               - ⚠️ **Symptômes observés**
                               - 🦠 **Diagnostic** (Maladie / Ravageur / Carence / Stress)
                               - 💊 **Traitement recommandé** (Solutions bio/locales et solutions chimiques si nécessaire)
                            4. Réponds toujours en FRANÇAIS.
                            """
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Analyse cette plante et donne-moi un diagnostic précis."
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

                # Appel à l'API OpenAI
                response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                
                # Vérification de la réponse
                if response.status_code == 200:
                    result = response.json()
                    analysis = result['choices'][0]['message']['content']
                    st.success("Diagnostic terminé !")
                    st.markdown(analysis)
                else:
                    st.error(f"Erreur API : {response.status_code} - {response.text}")

            except Exception as e:
                st.error(f"Une erreur s'est produite : {e}")
