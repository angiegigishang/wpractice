<template>
    <div>
        <div class="header">
            <div>
                <svg @click="goBack" class="icon" aria-hidden="true">
                    <use xlink:href="#iconfanhui"></use>
                </svg>
            </div>
            <div class="right">
                <p>
                    <span>{{facility}}</span>
                    <span>{{classes}}</span>
                </p>
            </div>
        </div>
        <div class="detail">
            <p>
                <span>产品：{{product}}</span>
            </p>
            <div>
                <div>
                    <p>
                        <span>生产指令编号：{{work_num}}</span>
                        <span>计划数量：{{plan_num}}个</span>
                    </p>
                    <p>
                        <span>计划开始时间：{{start_time}}</span>
                        <span>计划结束时间：{{end_time}}</span>
                    </p>
                </div>
                <p>
                    <b :style="`background:${status ? 'green' : 'red'}`">{{status ? '空闲' : '加工中'}}</b>
                </p>
            </div>
        </div>
        <div class="progress">
            <p class="outside" :style="`width:${progress_per}`"></p>
            <p class="inside"></p>
            <p class="text">完成{{progress_num}}个， 进度{{progress_per}}</p>
        </div>
        <router-view></router-view>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import http from 'http/serverRequests'
import { setTimeout } from 'timers';

@Component({
    created () {
        this['progress_per'] = '0%'
        this['progress_per_real'] = '0%'
    },
    mounted () {
        this['getHistoryHeaderData']().then(() => {
            this['progressAnimationInit']('88%')
            // setInterval(() => {
            //     this['progress_per_real'] = `${(Math.random()*100).toFixed(0)}%`
            // },2000)
        })
    }
})

export default class History extends Vue {
    public facility: string = '设备名称'
    public classes: string = '班次'
    public product: string = ''
    public work_num : string = ''
    public plan_num: string = ''
    public start_time: string = ''
    public end_time: string = ''
    public progress_num: string = '0'
    public progress_per: string = '0%'
    public progress_per_real: string = '0%'
    public status: boolean = false
    public timer: number | null = null
    public unWatchPer: { ():any } | null = null
    getHistoryHeaderData (): Promise<any> {
        return new Promise<any>((resolve: () => void, reject: () => void) => {
            let params: object = this['$route']['params']
            http['getHistoryHeaderData'](`${params['id']}/${params['pro']}`, res => {
                if (this['responseValidate'](res)) {
                    this['facility'] = res.data.device_info.name
                    this['product'] = res.data.worksheet_info.product
                    this['work_num'] = res.data.worksheet_info.worksheet_id
                    this['plan_num'] = res.data.worksheet_info.num
                    this['start_time'] = res.data.worksheet_info.start_time
                    this['end_time'] = res.data.worksheet_info.end_time
                    this['status'] = res.data.state === 'complete' ? true : false
                    resolve()
                } else {
                    reject()
                }
            }, err => {
                reject()
            })
        })
    }
    progressAnimationInit (num: string): void {
        this['unWatchPer'] && (() => {
            (<{ (): void }>this['unWatchPer'])()
            this['unWatchPer'] = null
        })()
        this['unWatchPer'] = this['$watch']('progress_per_real', (val) => {
            cancelAnimationFrame(<number>this['timer'])
            this['progressAnimationInit'](val)
        })
        let fn = ():void => {
            if (parseInt(this['progress_per']) !== parseInt(num)) {
                if (parseInt(this['progress_per']) > parseInt(num)) {
                    this['progress_per'] = `${parseInt(this['progress_per']) - 1}%`
                } else {
                    this['progress_per'] = `${parseInt(this['progress_per']) + 1}%`
                }  
                this['timer'] = requestAnimationFrame(fn)
            } else {
                cancelAnimationFrame(<number>this['timer'])
            }
        }
        this['timer'] = requestAnimationFrame(fn)
    }
}
</script>

<style lang="stylus" scoped>
    p
        margin 0
        padding 0
    .header
        display flex
        justify-content space-between
        align-items center
        padding 20px
        svg
            width 26px
            height 26px
            cursor pointer
        .right
            display flex
            justify-content space-between
            align-items center
            p:first-child
                span
                    background #E3E4E4
                    margin-right 10px
                    width 104px
                    display inline-block
                    text-align center
                    color #333
                    height 36px
                    line-height 36px
                    border-radius 5px
            .items
                margin-right 5px
    .detail
        display flex
        height 100px
        align-items center
        box-sizing border-box
        padding 0 20px
        >p
            width 20%
            height 100%
            background #F2F2F2
            text-align center
            &:after
                content: ''
                display inline-block
                height 100px
                vertical-align middle
            span
                vertical-align middle
        >div
            width 80%
            display flex
            border 1px solid #333
            border-radius 5px
            height 100%
            >div
                width 80%
                display flex
                flex-direction column
                justify-content space-around
                p
                    display flex
                    justify-content space-between
                    padding 0 10px
                    span
                        word-break break-all
            >p
                width 20%
                text-align center
                display flex
                justify-content center
                align-items center
                b
                    width 60px
                    height 60px
                    border-radius 50%
                    display inline-block
                    color white
                    font-weight normal
                    letter-spacing 1px
                    text-align center
                    display flex
                    justify-content center
                    align-items center
    .progress
        position relative
        height 40px
        width calc(100% - 40px)
        margin 10px auto
        border-radius 5px
        .outside
        .inside
        .text
            position absolute
            top 0
            left 0
            bottom 0
            border-radius 5px
        .outside
            z-index 10
            background linear-gradient(left, #5bd8ff, #FF8817)
            opacity .8
            border-top-right-radius 20px
            border-bottom-right-radius 20px
        .inside
            width 100%
            z-index 8
            background whitesmoke
            opacity .1
        .text
            width 100%
            z-index 12
            text-align center
            line-height 40px
            color #222
</style>
