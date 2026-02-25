import os

# Caminhos base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Arquivos de dados
PROBLEMS_FILE = os.path.join(DATA_DIR, "problems.json")
SCORES_FILE = os.path.join(DATA_DIR, "scores.json")
