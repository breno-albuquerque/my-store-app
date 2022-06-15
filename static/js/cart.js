const removeBtns = Array.from(document.getElementsByClassName('remove-btn'));
const cartSection = document.getElementById('cart-section');

const handleRemove = async ({ target }) => {
    const cartItem = target.parentElement;
    cartSection.removeChild(cartItem);

    await fetch(`http://localhost:5000/deleteCart?id=${cartItem.id}`, {
        method: "DELETE",
    });
}

removeBtns.forEach(btn => btn.addEventListener('click', handleRemove)); 