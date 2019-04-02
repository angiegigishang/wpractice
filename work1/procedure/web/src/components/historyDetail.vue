<template>
    <div style="padding: 20px">
        <v-table
            style="width:100%"
            :columns="columns"
            :table-data="tableData"
            :show-vertical-border="false"
            is-horizontal-resize
            is-vertical-resize=true
            title-bg-color="#0F9D58"
        ></v-table>
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import 'vue-easytable/libs/themes-base/index.css'
import { VTable,VPagination } from 'vue-easytable'
import http from 'http/serverRequests'

const k_v: any = {
    mark: '条码',
    start: '上料时间',
    person_name: '操作人',
    person_id: '操作人编号',
    code: '产品编号',
    description: '产品描述',
    name: '产品名称',
    component_num: '计划数量',
    end: '下料时间',
    procedure_name: '工序名称'
} 

export default Vue.extend({
    props: {
        id: {
            type: String,
            default: ''
        },
        pro: {
            type: String,
            default: ''
        },
        op: {
            type: String,
            default: ''
        }
    },
    data (): {
        columns: Array<{
            field: string,
            title: string,
            width: number,
            titleAlign: string,
            columnAlign: string,
            isResize?: boolean,
            overflowTitle?: boolean,
            titleCellClassName?: string
        }>,
        tableData: Array<{
            mark: string,
            start: string,
            person_name: string,
            person_id: string,
            code: string,
            description: string,
            name: string,
            component_num: string,
            end: string,
            procedure_name: string
        }>
    } {
        return {
            columns: [],
            tableData: []
        }
    },
    components:{
        VTable
    },
    created () {
        this['getHisDetailData']()
        this['$store']['commit'](`${process.env.APP_SCOPE_NAME}/setPageTitle`,'指令操作详细')
    },
    methods: {
        getHisDetailData (): Promise<any> {
            return new Promise<any>((resolve:() => void, reject: (err?: any) => void) => {
                http['getHisDetailData'](`${this.$props.id}/${this.$props.pro}/${this.$props.op}`,res => {
                    if (this['responseValidate'](res)) {
                        this['tableData'] = res.data.map(val => {
                            let obj = {...val.product_info}
                            delete val.product_info
                            return {
                                ...obj,
                                ...val
                            }
                        })
                        let keys = Object.keys(this['tableData'][0])
                        this['columns'] = keys.map(val => ({
                            field: val,
                            title: k_v[val],
                            width: 120,
                            titleAlign: 'center',
                            columnAlign: 'center',
                            isResize: true,
                            overflowTitle: true,
                            titleCellClassName: 'tHead'
                        }))
                        resolve()
                    } else {
                        reject()
                    }
                }, err => {
                    reject(err)
                })
            })
        }
    }
})
</script>

<style lang="stylus">
    .tHead
        color white
</style>


