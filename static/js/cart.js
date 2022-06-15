const removeBtns = Array.from(document.getElementsByClassName('remove-btn'));
const cartSection = document.getElementById('cart-section');
const flashProduct = document.getElementById('flash-product')

const handleRemove = async ({ target }) => {
    const cartItem = target.parentElement;
    cartSection.removeChild(cartItem);

    flashProduct.style.display = "block";

    setTimeout(() => {
       flashProduct.style.display = "none";
   }, 1500);

    await fetch(`http://localhost:5000/deleteCart?id=${cartItem.id}`, {
        method: "DELETE",
    });
}

removeBtns.forEach(btn => btn.addEventListener('click', handleRemove)); 