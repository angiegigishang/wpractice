<template>
	<div class="container">
		<img src="../../.././assets/images/jindu.png"/>
		<div class="process-table1">
			<div class="ptitle1">工序01</div>
			<div class="process1 process">
		    	<span class="progress__text">	      		
		    	</span>
			</div>
			<div class="pnum1">160/200</div>
			<div class="pnum2">80%(个)</div>
		</div>
		<div class="process-table2">
			<div class="ptitle1">工序01</div>
			<div class="process2 process">
		    	<span class="progress__text">      	
		    	</span>
			</div>
			<div class="pnum1">160/200</div>
			<div class="pnum2">80%(个)</div>
		</div>
		<div class="process-table3">
			<div class="ptitle1">工序01</div>
			<div class="process3 process">
		    	<span class="progress__text">      	
		    	</span>
			</div>
			<div class="pnum1">160/200</div>
			<div class="pnum2">80%(个)</div>
		</div>
		<div class="process-table4">
			<div class="ptitle1">工序01</div>
			<div class="process4 process">
		    	<span class="progress__text">      	
		    	</span>
			</div>
			<div class="pnum1">160/200</div>
			<div class="pnum2">80%(个)</div>
		</div>
		<div class="process-table5">
			<div class="ptitle1">工序01</div>
			<div class="process5 process">
		    	<span class="progress__text">      	
		    	</span>
			</div>
			<div class="pnum1">160/200</div>
			<div class="pnum2">80%(个)</div>
		</div>					
	</div>
</template>

