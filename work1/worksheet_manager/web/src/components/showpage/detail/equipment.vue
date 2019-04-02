<template>
	<div class="container">
		<img src="../../.././assets/images/v2/shebeibuju.png"/>
		<div class="equipment-img">
			<img src="../../.././assets/images/v2/content2.png"/>
		</div>
		<div class="detail2" @click="alerttext()">
			<img src="../../.././assets/images/v2/yuanse/2.png"/>
		</div>
		<div class="detail2-text" v-show="showDetail2">
			<img src="../../.././assets/images/dialogue.png"/>
			<div class="text1">产品名称： 产品1</div>
			<div class="text2">加工人数： 张三</div>
			<div class="text3">加工数量： 100</div>
		</div>

		<div class="detail5" @click="alerttext()" v-show="showDetail5" >
			<img src="../../.././assets/images/v2/yuanse/5.png"/>
		</div>
		<div class="detail5-text" v-show="showDetail5">
			<img src="../../.././assets/images/dialogue.png"/>
			<div class="text1">产品名称： 产品2</div>
			<div class="text2">加工人数： 李四</div>
			<div class="text3">加工数量： 300</div>
		</div>
	</div>
</template>

<script>
export default {
	data () {
		return {
			showDetail2: false,
			showDetail3: true,
			showDetail5: false
		}
	}, 
	methods: {
		alerttext2 () {	
		    var self = this;		
			setInterval(function(){ 
				self.showDetail2 = !self.showDetail2;		
			}, 3000);		
		},
		alerttext5 () {	
		    var self = this;		
			setInterval(function(){ 
				self.showDetail5 = !self.showDetail5;		
			}, 6010);		
		}
	},
	computed: {
		showDetail () {
			return this.alerttext()
		}
	},
	mounted () {
		this.alerttext2();
		this.alerttext5();
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
	.equipment-img {
		position: absolute;
		width: 90%;
		height: 88%;
		top: 8%;
		left: 4%;
	}
	.detail2 {
		position: absolute;
	    width: 3%;
	    height: 9%;
	    left: 27%;
	    top: 33%;
	}
	.detail5 {
		position: absolute;
	    width: 4%;
	    height: 9%;
	    left: 24%;
	    top: 73%;
	}
	.detail2-text {
		position: absolute;
		width: 15%;
		height: 16%;
		left: 31%;
		top: 30%;
	}
	.detail5-text {
		position: absolute;
		width: 15%;
		height: 16%;
		left: 28%;
		top: 70%;
	}
	.text1, .text2, .text3 {
		position: absolute;
		width: 90%;
		height: 30%;
        /*left: 28%;*/
        left: 9%;
        font-size: 0.4em;
        color: white;
        text-align: center;
	}
	.text1 {
		top: 9%;
	}
	.text2 {
		top: 35%;
	}
	.text3 {
		top: 61%;
	}
</style>