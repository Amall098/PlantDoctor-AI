[README.md](https://github.com/user-attachments/files/30960172/README.md)
<div align="center">

# 🌿 PlantDoctor AI

**Diagnostic des maladies des plantes par vision artificielle**
*Plant disease detection powered by computer vision*

[![Demo](https://img.shields.io/badge/Démo_en_ligne-plantdoctor--ai.onrender.com-2ea44f?style=for-the-badge)](https://plantdoctor-ai.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/Licence-MIT-lightgrey?style=flat-square)](LICENSE)

[Français](#-français) · [English](#-english)

</div>

<!-- Remplacez ce bloc par une capture d'écran ou un GIF de l'application en action.
     Placez le fichier dans /assets et référencez-le ainsi : -->
<!-- ![Aperçu de l'application](assets/demo.gif) -->

---

## 🇫🇷 Français

### Le problème

Les maladies des cultures détruisent une part considérable des récoltes chaque année, et les pertes sont les plus lourdes là où l'accès à l'expertise agronomique est le plus faible. Un producteur qui identifie tardivement un mildiou ou une alternariose perd souvent l'essentiel de sa parcelle. Le diagnostic précoce est donc décisif — mais il suppose habituellement la visite d'un technicien agricole, ressource rare et coûteuse en milieu rural.

### La solution

**PlantDoctor AI** met le diagnostic à portée d'un smartphone. L'utilisateur photographie une feuille malade ; un réseau de neurones convolutif analyse l'image et retourne en quelques secondes la maladie probable, un indice de confiance, et des pistes de traitement.

L'outil ne remplace pas l'agronome : il permet d'agir vite, de trier les urgences et de savoir quand il faut vraiment faire appel à un expert.

### Fonctionnalités

- 📸 **Diagnostic par photo** — dépôt d'image ou capture directe depuis un téléphone
- 🧠 **Modèle CNN entraîné** sur un corpus d'images de feuilles saines et malades
- 📊 **Indice de confiance** affiché avec chaque prédiction, pour une lecture honnête du résultat
- 🌱 **Cultures couvertes** — <!-- ex. : tomate, pomme de terre, maïs, manioc -->
- 🩺 **Maladies détectées** — <!-- listez les classes du modèle -->
- 🌍 **Interface accessible** depuis n'importe quel navigateur, sans installation

### Démonstration

👉 **[plantdoctor-ai.onrender.com](https://plantdoctor-ai.onrender.com)**

> ⏱️ *Note :* l'application est hébergée sur une offre gratuite qui se met en veille. Le premier chargement peut demander une trentaine de secondes ; les suivants sont immédiats.

### Performance du modèle

| Indicateur | Valeur |
|---|---|
| Architecture | <!-- ex. : CNN personnalisé / MobileNetV2 --> |
| Jeu de données | <!-- ex. : PlantVillage, N images, K classes --> |
| Exactitude (validation) | <!-- ex. : 94,2 % --> |
| Temps d'inférence | <!-- ex. : ~0,8 s --> |

### Architecture du projet

```
PlantDoctor-AI/
├── app.py              # Application web (interface et routage)
├── predict.py          # Chargement du modèle et inférence
├── train.py            # Entraînement du modèle
├── train_cnn.py        # Définition de l'architecture CNN
├── setup_tomates.py    # Préparation du jeu de données — tomates
├── setup_force.py      # Préparation du jeu de données — forcé
├── requirements.txt    # Dépendances Python
└── assets/             # Images de démonstration et captures
```

### Installation locale

```bash
# Cloner le dépôt
git clone https://github.com/Amall098/PlantDoctor-AI.git
cd PlantDoctor-AI

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py
```

L'application est ensuite accessible à l'adresse `http://localhost:5000`.

### Entraîner votre propre modèle

```bash
python setup_tomates.py     # Préparer et organiser le jeu de données
python train_cnn.py         # Lancer l'entraînement
```

### Feuille de route

- [ ] Recommandations de traitement (options biologiques et conventionnelles, dosages, coûts)
- [ ] Fonctionnement hors ligne via application web progressive (PWA)
- [ ] Interface multilingue — français, anglais, langues locales
- [ ] Version mobile légère (TensorFlow Lite)
- [ ] Élargissement du corpus à de nouvelles cultures d'Afrique de l'Ouest
- [ ] Historique des diagnostics et suivi par parcelle

### Limites et usage responsable

Ce système est un outil d'aide à la décision, pas un dispositif de certification phytosanitaire. Sa fiabilité dépend de la qualité de la photographie, des conditions d'éclairage et de la présence de la culture concernée dans le corpus d'entraînement. Une maladie absente du jeu de données ne sera pas reconnue — le modèle proposera alors la classe la plus proche, ce qui peut induire en erreur. En cas de doute, ou avant toute intervention phytosanitaire importante, la consultation d'un agronome demeure nécessaire.

### Une réflexion sur l'accès

Ce projet est né d'une double interrogation : technique — peut-on rendre le diagnostic agricole accessible à faible coût ? — et politique — qui bénéficie réellement des outils d'intelligence artificielle, et à quelles conditions ? Les systèmes prédictifs promettent l'universalité mais reproduisent souvent les inégalités d'accès existantes : ils supposent un smartphone, une connexion, une langue, et un corpus d'entraînement qui inclut vos cultures. PlantDoctor tente d'approcher ces contraintes de front plutôt que de les ignorer.

### Contribuer

Les contributions sont bienvenues : signalement d'anomalies, ajout de jeux de données pour de nouvelles cultures, traductions, améliorations de l'interface. Ouvrez une *issue* pour en discuter, ou proposez directement une *pull request*.

### Auteur

**Abakar Mall**
Docteur en pensée politique et administration publique · Chercheur et développeur
[GitHub](https://github.com/Amall098) · <!-- LinkedIn · courriel -->

### Licence

Distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE).

---

## 🇬🇧 English

### The problem

Crop diseases destroy a substantial share of harvests every year, and losses fall hardest where access to agronomic expertise is thinnest. A grower who identifies late blight or early blight too late often loses most of the plot. Early diagnosis is decisive — yet it normally requires a visit from an agricultural technician, a scarce and costly resource in rural areas.

### The solution

**PlantDoctor AI** puts diagnosis within reach of a smartphone. The user photographs an affected leaf; a convolutional neural network analyses the image and returns, within seconds, the likely disease, a confidence score, and treatment guidance.

The tool does not replace an agronomist. It allows growers to act quickly, triage urgent cases, and recognise when expert help is genuinely needed.

### Features

- 📸 **Photo-based diagnosis** — upload an image or capture directly from a phone
- 🧠 **Trained CNN model** built on a corpus of healthy and diseased leaf images
- 📊 **Confidence score** shown with every prediction, for an honest reading of the result
- 🌱 **Crops covered** — <!-- e.g. tomato, potato, maize, cassava -->
- 🩺 **Diseases detected** — <!-- list the model's classes -->
- 🌍 **Browser-accessible**, no installation required

### Live demo

👉 **[plantdoctor-ai.onrender.com](https://plantdoctor-ai.onrender.com)**

> ⏱️ *Note:* the app runs on a free tier that sleeps when idle. The first load may take around thirty seconds; subsequent requests are immediate.

### Model performance

| Metric | Value |
|---|---|
| Architecture | <!-- e.g. custom CNN / MobileNetV2 --> |
| Dataset | <!-- e.g. PlantVillage, N images, K classes --> |
| Validation accuracy | <!-- e.g. 94.2% --> |
| Inference time | <!-- e.g. ~0.8 s --> |

### Project structure

```
PlantDoctor-AI/
├── app.py              # Web application (interface and routing)
├── predict.py          # Model loading and inference
├── train.py            # Model training
├── train_cnn.py        # CNN architecture definition
├── setup_tomates.py    # Dataset preparation — tomatoes
├── setup_force.py      # Dataset preparation — forced run
├── requirements.txt    # Python dependencies
└── assets/             # Demo images and screenshots
```

### Local installation

```bash
# Clone the repository
git clone https://github.com/Amall098/PlantDoctor-AI.git
cd PlantDoctor-AI

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app is then available at `http://localhost:5000`.

### Training your own model

```bash
python setup_tomates.py     # Prepare and organise the dataset
python train_cnn.py         # Start training
```

### Roadmap

- [ ] Treatment recommendations (organic and conventional options, dosages, costs)
- [ ] Offline operation via progressive web app (PWA)
- [ ] Multilingual interface — French, English, local languages
- [ ] Lightweight mobile build (TensorFlow Lite)
- [ ] Corpus expansion to additional West African crops
- [ ] Diagnosis history and per-plot tracking

### Limitations and responsible use

This system is a decision-support tool, not a phytosanitary certification device. Its reliability depends on photo quality, lighting conditions, and whether the crop in question appears in the training corpus. A disease absent from the dataset will not be recognised — the model will return the nearest class instead, which can mislead. Where there is doubt, or before any significant phytosanitary intervention, consulting an agronomist remains necessary.

### A note on access

This project grew out of a double question: a technical one — can agricultural diagnosis be made accessible at low cost? — and a political one — who actually benefits from AI tools, and on what terms? Predictive systems promise universality but frequently reproduce existing inequalities of access: they presuppose a smartphone, a connection, a language, and a training corpus that includes your crops. PlantDoctor tries to meet those constraints head-on rather than ignore them.

### Contributing

Contributions are welcome: bug reports, datasets for additional crops, translations, interface improvements. Open an issue to discuss, or submit a pull request directly.

### Author

**Abakar Mall**
PhD in political thought and public administration · Researcher and developer
[GitHub](https://github.com/Amall098) · <!-- LinkedIn · email -->

### License

Released under the MIT License. See [LICENSE](LICENSE).

---

<div align="center">
<sub>Construit pour les producteurs qui n'ont pas d'agronome à portée de main.<br>
Built for growers who don't have an agronomist within reach.</sub>
</div>
