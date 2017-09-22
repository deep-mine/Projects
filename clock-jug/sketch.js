var canvas;
var hr,mn,sc;
var drops = []

function setup(){
	canvas = createCanvas(600,600);
	canvas.parent("canvas_p");
}

function draw(){
	background(51);
	frameRate(60);
	
	hr = hour();
	mn = minute();
	sc = second() + mn*60 + hr*3600;
	
	hrHeight = map(sc,0,24*60*60,0,height);
	
	noStroke();
	fill(150,200,255);
	rect(0,height-hrHeight,width,hrHeight);
	
	/* fill("pink");
	percentage = sc/(24*6*6);
	textFont("verdana");
	textSize(20);
	text(percentage+"% lost",0,height/2); */
	
	/* if(frameCount%60==0){
		drops.push(new Drop());
	}
	
	for(var i = 0 ; i < drops.length; i++){
		drops[i].move();
		drops[i].show();
	}
	
	for(var i = drops.length-1 ; i >=0; i--){
		if(drops[i].y>height){
			splice(i,1);
		}
	} */
	
	
}

function Drop(){
	this.x = random(width);
	this.y = 0;
	this.speed = 10;
	
	this.move = function(){
		this.y+=this.speed;
	}
	
	this.show = function(){
		noStroke();
		fill(150,200,255);
		rect(this.x,this.y,5,10);
	}
}