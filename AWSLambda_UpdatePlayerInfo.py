import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    
    #Get table
    table = dynamodb.Table('AWSDBTest')
    
    #Convert body(raw)(JSON) into python obj
    body = json.loads(event['body'])
    
    #update item
    table.update_item(
        Key={
            'user_id': body['user_id'],
        },
        UpdateExpression='SET skill_level = :val1',
        ExpressionAttributeValues={
            ':val1': body['skill_level']
        }
    )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
