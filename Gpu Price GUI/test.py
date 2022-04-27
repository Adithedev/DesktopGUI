from bs4 import BeautifulSoup
import requests

def gtx1080():
    url = "https://www.newegg.com/evga-geforce-gtx-1080-fe-08g-p4-6180-rx/p/N82E16814487322?Description=Nvidia%20GTX%201080&cm_re=Nvidia_GTX%201080-_-14-487-322-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text="$")
    parent = tags[0].parent
    strong = parent.find("strong")
    print (strong)