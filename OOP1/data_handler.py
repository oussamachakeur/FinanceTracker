import pickle

def save_data(finance_tracker, filename):
    with open(filename, 'wb') as file:
        pickle.dump(finance_tracker, file)

def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None
