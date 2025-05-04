from PyInstaller.__main__ import run

def main():
    try:
        run([
            '--onefile',
            '--icon=BuperSher.ico',
            '--name=BuperSher',

            'start.py',

            'assist.py',
        ])
        print("打包完成")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == '__main__':
    main()
