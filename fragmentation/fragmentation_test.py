frame = []
msg = input("MSG")
size = 4
for i in range(0,len(msg),size):
    frame.append(msg[i:i+size])

print('fragment msg: {}',format(frame))
print('재조립된 메시지: {}',format(''.join(frame)))