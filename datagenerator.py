import random
import time

class DataGenerator:
    def generate_data(self):
        return {
            'timestamp': time.time(),
            'value': random.randint(1, 100)
        }

    def stream_data(self, interval=1):
        while True:
            data = self.generate_data()
            print(data)  # In a real scenario, you'd send this data to the streaming API
            time.sleep(interval)

# Example Usage
if __name__ == "__main__":
    data_generator = DataGenerator()
    data_generator.stream_data()
