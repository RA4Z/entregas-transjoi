from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://quick.transjoi.com.br/web/")

class NavegarWeb():
    def transjoi(cnpj, numero_documento):
        driver.implicitly_wait(5)
        elemCNPJ = driver.find_element(By.NAME, "cnpj")
        elemFiscal = driver.find_element(By.NAME, "notafiscal")
        elemDestinatario = driver.find_element(By.XPATH, '//*[@id="buscacte"]/div[1]/div[2]/label/span[4]')

        driver.implicitly_wait(5)
        elemCNPJ.clear()
        elemFiscal.clear()

        elemCNPJ.send_keys(cnpj)
        elemFiscal.send_keys(numero_documento)
        elemDestinatario.click()
        driver.implicitly_wait(5)

        elemFiscal.send_keys(Keys.RETURN)

        driver.implicitly_wait(30)

        dataColetado = driver.find_element(By.XPATH, '//*[@id="infocte"]/table/tbody/tr[2]/td[3]').get_attribute("innerHTML")
        dataEntregue = driver.find_element(By.XPATH, '//*[@id="infocte"]/table/tbody/tr[6]/td[3]').get_attribute("innerHTML")

        indiceColetado = dataColetado.find(' ')
        indiceEntregue = dataEntregue.find(' ')

        dataColetado = dataColetado[:indiceColetado]
        dataEntregue = dataEntregue[:indiceEntregue]

        driver.implicitly_wait(5)
        return '{}, {}'.format(dataColetado, dataEntregue)

    def fechar():
        driver.close()

    def nova_consulta():
        driver.get("https://quick.transjoi.com.br/web/")
        driver.implicitly_wait(30)