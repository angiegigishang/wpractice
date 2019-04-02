<template>
	<div style="height: 100%">
		<div id="mains" style="width: 100%;height:100%; "></div>
        <!-- <img class="bluelight" src="../.././assets/images/bluelight.png"/> -->
	</div>
</template>

<script>

export default {
    props: {
        list: Array
    },
    data () {
        return {
           
        }
    },
    mounted() {
         var echarts = this.$echarts;
       	 var myChartTree = this.$echarts.init(document.getElementById('mains'));
         //window.onresize = myChartTree.resize;
       	 var option ={
                        legend: {
                           textStyle: {
                               color: 'white'
                           }
                        },
                         grid: {
                            left: '5%',
                            right: '4%',
                            width: '85%'
                        },
                        tooltip: {},
                        dataset: {
                            source: this.list
                        }, 
                        xAxis: {
                            type: 'category',
                            color: '#2190fe',
                            axisLine: {
                                lineStyle: {
                                    color: '#2190fe',
                                    width: 0.6
                                }
                            },
                            splitLine: {
                                show: true,
                                lineStyle: {
                                    type: 'solid',
                                    color: '#2190fe',
                                    width: 0.3
                                }
                            },
                            splitArea : {
                                show : false
                            },
                            axisLabel: {  
                               color: '#2190fe',
                               fontWeight: 'bolder',
                               fontSize: 16
                            }  
                        },
                        yAxis: {
                            axisLine: {
                                lineStyle: {
                                    color: '#2190fe',
                                    width: 0.5
                                }
                            },
                            splitLine: {
                                show: true,
                                lineStyle: {
                                    type: 'solid',
                                    color: '#2190fe',
                                    width: 0.3
                                }
                            },
                            splitArea : {
                                show : false,
                            },
                            axisLabel: {  
                               color: '#2190fe',
                               fontWeight: 'bolder',
                               fontSize: 13
                            }  
                        },
                        // Declare several bar series, each will be mapped
                        // to a column of dataset.source by default.
                        series: [
                            {
                                type: 'bar',
                                color: new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#45cce7'},
                                        {offset: 0.1, color: '#1fc1e3'},
                                        {offset: 0.2, color: '#1ea4c4'},
                                        {offset: 0.3, color: '#1589a9'},
                                        {offset: 0.4, color: '#187494'},
                                        {offset: 0.6, color: '#144762'},
                                        {offset: 1, color: '#0e1d2d'}
                                    ]
                                ),
                                barCategoryGap:'80%',
                                label: {
                                    normal: {
                                        show: true,
                                        position: 'top',
                                        color: 'white'
                                    }
                                }
                            },
                        ]
                };
                
            if (option && typeof option === "object") {
                myChartTree.setOption(option, true);
            }
   }
}
</script>

<style scoped>
    body {
        position: relative;
        height: 100%;
    }
    .mains {
        position:absolute;
    }
    .bluelight {
        position: absolute;
        bottom: 8%;
        left: 0;
        width: 100%;
        height: 30%;
    }
</style>