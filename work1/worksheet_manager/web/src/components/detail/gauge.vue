<template>
	<div style="height: 100%">
		<div :id="this.list.title" style="height: 100%; width: 100%"></div>
	</div>
</template>

<script>

export default {
    props: {
        list: Object
    },
    data() {
        
    },
    mounted() {
        console.log('list', this.list)
        var gaugeName = this.list.title;
        var data = this.list.gaugeData;
        var color = this.list.gaugeColor;
        var name = this.list.gaugeName;
        var textColor = this.list.textColor;
        var myChart = this.$echarts.init(document.getElementById(gaugeName));
       	var option ={
                    tooltip : {
                        formatter: "{a} <br/>{c} {b}"
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: true},
                            restore : {show: false},
                            saveAsImage : {show: false}
                        }
                    },
                    series : [
                        {
                            name:name,
                            type:'gauge',
                            min:0,
                            max:100,
                            splitNumber:10,
                            radius: '100%',
                            axisLine: {            // 坐标轴线
                                lineStyle: {       // 属性lineStyle控制线条样式
                                    color: color,
                                    width: 3.5,
                                    shadowColor : '#fff', //默认透明
                                    shadowBlur: 10
                                }
                            },
                            axisLabel: {            // 坐标轴小标记
                                textStyle: {       // 属性lineStyle控制线条样式
                                    fontWeight: 'bolder',
                                    color: '#fff',
                                    shadowColor : '#fff', //默认透明
                                    shadowBlur: 10
                                }
                            },
                            axisTick: {            // 坐标轴小标记
                                length :10,        // 属性length控制线长
                                lineStyle: {       // 属性lineStyle控制线条样式
                                    color: 'auto',
                                    shadowColor : '#fff', //默认透明
                                    shadowBlur: 10
                                }
                            },
                            splitLine: {           // 分隔线
                                length :15,         // 属性length控制线长
                                lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                                    width:3,
                                    color: '#fff',
                                    shadowColor : '#fff', //默认透明
                                    shadowBlur: 10
                                }
                            },
                            pointer: {           // 分隔线
                                shadowColor : '#fff', //默认透明
                                shadowBlur: 5
                            },
                            title : {
                                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                                    fontWeight: 'bolder',
                                    fontSize: 30,
                                    fontStyle: 'italic',
                                    color: textColor,
                                    shadowColor : '#fff', //默认透明
                                    shadowBlur: 10
                                }
                            },
                            detail : {
                                backgroundColor: 'rgba(30,144,255,0.8)',
                                shadowColor : '#fff', //默认透明
                                shadowBlur: 10,
                                offsetCenter: ['22%', '75%'],       // x, y，单位px
                                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                                    fontWeight: 'bolder',
                                    color: '#fff',
                                    fontSize: 13
                                }
                            },
                            data:[data]
                        }
                    ]
                }; 

        setInterval(function (){
            option.series[0].data[0].value += 1;
            if(option.series[0].data[0].value == 100) {
                option.series[0].data[0].value = 0
            }
            myChart.setOption(option);
        },500)

        if (option && typeof option === "object") {
            myChart.setOption(option, true);
        }
    }
}
</script>

<style scoped>
     body {
        position: relative;
        height: 100%;
    }
    #gauge {
        position:absolute;
    }
</style>
