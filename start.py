import itchat
import tkinter as tk

def search_donate():
    query = "your search query"
    url = f"bitcoin:bc1qnk0ftxa4ep296phhnxl5lv9c2s5f8xakpcxmth?message=Donate={query}"
    webbrowser.open(url)

def send_message():
    itchat.send('替换您要轰炸的字词', toUserName='替换您要轰炸的人')
    root.after(1000, send_message)  # Schedule the next message after 1000 milliseconds (1 second)

def start_bombardment():
    # Login to WeChat
    itchat.auto_login(hotReload=True)
    
    # Start sending messages
    send_message()

# Initialize Tkinter
root = tk.Tk()
root.title('微信轰炸机')

# Create start button
start_button = tk.Button(root, text='开始轰炸', command=start_bombardment)
start_button.pack()

start_button = tk.Button(root, text='Donate BTC', command=search_donate)

# Run the Tkinter event loop
root.mainloop()