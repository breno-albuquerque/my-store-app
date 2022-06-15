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
        flashProduct.innerHTML = '<span>Your order has been fulfilled!</span>'
        flashProduct.style.display = "block";
    } else {
        cartItem = target.parentElement;
        URL = `http://localhost:5000/deleteCart?id=${cartItem.id}`;
        cartSection.removeChild(cartItem);
        flashProduct.innerHTML = '<span>Product Removed!</span>'
        flashProduct.style.display = "block";
    }
    
    setTimeout(() => {
        flashProduct.style.display = "none";
    }, 1500);

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
    totalPrice.innerText = `Total: ${total.toFixed(2)}`;
}

removeBtns.forEach(btn => btn.addEventListener('click', handleRemove));

window.onload = () => {
    handlePrice();

    if (!flashMsg) return;

    setTimeout(() => {
        flashMsg.style.display = 'none';
    }, 1500);
}