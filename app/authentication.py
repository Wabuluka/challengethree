from app import app
from werkzeug import safe_str_cmp
from app.user import User
users = [
    User(1, 'bob', '123')
]

username_mapping = {u.username: u for u in users}
userid_mapping ={u.id: u for u in users }


userid_mapping= {1:{
        'id':1,
        'username':'bob',
        'password': '123'
    }
}

def authenticate(username, password): 
    user = username_mapping.get(username,None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)
