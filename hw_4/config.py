import os
from dotenv import load_dotenv


load_dotenv()

# чтобы сгенерировать соль - можно воспользоваться функцией bcrypt.gensalt()
password_salt = os.getenv('SALT').encode()
