from tkinter import *
from tkinter import font, ttk
import bs4
import requests
from bs4 import BeautifulSoup
from bs4.builder import HTMLTreeBuilder
from requests.models import parse_url

window = Tk()

window.title("Mi APP")

#VARIABLES CONSTANTES 

url_pagina = 'https://www.theroomsk8.com/categoria-producto/skateshop/tablas/'

tablas_skate = {
    "url_imagen":"",
    "nombre": "",
    "precio": "",
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
        url_imagen = elemento.find("div", {"class": "kad_img_flip image_flip_front"}).find('img').attrs['src']
        nombre = elemento.find("div", {"class": "details_product_item"}).find("div", {"class": "product_details"}).find("a",{"class": "product_item_link product_title_link"}).find('h5').text
        precio = elemento.find("")
        





window.mainloop()
