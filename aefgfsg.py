
import h5py

file_path = 'linear_regression_model.h5'

try:
    with h5py.File(file_path, 'r') as file:
        # Check the content of the file
        print(list(file.keys()))
except Exception as e:
    print(f"Error: {e}")
