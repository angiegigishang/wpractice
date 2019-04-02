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
                <p>
                    <template v-for="(item,idx) in btns">
                        <q-btn-dropdown :label="item.label" :key="idx" class="items">
                            <q-list link>
                                <q-item v-for="(mem,i) in item.items" :key="i" @click.native="filterChange(idx, i)">
                                    <q-item-main>
                                        <q-item-tile label>{{mem}}</q-item-tile>
                                    </q-item-main>
                                    <q-item-side v-if="idx === 2" :icon="sort[i]"></q-item-side>
                                </q-item>
                            </q-list>
                        </q-btn-dropdown>
                    </template>
                </p>
            </div>
        </div>
        <div class="content" v-if="allData.length > 0">
            <div class="content-item" v-for="(item,idx) in filter(allData)" :key="idx">
                <div class="content-item-left">
                    <p>产品: {{item.name}}</p>
                    <b></b>
                    <p>加工详情</p>
                </div>
                <div class="content-item-right" :style="`background: ${item.state === 'running' ? '#66CC01' : '#CBCBCB'}`">
                    <div class="c-i-r-l" @click="enterHisRun(item.worksheet_id)">
                        <p>
                            <span>生产指令编号：{{item.worksheet_id}}</span>
                            <span>计划数量：{{item.num}}个</span>
                        </p>
                        <p>
                            <span>计划开始时间：{{item.start_time}}</span>
                            <span>计划结束时间：{{item.end_time}}</span>
                        </p>
                        <b></b>
                        <div>
                             <p>
                                <span v-for="(op,i) in item.procedure" :key="i">
                                    {{op.name}}
                                    <b v-if="i !== item.procedure.length - 1">></b>
                                </span>
                            </p>
                            <p>该设备已加工了{{item.completed_count}}个</p>
                        </div>
                    </div>
                    <div class="c-i-r-r">
                        <b></b>
                        <p>
                            <svg class="icon" aria-hidden="true" @click="beforeChange(item.state, item.worksheet_id, item.person_id, item.person_name)">
                                <use :xlink:href="`${item.state === 'running' ? '#iconjieshu1' : '#iconbofang'}`"></use>
                            </svg>
                        </p>
                    </div>
                </div>
            </div>            
        </div>
        <p v-else style="text-align:center;margin-top:80px">
            暂无数据
        </p>
        <Dialog v-model="diaFlag" :mode="mode" :ok="changeStatus" :worksheet_id="worksheet_id" :name="bindName" :id="bindId"></Dialog>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop, Watch } from "vue-property-decorator"
import http from 'http/serverRequests'
import { mapMutations, mapState } from 'vuex'
import Dialog from "./dialog.vue"

@Component({
    created () {
        let i = this['titles'].find(v => v['code'] === this['id'])
        this['fillSort']()
        this['getData']()
        this['setPageTitle'](i ? `${i['name']} ${i['description']}` : '')
        i ? this['facility'] = i['name'] : ''
    },
    components: {
        Dialog
    },
    computed: {
        ...mapState(<string>process.env.APP_SCOPE_NAME, ['titles'])
    },
    methods: {
        ...mapMutations(<string>process.env.APP_SCOPE_NAME, ['setPageTitle'])
    }
})
export default class Choose extends Vue {
    @Prop({ default: '', type: String }) id!: string
    public facility: string = '设备名称'
    public classes: string = '班次'
    public btns: Array<{label: string, items: string[]}> = [
        {label: '产品', items: []},
        {label: '状态', items: ['全部','加工中', '空闲']},
        {label: '排序', items: ['按状态排序', '按计划数量排序', '按开始时间排序', '按结束时间排序', '按产品拼音排序','按指令编号排序']}
    ]
    public sort: string[] = []
    public allData: chooseData[] = []
    public diaFlag: boolean = false
    public mode: boolean = true
    public worksheet_id: string = ''
    public bindName: string = ''
    public bindId: string = ''
    public filterData: (arr: chooseData[]) => chooseData[] = arr => arr
    
