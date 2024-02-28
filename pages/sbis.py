import os
import time
from urllib import request

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

LOCATOR_SBIS_TENSOR_BANNER = (
    By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
)
LOCATOR_SBIS_REGION = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
)
LOCATOR_SBIS_CONTACTS_LIST = (
    By.CLASS_NAME, 'sbisru-Contacts-List__col-1'
)
LOCATOR_SBIS_REGION_KAMCHATSKIJ_KRAJ = (
    By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span'
)
LOCATOR_SBIS_DOWNLOAD_FOOTER = (
    By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a'
)
LOCATOR_SBIS_FILE_DOWNLOAD = (
    By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink'
)
LOCATOR_SBIS_DOWNLOAD_PLUGIN = (
    By.XPATH, '//*[@id="ws-6dfkbpv5zkq1709036961933"]/div[2]'
)


class Sbis(BasePage):

    """
    Класс с методами которые описывают необходимые действия
    для реализации тестового сценария на странице https://sbis.ru/
    """

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.driver.get('https://sbis.ru/')

    def open_contacts(self):
        self.driver.get("https://sbis.ru/contacts")

    def click_on_tensor_banner(self):
        tensor_banner = self.find_element(LOCATOR_SBIS_TENSOR_BANNER, time=4).click()
        self.switch_window()
        return tensor_banner

    def get_region_text(self):
        return self.find_element(LOCATOR_SBIS_REGION).text

    def get_contacts_list(self):
        return self.find_elements(LOCATOR_SBIS_CONTACTS_LIST)

    def switch_region_kamchatskij_kraj(self):
        self.find_element(LOCATOR_SBIS_REGION).click()
        self.find_element(LOCATOR_SBIS_REGION_KAMCHATSKIJ_KRAJ).click()
        time.sleep(2)

    def get_first_contact_text(self):
        return self.get_contacts_list()[0].text

    def open_download_footer(self):
        self.click_button(LOCATOR_SBIS_DOWNLOAD_FOOTER)

    def get_download_class(self):
        return self.find_element(LOCATOR_SBIS_FILE_DOWNLOAD)

    def get_download_href(self):
        """
         не смог напрямую найти элемент, получилось через дочерний тег 'a'
         возвращает ссылку вида:
         https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe
        """
        return self.get_download_class().find_element(By.TAG_NAME, 'a').get_property('href')

    def compare_file_sizes(self):
        d_class_text = self.get_download_class().text
        d_link = self.get_download_href()
        self.download_sbis_file(d_link)
        return self.get_downloaded_sbis_filesize(), self.get_file_size_from_link(d_class_text)

    def get_file_size_from_link(self, link):
        return ''.join([i for i in link if i.isdigit()])

    def download_sbis_file(self, link):
        name = 'sbis.exe'
        # request.urlretrieve(link, name)

    def get_downloaded_sbis_filesize(self):
        file_size = os.path.getsize('sbis.exe') / 1048576
        file_size = str(round(file_size, 2)).replace('.', '')
        return file_size
