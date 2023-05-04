const process  = require("process");
const pty = require("node-pty");
const ws  = require("ws");
const express = require("express");

const app = express();
app.use(express.static(__dirname + "/public"));

const port = process.env.PORT || 8080;
const httpServer = app.listen(port, () => {
    console.log(`Socket is up and running on port ${port}`)
});
const wss = new ws.Server({noServer: true});

httpServer.on("upgrade", (req, socket, head) => {
    wss.handleUpgrade(req, socket, head, (ws) => {
        wss.emit("connection", ws, req);
    });
});

let i = 0;
wss.on("connection", (ws) => {

    const sessionId = ++i;
    console.log(`New session opened (#${sessionId})`);

    const ptyProcess = pty.spawn("mtp", ["sample.ciphertexts"], {
		name: "xterm-color",
        env: process.env,
        rows: 26, cols: 170
    });
	
	let lastData = new Date();

    ptyProcess.on("data", (data) => {
		ws.send(data);
		lastData = new Date();
    });

    ws.on("message", (data) => {
		if (data.toString() === '\u0003') return;
		if (data.toString() === '\u001b') return;
		ptyProcess.write(data);
    });
    
    const pingInterval = setInterval(() => {
		ws.ping();
		const now = new Date();
		const diff = now - lastData;
		if (diff > (10 * 60 * 1000)) ws.terminate();
    }, 5000);

    ws.on("close", () => {
        console.log(`Session closed (#${sessionId})`);
        ptyProcess.kill();
		clearInterval(pingInterval);
    });

});

process.on("SIGINT", () => {
    process.exit();
});

process.on("SIGTERM", () => {
    process.exit();
});
