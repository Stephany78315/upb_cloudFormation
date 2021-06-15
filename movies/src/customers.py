import json
import boto3
import os

users_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def customerWatched(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/cinema-rooms/cinema_01"
    array_path = path.split("/") # ["", "movie", "cinema_01"]
    customer_id = array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': customer_id,
            'sk': 'info_' + customer_id
        }
    )
    item = response['Item']
    
    
    
    
    
    
    return {
        #'statusCode': 200,
        'body': json.dumps(item)
    }
    
    

