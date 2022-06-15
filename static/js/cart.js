const removeBtns = Array.from(document.getElementsByClassName('remove-btn'));
const cartSection = document.getElementById('cart-section');
const flashProduct = document.getElementById('flash-product');
let productsPrices = Array.from(document.getElementsByClassName('product-price'));
const totalPrice = document.getElementById('total-price');

const handleRemove = async ({ target }) => {
    const cartItem = target.parentElement;
    cartSection.removeChild(cartItem);

    productsPrices = Array.from(document.getElementsByClassName('product-price'));
    const total = productsPrices.reduce((acc, curr) => {
        console.log(curr)
         return parseFloat(curr.innerText) + acc
     }, 0);
     totalPrice.innerText = `Total: ${total.toFixed(2)}`;

    flashProduct.style.display = "block";
    setTimeout(() => {
       flashProduct.style.display = "none";
    }, 1500);

    await fetch(`http://localhost:5000/deleteCart?id=${cartItem.id}`, {
        method: "DELETE",
    });
}

removeBtns.forEach(btn => btn.addEventListener('click', handleRemove));

window.onload = () => {
    const total = productsPrices.reduce((acc, curr) => {
        return parseFloat(curr.innerText) + acc
    }, 0);

    totalPrice.innerText = `Total: ${total.toFixed(2)}`;
}