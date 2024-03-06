const logoutBtn = document.querySelector("#logout-btn")
const BASE_URL = 'http://localhost:8000'

logoutBtn.addEventListener('click', async (e) => {
    e.preventDefault()

    try {
        document.cookie = 'login_session' + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        console.log('Logging out...')

        // TODO: any better approach?
        location.href = `${BASE_URL}/login`
    } catch(err) {
        console.error(err)
    }
})