let hamburgerBtn = document.querySelector('.hamburger-btn')
let sideBar = document.querySelector('.side-bar')

hamburgerBtn.addEventListener('click', sidebarToggle);
function sidebarToggle() {
    sideBar.classList.toggle('active');
}

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('author-image');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}
