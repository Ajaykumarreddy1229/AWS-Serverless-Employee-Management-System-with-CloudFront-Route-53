import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employees')

def lambda_handler(event, context):

    for record in event['Records']:

        employee = json.loads(record['body'])

        table.put_item(
            Item=employee
        )

        print("Employee inserted:", employee)

    return {
        'statusCode': 200
    }


