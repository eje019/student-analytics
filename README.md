# Student Performance Analytics

Application de suivi et analyse des performances académiques.

## Fonctionnalités

- Authentification
- Gestion des matières
- Saisie et calcul des notes
- Visualisation graphique
- Analyse des progrès

## Stack

- Backend : FastAPI / PostgreSQL
- Frontend Web : React / Tailwind
- Mobile : React Native

## organisation des dossiers

student-analytics/
├── backend/               # Tout le code du serveur
│   ├── app/               # L'application principale
│   │   ├── routers/       # Les endpoints (URLs)
│   │   ├── __init__.py
│   │   ├── auth.py        # Connexion
│   │   ├── crud.py        # Les fonctions qui parlent à la base
│   │   ├── database.py    # La connexion à PostgreSQL
│   │   ├── main.py        # Le point d'entrée
│   │   ├── models.py      # Les plans des tables
│   │   └── schemas.py     # Pour validation
│   ├── venv/              # L'environnement virtuel
│   └── .env               # Les informations secrètes
├── frontend-web/          # Pour React
├── mobile-app/            # Pour React Native
└── docs/                  # Documentation