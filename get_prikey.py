import json
from eth_keyfile import decode_keyfile_json
keyfile_json = json.loads(open('execution/keystore/UTC--2022-08-19T17-38-31.257380510Z--123463a4b065722e99115d6c222f267d9cabb524').read())
passphrase = open('execution/geth_password.txt').read()
private_key = decode_keyfile_json(keyfile_json, passphrase.encode())
print(private_key.hex())
# 2e0834786285daccd064ca17f1654f67b4aef298acbb82cef9ec422fb4975622