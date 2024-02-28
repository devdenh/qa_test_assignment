from selenium.webdriver.common.by import By
from pages.base_page import BasePage


LOCATOR_TENSOR_PEOPLE_POWER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div')
LOCATOR_TENSOR_PEOPLE_POWER_DETAILS = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
LOCATOR_TENSOR_WORKING_DIV = (By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')


class Tensor(BasePage):

    """
     Класс с методами которые описывают необходимые действия
     для реализации тестового сценария на странице https://tensor.ru/
     """

    def __init__(self, driver):
        super().__init__(driver)

    def is_people_power(self):
        self.find_element(LOCATOR_TENSOR_PEOPLE_POWER, time=4).is_displayed()

    def open_about(self):
        self.click_button(LOCATOR_TENSOR_PEOPLE_POWER_DETAILS)

    def is_images_same(self):
        working_images = self.find_elements(LOCATOR_TENSOR_WORKING_DIV, time=5)
        first_img_size = working_images[0].size
        return all(first_img_size == img.size for img in working_images[1:])
