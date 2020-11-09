import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    requestedId = event["queryStringParameters"]["user_id"]
    #requestedId = event["body"]["user_id"]
    
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    
    #Get table
    table = dynamodb.Table('AWSDBTest')
    
    #Get item using table   
    response = table.get_item(
        Key={
            'user_id': requestedId
        }
    )
    item = response['Item']
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }