from pages.sbis import Sbis


def test_third_scenario(browser):
    """
    не получилось кликнуть на 'СБИС Плагин'
    скачал 'СБИС Отчетность'
    """
    sbis = Sbis(browser)
    sbis.open_main_page()
    sbis.open_download_footer()
    local_size, expected_size = sbis.compare_file_sizes()
    assert local_size == expected_size
