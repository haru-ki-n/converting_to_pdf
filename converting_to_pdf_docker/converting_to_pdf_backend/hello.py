import fastapi
import sys
def handler(event, context): 
    response = 'Hello, This is Lambda Test\n' + event['request_messege'] + '\n' + context.function_name
    return response