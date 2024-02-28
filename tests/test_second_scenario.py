from pages.sbis import Sbis


def test_second_scenario(browser):
    sbis = Sbis(browser)
    sbis.open_contacts()
    assert sbis.get_region_text() == 'Челябинская обл.'
    assert len(sbis.get_contacts_list()) > 0
    sbis.switch_region_kamchatskij_kraj()
    assert 'Камчатский край' in browser.title
    assert '41-kamchatskij-kraj?' in browser.current_url
    assert 'Камчатка' in sbis.get_first_contact_text()
