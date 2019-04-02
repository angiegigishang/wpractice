<template>
	<div class="container">
		<img src="../../.././assets/images/v2/kucun.png"/>
		<div class="animate1">
			<animates :list="c1List"></animates>
		</div>
		<div class="animate2">
			<animates :list="c2List"></animates>
		</div>
		<div class="animate3">
			<animates :list="c3List"></animates>
		</div>
		<div class="animate4">
			<animates :list="c4List"></animates>
		</div>
		<div class="animate5">
			<div class="mask6"></div>
			<animates :list="c5List"></animates>
		</div>
		<div class="animate6">
			<div class="mask6"></div>
			<animates :list="c6List"></animates>
		</div>
		<div class="animate7">
			<animates :list="c7List"></animates>
		</div>
		<div class="animate8">
			<animates :list="c8List"></animates>
		</div>
		<div class="animate9">
			<animates :list="c9List"></animates>
		</div>
		<div class="sparkLine line1">			    		
     	</div>
     	<div class="sparkLine line2">			    		
     	</div>
     	<div class="sparkLine line3">			    		
     	</div>
     	<div class="sparkLine line4">			    		
     	</div>
     	<div class="sparkLine line5">			    		
     	</div>
     	<div class="sparkLine line6">			    		
     	</div>
     	<div class="sparkLine line7">			    		
     	</div>
     	<div class="sparkLine line8">			    		
     	</div>
     	<div class="sparkLine line9">			    		
     	</div>
     	<div class="sparkLine line10">			    		
     	</div>
     	<div class="sparkLine line11">			    		
     	</div>
     	<div class="sparkLine1 line1-1">			    		
     	</div>
     	<div class="sparkLine1 line1-2">			    		
     	</div>
     	<div class="sparkLine1 line1-3">			    		
     	</div>		
	</div>
</template>

<script>
import animates from './animate.vue'
export default {
	data () {
		return {
			c1List: {
				'title': 'c1'
			},
			c2List: {
				'title': 'c2'
			},
			c3List: {
				'title': 'c3'
			},
			c4List: {
				'title': 'c4'
			},
			c5List: {
				'title': 'c5'
			},
			c6List: {
				'title': 'c6'
			},
			c7List: {
				'title': 'c7'
			},
			c8List: {
				'title': 'c8'
			},
			c9List: {
				'title': 'c9'
			}
		}
	},
	components: {
		animates
	},
	methods: {
		
	},
	mounted () {
		
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
	.sparkLine1 {
		position: absolute;
		background: #67b4c9;	
		width: 3px;
		border-radius: 5px;	
	}
	.line1-1 {
		height: 45%;
		top: 29%;
		left: 24.1%;
	}
	.line1-2 {
		height: 23%;
		top: 18%;
		left: 47.1%;
	}
	.line1-3 {
		height: 23%;
		top: 63%;
		left: 47.1%;
	}
	.sparkLine {
		position: absolute;
		background: #67b4c9;	
		height: 3px;
		border-radius: 5px;		
	}
	.line1 {
		width: 3%;
		top: 50%;
		left: 21.2%;
	}
	.line2 {
		width: 3%;
		top: 29%;
		left: 24.1%;
	}
	.line3 {
		width: 3%;
		top: 73.4%;
		left: 24.1%;
	}
	.line4 {
		width: 3%;
		top: 29%;
		left: 44.2%;
	}
	.line5 {
		width: 3%;
		top: 73.4%;
		left: 44.2%;
	}
	.line6 {
		width: 3%;
		top: 18%;
		left: 47.2%;
	}
	.line7 {
		width: 3%;
		top: 40.5%;
		left: 47.2%;
	}
	.line8 {
		width: 3%;
		top: 63%;
		left: 47.2%;
	}
	.line9 {
		width: 3%;
		top: 85.5%;
		left: 47.2%;
	}
	.line10 {
		width: 6%;
		top: 40.5%;
		left: 67.2%;
	}
	.line11 {
		width: 6%;
		top: 85.5%;
		left: 67.2%;
	}
	.animate1, .animate2, .animate3, .animate4, .animate5, .animate6, .animate7, .animate8, .animate9{
		position: absolute;
		width: 17%;
		height: 15%;	
	}
	.animate1 {
		top: 42.5%;
		left: 4%;
	}
	.animate2 {
		top: 21%;
		left: 27%;
	}
	.animate3 {
		bottom: 19%;
		left: 27%;
	}
	.animate4{
		top: 10%;
		left: 50%;
	}
	.animate5 {
		top: 32%;
		left: 50%;
	}
	.animate6 {
		top: 55%;
		left: 50%;
	}
	.mask6 {
		position: absolute;
		width: 100%;
		height: 100%;
		z-index: 2;
		background: red;
		opacity: 0.4;
		border: 2px solid red;
        box-shadow: 0px 0px 0.1px 0.8px red;
        border-radius: 10px;
	}
	.animate7 {
		top: 78%;
		left: 50%;
	}
	.animate8 {
		top: 32%;
		left: 73%;
	}
	.animate9 {
		top: 78%;
		left: 73%;
	}

</style>