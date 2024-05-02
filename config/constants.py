from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TMDB_API_TOKEN')
TMDB_BASE_URL = os.getenv('TMDB_BASE_URL')
QUOTE_TABLE = 'quotes'
CATEGORY_TABLE = 'categories'
REACTION_TABLE = 'reactions'
USER_TABLE = 'users'
DATABASE_URL = 'sqlite:///mydb.db'
TMDB_IMAGE_BASE_URL = os.getenv('TMDB_IMAGE_BASE_URL')
ENV = os.getenv('ENV')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
