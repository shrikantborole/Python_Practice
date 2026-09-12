for arr in range(6):
    print(arr)

for arr in range(80):
    if(arr % 2 == 0):
        print(f"Value divide by 2: {arr}")

# Dictionary - Keys maps to the value
acronys = {
            'LOL': 'laugh out loud',
           'TEST' : 'Test',
            'Hello' : 'Hello'
           }

print(acronys)
acronys['Hello'] = 'TEST hello'
print(acronys)
defination = acronys.get('OOO')
print(defination)