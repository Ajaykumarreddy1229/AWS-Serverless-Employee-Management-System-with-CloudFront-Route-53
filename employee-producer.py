import json
import boto3
import uuid
import os

sqs = boto3.client('sqs')

QUEUE_URL = os.environ['QUEUE_URL']

def lambda_handler(event, context):

    body = json.loads(event['body'])

    employee = {
        "id": str(uuid.uuid4()),
        "name": body['name'],
        "email": body['email'],
        "department": body['department']
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(employee)
    )

    return {
        "statusCode": 200,

        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },

        "body": json.dumps({
            "message": "Employee added to queue"
        })
    }

