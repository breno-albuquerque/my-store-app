const addBtns = Array.from(document.getElementsByClassName('product-btn'));
const productForm = document.getElementById('product-form');
const flashProduct = document.getElementById('flash-product');

const handleAddBtnClick = async (event) => {
    const productId = event.target.parentElement.id;

    flashProduct.style.display = 'block';
    flashProduct.style.width = '150px';
    flashProduct.style.top = '10px';
    flashProduct.style.left = 'calc(50% - 75px)';

     setTimeout(() => {
        flashProduct.style.display = "none";
    }, 1000);


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