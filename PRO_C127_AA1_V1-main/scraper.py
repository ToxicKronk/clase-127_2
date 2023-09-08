from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
browser = webdriver.Chrome("C:/Users/Owen/Downloads/PRO_C127_AA1_V1-main/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        soup=BeautifulSoup(browser.page_source, "html.parser")
        for tags_ul in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = tags_ul.find_all("li")
            temp_list=[]
            for tag_num, tag in enumerate(li_tags):
                if tag_num == 0:
                    temp_list.append(tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tag.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by = By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 

        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas
dataframe = pd.DataFrame(planets_data, columns= headers)

# Convertir a CSV
dataframe.to_csv("Exoplanetas_Info.csv", index=True, index_label="id")
    


