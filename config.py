import os
from dotenv import load_dotenv

load_dotenv()

CRON_USER = os.getenv('CRON_USER', default='root')
