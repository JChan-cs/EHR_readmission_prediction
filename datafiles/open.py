import pickle

file_path = r'C:\Users\Jensen\Documents\STAT3612\Group_project\ehr_preprocessed_seq_by_day_cat_embedding.pkl'
try:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    print(data)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except pickle.UnpicklingError:
    print("Error: The file content is not a valid pickle format.")
except EOFError:
    print("Error: The file is incomplete or corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
