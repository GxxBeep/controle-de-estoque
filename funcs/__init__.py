
from .sistema import Database
import os

if not os.path.exists('database') or not os.path.exists('database/imagens'):
    print("Nao existe")
    os.makedirs('database/imagens', exist_ok=True)

Database()