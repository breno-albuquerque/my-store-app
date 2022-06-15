const mainForm = document.getElementById('main-form');
const flashMsg = document.getElementById('flash-main');

const categories = ['Desktop', 'Notebook', 'Monitors', 'Macbook', 'Tablet', 'Ipad', 'Keyboard', 'Mouse', 'Smartphone', 'Iphone', 'Smart Tv', 'Alexa', 'Playstation 5', 'Xbox series x']

function handleCartBtnClick(event) {
    event.preventDefault();

    mainForm.method = 'GET';
    mainForm.action = '/cart';

    mainForm.submit();

    mainForm.method = 'POST';
    mainForm.action = '/main';
}

window.onload = () => {
    categories.forEach(item => {
        const btn = document.createElement('button');
        btn.name = "category";
        btn.className = "main-btn";
        btn.value = item;
        btn.type = "submit";
        btn.id = `${item.toLowerCase()}-btn`;
        btn.innerText = item;

        mainForm.appendChild(btn);
    });

    if (!flashMsg) return;

    setTimeout(() => {
        flashMsg.style.display = 'none';
    }, 1500);
}