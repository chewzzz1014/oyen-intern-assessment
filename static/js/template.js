const logoutBtn = document.querySelector("#logout-btn")
const BASE_URL = 'http://localhost:8000'

logoutBtn.addEventListener('click', async (e) => {
    e.preventDefault()

    try {
        document.cookie = ''
        console.log('Logging out...')

        // TODO: any better approach?
        location.href = `${BASE_URL}/login`
    } catch(err) {
        console.error(err)
    }
})