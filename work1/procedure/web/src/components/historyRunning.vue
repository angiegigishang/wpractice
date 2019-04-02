<template>
    <div>
        <div class="content">
            <div class="items" v-for="(item,idx) in historyData" :key="idx">
                <p><span>{{item.name + item.description}}</span></p>
                <div>
                    <div>
                        <p v-for="i in [0,1]" :key="i">
                            <span><b>{{i === 0 ? '上料' : '下料'}}</b></span>
                            <span>条码：{{i === 0 ? item.mark_one : item.mark_two}}</span>
                            <span>物料名称：{{i === 1 ? (item.end ? (item.product_info ? item.product_info.name : '') : '') : (item.product_info ? item.product_info.name : '')}}</span>
                            <span>零件码：{{i === 1 ? (item.end ? (item.product_info ? item.product_info.component_num : '') : '') : (item.product_info ? item.product_info.component_num : '')}}</span>
                            <span>数量： 1</span>
                            <span>时间：{{i === 0 ? item.start : item.end}}</span>
                            <span>操作人：{{i === 1 ? (item.end ? item.person_name : '') : item.person_name}}</span>
                            <span>操作人编号：{{i === 1 ? (item.end ? item.person_id : '') : item.person_id}}</span>
                        </p>
                    </div>
                    <p>
                        <span @click="enterDetail(item.code)">详情</span>
                        <svg @click="enterDetail(item.code)" class="icon" aria-hidden="true">
                            <use xlink:href="#icon-"></use>
                        </svg>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { Vue, Component, Prop, Watch } from "vue-property-decorator";
    import http from '@/api/http/serverRequests'
    import { date } from 'quasar'

    type hd = {
        name: string,
        code: string,
        description: string,
        mark_one?: string,
        mark_two?: string,
        start?: string,
        person_id?: string,
        person_name?: string,
        product_info?: {
            code: string,
            description: string,
            name: string,
            component_num: string
        },
        end?: string,
        procedure_name?: string
    }[]
    @Component({
        created () {
            this['setKeyListen']()
            this['getHisRunData']()
            this['$store']['commit'](`${process.env.APP_SCOPE_NAME}/setPageTitle`,'指令操作记录')
        },
        beforeDestroy () {
            this['unSetKeyListen']()
        }
    })
    export default class HistoryRun extends Vue {
        @Prop({default: '', type: String}) id!: string
        @Prop({default: '', type: String}) pro!: string
        public historyData: hd = []
        public start: boolean = false
        public end: boolean = false
        public mark: string[] = []
        public onoff: boolean = true
        get getNow () {
            let i = 0
            this.historyData.forEach(v => {
                if (v.start) {
                    i++
                }
                if (v.end) {
                    i++
                }
            })
            return i
        }
        @Watch('getNow')
        handlerGetNow (val: number): void {
            if (val === this.historyData.length * 2) {
                let timer = setTimeout(() => {
                    this.historyData = this.historyData.map(v => ({
                        name: v.name,
                        code: v.code,
                        description: v.description
                    }))
                    clearTimeout(timer)
                },2000)
            }
        }
        @Watch('mark', { deep: true })
        handlerMark (val: string[]): void {
            let m: string
            if (this.getNow%2 === 1) {
                m = 'mark_two'
            } else {
                m = 'mark_one'
            }
            let i: number = Math.floor(this.getNow / 2)
            this.$set(this.historyData, i, Object.assign(this.historyData[i], { [m]: val.join('')}))
        }
        getHisRunData (): Promise<any> {
            return new Promise<any>((resolve: () => void,reject: () => void) => {
                http['getHisRunData'](`${this.$props.id}/${this.$props.pro}`, res => {
                    if (this['responseValidate'](res)) {
                        this['historyData'] = res.data.procedure_info.map((val, i) => ({
                            ...val,
                            ...res.data.data[i],
                            mark_one: res.data.data[i] && res.data.data[i].start ? res.data.data[i].mark : '',
                            mark_two: res.data.data[i] && res.data.data[i].end ? res.data.data[i].mark : ''
                        }))
                    } else {

                    }
                }, err => {

                })
            })
        }
        enterDetail (op: string): void {
            this['$router']['push'](`/history/detail/${this.$props.id}/${this.$props.pro}/${op}`)
        }
        setKeyListen (): void {
            document.addEventListener('keydown', this.solveKeyPress)
        }
        unSetKeyListen (): void {
            document.removeEventListener('keydown', this.solveKeyPress)
        }
        solveKeyPress (e: any) : void {
            e.preventDefault()
            if (!this.onoff) return
            if (e.key === 'F10' && !this.start) {
                this.start = true
                this.end = false
                this.mark = []
                return
            }
            if (e.key === 'F9' && !this.end && this.mark.join('').trim().length > 0) {
                this.end = true
                this.start = false

                let arg: postMarkData = {
                    worksheet_id: this.$props.pro,
                    device_code: this.$props.id,
                    procedure_code: this.historyData[Math.floor(this.getNow / 2)].code,
                    mark: this.mark.join(''),
                    mark_time: date.formatDate(new Date().getTime(), 'YYYY-MM-DD HH:mm:ss'),
                    state: this.getNow%2 === 0 ?  'start' : 'end'
                }

                this.postMark(arg).then(res => {
                    let i: number = Math.floor(this.getNow / 2)
                    this.$set(this.historyData, i, Object.assign(this.historyData[i], res))
                    this.onoff = true
                }).catch(() => {
                    this.onoff = true
                })
                return 
            }
            if (this.start) {
                this.mark.push(e.key)
            }
        }
        postMark (arg: postMarkData): Promise<any> {
            return new Promise<any>((resolve: (res?: any) => void, reject: (err?: any) => void): void => {
                this.onoff = false
                http['postMark'](arg, res => {
                    if (this['responseValidate'](res)) {
                        let person_id: string = res.data.person_id
                        let person_name: string = res.data.person_name
                        delete res.data.person_id
                        delete res.data.person_name
                        let obj: any = {
                            person_id: person_id,
                            person_name: person_name,
                            product_info: {
                                ...res.data
                            },
                            mark: arg.mark
                        }
                        if (arg.state === 'start') {
                            obj.start = arg.mark_time
                        } else {
                            obj.end = arg.mark_time
                        }
                        resolve(obj)
                    } else {
                        reject()
                    }
                }, err => {
                    reject()
                })
            })
        }
    }
