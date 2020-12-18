import boto3
import os
import random, string
from dotenv import load_dotenv


load_dotenv(".env")

dynamodb = boto3.resource("dynamodb",
    aws_access_key_id= os.getenv("ACCESS_KEY_ID"),
    aws_secret_access_key= os.getenv("ACCESS_SECRET_KEY"),
    region_name= os.getenv("REGION")
    #aws_session_token= keys.ACCESS_SESSION_TOKEN
    )

from boto3.dynamodb.conditions import Key, Attr

class User_info:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
		user_id = name + str(res)
		self.id = user_id

	def insert_item(self):
		table = dynamodb.Table('userdata')
		table.put_item(
			Item={
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'id': self.id
			}
			)

class Check_info:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self._list = []

	def check_user(self):
		table = dynamodb.Table('userdata')
		response = table.query(
			KeyConditionExpression=Key('email').eq(self.email)
			)
		items = response['Items']
		if items and self.password == items[0]['password']:
			checked = True
			name = items[0]['name']
			user_id = items[0]['id']
		else:
			checked = False
			name, user_id = None, None
		self._list.extend([checked, name, user_id])
	def get_list(self):
		return self._list

