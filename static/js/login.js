const loginForm = document.querySelector("#login_form")
const usernameField = document.querySelector("#l-username")
const passwordField = document.querySelector("#l-password")
const noAccountWarning = document.querySelector("#no-account-warning")
const BASE_URL = 'http://localhost:8000'

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault()

    const {value: username} = usernameField
    const {value: password} = passwordField

    try {
        const response = await fetch(`${BASE_URL}/login`, {
            method: 'POST',
            body: JSON.stringify({username, password}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        })
        if (response.status === 400) {
            noAccountWarning.classList.remove('hide')
            noAccountWarning.classList.add('visible')
        } else if (response.status === 500){
            console.log(500)
        } else if (response.ok) {
            console.log('Logging...')
            // TODO: redirect to main page
        }
    } catch(err) {
        console.log(err)
    }
})