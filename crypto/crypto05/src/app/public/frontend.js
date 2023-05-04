const protocol = window.location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(`${protocol}://${window.location.host}`);
const term = new window.Terminal({rows: 26, cols: 170});
const fitAddon = new FitAddon.FitAddon();
term.loadAddon(fitAddon);

socket.onmessage = (event) => {
	term.write(event.data);
}

term.onData((data) => {
	socket.send(data);
});

setTimeout(() => document.getElementsByTagName("textarea")[0].focus(), 500);

term.open(document.getElementById("terminal"));
setTimeout(() => fitAddon.fit(), 1000);
