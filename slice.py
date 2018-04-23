"""
    Slice string
"""
string = "abcdefghijklmnopqrstuvwxyz"

print("From start to fourth letter")
print(string[:4])

print("\nFrom fifth letter to eighth")
print(string[4:8])

print("\nFrom ninth letter to end")
print(string[8:])

print("\nFrom start to three letters before end")
print(string[:-3])

print("\nOnly last three letters")
print(string[-3:])

print("\nAntepenultimate letter")
print(string[-3:-2])

print("\nFrom start to end with shift of one letter")
print(string[::2])

print("\nFrom end to start")
print(string[::-1])

print("\nFrom end to start with shift of one letter")
print(string[::-2])
