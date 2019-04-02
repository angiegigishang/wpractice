<template>
	<div class="container">
		<img src="../../.././assets/images/v2/scjindu.png"/>
		
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
			            <div class="middle-finish">
			                <p class="finish-title">完成数</p>
			                <p class="finish-number">{{item.finishNumber}}</p>
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
                var finishlength = String(item.finishNumber).length;
                if (targetlength !== finishlength) {
                    item.finishNumber = (Array(targetlength).join('0') + item.finishNumber).slice(-targetlength)
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
    #productsquare1, #productsquare5 {
    	position: absolute;
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	border-radius: 3px;
    	width: 40%;
    	height: 35%;
    	top: 18%;
    	left: 7%;
    	cursor: pointer;
    }
    #productsquare2, #productsquare6 {
    	position: absolute;
    	border: 1px solid #bb494d;
    	box-shadow: 0px 0px 0.1px 0.8px #bb494d;
    	border-radius: 3px;
    	width: 40%;
    	height: 35%;
    	top: 18%;
    	right: 7%;
    	cursor: pointer;
    }
    #productsquare3, #productsquare7 {
    	position: absolute;
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	border-radius: 3px;
    	width: 40%;
    	height: 35%;
    	bottom: 5%;
    	right: 7%;
    	cursor: pointer;
    }
    #productsquare4, #productsquare8 {
    	position: absolute;
    	border: 1px solid #6dabb9;
    	box-shadow: 0px 0px 0.1px 0.8px #6dabb9;
    	border-radius: 3px;
    	width: 40%;
    	height: 35%;
    	bottom: 5%;
    	left: 7%;
    	cursor: pointer;
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
        top: 30%;
        left: 0;
    }
    .middle-finish {
    	position: absolute;
    	height: 25%;
    	width: 100%;
        text-align: center;
        top: 65%;
        left: 0;
    }
    .target-title, .finish-title {
    	color: #62b0c9;
    	letter-spacing: 0.1vw;
    }
    .target-number, .finish-number {
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