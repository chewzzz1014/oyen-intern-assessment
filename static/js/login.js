const loginForm = document.querySelector("#login_form")
const usernameField = document.querySelector("#l-username")
const passwordField = document.querySelector("#l-password")
const noAccountWarning = document.querySelector("#no-account-warning")
const wrongPasswordWarning = document.querySelector("#wrong-warning")
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
                'Content-Type': 'application/json',
                'Authorization': `${token_type} ${access_token}`
            },
        })
        if (response.status === 404) {
            noAccountWarning.classList.remove('hide')
            noAccountWarning.classList.add('visible')
        } else if (response.status === 400) {
            wrongPasswordWarning.classList.remove('hide')
            wrongPasswordWarning.classList.add('visible')
        } else if (response.status === 500){
            console.log(500)
        } else if (response.ok) {
            console.log('Logging...')
            
            // TODO: any better approach?
            location.href = `${BASE_URL}`
        }
    } catch(err) {
        console.log('errr')
        console.log(err)
    }
})