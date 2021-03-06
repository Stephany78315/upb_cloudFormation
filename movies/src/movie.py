
import json
import boto3
import os
from boto3.dynamodb.conditions import Key

users_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getInfoMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/movie/movie_01"
    array_path = path.split("/") # ["", "movie", "movie_01"]
    user_id = array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'info_' + user_id 
        }
    )
    item = response['Item']
    #print(item)
    return {
        #'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/movie/movie_01"
    array_path = path.split("/") # ["", "movie", "movie_01"]
    user_id = array_path[-1]
    
    body = event["body"] 
    body_object = json.loads(body)
    
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk': 'info_' + user_id, #mejorar
            'title': body_object['title'],
            'actors': body_object['actors'],
            'year': body_object['year']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Put Movie Exitoso')
    }

def roomsPerDay(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/roomsPerDay/movie/movie_01"
    array_path = path.split("/") # ["", "roomsPerDay", "movie","movie_01","date"]
    user_id = array_path[-1]
    
    query_date = event["queryStringParameters"]["date"]
    
    
    
    response = table.query(
        KeyConditionExpression=Key('pk').eq(user_id) & Key('sk').begins_with('cinema_')
    )
   
    #print(json.dumps(response['Items']))
    items = response['Items']
    
    finales = []
    for s in items:
        if s['date'] == '14/6/2021':
            finales.append(s)
    # scan_kwargs = {
    #     'FilterExpression': Key('pk').eq(user_id) & Key('sk').begins_with('cinema_') & 'date = :s',
    #     'ExpressionAttributeNames': ':s' = {"S": "14/6/2021"}
    # }
   
    # schedules = []
    # for f in finales:
    #     schedules = f['schedule']
    #     print('guarda')
        
   
    return {
        'body': json.dumps(finales)
    }
    
   
    
def peopleAttend(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/peopleAttend/movie/{movie_id}/cinema-rooms/{room_id}"
    array_path = path.split("/") # ["", "movie", "movie_id","cinema-rooms","room_id"]
    movie_id = array_path[-3]
    cinema_id = array_path[-1]
    
    
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': cinema_id
        }
    )
    item = response['Item']['customers']
    
    return {
        'body': json.dumps(item)
    }