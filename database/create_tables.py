from database.database import Base, engine
import logging
from schemas.user_schema import UserSchema  # Importa UserSchema per la tabella users
from schemas.items_schema import ItemSchema  # Importa ItemSchema per la tabella items


logging.basicConfig(level=logging.INFO)

try:
    print("Creazione delle tabelle nel database...")
    Base.metadata.create_all(bind=engine)
    logging.info("Tabelle create con successo!")

    # Verifica che le tabelle siano effettivamente create
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    logging.info(f"Tabelle nel database: {tables}")

except Exception as e:
    logging.error(f"Errore durante la creazione delle tabelle: {str(e)}")
