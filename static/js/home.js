const flashMsg = document.getElementById('flash-home');

window.onload = () => {
    if (!flashMsg) return;

    setTimeout(() => {
        flashMsg.style.display = 'none';
    }, 3000);
}