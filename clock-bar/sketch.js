var canvas;
var hr,mn,sc;

function setup(){
	canvas = createCanvas(600,600);
	canvas.parent("canvas_p");
}

function draw(){
	background(51);
	
	hr = hour();
	mn = minute();
	sc = second();
	
	hrHeight = map(hr,0,24,0,height);
	mnHeight = map(mn,0,60,0,height);
	scHeight = map(sc,0,60,0,height);
	
	noStroke();
	fill(150,200,255);
	rect(0,height-hrHeight,width/3,hrHeight);
	
	fill(150,255,125);
	rect(width/3,height-mnHeight,width/3,mnHeight);
	
	fill(255,150,125);
	rect(2*width/3,height-scHeight,width/3,scHeight);
}