from tkinter import *
from bs4 import BeautifulSoup
import requests

root = Tk()
root.geometry("700x450")
root.resizable(0,0)
root.title("Krynx.exe")
root.config(bg = "LightGreen")

print_panel = StringVar()

def gtx1080():
    url = "https://www.newegg.com/evga-geforce-gtx-1080-fe-08g-p4-6180-rx/p/N82E16814487322?Description=Nvidia%20GTX%201080&cm_re=Nvidia_GTX%201080-_-14-487-322-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text="$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def gtx1070():
    url = "https://www.newegg.com/nvidia-geforce-gtx-1070/p/1FT-0004-001T6?Description=Nvidia%20GTX%201070&cm_re=Nvidia_GTX%201070-_-1FT-0004-001T6-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text="$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def gtx1660ti():
    url = "https://www.newegg.com/gigabyte-geforce-gtx-1660-ti-gv-n166toc-6gd/p/N82E16814932131?Item=9SIAPNMG017509&Description=Nvidia%20GTX%201660&cm_re=Nvidia_GTX%201660-_-9SIAPNMG017509-_-Product&cm_sp=SP-_-949655-_-0-_-2-_-9SIAPNMG017509-_-Nvidia%20GTX%201660-_-1660|gtx-_-3"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def gtx1650():
    url = "https://www.newegg.com/msi-geforce-gtx-1650-gtx-1650-4gt-lp-oc/p/N82E16814137480?Item=9SIAPNMEUJ7383&Description=Nvidia%20GTX%201650&cm_re=Nvidia_GTX%201650-_-9SIAPNMEUJ7383-_-Product&cm_sp=SP-_-966519-_-0-_-2-_-9SIAPNMEUJ7383-_-Nvidia%20GTX%201650-_-1650|gtx-_-4"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def rtx3050():
    url = "https://www.newegg.com/gigabyte-geforce-rtx-3050-gv-n3050gaming-oc-8gd/p/N82E16814932496?Description=rtx%203050&cm_re=rtx_3050-_-14-932-496-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def rtx3060elite():
    url = "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060aorus-e-12gd/p/N82E16814932431?Description=rtx%203060&cm_re=rtx_3060-_-14-932-431-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def rtx3070ti():
    url = "https://www.newegg.com/gigabyte-geforce-rtx-3070-ti-gv-n307tgaming-oc-8g/p/N82E16814932443?Description=rtx%203070&cm_re=rtx_3070-_-14-932-443-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def rtx3080():
    url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-12gd/p/N82E16814932489?Description=rtx%203080&cm_re=rtx_3080-_-14-932-489-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def rtx3080fe():
    url = "https://www.newegg.com/p/1FT-0004-007N9?Description=rtx%203080%20founders%20edition&cm_re=rtx_3080%20founders%20edition-_-9SIARUXHT48523-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)


def rtx3090():
    url = "https://www.newegg.com/gigabyte-geforce-rtx-3090-gv-n3090gaming-oc-24gd/p/N82E16814932327?Description=rtx%203090&cm_re=rtx_3090-_-14-932-327-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)
def rtx3090fe():
    url = "https://www.newegg.com/nvidia-9001g1362510000/p/1FT-0004-007J3?Description=rtx%203090%20founders%20edtion&cm_re=rtx_3090%20founders%20edtion-_-1FT-0004-007J3-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def EXIT():
    root.destroy()

Label(root, text = "GTX", font="AgencyFb", bg= "LightGreen").place(x=220, y=30)
Label(root, text = "RTX", font="AgencyFb", bg= "LightGreen").place(x=70, y=30)
Label(root, text = "Founders Editions", font="AgencyFb", bg= "LightGreen").place(x=390, y=30)

Label(root, text = "Price: ", font=("AgencyFb", 15), bg = "LightGreen").place(x=165, y=355)
Entry(root,textvariable = print_panel, font = ("Arial", 15 ), bg = "LightGreen").place(x=220, y=355)


Button(root,text = "Quit", font = "ColonnaMT", command = EXIT, bg= "SlateGray").place(x=500, y=400)

Button(root,text = "GTX 1080", font = "ColonnaMT", command = gtx1080, bg= "SlateGray3",).place(x=220, y=100)
Button(root,text = "GTX 1070", font = "ColonnaMT", command = gtx1070, bg= "SlateGray3").place(x=220, y=140)
Button(root,text = "GTX 1650", font = "ColonnaMT", command = gtx1650, bg= "SlateGray3").place(x=220, y=180)
Button(root,text = "GTX 1660 TI", font = "ColonnaMT", command = gtx1660ti, bg= "SlateGray3").place(x=220, y=220)
Button(root,text = "RTX 3050", font = "ColonnaMT", command = rtx3050, bg= "SlateGray3").place(x=50, y=100)
Button(root,text = "RTX 3060 Elite", font = "ColonnaMT", command = rtx3060elite, bg= "SlateGray3").place(x=50, y=140)
Button(root,text = "RTX 3070 TI", font = "ColonnaMT", command = rtx3070ti, bg= "SlateGray3").place(x=50, y=180)
Button(root,text = "RTX 3080", font = "ColonnaMT", command = rtx3080, bg= "SlateGray3").place(x=50, y=220)
Button(root,text = "RTX 3090", font = "ColonnaMT", command = rtx3090, bg= "SlateGray3").place(x=50, y=260)
Button(root,text = "RTX 3080 Founders Edition", font = "ColonnaMT", command = rtx3080fe, bg= "SlateGray3").place(x=370, y=100)
Button(root,text = "RTX 3090 Founders Edition", font = "ColonnaMT", command = rtx3090fe, bg= "SlateGray3").place(x=370, y=140)
root.mainloop() 