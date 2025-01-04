document.addEventListener('DOMContentLoaded', () => {
	var joy1 = new JoyStick('joy1Div', {
		externalStrokeColor: '#000',
		internalFillColor: '#000',
	});
	var joy2 = new JoyStick('joy2Div', {
		externalStrokeColor: '#000',
		internalFillColor: '#000',
	});
	setInterval(() => {
		
		joy1PosX = joy1.GetX();
		joy1PosY = joy1.GetY();
		joy2PosX = joy2.GetX();
		joy2PosY = joy2.GetY();
		sendPositions(joy1PosX, joy1PosY, joy2PosX, joy2PosY);
	
	}, 300);
})

function sendPositions(joy1PosXValue, joy1PosYValue, joy2PosXValue, joy2PosYValue) {
    fetch('/', {
		method: "POST",
		headers: {
			"X-CSRFToken": getCookie("csrftoken"),
		},
		body: JSON.stringify({
			joy1PosX: joy1PosXValue,
			joy1PosY: joy1PosYValue,
			joy2PosX: joy2PosXValue,
			joy2PosY: joy2PosYValue,
		}),
		credentials: 'include',
	});
	console.log('ok');
}

function getCookie(cname) {
	let name = cname + "=";
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(';');
	for(let i = 0; i <ca.length; i++) {
		let c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
		return c.substring(name.length, c.length);
		}
	}
	return "";
}