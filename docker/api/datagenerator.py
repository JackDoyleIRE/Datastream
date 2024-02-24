import random
import time

class DataGenerator:
    def generate_data(self):
        vector_type = random.choice(['point', 'line', 'polygon'])
        if vector_type == 'point':
              return {
                'type': 'point',
                'coordinates': [random.uniform(-180, 180), random.uniform(-90, 90)],
                'attributes': {'attribute1': 'value1', 'attribute2': 'value2'}
            }  
        elif vector_type == 'line':
            # Generating a line with random number of vertices
            num_vertices = random.randint(2, 5)
            coordinates = [[random.uniform(-180, 180), random.uniform(-90, 90)] for _ in range(num_vertices)]
            return {
                'type': 'line',
                'coordinates': coordinates,
                'attributes': {'attribute1': 'value1', 'attribute2': 'value2'}
            }
        elif vector_type == 'polygon':
            # Generating a polygon with random number of vertices
            num_vertices = random.randint(3, 6)
            coordinates = [[random.uniform(-180, 180), random.uniform(-90, 90)] for _ in range(num_vertices)]
            # Closing the polygon by repeating the first vertex at the end
            coordinates.append(coordinates[0])
            return {
                'type': 'polygon',
                'coordinates': coordinates,
                'attributes': {'attribute1': 'value1', 'attribute2': 'value2'}
            }


if __name__ == "__main__":
    data_generator = DataGenerator()
    data_generator.stream_data()
