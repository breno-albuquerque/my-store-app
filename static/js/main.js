const mainForm = document.getElementById('main-form');
const flashMsg = document.getElementById('flash-main');

function handleCartBtnClick(event) {
    event.preventDefault();

    mainForm.method = 'GET';
    mainForm.action = '/cart';

    mainForm.submit();

    mainForm.method = 'POST';
    mainForm.action = '/main';
}

window.onload = () => {
    if (!flashMsg) return;

    setTimeout(() => {
        flashMsg.style.display = 'none';
    }, 1500);
}