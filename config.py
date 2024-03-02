import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
print(dotenv_path)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    USERFILE = os.environ.get("USERFILE")
    print("APP_NAME is {}".format(os.environ.get("APP_NAME")))
    print("USER FILE is {}".format(USERFILE))
    db_file_path=os.path.join(os.path.dirname(__file__),os.environ.get("DB_FILE"))
    print(db_file_path)
    connection_string="sqlite:///" + db_file_path
    print(connection_string)
else:
    raise RuntimeError("Not found application configuration")