    @Watch('titles', { immediate: true, deep: true })

    get filter (): (arr: chooseData[]) => chooseData[] {
        return this.filterData
    }

    filterChange (one: number, two: number) {
        switch (one) {
            case 0: {
                switch (two) {
                    default:
                    break
                }
                return
            }
            case 1: {
                switch (two) {
                    case 0: {
                        this.filterData = arr => arr
                        break
                    }
                    case 1: {
                        this.filterData = arr => arr.filter(v => v.state === 'running')
                        break
                    }
                    case 2: {
                        this.filterData = arr => arr.filter(v => v.state === 'complete')
                        break
                    }
                    default:
                    break
                }
                return
            }
        }
    }

    resetTitle (val) {
        let i: any = this['titles'].find(v => v['code'] === this['id'])
        this['setPageTitle'](i ? `${i['name']} ${i['description']}` : '工序管理')
        i ? this['facility'] = i['name'] : ''
    }
    fillSort (): void {
        for (let i = 0;i < this.btns[2].items.length;i++){
            this.$set(this.sort, i, 'arrow_drop_down')
        }
    }
    getData (): Promise<any> {
        return new Promise<any>((resolve: (res?: any) => void, reject: (err?: any) => void) => {
            http['getAllData'](this.$props['id'], res => {
                if (this['responseValidate'](res)) {
                    this['allData'] = <chooseData[]>res.data
                }
                resolve()
            }, err => {
                reject()
            })
        })
    }
    enterHisRun (code: string): void {
        this['$router']['push'](`/history/run/${this['id']}/${code}`)
    }
    beforeChange (s: string, worksheet_id: string, id: string, name: string): void {
        if (s === 'running') {
            this['mode'] = false
            this['bindName'] = name
            this['bindId'] = id
        } else {
            this['mode'] = true
            this['bindName'] = this['bindId'] = ''
        }
        this['worksheet_id'] = worksheet_id
        this['diaFlag'] = true
    }
    changeStatus (data: {
        worksheet_id: string,
        person_id?: string,
        person_name?: string
    }, url: string = 'startOp'): Promise<any> {
        return new Promise<any>((resolve: (res?: any) => void, reject: (err?: any) => void): void => {
            http[url]({
                ...data,
                device_code: this.$props.id
            }, res => {
                if (this['responseValidate'](res)) {
                    let i: number = this.allData.findIndex(val => val.worksheet_id === res.data.worksheet_id)
                    let obj = { ...this.allData[i] }
                    obj.state = res.data.state
                    if (res.data.person_id) {
                        obj.person_id = res.data.person_id
                    }
                    if (res.data.person_name) {
                        obj.person_name = res.data.person_name
                    }
                    this.$set(this.allData, i, obj)
                    resolve()
                } else {
                    reject()
                }
            }, err => {
                reject(err)
            })
        }).then(() => {
            
        })
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
    .content
        margin-top 10px
        padding 0 20px
    .content-item
        margin-bottom 20px
        border-radius 5px
        display flex
        justify-content flex-start
        min-height 120px
        overflow hidden
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
        .content-item-left
            background #F2F2F2
            display flex
            flex-direction column
            justify-content space-around
            width 20%
            align-items center
            b
                height 1px
                background gray
                width 80%
        .content-item-right
            display flex
            width 80%
            .c-i-r-l
                display flex
                flex-direction column
                justify-content space-around
                align-items center
                width 80%
                cursor pointer
                >div
                    width 100%
                    padding 0 20px
                >p
                    width 100%
                    padding 0 20px
                    display flex
                    justify-content space-between
                >b
                    display inline-block
                    height 1px
                    width 90%
                    background gray
            .c-i-r-r
                width 20%
                display flex
                align-items center
                b
                    display inline-block
                    height 80%
                    width 1px
                    background gray
                p
                    text-align center
                    width calc(100% - 1px)
                    svg
                        width 60px
                        height 40px
                        cursor pointer

</style>

