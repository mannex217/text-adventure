import time
print("To start, type \'commit murder\'")
fromUser = input()
while True:
    if fromUser == "commit murder":
        print("Very well")
    elif fromUser == "quit":
        print("good choice")
        break
    else:
        print("To start, type \'commit murder\'")
    fromUser = input()
