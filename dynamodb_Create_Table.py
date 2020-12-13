import boto3
# Get the service resource.

import key_config as keys

dynamodb = boto3.resource("dynamodb"
    #aws_access_key_id= keys.ACCESS_KEY_ID,
    #aws_secret_access_key= keys.ACCESS_SECRET_KEY
    #aws_session_token= keys.ACCESS_SESSION_TOKEN
    )

#dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'password',
            'KeyType': 'RANGE'
        }
        
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)