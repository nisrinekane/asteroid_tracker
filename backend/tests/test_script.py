from ..analysis import load_data, process_data

test_data = load_data('test_data.json')

print(test_data)  # Add this line for debugging

processed_data = process_data(test_data)
assert processed_data == [('Asteroid 1', 5000.0, False), 
                        ('Asteroid 2', 15000.0, True), 
                        ('Asteroid 3', 25000.0, True), 
                        ('Asteroid 4', 35000.0, False), 
                        ('Asteroid 5', 45000.0, True)]
