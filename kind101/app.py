from bottle import Bottle, response
import socket
import json
from typing import Dict, Any

app = Bottle()

@app.route('/')
def get_hostname() -> Dict[str, Any]:
    hostname = socket.gethostname()
    data = {'hostname': hostname}
    response.content_type = 'application/json'
    res = json.dumps(data)
    print(res)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

