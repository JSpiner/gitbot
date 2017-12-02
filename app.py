from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
	return 'hello world'

@app.route('/git', methods=['POST'])
def route_git():
    data = request.get_json()
    print(data)
    return 'received'

if __name__ == '__main__': 
  app.run(host='0.0.0.0')