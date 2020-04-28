from tkinter import *
import requests


#请求处理
def btnsubmitOp(self):

    url = "http://" + url_entry.get()
    para = para_entry.get()

    result = "请求的地址："+ url
    result = result + "\n请求的方式："
    result = result + ["GET", "POST"][v.get()]
    result = result + "\n请求的参数：" + para

    if v.get() == 1:
        if para == "":
            r = requests.post(url)
            r1 = str(r.json())
            result = result + "\n" + "-" * 20 + "请求结果" + "-" * 20 + "\n" + r1
        else:
            para = eval(para)
            r = requests.post(url, params=para)
            r1 = str(r.json())
            result = result + "\n" + "-" * 20 + "请求结果" + "-" * 20 + "\n" + r1
    else:
        if para == "":
            r = requests.get(url)
            r1 = str(r.json())
            result = result + "\n" + "-" * 20 + "请求结果" + "-" * 20 + "\n" + r1
        else:
            para = eval(para)
            r = requests.get(url, params=para)
            r1 = str(r.json())
            result = result + "\n" + "-" * 20 + "请求结果" + "-" * 20 + "\n" + r1
    text_result.delete(0.0, END)
    text_result.insert(1.0, result)


#插件框
app = Tk()
app.title("HTTP请求模拟  v0.1")
app.geometry('500x500')

#第一行，URL输入
url_label = Label(app, text="URL 链接")
url_label.grid(row=0, column=0, sticky=W,pady=5,padx=10)
url_entry = Entry(app, width=50)
url_entry.grid(row=0, column=1, sticky=W)

#第二行，模式选择
method_label = Label(app,text="POST/GET")
method_label.grid(row=1, column=0,sticky=W,pady=5,padx=10)
fm1 = Frame()
fm1.grid(row=1, column=1, sticky=W)
v=IntVar()
v.set(1)
btn_method = Radiobutton(fm1, variable=v, value=1, text="POST")
btn_method.pack(side = LEFT)
btn_method = Radiobutton(fm1, variable=v, value=0, text="GET")
btn_method.pack()

#第三行，参数填写
para_label = Label(app, text="参数")
para_label.grid(row=2, column=0,sticky=W,pady=5,padx=10)
para_entry = Entry(app, width=50)
para_entry.grid(row=2, column=1, sticky=W)

#第四行，请求发送
btn_submit = Button(app, text="发送")
btn_submit.bind('<Button-1>', btnsubmitOp)
btn_submit.grid(row=3, column=0, sticky=W, padx=10,pady=10)

#第五行，结果框
text_result = Text(app, width=48, height=60)
text_result.grid(row=4, column=0, columnspan=2, sticky=W, padx=10)


app.mainloop()
