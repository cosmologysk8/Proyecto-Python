from tkinter import font
from bs4 import BeautifulSoup
import bs4
from bs4.builder import HTMLTreeBuilder
from tkinter import *
from tkinter import ttk
import requests
from requests.models import parse_url

window = Tk()

window.title("Mi APP")

#VARIABLES CONSTANTES 

url_pagina = 'https://www.theroomsk8.com/categoria-producto/skateshop/tablas/'

tablas_skate = {
    "url_imagen":"",
    "nombre": "",
    "boton_acceder": "",
}

def cargar_pagina():
    
    html = requests.get('https://www.theroomsk8.com/categoria-producto/skateshop/tablas/').content
    pagina = BeautifulSoup(html, 'html.parser')

    return pagina

def cargar_elementos():
    pagina = cargar_pagina()
    list_elementos = pagina.findAll("div",{"class": "product type-product post-29781 status-publish first instock product_cat-skateshop product_cat-tablas product_tag-carmona product_tag-jacobo product_tag-room product_tag-step-to-my product_tag-tabla product_tag-the-room has-post-thumbnail taxable shipping-taxable purchasable product-type-variable tcol-md-3 tcol-sm-4 tcol-xs-6 tcol-ss-12 skateshop tablas kad_product"})
    for elemento in list_elementos:
        url_imagen = elemento.find("div", {"class": "https://i2.wp.com/www.theroomsk8.com/wp-content/uploads/2021/11/step-to-my-room-2.jpg?fit=2000%2C2000&ssl=1&resize=300%2C300"})
        





window.mainloop()