<template>
	<div>
		<div class="treeimage">
			<div class="box1">
				<p class="box1-target">任务数</p>
				<p class="box1-plan">计划数:100</p>
			</div>
			<div class="box2">
				<p class="box-product">零件1</p>
				<p class="box-neednum">需求数:13</p>
				<p class="box-storenum">库存数:11</p>
			</div>
			<div class="box3">
				<p class="box-product">零件2</p>
				<p class="box-neednum">需求数:19</p>
				<p class="box-storenum">库存数:12</p>
			</div>
			<div class="box4">
				<p class="box-product">零件3</p>
				<p class="box-neednum">需求数:50</p>
				<p class="box-storenum">库存数:41</p>
			</div>
			<div class="line1"></div>
			<div class="line2"></div>
			<div class="line3"></div>
			<div class="line4"></div>
			<div class="line5"></div>
		</div>
	</div>
</template>

<script></script>

<style lang="stylus" scoped>
    * {
    	padding: 0;
    	margin: 0;
    }
	.treeimage{
		position: relative;
		width: 100%;
		height: 20em;
		left: 0;
	}
	.box1, .box2, .box3, .box4 {
		position: absolute;
		width: 20%;		
		border: 1px solid #6dabb9;
        box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
        border-radius: 10px;
        text-align: center;
	}
	p {
    	color: white;
    }
	.box1{	
		left: 1%;		
        top: 15%; 
        height: 27%;   
    }
    .box1 p {
    	margin-top: 10%;
    } 
    .box2{
		left: 35%;
        top: 5%;
        height: 20%; 
    }
    .box3{
    	left: 35%;
    	top: 30%;
    	height: 20%; 
    }
    .box4{
    	left: 70%;
    	top: 5%;
    	height: 20%; 
    }
    .line1, .line2, .line3, .line4, .line5 {
    	position: absolute;
    	overflow:hidden;
    	border-radius: 2px;
    	background-color:#74b9c5;
    }
    .line1 {  	
    	width:8%;
    	height:2%;  		
    	top: 24%;
    	left: 21%
    }
    .line2 {
    	width: 1%;
    	height: 24%;
    	left: 28%;
    	top: 14%;
    }
    .line3 {  	
    	width:7%;
    	height:2%;  		
    	top: 14%;
    	left: 28%
    }
    .line4 {  	
    	width:7%;
    	height:2%;  		
    	top: 37%;
    	left: 28%
    }
    .line5 {  	
    	width:15%;
    	height:2%;  		
    	top: 14%;
    	left: 55%
    }
    .box-product, .box1-target {
    	color: #a6adb2;
    	font-size: 0.8em;
    }
	    		
</style>