<template>
	<div class="swiper-container">
	    <swiper class="swiper-slide" :options="swiperOption">
	        <swiper-slide >
	        	<div class="swiper-div">
	        		<div class="top-left">
	        			<product></product>
	        		</div>
	        		<div class="top-right">
	        			<process></process>
	        		</div>
	        		<div class="box-bottom">
	        			<equipment></equipment>
	        		</div>
	        	</div>
	        </swiper-slide>
	        <swiper-slide>
	        	<div class="swiper-div">
	        		<div class="top-left">
	        			<classification></classification>
	        		</div>
	        		<div class="top-right">
	        			<qitao></qitao>
	        		</div>
	        		<div class="box-bottom">
	        			<inventory></inventory>
	        		</div>
	        	</div>
	        </swiper-slide>
	    </swiper>
	    
        <img class="imgtitle" src="../.././assets/images/title.png"/>
        <img class="imgbottom" src="../.././assets/images/bluelight-bottom.png"/>
	    <div class="swiper-button-prev"></div>
	    <div class="swiper-button-next"></div> 
	</div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import product from './detail/product.vue'
import process from './detail/process.vue'
import equipment from './detail/equipment.vue'
import classification from './detail/classification.vue'
import qitao from './detail/qitao.vue'
import inventory from './detail/inventory.vue'

export default {
	components: {
	    swiper,
	    swiperSlide,
	    product,
	    process,
	    equipment,
	    classification,
	    qitao,
	    inventory
	},
	data () {
		return {
			swiperOption: {
				navigation: {
			      nextEl: '.swiper-button-next',
			      prevEl: '.swiper-button-prev'
			    },
				loop: true,
				// autoplay: {
				//     delay: 5000,
				//     stopOnLastSlide: false,
				//     disableOnInteraction: true,
				// }
			}
		}
	},
	mounted () {
		console.log(swiper, swiperSlide)
	}
}
</script>

<style>
	body {
		background-image: url('../.././assets/images/v2/background2.png');
		background-size: cover;
		background-position: center;
		z-index: -9;
		position: relative;
		height: 100%;
	    overflow: hidden;
	    font-size: 1em;
	}
	.swiper-container {
		position: absolute;
		height: 100%;
		width: 100%;
	}
	.swiper-div {
		position: absolute;
		width: 100%;
		height: 100%;
	}
	.swiper-button-next, .swiper-button-prev {
		outline: none;
		opacity: 0.3;
		z-index: 10;
	}
	.swiper-button-next:hover, .swiper-button-prev:hover {
		outline: none;
		opacity: 1;
		z-index: 10;
	}
	.imgtitle, .imgbottom {
		position: absolute;
		width: 100%;
		height: 20%;
		z-index: -10;
	}
	.imgbottom {
		bottom: 0;
	}
	.imgtitle {
		top: 0;
	}
	.top-left, .top-right, .box-bottom {
		position: absolute;
	}
	.top-left {
		top: 6%;
		width: 48.5%;
		height: 27%;
		left: 1%;
	}
	.top-right {
		top: 6%;
		width: 48.5%;
		height: 27%;
		right: 1%;
	}
	.box-bottom {
		bottom: 4%;
		height: 60%;
		width: 98%;
		left: 1%;
	}
</style>