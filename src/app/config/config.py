import os

from dotenv import load_dotenv

load_dotenv()

SERVICE_HOST = os.environ.get('SERVICE_HOST')
SERVICE_PORT = os.environ.get('SERVICE_PORT')
