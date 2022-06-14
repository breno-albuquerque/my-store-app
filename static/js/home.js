const homeForm = document.getElementById('home-form');
const registerBtn = document.getElementById('register-btn');
const loginBtn = document.getElementById('login-btn');

registerBtn.addEventListener('click', handleFormSubmit)
loginBtn.addEventListener('click', handleFormSubmit)

function handleFormSubmit(event) {
    event.preventDefault()

    if (event.target.innerText === "Register") {
        homeForm.action = "/register"
    } else {
        homeForm.action = "/login"
    }

    homeForm.submit()
}