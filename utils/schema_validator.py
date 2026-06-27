import json
from jsonschema import validate

class SchemaValidator:

    @staticmethod
    def validate_schema(response_data, schema_path):

        with open(schema_path) as file:
            schema = json.load(file)

        validate(instance=response_data, schema=schema)