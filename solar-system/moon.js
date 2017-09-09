function Moon(planet,r,d,col){

	this.a = 0;
	this.aVel = 0;
	this.aAcc = 0.001;
	
	this.orbitalRadius = d;
	this.radius = r;
	
	this.col = col;
	
	this.move = function(){
		
		this.a += this.aVel;
		this.aVel += this.aAcc;
		this.a *= (0.98 + (0.9-0.98)*(d/width));
		
		
		rotate(this.a);
	}
	
	this.show = function(){
		fill(col);
		ellipse(this.orbitalRadius,this.orbitalRadius,this.radius*2,this.radius*2);
	}
}

/*
0.98 + (0.9-0.98)*(d/width);
*/