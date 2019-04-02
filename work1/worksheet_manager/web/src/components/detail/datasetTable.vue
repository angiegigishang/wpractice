<template>
	<div style="height: 100%">
		<div id="main" style="width: 100%;height:100%; "></div>
        <img class="bluelight" src="../.././assets/images/bluelight.png"/>
	</div>
</template>

<script>

export default {
    name: "datasetTable",
    props: {
        list: Array
    },
    data() {
        return {
            data: []
        }
    },
    mounted() {
       	var myChartTable = this.$echarts.init(document.getElementById('main'));
        window.onresize = myChartTable.resize;
        var data = this.list;
       	var option ={
                        legend: {
                           textStyle: {
                               color: 'white'
                           }
                        },
                         grid: {
                            left: '3%',
                            right: '4%',
                            width: '95%'
                        },
                        tooltip: {},
                        dataset: {
                            source: data
                        },
                        xAxis: {
                            type: 'category',
                            color: '#2190fe',
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
                                color: '#155ea5',
                                barCategoryGap:'60%',
                                label: {
                                    normal: {
                                        show: true,
                                        position: 'top',
                                        color: 'white'
                                    }
                                }
                            },
                            {
                                type: 'bar',
                                color: '#2190fe',
                                label: {
                                    normal: {
                                        show: true,
                                        position: 'top',
                                        color: 'white'
                                    }
                                }
                            }
                        ]
                };
                
            if (option && typeof option === "object") {
                myChartTable.setOption(option, true);
            }
   }
}
</script>

<style scoped>
    body {
        position: relative;
        height: 100%;
    }
    .main {
        position:absolute;
    }
    .bluelight {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30%;
    }
</style>