import apache_beam as beam
import logging
import requests

class ProcessStreamData(beam.DoFn):
    def process(self, element):
        # Log custom message
        logging.info("Processing stream data...")

        # Make a request to the API endpoint to get the data
        api_url = "http://flask-app:8000/stream-data"

        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Processed data: {data}")
        else:
            logging.error(f"Failed to fetch data from API. Status code: {response.status_code}")

def run():
    # Log custom message
    logging.info("Beam pipeline is running.")

    with beam.Pipeline(runner='PortableRunner', options=options) as pipeline:
        # Use a dummy source, as we fetch data from the API in the ParDo transform
        result = (
            pipeline
            | "CreateDummyData" >> beam.Create([None])
            | "ProcessStreamData" >> beam.ParDo(ProcessStreamData()))
        
        # Optionally, you can log the final result if needed
        result | "LogFinalResult" >> beam.Map(logging.info)

if __name__ == "__main__":
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    # Set Flink job server host as an option
    options = beam.options.pipeline_options.PipelineOptions()
    options.view_as(beam.options.pipeline_options.PortableOptions).job_endpoint = "localhost:8099"  # Adjust the port as needed

    run()

