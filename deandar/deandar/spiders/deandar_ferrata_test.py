from .deandar_ferrata import is_vf_detail_url

def test_vf_detail_page_returns_true():
    assert is_vf_detail_url("https://deandar.com/en/ferratas/via-ferrata-agulles-rodones")


def test_vf_status_page_returns_false():
    assert not is_vf_detail_url("https://deandar.com/en/ferratas/via-ferrata-agulles-rodones/estado")


def test_area_page_returns_false():
    assert not is_vf_detail_url("https://deandar.com/en/ferratas/todas/Santa+Cristina+d%27Aro")
