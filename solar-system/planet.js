function Planet(r,d,col){

	this.a = 0;
	this.aVel = 0.0;
	this.aAcc = 0.0001;
	
	this.orbitalRadius = d;
	this.radius = r;
	
	this.col = col;
	
	this.move = function(){
		
		this.a += this.aVel;
		this.aVel += this.aAcc;
		this.a *= (0.98 + (0.9-0.98)*(d/width));
		
		
		rotate(this.a);
	}
	
	this.show = function(ring){
		fill(col);
		stroke(255);
		line(0,0,this.orbitalRadius,this.orbitalRadius);
		noStroke();
		ellipse(this.orbitalRadius,this.orbitalRadius,this.radius*2,this.radius*2);
		
		if(ring){
			for(var i =0 ;i<20;i++){
				stroke("yellow");
				noFill();
				ellipse(this.orbitalRadius,this.orbitalRadius,i+this.radius*3,i+this.radius*2.5);
			}
		}
	}
}

/*
0.98 + (0.9-0.98)*(d/width);
*/