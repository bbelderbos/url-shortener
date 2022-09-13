from script import shorten_url


def test_shorten_url():
    url = "https://pybit.es/articles/what-we-learned-from-building-our-own-cms-using-django/"
    actual = shorten_url(url)
    assert actual == "7AGpGnB"
