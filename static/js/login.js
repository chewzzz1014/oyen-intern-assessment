const loginForm = document.querySelector("#login_form")
const usernameField = document.querySelector("#username")
const passwordField = document.querySelector("#password")
const BASE_URL = 'http://localhost:8000'

async function postData(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: data
        })
        return response.json()
    } catch(err) {
        console.log(err)
    }
}

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
        console.log(response.json())
    } catch(err) {
        console.log(err)
    }

    usernameField.value = ''
    passwordField.value = ''
})