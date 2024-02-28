from pages.sbis import Sbis
from pages.tensor import Tensor


def test_first_scenario(browser):
    sbis = Sbis(browser)
    tensor = Tensor(browser)
    sbis.open_contacts()
    sbis.click_on_tensor_banner()
    tensor.is_people_power()
    tensor.open_about()
    assert browser.current_url == "https://tensor.ru/about"
    assert tensor.is_images_same()
