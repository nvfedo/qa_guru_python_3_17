from selene import have
from utils.base_session import demowebshop


def test_login(register):
    register.open('')
    register.element('.account').should(have.exact_text('nvfedoqaguru3_16@mail.ru'))


def test_add_cart():
    response = demowebshop.post('/addproducttocart/catalog/31/1/1')
    assert response.status_code == 200


def test_delete_cart(register):
    register.open('')
    register.element('.ico-cart').click()
    register.element('.qty-input').clear().send_keys(0).press_enter()


def test_printers(register):
    register.open('')
    register.element('.search-box-text').type('print').press_enter()
    register.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(register):
    register.open('')
    register.element('.ico-logout').click()
    response = demowebshop.get('/logout', allow_redirects=False)
    assert response.status_code == 302
