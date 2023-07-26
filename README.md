# FastAPI Faker Server
This is a FastAPI based server that generates fake data using the Faker library. This server can be used to quickly generate mock data for testing or development purposes.

# Features
- Get a list of available fields that can be used to generate data.
- Generate data with custom fields and in different locales.
- Limit the number of data entries to be generated.
# Endpoints
- `/available_field`s: Returns a list of fields available for data generation.
- `/{any}`: Returns fake data entries. You can specify the locale, limit the number of entries, and optionally provide specific fields.
# Quick Start
1. Clone this repository.
2. Install the requirements: pip install -r requirements.txt
3. Run the server: python main.py
4. Visit http://localhost:8000/docs for the interactive API documentation.

# Contributing
Contributions are welcome! Please open an issue if you find a bug or wish to propose a feature. Pull requests are also appreciated.

# License
MIT
