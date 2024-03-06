const registerForm = document.querySelector("#register_form")
const usernameField = document.querySelector("#r-username")
const passwordField = document.querySelector("#r-password")
const confirmedPasswordField = document.querySelector("#r-cPassword")
const passwordWarning = document.querySelector("#password-warning")
const gotAccountWarning = document.querySelector("#got-account-warning")
const BASE_URL = 'http://localhost:8000'

const {access_token = '', token_type = ''} = JSON.parse(localStorage.getItem('token')) || {}

const unmatchedPasswords = () => {
    return (passwordField.value && !confirmedPasswordField.value) || (passwordField.value !== confirmedPasswordField.value)
}

[passwordField, confirmedPasswordField].forEach(ele => ele.addEventListener("keyup", (e) => {
    if (unmatchedPasswords()) {
        passwordWarning.classList.remove('hide')
        passwordWarning.classList.add('visible')
    } else {
        passwordWarning.classList.remove('visible')
        passwordWarning.classList.add('hide')
    }
}))

registerForm.addEventListener("submit", async (e) => {
    e.preventDefault()

    if (unmatchedPasswords()) return false

    const {value: username} = usernameField
    const {value: password} = passwordField 

    try {
        const response = await fetch(`${BASE_URL}/register`, {
            method: 'POST',
            body: JSON.stringify({username, password}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        })
        
        if (response.status === 400) {
            gotAccountWarning.classList.remove('hide')
            gotAccountWarning.classList.add('visible')
        } else if (response.status === 500){
            console.log(500)
        } else if (response.ok) {
            console.log('Registering...')
            const data = await response.json()
            const {access_token, token_type} = data[0]
            if (access_token && token_type) {
                localStorage.setItem('token', JSON.stringify({
                    access_token, token_type
                }))
            }
            // TODO: any better approach?
            location.href = `${BASE_URL}`
        }
    } catch(err) {
        console.log(err)
    }
})