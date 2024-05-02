from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config.constants import DATABASE_URL


class DBEngine:
    '''Database engine'''

    def __init__(self):
        """ Instantiale db """
        self.__engine = create_engine(DATABASE_URL, echo=True)