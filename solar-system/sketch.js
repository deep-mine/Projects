var mercury;
var venus;
var earth;
var mars;
var jupiter;
var saturn;
var uranus;
var neptune;
var pluto;

var x,y,r;
function setup(){
	var canvas = createCanvas(3000,2000);
	canvas.parent("canvas_p");
	mercury = new Planet(10,60,"orange");//60
	venus = new Planet(10,90,"maroon");//90
	earth = new Planet(15,120,"blue");//120
	mars = new Planet(12,150,"red");
	jupiter = new Planet(50,250,"orange");
	saturn = new Planet(25,350,"red");
	uranus = new Planet(25,450,"purple");
	neptune = new Planet(25,550,"cyan");
	pluto = new Planet(10,650,"white");
}

function draw(){
	background(51);

	x = mouseX;
	y = mouseY;
	r = 60;
	
	translate(x,y);
	
	fill("yellow");
	noStroke();
	ellipse(0,0,r*2,r*2);
	
	/* for(var i =0 ;i<100;i++){
		fill(255);
		ellipse(random(-width,width),random(-height,height),10,10);
	} */
	
	pluto.move();
	pluto.show();
	
	neptune.move();
	neptune.show();
	
	uranus.move();
	uranus.show();
	
	saturn.move();
	saturn.show(true);
	
	jupiter.move();
	jupiter.show();
	
	mars.move();
	mars.show();
	
	earth.move();
	earth.show();
	
	venus.move();
	venus.show();
	
	mercury.move();
	mercury.show();

	
	
	
	
	//console.log(mercury.a+"\n"+venus.a+"\n"+earth.a+"\n");
	
	
}