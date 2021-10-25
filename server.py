import socket
#initializations
HOST = '127.0.0.1'
PORT = 65433
leftWheels = 'null'
rightWheels = 'null'
speed = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            x = str(data)[2:3]
            #sets speed
            if x.isdigit():
                speed = int(x) * 51
            #sets direction
            else:
                if x == 'w':
                    leftWheels = 'f'
                    rightWheels = 'f'
                if x == 'a':
                    leftWheels = 'r'
                    rightWheels = 'f'
                if x == 's':
                    leftWheels = 'r'
                    rightWheels = 'r'
                if x == 'd':
                    leftWheels = 'f'
                    rightWheels = 'r'
            #only prints if direction is set (assuming speed is set first)
            if leftWheels!= 'null' and rightWheels!= 'null':
                print('['+str(leftWheels)+''+str(speed)+']'+ '['+str(leftWheels)+''+str(speed)+']'+'['+str(rightWheels)+''+str(speed)+']'+'['+str(rightWheels)+''+str(speed)+']')
            if not data:
                break
        conn.sendall(data)
