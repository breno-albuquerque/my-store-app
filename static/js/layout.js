const layoutBtns = Array.from(document.getElementsByClassName('layout-btn'));
const layoutForm = document.getElementById('layout-form');

const anchors = [searchAnchor, cartAnchor, logoutAnchor];

function handleLayoutBtnClick(event) { 
    event.preventDefault();
    
    const { value } = event.target;
    layoutForm.action = '/' + value;
}

layoutBtns.forEach(btn => btn.addEventListener('click', handleLayoutBtnClick));
