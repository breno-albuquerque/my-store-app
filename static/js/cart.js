const removeBtns = Array.from(document.getElementsByClassName('remove-btn'));
const cartSection = document.getElementById('cart-section');
const flashProduct = document.getElementById('flash-product');
const totalPrice = document.getElementById('total-price');
const flashMsg = document.getElementById('flash-product')
let productsPrices = Array.from(document.getElementsByClassName('product-price'));

const handleRemove = async ({ target }) => {
    let cartItem;
    let URL;

    if (productsPrices.length === 0) return;

    if (target.innerText === 'Buy') {
        URL = `http://localhost:5000/deleteCart?id=all`
        cartSection.innerHTML = '';
        flashProduct.innerHTML = '<span>Order fulfilled!</span>'
        alertStyle(flashProduct);
    } else {
        cartItem = target.parentElement;
        URL = `http://localhost:5000/deleteCart?id=${cartItem.id}`;
        cartSection.removeChild(cartItem);
        flashProduct.innerHTML = '<span>Product Removed!</span>'
        alertStyle(flashProduct);
    }
    
    setTimeout(() => {
        flashProduct.style.display = "none";
    }, 3000);

    handlePrice()

    await fetch(URL, {
        method: "DELETE",
    });
}

function handlePrice() {
    productsPrices = Array.from(document.getElementsByClassName('product-price'));
    const total = productsPrices.reduce((acc, curr) => {
        return parseFloat(curr.innerText) + acc
    }, 0);
    totalPrice.innerText = `${total.toFixed(2)}`;
}

function alertStyle(flash) {
    flash.style.display = 'block';
    flash.style.width = '200px';
    flash.style.top = '10px';
    flash.style.left = 'calc(50% - 100px)';
}

removeBtns.forEach(btn => btn.addEventListener('click', handleRemove));

window.onload = () => {
    handlePrice();

    if (!flashMsg) return;

    setTimeout(() => {
        flashMsg.style.display = 'none';
    }, 3000);
}