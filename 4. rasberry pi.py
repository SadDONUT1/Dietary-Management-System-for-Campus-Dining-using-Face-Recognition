import socket
import time
import tkinter
import tkinter.ttk
from datetime import datetime
import matplotlib
from PIL import Image, ImageTk

def make_window(food_list, school_id, info_dic):
    global window
    # global window
    window = tkinter.Tk()
    icon = ImageTk.PhotoImage(Image.open(info_dic[school_id][2]))

    window.title("Safe Meals")  # 제목
    window.geometry("1920x1080")  # 윈도우 창의 너비와 높이, 초기 윈도우 위치 좌표
    window.resizable(True, True)  # 상하 좌우

    label = tkinter.Label(window, text="Safe Meals", font=("Arial", 100, 'bold'))  # label 이라는 위젯 설정
    label.pack()

    label_school_id = tkinter.Label(window, text=f"Student ID: {school_id}", font=("Arial", 50))  # label 이라는 위젯 설정
    label_school_id.pack()

    label_name = tkinter.Label(window, text=f"Student Name: {info_dic[school_id][0]}", font=("Arial", 50))  # label 이라는 위젯 설정
    label_name.pack()
    
    label_student_image = tkinter.Label(window, text=f"Student image:", font = ("Arial", 50), justify="left")
    label_student_image.pack()
    
    label_student_image = tkinter.Label(window, image = icon)
    label_student_image.pack()

    treeview = tkinter.ttk.Treeview(window, columns=["#0", "#1"], displaycolumns=["#0", "#1"])
    treeview.pack()

    treeview.column("#0", width=70, anchor="center")
    treeview.heading("#0", text="Food number", anchor="center")

    treeview.column("#2", width=300, anchor="center")
    treeview.heading("#2", text="Allergy",anchor="center")

    treeview.column("#1", width=200, anchor="center")
    treeview.heading("#1", text="Food", anchor="center")

    for i in range(len(food_list)):
        flag = False
        for k in range(len(dic[school_id][1])):
            if str(dic[school_id][1][k]) in food_list[i][1]:
                flag = True
                
        if flag == True:
            treeview.insert('', 'end', text=(i + 1), values=("{}".format(food_list[i][0]), "X"))
        else:
            treeview.insert('', 'end', text=(i + 1), values=("{}".format(food_list[i][0]), "O"))
    window.mainloop()
    
HOST = '172.30.88.219'  # ifconfig
# Server IP or Hostname
PORT = 20000
# Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

dic = {
    "12345": ['원석', [1, 5, 9, 10, 15], "/Users/wonseokhan/Desktop/Visual Studio Code/Python/EPQ/safemeal/dataset/12345.1.jpg"],
    "12346": ['수경', [9, 15, 17], "/Users/wonseokhan/Desktop/Visual Studio Code/Python/EPQ/safemeal/dataset/12345.2.jpg"],
}

# managing error exception
try:
    s.bind((HOST, PORT))
except socket.error:
    print('Bind failed ')

s.listen(5)
print('Socket awaiting messages')
(conn, addr) = s.accept()
print('Connected')

# awaiting for message
cnt = 0
device_food = []
now_tkinter_on = False
while True:
    data = conn.recv(1024)
    data = data.decode('utf-8')
    if cnt == 0:
        data = eval(data)
        cnt += 1
        food_list = data
    else:
        school_id = data
        if len(school_id) != 5:
            continue
        print('school id:', data)
        print('name:', dic[data][0])
        print('no food num:', dic[data][1])
        print('\n')
        make_window(food_list, school_id, dic)
        
    data = ''

conn.close()
# Close connections