</script>

<style lang="stylus" scoped>
    .content
        p
            margin 0
            padding 0
        margin-top 20px
        .items
            display flex
            width calc(100% - 40px)
            padding 10px
            margin 0 auto
            margin-bottom 20px
            min-height 80px
            border 1px solid 2D91E9
            border-radius 5px
            box-shadow:#2D91E9 0px 0px 18px
            animation light 1.4s infinite alternate
            @keyframes light {
                from {
                    box-shadow #2D91E9 0px 0px 18px
                }
                to {
                    box-shadow rgba(45, 145, 233, .3) 0px 0px 18px
                }  
            }
            >p
                width 20%
                word-break break-all
                text-align center
                padding 0 10px
                span
                    display inline-block
                    vertical-align middle
                &:after
                    content: ''
                    display inline-block
                    height 100%
                    vertical-align middle
            >div
                width 80%
                display flex
                >div
                    width 80%
                    display flex
                    justify-content space-around
                    p
                        display flex
                        flex-direction column
                        justify-content space-around
                        span
                            word-break break-all
                >p
                    width 20%
                    span
                    svg
                        vertical-align middle
                        display inline-block
                        cursor pointer
                    span
                        color #2D91E9
                    svg
                        width 40px
                        height 40px
                        position relative
                        top 2px
                        animation more 1.2s infinite
                        @keyframes more
                        {
                            from {
                                transform translateX(0)
                                opacity 1
                            }
                            to {
                                transform translateX(40px)
                                opacity 0
                            }
                        }
                    &:after
                        content: ''
                        display inline-block
                        height 100%
                        vertical-align middle
</style>

