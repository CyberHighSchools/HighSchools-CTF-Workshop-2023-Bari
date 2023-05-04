from flask import Flask, send_file, render_template, request, jsonify
from os import getenv
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html', flag_enc = encrypt(getenv('FLAG').encode(), getenv('KEY').encode()))

xor = lambda a, b: bytes([int(x) ^ int(y) for x, y in zip(a, b)]) # from danidisp import xor

def encrypt(plain: bytes, key: bytes) -> str:
	if len(key) == 0:
		return ''
	if len(key) < len(plain):
		key = key * (len(plain)//len(key) + 1)
	return xor(plain, key).hex()

@app.route('/api/xor', methods=['POST'])
def xored_value():
	json = request.get_json()
	text = bytes.fromhex(json['text'])
	key = json['key'].encode()
	result = encrypt(text, key)
	return jsonify({'ascii': bytes.fromhex(result).decode(), 'hex': result})
	
if __name__ == '__main__':
    from waitress import serve
    serve(app, port=8080, host="0.0.0.0")
