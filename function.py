import json
import datetime

# THIS IS VSCODE Specific
import ptvsd
print('waiting for debugger... you should start it now')
# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()
print('debugger attached')
# END VSCODE SPECIFIC


def lambda_handler(event, context):
    current_time = str(datetime.datetime.now())
    response_body = {
        "message": "Hello, world!",
        "current_time": current_time
    }
    print(response_body)
    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
    return response
