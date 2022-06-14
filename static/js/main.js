const cartPageBtn = document.getElementById('cart-page-btn');
const mainForm = document.getElementById('main-form');

console.log(mainForm)

function handleCartBtnClick(event) {
    console.log('gere')
    event.preventDefault();
    mainForm.method = 'GET';
    mainForm.action = '/cart';
    console.log(mainForm)
    mainForm.submit();
}

cartPageBtn.addEventListener('click', handleCartBtnClick);