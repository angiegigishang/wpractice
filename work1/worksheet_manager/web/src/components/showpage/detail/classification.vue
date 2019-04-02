<template>
	<div class="container">
		<img src="../../.././assets/images/v2/leibie.png"/>
		
		<swiper class="swiper-slide" :options="swiperOption">
			<swiper-slide v-for="(page, index) of pages" :key="index">
				<div class="productsquare"
				     v-for="item of page"
				     :key="item.id">
					<div class="productsquare1" :id="item.id">
						<div class="product-title">
			                {{item.productTitle}}
			            </div>
			            <div class="middle-target">
			                    <p class="target-title">任务数<p>
			                    <p class="target-number">{{item.targetNumber}}</p>
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
    name: "classification",
    components: {
    	swiper,
	    swiperSlide
    },
    props: {
        list: Array
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
	},
	computed: {
		pages () {
			var self = this
            for(var key in this.list) {
                var item = this.list[key] 
                var targetlength = String(item.targetNumber).length;
                var finishlength = 4;
                if (targetlength !== finishlength) {
                    item.targetNumber = (Array(finishlength).join('0') + item.targetNumber).slice(-finishlength)
                }            
            }
			const pages = []
			this.list.forEach( (item, index) => {
				const page = Math.floor(index / 4)
				if(!pages[page]) {
					pages[page] = []
				}
				pages[page].push(item)
			})
			return pages
		}
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
    .productsquare {
    	position: absolute;
    	height: 100%;
    	width: 100%;
    }
    .productsquare1 {
    	position: absolute;
		width: 40%;
    	height: 28%;
    	border-radius: 3px;
    	cursor: pointer;
    }
    #productsquare1, #productsquare5 {	
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;	
    	top: 19%;
    	left: 7%;	
    }
    #productsquare2, #productsquare6 {
    	border: 1px solid #bb494d;
    	box-shadow: 0px 0px 0.1px 0.8px #bb494d;
    	top: 19%;
    	right: 7%;
    }
    #productsquare3, #productsquare7 {
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	bottom: 14%;
    	right: 7%;
    }
    #productsquare4, #productsquare8 {
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