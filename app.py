from flask import Flask
import redis
import os
app = Flask(__name__)

def addVisitor():
    r = redis.Redis(host=os.environ['REDIS_HOST'],port=os.environ['REDIS_PORT'],password=os.environ['REDIS_PASS'],charset="utf-8", decode_responses=True)
    value = r.get('visitor')
    if (value==None):
        r.set('visitor', 0)
        value = r.get('visitor')
        print(value)
        return value
    else:
        value = int(r.get('visitor'))
        value = value + 1
        r.set('visitor', str(value))
        return value

@app.route('/')
def hello_geek():
    visitor = addVisitor()
    return f"<h1>This is the {visitor} visitor</h2>"

if __name__ == "__main__":
    app.run(debug=True)

