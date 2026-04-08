
const clickSound = new Audio("static/audley_fergine-ui-button-click-5-327756.mp3");
const hoverSound = new Audio("static/difreek.mp3"); 


function playsound(event) {
    event.preventDefault();
    const targetUrl = event.currentTarget.href;
    
    clickSound.currentTime = 0;
    clickSound.play().then(() => {
        setTimeout(() => { window.location.href = targetUrl; }, 250);
    }).catch(() => { window.location.href = targetUrl; });
}
//might look for it in one of the games

function playHover() {
    hoverSound.currentTime = 0; 
    
    hoverSound.play().catch(() => {
    });
}

