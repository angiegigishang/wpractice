<template>
	<div class="container">
		<div class="title">
			<div class="container-title">分零件1-1</div>
		</div>
		<div class="need">
			<div class="need-title">库存数</div>
			<div class="need-number">640</div>
		</div>
		<div class="store">
			<div class="store-title">需求数</div>
			<div class="store-number">800</div>
		</div>
		<div class="showImage">
			<canvas :id="this.list.title" class="c"></canvas>
			<input type="range" id="r1" min="0" max="100" step="1">
		</div>
	</div>
</template>

<script>
export default {
	props: {
        list: Object
    },
	methods: {
		createCanvas () {
			var ctitle = this.list.title;
			var canvas = document.getElementById(ctitle);
			var ctx = canvas.getContext('2d');
			var range = document.getElementById('r1');
			 
			var rangeValue = range.value;
			var nowRange = 0; 
			 
			var mW = canvas.width = 250;
			var mH = canvas.height = 250;
			var lineWidth = 2;
			 
			var r = mH / 2; 
			var cR = r - 16 * lineWidth; 
			 
			var sX = 0;
			var sY = mH / 2;
			var axisLength = mW; 
			var waveWidth = 0.015 ; 
			var waveHeight = 20; 
			var speed = 0.06; 
			var xOffset = 25;
			ctx.lineWidth = lineWidth;
			 
			var IsdrawCircled = false;

			var drawCircle = function(){

				ctx.lineWidth = 10; 

				ctx.beginPath();

				var gradient=ctx.createLinearGradient(0,0,250,0);
				gradient.addColorStop("0","#04bbbc");
				gradient.addColorStop("0.3","#67b4c9");
				gradient.addColorStop("0.6","#158ac9");
				gradient.addColorStop("1.0","#04bc65");
			

			    ctx.strokeStyle = gradient;

			    ctx.arc(r, r, cR+16, 0, 2 * Math.PI);
			    ctx.stroke();

			    ctx.beginPath();
			    ctx.arc(r, r, cR, 0, 2 * Math.PI);
			    ctx.clip();
			}
			 

			var drawSin = function(xOffset){

			    ctx.save();
			 
			    var points=[]; 
			 
			    ctx.beginPath();

			    for(var x = sX; x < sX + axisLength; x += 20 / axisLength){
			    
			        var y = -Math.sin((sX + x) * waveWidth + xOffset);
			 
			        var dY = mH * (1 - nowRange / 100 );
			 
			        points.push([x, dY + y * waveHeight]);
			        ctx.lineTo(x, dY + y * waveHeight);  
			    }
			 

			    ctx.lineTo(axisLength, mH);
			    ctx.lineTo(sX, mH);
			    ctx.globalAlpha = 0.8;
			    ctx.lineTo(points[0][0],points[0][1]);	 

			    var gradient=ctx.createLinearGradient(0,0,250,0);
				gradient.addColorStop("0","#04bbbc");
				gradient.addColorStop("0.1","#67b4c9");
				gradient.addColorStop("0.3","#158ac9");
				gradient.addColorStop("1.0","#04bc65");
			    ctx.fillStyle = gradient;
			    ctx.fill();


			 
			    ctx.restore();
			};
			 

			var drawText = function(){
			   ctx.save();
			 
			   var size = 0.65*cR;
			   ctx.font = size + 'px led-number';
			   ctx.textAlign = 'center';
			   ctx.fillStyle = "#c5f0f9";
			   ctx.fillText(~~nowRange + '%', r, r -28);

			
			 
			   ctx.restore();
			};
			 
			var render = function(){
			    ctx.clearRect(0, 0, mW, mH);
			 
			    rangeValue = range.value;
			 
			    if(IsdrawCircled == false){
			    	drawCircle(); 
			    }
			 
			    if(nowRange <= rangeValue){
			        var tmp = 1;
			        nowRange += tmp;
			    }
			 
			    if(nowRange > rangeValue){
			        var tmp = 1;
			        nowRange -= tmp;
			    }
			 
			    drawSin(xOffset);
			    drawText();
			 
			    xOffset += speed;
			    requestAnimationFrame(render);
			}
			 
			render();  
	    }
	},
	mounted () {
		this.createCanvas()
	}
}
</script>

<style scoped>
	.container {
		position: absolute;
		width: 100%;
		height: 100%;
		border: 2px solid #67b4c9;
        box-shadow: 0px 0px 0.1px 0.8px #67b4c9;
        border-radius: 10px;
	}
	img {
		position: absolute;
		width: 100%;
		height: 100%;
	}
	@font-face {
      font-family:led-number;
      src:url("~assets/led-number.ttf");
    }
	.title, .need, .store {
		position: absolute;
		width: 40%;
		height: 30%;
		left: 10%;
		display: inline-block;
	}
	.need {
		top: 36%;
	}
	.store {
		top: 63%;
	}
	.need-title, .store-title {
		position: absolute;
		color: white;
		font-size: 0.8em;
		top: 21%;
	}
	.container-title {
		position: absolute;
		color: white;
		font-size: 1em;
		top: 21%;
	}
	.need-number, .store-number {
		position: absolute;
		font-family: led-number;
		top: 23%;
		font-size: 1em;	
		width: 55%;
		left: 67%;
	}
	.need-number {
		color: #04bbbc;
	}
	.store-number {
		color: #04bc65;
	}
	.showImage {
		position: absolute;
		width: 50%;
		height: 92%;
		top: 5%;
		right: 1%;
	}
	.c {
		position: absolute;
		top: 4%;
		right: 0;
		width: 85%;
		height: 95%;
		display: block;
   		margin: 0 auto;
	}
	#r1{
	   display: none;
	   margin: 0 auto;
	  }
	  #r1::before{
	   color: black;
	   content: attr(min);
	   padding-right: 10px;
	  }
	  #r1::after{
	   color: black;
	   content: attr(max);
	   padding-left: 10px;
	  }  
</style>