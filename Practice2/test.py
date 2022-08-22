from Online_shop_practice import Shop
from Online_shop_practice import Generator


def test_shop():
    p = Shop('Jame', 'Sanders','+380672861619', 'danilgordiychenko@gmail.com', )
    assert p.name == 'Jame'
    assert p.surname == 'Sanders'
    assert p.phone == '+380672861619'
    assert p.mail == 'danilgordiychenko@gmail.com'


def test_person_full():
    p = Shop('Jame', 'Sanders','+380672861619', 'danilgordiychenko@gmail.com', )
    assert p.name == 'Jame'
    assert p.surname == 'Sanders'
    assert p.phone == '+380672861619'
    assert p.mail == 'danilgordiychenko@gmail.com'


def test_person_getinfo():
    p = Shop('Jame', 'Sanders', '+380672861619', 'danilgordiychenko@gmail.com')
    assert isinstance(p.get_info(), str)


def test_gen_single_types():
    g = Generator()
    p = g.generate_single()
    assert isinstance(p, Shop)
    assert isinstance(p.name, str)
    assert isinstance(p.surname, str)
    assert isinstance(p.mail, str)
    assert isinstance(p.phone, str)


def test_gen_1000_type():
    g = Generator()
    plist = g.generate_1000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Shop)
    assert len(plist) == 1000


def test_gen_10_000_type():
    g = Generator()
    plist = g.generate_10_000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Shop)
    assert len(plist) == 10000