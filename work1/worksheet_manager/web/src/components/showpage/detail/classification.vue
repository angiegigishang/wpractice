<template>
	<div class="container">
		<img src="../../.././assets/images/v2/leibie.png"/>
		
		<swiper class="swiper-slide" :options="swiperOption">
			<swiper-slide>
				<div class="productsquare">
					<div class="productsquare1">
						<div class="product-title">
			                产品1
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">2000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare2">
						<div class="product-title">
			                产品2
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">2000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare3">
						<div class="product-title">
			                产品3
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">2000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare4">
						<div class="product-title">
			                产品4
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">2000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
				</div>
			</swiper-slide>
			<swiper-slide>
				<div class="productsquare">
					<div class="productsquare1">
						<div class="product-title">
			                产品5
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">3000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare2">
						<div class="product-title">
			                产品6
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">3000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare3">
						<div class="product-title">
			                产品7
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">3000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
					<div class="productsquare4">
						<div class="product-title">
			                产品8
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">3000</p>
			                    <p class="unit">个</p>
			            </div>
					</div>
				</div>
			</swiper-slide>
		</swiper>
		
	</div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
export default {
    name: "product",
    components: {
    	swiper,
	    swiperSlide
    },
    data () {
		return {
			swiperOption: {
				loop: true,
				autoplay: {
				    delay: 5000,
				    stopOnLastSlide: false,
				    disableOnInteraction: true,
				}
			}
		}
	}
    // props: {
    //     list: Array
    // },
    // data () {
    //     return {
    //         finishnumber: 200
    //     }
    // },
    // computed: {
    //     finishnumbers () {
    //         var self = this
    //         for(var key in this.list) {
    //             var item = this.list[key] 
    //             var targetlength = String(item.targetnum).length;
    //             var finishlength = String(item.finishnum).length;
    //             if (targetlength !== finishlength) {
    //                 item.finishnum = (Array(targetlength).join('0') + item.finishnum).slice(-targetlength)
    //                 //self.changeNum(item.finishnum, targetlength)
    //             }            
    //         }
    //         return this.list
    //     }
    // },
    // methods: {
      
    // }
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
    .productsquare {
    	position: absolute;
    	height: 100%;
    	width: 100%;
    }
    .productsquare1, .productsquare2, .productsquare3, .productsquare4 {
    	position: absolute;
		width: 40%;
    	height: 28%;
    	border-radius: 3px;
    	cursor: pointer;
    }
    .productsquare1 {	
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;	
    	top: 19%;
    	left: 7%;	
    }
    .productsquare2 {
    	border: 1px solid #bb494d;
    	box-shadow: 0px 0px 0.1px 0.8px #bb494d;
    	top: 19%;
    	right: 7%;
    }
    .productsquare3 {
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	bottom: 14%;
    	right: 7%;
    }
    .productsquare4 {
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	bottom: 14%;
    	left: 7%;
    }
    .product-title {
    	position: absolute;
        height: 25%;
        text-align: center;
        display:table;
        width: 100%;
        top:0;
        left:0;
        background:#1f5972;
        color:#ecffff;
    }
    .middle-target {
    	position: absolute;
    	height: 25%;
    	width: 100%;
        text-align: center;
        top: 50%;
        left: 0;
    }
    .target-title {
    	color: #62b0c9;
    	letter-spacing: 0.1vw;
    }
    .target-number {
    	font-family: led-number;
    	font-size: 1.3rem;
    	color: white;
    	background: black;
    	margin-left: 4%;
    	margin-right: 3%;
    	letter-spacing: 0.8vw;
    	border: 0.2px solide #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	border-radius: 3px;
    }
    .unit {
    	color: white;
    	font-weight: bold;
    }
    p {
    	display: inline-block;
    }          
</style>