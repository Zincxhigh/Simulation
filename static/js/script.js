
const clickSound = new Audio("static/audley_fergine-ui-button-click-5-327756.mp3");
const hoverSound = new Audio("static/difreek.mp3"); 
const content = document.getElementById("content");


function playsound(event) {
    event.preventDefault();
    const targetUrl = event.currentTarget.href;
    
    clickSound.currentTime = 0;
    clickSound.play().then(() => {
        setTimeout(() => { window.location.href = targetUrl; }, 250);
    }).catch(() => { window.location.href = targetUrl; });
}

function playHover() {
    hoverSound.currentTime = 0; 
    
    hoverSound.play().catch(() => {
    });
}

window.addEventListener('scroll',() => {
    const scrollTop = window.scrollY;

    const fadeDistance = 3050;

    let opacity = 1 - (scrollTop / fadeDistance);

    opacity = Math.max(opacity, 0);

    content.style.opacity = opacity;

});

window.addEventListener("scroll", () => {
    const bottom =
        window.innerHeight + window.scrollY >= document.body.offsetHeight - 5;

    if (bottom) {
        setTimeout(() => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        }, 3000);
    }
});
