const mainBtns = Array.from(document.getElementsByClassName('main-btn'))

function handleMainBtnClick(event) {
    const { value } = event.target;

    
}

mainBtns.forEach(item => item.addEventListener('click', handleMainBtnClick))