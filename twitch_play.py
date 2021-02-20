import socket, pynput, time

import passwords

server = 'irc.chat.twitch.tv'
port = 6667
nickname = '' # bot name here
token = passwords.token
channel = '#mizkif'


sock = socket.socket()
sock.connect((server,port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))



key = pynput.keyboard.Controller()

while True:
    resp = sock.recv(2048).decode('utf-8')
    command = resp.split(channel)[-1].replace(':', '').rstrip().strip(' ')
    command = command.lower()

    if command == 'up':
        key.press('w')
        time.sleep(.1)
        key.release('w')
        print('up!')

    elif command == 'down':
        key.press('s')
        time.sleep(.1)
        key.release('s')
        print('down!')

    elif command == 'left':
        key.press('a')
        time.sleep(.1)
        key.release('a')
        print('left!')

    elif command == 'right':
        key.press('d')
        time.sleep(.1)
        key.release('d')
        print('right!')

    elif command == 'a':
        key.press('x')
        time.sleep(.03)
        key.release('x')
        print('A Button!')
        
    elif command == 'b':
        key.press('z')
        time.sleep(.03)
        key.release('z')
        print('z Button!')

    elif command == 'start':
        key.press('v')
        time.sleep(.03)
        key.release('v')
        print('Start Button!')

    elif command == 'leftb':
        key.press('q')
        time.sleep(.03)
        key.release('q')
        print('Left B Button!')

    elif command == 'rightb':
        key.press('e')
        time.sleep(.03)
        key.release('e')
        print('Right B Button!')

    elif 'PING' in resp:
        sock.send(resp.replace('PING', 'PONG').encode('utf-8'))
        print(resp)
    else:
        pass
