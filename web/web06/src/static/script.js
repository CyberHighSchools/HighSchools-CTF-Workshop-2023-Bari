// Definisci un array di colori dell'arcobaleno
let rainbowColors = [
  'rgba(255, 0, 0, 1)', 'rgba(255, 154, 0, 1)', 'rgba(208, 222, 33, 1)',
  'rgba(79, 220, 74, 1)', 'rgba(63, 218, 216, 1)', 'rgba(47, 201, 226, 1)',
  'rgba(28, 127, 238, 1)', 'rgba(95, 21, 242, 1)', 'rgba(186, 12, 248, 1)',
  'rgba(251, 7, 217, 1)', 'rgba(255, 0, 0, 1)'
];

// Definisci una funzione per cambiare il colore del testo
function changeColor() {
  // Ottieni l'elemento span
  let span = document.getElementById('itasec-text');

  // Seleziona il prossimo colore dell'arcobaleno
  let nextColor = rainbowColors.shift();
  rainbowColors.push(nextColor);

  // Applica l'animazione CSS per la sfumatura arcobaleno al testo
  span.style.webkitTextFillColor = 'transparent';
  span.style.webkitBackgroundClip = 'text';
  span.style.backgroundImage = `linear-gradient(-45deg, ${rainbowColors.join(', ')})`;
  span.style.animation = 'rainbow 6s linear infinite';
}

// Chiama la funzione changeColor una volta dopo che la pagina è stata caricata
window.addEventListener('load', function() {
  changeColor();
  setInterval(changeColor, 80)
});

