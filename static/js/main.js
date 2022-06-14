const cartPageBtn = document.getElementById('cart-page-btn');
const mainForm = document.getElementById('main-form');

function handleCartBtnClick(event) {
    event.preventDefault();

    mainForm.method = 'GET';
    mainForm.action = '/cart';

    mainForm.submit();

    mainForm.method = 'POST';
    mainForm.action = '/main';
}

cartPageBtn.addEventListener('click', handleCartBtnClick);