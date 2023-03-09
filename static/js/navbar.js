const menuToggle = document.getElementById('menu')
const right = document.querySelector('.right')
const navbarTop = document.querySelector('.navbar_top')

menuToggle.addEventListener('click', ()=>{
    right.classList.toggle('active')
    navbarTop.classList.toggle('active')
})

var typed = new Typed('#multi-text',
{
    strings:[
        "Test Books",
        'Refrence Books',
        'Guide and Guess Papers',
        'Handwritten Notes',
        'Courses',
        'Religious Books',
        'Motivational Books',
        'Other Books',
    ],
    typeSpeed:100,
    backSpeed:100,
    backDelay:1000,
    loop:true
})