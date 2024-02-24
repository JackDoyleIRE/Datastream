import apache_beam as beam
import requests

class ProcessStreamData(beam.DoFn):
    def process(self, element):
        # Make a request to the API endpoint to get the data
        api_url = "http://flask-app:8000/stream-data" 
        
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print("Processed data:", data)
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")

def run():
    with beam.Pipeline() as pipeline:
        # Use a dummy source, as we fetch data from the API in the ParDo transform
        (pipeline
         | "CreateDummyData" >> beam.Create([None])
         | "ProcessStreamData" >> beam.ParDo(ProcessStreamData()))

if __name__ == "__main__":
    run()
