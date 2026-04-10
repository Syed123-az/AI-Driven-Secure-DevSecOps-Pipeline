import pickle

MODEL_PATH = "../ML_Model/threat_model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)