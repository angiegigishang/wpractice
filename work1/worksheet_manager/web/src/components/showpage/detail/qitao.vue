<template>
	<div class="container">
		<img src="../../.././assets/images/v2/qitao.png"/>
		<div class="need">
			<div class="need-title">需求数</div>
			<div class="need-number">640</div>
			<div class="need-unit">个</div>
		</div>
		<div class="store">
			<div class="store-title">库存数</div>
			<div class="store-number">800</div>
			<div class="store-unit">个</div>
		</div>
		<div class="showImage">
			<canvas id="c"></canvas>
			<input type="range" id="r" min="0" max="100" step="1">
		</div>
	</div>
</template>

<script>
export default {
	methods: {
		createCanvas () {
			var canvas = document.getElementById('c');
			var ctx = canvas.getContext('2d');
			var range = document.getElementById('r');
			 
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
			var xOffset = 30;
			ctx.lineWidth = lineWidth;
			 
			var IsdrawCircled = false;

			var drawCircle = function(){

				ctx.setLineDash([4,5]); 
				ctx.lineWidth = 16; 

				ctx.beginPath();
			    ctx.strokeStyle = 'white';
			    ctx.arc(r, r, cR+14, 0, 2 * Math.PI);
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
			    ctx.globalAlpha = 0.2;
			    ctx.lineTo(points[0][0],points[0][1]);
			    ctx.fillStyle = 'white';
			    ctx.fill();


			 
			    ctx.restore();
			};
			 

			var drawText = function(){
			   ctx.save();
			 
			   var size = 0.8*cR;
			   ctx.font = size + 'px led-number';
			   ctx.textAlign = 'center';
			   ctx.fillStyle = "#c5f0f9";
			   ctx.fillText(~~nowRange + '%', r, r + size / 2);

			
			 
			   ctx.restore();
			};

			var drawTitle = function(){
			   ctx.save();
			 
			   var size = 0.25*cR;
			   ctx.font = size + 'px led-number';
			   ctx.textAlign = 'center';
			   ctx.fillStyle = "#c5f0f9";
			   ctx.fillText('齐套率', r, r-50);	
			 
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
			    drawTitle(); 
			 
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
	.need, .store {
		position: absolute;
		width: 40%;
		height: 30%;
		left: 15%;
	}
	.need {
		top: 18%;
	}
	.store {
		top: 58%;
	}
	.need-title, .store-title {
		position: absolute;
		color: #02d8d8;
		font-size: 1em;
		top: -5%;
	}
	.need-number, .store-number {
		position: absolute;
		font-family: led-number;
		top: 33%;
		font-size: 3em;
		color: white;
		background: black;
		width: 55%;
		letter-spacing: 2.1vw;
		border: 0.2px solide #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	border-radius: 3px;
	}
	.need-unit, .store-unit {
		position: absolute;
		font-family: led-number;
		font-size: 1.9em;
		color: white;
		left: 65%;
		bottom: -11%;
	}
	.showImage {
		position: absolute;
		width: 40%;
		height: 80%;
		top: 10%;
		right: 4%;
	}
	#c {
		position: absolute;
		top: 10%;
		left: 0;
		width: 83%;
		height: 91%;
		display: block;
   		margin: 0 auto;
	}
	#r{
	   display: none;
	   margin: 0 auto;
	  }
	  #r::before{
	   color: black;
	   content: attr(min);
	   padding-right: 10px;
	  }
	  #r::after{
	   color: black;
	   content: attr(max);
	   padding-left: 10px;
	  }  
</style>