import base64

f = open('redblue.ico', 'rb')
f1 = open('redblue1.ico', 'wb')

data = base64.b64encode(f.read())
raw = base64.b64decode(data)

f1.write(raw)
print(data)
f.close()
f1.close()
