from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charge les variables du fichier .env
load_dotenv()

# Récupère l'URL de la base de données
DATABASE_URL = os.getenv("DATABASE_URL")

# Crée le moteur de connexion
engine = create_engine(DATABASE_URL)

# Crée une session pour parler à la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()