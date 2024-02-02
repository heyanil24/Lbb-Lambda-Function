import json

def lambda_handler(event, context):
    site_health_score = 90   (  logic )
    return  {
        "statusCode": 200,
       'body': json.dumps({'site_health_score': site_health_score_value})
        # "message": "hello world", 
    }
    return response
