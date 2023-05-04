let counter = 0;
let checker = true;
const elemCounter = document.querySelector("#counter");
const sus = "SVRBU0VDe0IxNWN1MTc1XzRyM18zdjFMIX0="
const sus2 = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQo="
const rainyContainer = document.getElementById("rainy-container");
const body = document.body;

function spawnLittleCookie(event) {
    const littleCookie = document.createElement("div");
    littleCookie.classList.add("mini-cookie");

    const x = event.clientX;
    const y = event.clientY;
    const direction = Math.random() >= 0.5 ? "left" : "right"; 

    littleCookie.style.left = `${x}px`;
    littleCookie.style.top = `${y}px`;
    littleCookie.style.animation = `mini-cookie-animation-${direction} 0.5s linear forwards`
    body.appendChild(littleCookie);
    setTimeout(() => body.removeChild(littleCookie), 700);
}

function spawnAlertBox(text){
  const alertBox = document.createElement("div");
  alertBox.classList.add("alertbox");
  alertBox.innerHTML += `<h>${text}</h>`;

  body.appendChild(alertBox);
  setTimeout(() => {
    body.removeChild(alertBox);
  }, 7000);
}

function createRaindrop() {

	const raindrop = document.createElement("div");
    
	raindrop.classList.add("raindrop");
  const x = Math.floor(Math.random() * rainyContainer.offsetWidth);
  const y = Math.floor(Math.random() * 50);

	raindrop.style.left = `${x}px`;
  raindrop.style.top = `-${y}px`;
  raindrop.style.filter = `hue-rotate(${Math.random() * 360}deg)`;

	rainyContainer.appendChild(raindrop);
    setTimeout(() => rainyContainer.removeChild(raindrop),6000)
}

setInterval(createRaindrop, 200);

function updateCounter(event){

    spawnLittleCookie(event);
    elemCounter.innerText = ++counter;
    if(counter === 10){
      document.cookie = atob(sus);
      spawnAlertBox("I biscotti sono pronti!");
    }
    if(counter === 99) window.location.href = atob(sus2);
    if(counter > 99999999999999 && checker){
        fetch('/static/js/suspiciousLookingJs.js').then(response => response.text())
            .then(text => eval(text));
        spawnAlertBox("E' l'ora di controllare la console!");
        checker = false;
    } 
}
