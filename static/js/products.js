const addBtns = Array.from(document.getElementsByClassName('product-btn'));
const productForm = document.getElementById('product-form');


const handleAddBtnClick = async (event) => {
    const productId = event.target.parentElement.id;
    await fetch(`http://localhost:5000/products`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'productId': productId,
        })
    });
}

addBtns.forEach(btn => btn.addEventListener('click', handleAddBtnClick));