var canvas;
var hr,mn,sc;
var dia;

function setup(){
	canvas = createCanvas(600,600);
	canvas.parent("canvas_p");
	
	

	angleMode(DEGREES);

}

function draw(){
	background(51);

	hr = hour();
	mn = minute();
	sc = second();

	dia = 300;
	

	translate(300,300);
	rotate(-90);
	
	push()
	rotate(90);
	for(var i = 1 ; i <= 12 ; i++){
		var angle = i * 30;
		rotate(angle);
		translate(0,-125);
		rotate(-1*angle);
		fill(255,150,125);
		strokeWeight(1);
		textSize(20);
		textAlign(CENTER);
		text(i,0,5);
		rotate(angle);
		translate(0,125);
		rotate(-1*angle);
	}
	pop();

	//hours
	stroke(150,200,255);
	noFill();
	strokeWeight(15);
	var hr_end = map(hr%12,0,12,0,360);
	//var hr_end = map(hr,0,24,0,360);
	arc(0,0,dia,dia,0,hr_end);

	push();
	strokeWeight(5);
	rotate(hr_end);
	line(0,0,80,0);
	pop();

	//fill(150,200,255);
	push();
	var dhr = hr%12;
	if(dhr<10){
		dhr = "0"+str(dhr);
	}
	rotate(90);
	fill(150,200,255);
	strokeWeight(1);
	textSize(30);
	textFont("verdana");
	text(dhr,-50,250);
	pop();


	//minutes
	stroke(150,255,125);
	noFill();
	strokeWeight(10);
	var mn_end = map(mn,0,60,0,360);
	arc(0,0,dia+40,dia+40,0,mn_end);

	push();
	if(mn<10){
		mn = "0"+str(mn);
	}
	strokeWeight(4);
	rotate(mn_end);
	line(0,0,100,0);
	pop();

	push();
	rotate(90);
	fill(150,255,125);
	strokeWeight(1);
	textSize(30);
	textFont("verdana");
	text(mn,0,250);
	pop();



	//seconds
	stroke(255,150,125);
	noFill();
	strokeWeight(5);
	var sec_end = map(sc,0,60,0,360);
	arc(0,0,dia+60,dia+60,0,sec_end);

	push();
	if(sc<10){
		sc = "0"+str(sc);
	}
	strokeWeight(3);
	rotate(sec_end);
	line(0,0,120,0);
	pop();

	push();
	rotate(90);
	fill(255,150,125);
	strokeWeight(1);
	textSize(30);
	textFont("verdana");
	text(sc,50,250);
	pop();



}