<script>
export default {

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
  .ptitle1, .pnum1, .pnum2 {
    position: absolute;
    font-weight: bold;  
  }
  .ptitle1 {  
    color: #02dbdb;
    width: 20%;
    left: 5%;
    top: -22%;      
  }
  .pnum1 {
    color: white;
    right: 22%;
  }
  .pnum2 {
    color: #03d8d7;
    right: 10%;
    top: -22%;
  }
  .process-table1, .process-table2, .process-table3, .process-table4, .process-table5 {
    position: absolute;
    height: 5%;
    width: 100%;  
  }
  .process-table1 {
    top: 18%;
  }
  .process-table2 {
    top: 32%;
  }
  .process-table3 {
    top: 47%;
  }
  .process-table4 {
    top: 62%;
  }
  .process-table5 {
    top: 77%;
  }
  .process1 {
    width: 80%;
     -color: rgba(18, 135, 204, 0.95);
      background-image: -webkit-linear-gradient(0deg, rgba(20, 151, 227, 0) 10%, rgba(37, 162, 236, 0.8) 30%, #3dacee 70%, rgba(37, 162, 236, 0.8) 80%, rgba(20, 151, 227, 0) 90%), -webkit-linear-gradient(left, rgba(61, 172, 238, 0) 0%, #3dacee 100%), -webkit-linear-gradient(right, rgba(61, 172, 238, 0) 0%, #3dacee 100%);
      background-image: linear-gradient(90deg, rgba(20, 151, 227, 0) 10%, rgba(145, 209, 247, 0.8) 30%, #57fff7 70%, rgba(87, 174, 226, 0.8) 80%, rgba(20, 151, 227, 0) 90%), linear-gradient(to right, rgba(61, 172, 238, 0) 0%, #0d7ec1 100%), linear-gradient(to left, rgba(61, 172, 238, 0) 0%, #3dacee 100%);
      border-color: #54b6f0;
      box-shadow: 0 0 0.6em #25a2ec inset, 0 0 0.4em #1497e3 inset, 0 0 0.5em rgba(18, 135, 204, 0.5), 0 0 0.1em rgba(225, 242, 252, 0.5);
  }
  .process2 {
    width: 50%;
    background-color: rgba(232, 158, 0, 0.95);
      background-image: -webkit-linear-gradient(0deg, rgba(255, 174, 2, 0) 10%, rgba(255, 183, 28, 0.8) 30%, #ffbf36 70%, rgba(255, 183, 28, 0.8) 80%, rgba(255, 174, 2, 0) 90%), -webkit-linear-gradient(left, rgba(255, 191, 54, 0) 0%, #ffbf36 100%), -webkit-linear-gradient(right, rgba(255, 191, 54, 0) 0%, #ffbf36 100%);
      background-image: linear-gradient(90deg, rgba(255, 174, 2, 0) 10%, rgba(255, 183, 28, 0.8) 30%, #ffbf36 70%, rgba(255, 183, 28, 0.8) 80%, rgba(255, 174, 2, 0) 90%), linear-gradient(to right, rgba(255, 191, 54, 0) 0%, #ffbf36 100%), linear-gradient(to left, rgba(255, 191, 54, 0) 0%, #ffbf36 100%);
      border-color: #ffc74f;
      box-shadow: 0 0 0.6em #ffb71c inset, 0 0 0.4em #ffae02 inset, 0 0 0.5em rgba(232, 158, 0, 0.5), 0 0 0.1em rgba(255, 248, 232, 0.5);
  }
  .process3 {
    width: 60%;
    background-color: rgba(18, 135, 204, 0.95);
      background-image: -webkit-linear-gradient(0deg, rgba(20, 151, 227, 0) 10%, rgba(37, 162, 236, 0.8) 30%, #3dacee 70%, rgba(37, 162, 236, 0.8) 80%, rgba(20, 151, 227, 0) 90%), -webkit-linear-gradient(left, rgba(61, 172, 238, 0) 0%, #3dacee 100%), -webkit-linear-gradient(right, rgba(61, 172, 238, 0) 0%, #3dacee 100%);
      background-image: linear-gradient(90deg, rgba(20, 151, 227, 0) 10%, rgba(145, 209, 247, 0.8) 30%, #57fff7 70%, rgba(87, 174, 226, 0.8) 80%, rgba(20, 151, 227, 0) 90%), linear-gradient(to right, rgba(61, 172, 238, 0) 0%, #0d7ec1 100%), linear-gradient(to left, rgba(61, 172, 238, 0) 0%, #3dacee 100%);
      border-color: #54b6f0;
      box-shadow: 0 0 0.6em #25a2ec inset, 0 0 0.4em #1497e3 inset, 0 0 0.5em rgba(18, 135, 204, 0.5), 0 0 0.1em rgba(225, 242, 252, 0.5);
  }
  .process4 {
    width: 10%;
    background-color: rgba(0, 178, 23, 0.95);
      background-image: -webkit-linear-gradient(0deg, rgba(0, 203, 26, 0) 10%, rgba(0, 229, 30, 0.8) 30%, #00fe21 70%, rgba(0, 229, 30, 0.8) 80%, rgba(0, 203, 26, 0) 90%), -webkit-linear-gradient(left, rgba(0, 254, 33, 0) 0%, #00fe21 100%), -webkit-linear-gradient(right, rgba(0, 254, 33, 0) 0%, #00fe21 100%);
      background-image: linear-gradient(90deg, rgba(0, 203, 26, 0) 10%, rgba(0, 229, 30, 0.8) 30%, #00fe21 70%, rgba(0, 229, 30, 0.8) 80%, rgba(0, 203, 26, 0) 90%), linear-gradient(to right, rgba(0, 254, 33, 0) 0%, #00fe21 100%), linear-gradient(to left, rgba(0, 254, 33, 0) 0%, #00fe21 100%);
      border-color: #19ff37;
      box-shadow: 0 0 0.6em #00e51e inset, 0 0 0.4em #00cb1a inset, 0 0 0.5em rgba(0, 178, 23, 0.5), 0 0 0.1em rgba(178, 255, 188, 0.5);
  }
  .process5 {
    width: 80%;
    background-color: rgba(201, 47, 0, 0.95);
    background-image: -webkit-linear-gradient(0deg, rgba(227, 53, 0, 0) 10%, rgba(252, 59, 0, 0.8) 30%, #ff4d17 70%, rgba(252, 59, 0, 0.8) 80%, rgba(227, 53, 0, 0) 90%), -webkit-linear-gradient(left, rgba(255, 77, 23, 0) 0%, #ff4d17 100%), -webkit-linear-gradient(right, rgba(255, 77, 23, 0) 0%, #ff4d17 100%);
    background-image: linear-gradient(90deg, rgba(227, 53, 0, 0) 10%, rgba(241, 200, 86, 0.8) 30%, #fda850 70%, rgba(156, 90, 36, 0.8) 80%, rgba(227, 53, 0, 0) 90%), linear-gradient(to right, rgba(255, 77, 23, 0) 0%, #ef9942 100%), linear-gradient(to left, rgba(255, 77, 23, 0) 0%, #f56134 100%);
    border-color: #ff6030;
    box-shadow: 0 0 0.6em #fc3b00 inset, 0 0 0.4em #e33500 inset, 0 0 0.5em rgba(201, 47, 0, 0.5), 0 0 0.1em rgba(255, 214, 201, 0.5);
  }
  .process {
    position: absolute;
    left: 16%;
    height: 100%; 
    font-size: 0.8em;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 2px;
    border: 1px solid white;
    color: white;       
    -webkit-transition: opacity 0.2s ease, width 0.8s ease-out, background-color 1s ease, border-color 0.3s ease, box-shadow 1s ease;
        transition: opacity 0.2s ease, width 0.8s ease-out, background-color 1s ease, border-color 0.3s ease, box-shadow 1s ease;
      -webkit-animation: pulse 2s ease-out infinite;
            animation: pulse 2s ease-out infinite;
      
  }
</style>