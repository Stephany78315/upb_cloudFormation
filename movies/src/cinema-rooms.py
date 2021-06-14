import json
import boto3
import os

users_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getCinema(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/cinema-rooms/cinema_01"
    array_path = path.split("/") # ["", "movie", "cinema_01"]
    cinema_id = array_path[-1]
    
    # response = table.get_item(
    #     Key={
    #         'pk': cinema_id
    #     }
    # )
    # item = response['Item']
    # #print(item)
    return {
        #'statusCode': 200,
        'body': json.dumps("get cinema")
    }
    
def putCinema(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/movie/movie_01
    array_path = path.split("/") # ["", "movie", "movie_01"]
    cinema_id = array_path[-1]
    
    body = event["body"] 
    body_object = json.loads(body)
    
    
    # table.put_item(
    #     Item={
    #         'pk': cinema_id,
    #         'sk': ,
    #         'schedule': body_object['schedule'],
    #         '3D': body_object['3D'],
    #         'people-attend': body_object['year']
    #     }
    # )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Put Cinema Exitoso')
    }

def seatsAvailable(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/cinema-rooms/cinema_01"
    array_path = path.split("/") # ["", "movie", "cinema_01"]
    cinema_id = array_path[-1]
    
    # response = table.get_item(
    #     Key={
    #         'pk': cinema_id
    #     }
    # )
    # item = response['Item']
    # #print(item)
    return {
        #'statusCode': 200,
        'body': json.dumps("5.- seatsAvailable")
    }
