const layoutBtns = Array.from(document.getElementsByClassName('layout-btn'));
const layoutForm = document.getElementById('layout-form');

console.log(layoutBtns)

function handleLayoutBtnClick(event) {
    
    event.preventDefault();
    const { value } = event.target;
    layoutForm.action = '/' + value;

    console.log(layoutForm)

}


layoutBtns.forEach(btn => btn.addEventListener('click', handleLayoutBtnClick))