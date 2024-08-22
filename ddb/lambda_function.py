import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.put_item(
        TableName = 'MyTable',
        Item = {
              'id': {'S': context.aws_request_id, },
              'event': {'S': json.dumps(event), },
        } 
    )
    return {
    "statusCode": 200,
    "body": json.dumps(response)
}

