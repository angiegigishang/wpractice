<template>
	<div>
    <img src=".././assets/images/title.png" style="width: 100%;"/>

		<div class="product-square">		
			<p class="title">|产品纬度统计生产进度</p>
			<productSquare :list="productList"></productSquare>
		</div>

		<div class="datasetTable">
			<datasetTable :list="datasetList"></datasetTable>
		</div>


    <div class="gauge1">
      <gauge :list="gagueaaList"></gauge>
      <p class="gongxu1">完成率</p>
      <p class="gongxu-title">工序1</p>
    </div>
    <div class="gauge2">
      <gauge :list="gagueabList"></gauge>
      <p class="gongxu2">完成率</p>
      <p class="gongxu-title">工序2</p>
    </div>
    <div class="gauge3">
      <gauge :list="gagueacList"></gauge>
      <p class="gongxu3">完成率</p>
      <p class="gongxu-title">工序3</p>
    </div>

    <div class="treeTable">
      <p class="treeTable-title">|设备纬度统计生产进度</p> 
      <treeTable :list="tableList"></treeTable>     
    </div>

    <div class="treeimage">
      <treeImage></treeImage>
    </div>

		<div class="treeCalculate">
      <p class="calculate-title">|零件库存情况</p> 
      <treeCalculate :list="calculateList"></treeCalculate>
    </div>

    <div class="bottomtable">
    	<img src=".././assets/images/bluelight-bottom.png" style="width: 100%; bottom: 0; position: absolute; z-index: -1"/>
    </div>
	</div>
</template>

<script>
import datasetTable from './detail/datasetTable.vue'
import gauge from './detail/gauge.vue'
import productSquare from './detail/productSquare'
import treeTable from './detail/treeTable.vue'
import treeCalculate from './detail/treeCalculate.vue'
import treeImage from './detail/treeImage.vue'
export default {

  components: {
    datasetTable,
   	gauge,
   	productSquare,
    treeTable,
    treeCalculate,
    treeImage
  },
  data () {
    return {
      productList: [
       {
            'name': '产品01',
            'targetnum': 1000,
            'finishnum': 800,
            'id': 1
        }, {
            'name': '产品02',
            'targetnum': 2000,
            'finishnum': 90,
            'id': 2
        }, {
            'name': '产品03',
            'targetnum': 1800,
            'finishnum': 300,
            'id': 3
        }, {
            'name': '产品04',
            'targetnum': 5000,
            'finishnum': 400,
            'id': 4
        }, {
            'name': '产品05',
            'targetnum': 1200,
            'finishnum': 1100,
            'id': 5
        }, {
            'name': '产品06',
            'targetnum': 2200,
            'finishnum': 101,
            'id': 6
        }
      ],
      datasetList: [
        ['product', '完成数', '任务数'],
        ['工序1', 400, 1000],
        ['工序2', 300, 800],
        ['工序3', 700, 1000]
      ],
      gagueaaList: {
          'title': 'gaugea',
          'textColor': '#1e90ff',
          'gaugeName': '工序1',
          'gaugeData': {
              'value': 82, 
              'name': '82%'
          },
          'gaugeColor':[[0.82, '#1e90ff'],[1, 'grey']],
          'id': 1
      },
      gagueabList: {
          'title': 'gaugeb',
          'textColor': 'lime',
          'gaugeName': '工序2',
          'gaugeData': {
              'value': 60, 
              'name': '60%'
          },
          'gaugeColor': [[0.6, 'lime'],[1, 'grey']],
          'id': 2
      },  
      gagueacList: {
          'title': 'gaugec',
          'textColor': '#ff4500',
          'gaugeName': '工序3',
          'gaugeData': {
              'value': 70, 
              'name': '70%'
          },
          'gaugeColor': [[0.7, '#ff4500'],[1, 'grey']],
          'id': 3
      },
      tableList: [
       {
            'name': '产品01',
            'targetnum': 1000,
            'id': 1
        }, {
            'name': '产品02',
            'targetnum': 2000,
            'id': 2
        }, {
            'name': '产品03',
            'targetnum': 1800,
            'id': 3
        }, {
            'name': '产品04',
            'targetnum': 5000,
            'id': 4
        }, {
            'name': '产品05',
            'targetnum': 1200,
            'id': 5
        }, {
            'name': '产品06',
            'targetnum': 2200,
            'id': 6
        }
      ],
      calculateList:[
        ['product', '完成数', '任务数'],
        ['设备1', 400],
        ['设备2', 300],
        ['设备3', 600],
        ['设备4', 200],
        ['设备5', 700]
      ]
    }
  }
}
</script>

<style lang="stylus">
  body {
		background-image: url('.././assets/images/background.png');
		background-size: cover;
		background-position: center;
		position: relative;
		height: 100%;
    overflow: hidden;
    font-size: 1em;
  }
  html {
    font-size: 100%;
  }
  ::-webkit-scrollbar {/*滚动条整体样式*/
    width: 1em;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 1em;
    background: #121924;
  }
  ::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    background-image: url('.././assets/images/bluelight.png');
    background-size: cover;
    background-position: center;
  }
  ::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
    border-radius: 10px;
    background: #121924;
  }
    
  .product-square 
    position absolute
    height 25%
    width 100%
    top 2.5%
    overflow-x auto
    overflow-y hidden
    white-space nowrap
    .title 
    	font-size 1.2em
    	font-weight bold
    	color #38b8e5
    	position fixed
    	top 4%
    	left 1%      
   
  .datasetTable {
  	position: absolute;
  	top: 28%;
  	left: 2%;
  	width: 77%;
  	height: 40%; 
  }
  
  .gongxu1, .gongxu2, .gongxu3 {
    position: absolute;
    bottom: 0;
    left: 35%;
    font-size: 1em;
    font-weight: bold;
    color: grey;
    font-style: 'italic';
  }
  .gongxu-title {
    position: absolute;
    bottom: 20%;
    left: 42%;
    font-size: 1.3em;
    color: white;
    font-size: 'italic';
  }
  .gauge1 {
    position: absolute;
    top: 29%;
    right: 1%;
    width: 20%;
    height: 21%;
  }
  .gauge2 {
    position: absolute;
    top: 52%;
    right: 1%;
    width: 20%;
    height: 21%;
  }
  .gauge3 {
    position: absolute;
    top: 75%;
    right: 1%;
    width: 20%;
    height: 21%;
  }

  .bottomtable {
  	position: absolute;
  	bottom: 0;
  	height: 30%;
  	width: 100%;
  }
  .treeTable {
    position: absolute;
    top: 70%
    right: 20%;
    bottom: 5%;
    width: 40%;
    height: 12%;
    overflow-x: auto;
    overflow-y hidden
    white-space: nowrap;
    z-index: 2;
  }
  .treeTable-title {
    font-size: 1.2em;
    font-weight: bold;
    color: #38b8e5;
    position: fixed;
    top: 67%;
    left: 40%;
  }
  .calculate-title {
    font-size: 1.2em;
    font-weight: bold;
    color: #38b8e5;
    position: fixed;
    top: 67%;
    left: 2%;
  }
  .treeCalculate{
    position: absolute;
    left: 2%;
    bottom: 0;
    width: 40%;
    height: 34%;
  }
  .treeimage {
    position: absolute;
    top: 81%
    right: 20%;
    bottom: 5%;
    width: 40%;
    height: 18%;
    z-index: 1;
  }
</style>
