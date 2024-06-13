import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

from exceptions.error_messages import ErrorMessage
from exceptions.custom_exception import CustomException

ENVIRONMENT = os.environ.get("ENVIRONMENT")
AWS_REGION = os.environ.get("AWS_REGION")
ENDPOINT_URL = None if ENVIRONMENT != "local" else "http://localhost"

class ExampleEModel(Model):
    class Meta:
        table_name  = "example_table"
        region      = AWS_REGION
        host        = ENDPOINT_URL

    # NumberAttribute:数値型 UnicodeAttribute:文字列
    id                      = UnicodeAttribute(hash_key=True)

def get():
    try:
        return {'id': 'test'}
    except ExampleEModel.DoesNotExist:
        raise CustomException(ErrorMessage.CUSTOM_ERROR_EXAMPLE)
