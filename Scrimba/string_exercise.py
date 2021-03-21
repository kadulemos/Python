msg='welcome to Python 101: Strings'
    #012345678901234567890123456789
    #098765432109876543210987654321
message = msg[18] + ' ' + msg[:8] + msg[25:29] + ' ' + msg[8:11] + msg[13] + msg[12] + msg[2] + msg[1] + msg[25]

print(message.title())

#Backwards
print(message[::-1].title())