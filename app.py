import openai
from dateutil.parser import parse
from datetime import timedelta
import json

openai.api_key = 'your_api_key'

def process_user_query(query):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        logprobs=None,
        echo=True
    )
    print("API Response:", response)  # Print API response for debugging
    return response.choices[0].text.strip()

def extract_information(response):
    # Parse the response to extract relevant information
    # You'll need to implement this part based on your specific use case
    # Extract entity, parameter, start date, end date, and handle multiple companies or comparison requests
    # Handle variations in user queries and error cases
    # Return the extracted information as a dictionary
    extracted_info = {
        "entity": "Company X",
        "parameter": "Revenue",
        "start_date": "2023-01-01",
        "end_date": "2023-12-31"
    }
    return extracted_info

def handle_dates(start_date, end_date):
    # If start date and end date are not provided, set defaults
    if not start_date:
        start_date = (parse('today') - timedelta(days=365)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = parse('today').strftime('%Y-%m-%d')
    
    # Convert dates to ISO 8601 format
    start_date_iso = parse(start_date).strftime('%Y-%m-%d')
    end_date_iso = parse(end_date).strftime('%Y-%m-%d')
    
    return start_date_iso, end_date_iso

# Example usage
query = "What is the revenue of Company X from 2021 to 2022?"
processed_query = process_user_query(query)
print("Processed Query:", processed_query)  # Print processed query for debugging

extracted_info = extract_information(processed_query)
print("Extracted Information:", extracted_info)  # Print extracted information for debugging

start_date_iso, end_date_iso = handle_dates(extracted_info['start_date'], extracted_info['end_date'])
print("Start Date (ISO 8601):", start_date_iso)
print("End Date (ISO 8601):", end_date_iso)

# Generate JSON output
json_output = json.dumps(extracted_info, indent=4)
print("JSON Output:")
print(json_output)
