<template>
    <div class="deliveryworksheet">
        <div class="order">
            <p style="float: left;width: 15%;text-align: center;line-height: 150px;background: #26a69a;color: #fff;font-size:20px ">指令:</p>
            <div style="float: left;width: 70%;padding: 0 10%">
                <div class="row">
                    <span class="label-font" style="margin-top: 10px">生产产品:</span>
                    <q-select
                      color="secondary"
                      style="width: 180px;margin-right: 98px"
                      class="q-mr-lg"
                      v-model="product"
                      :options="selectOptions"
                      @input="inputChange"
                    />
                </div>
                <div class="row" style="margin-bottom: 20px">
                    <span class="label-font" style="margin-top: 10px">&nbsp;&nbsp;&nbsp;派工数:</span>
                    <q-input color="secondary" v-model="worknum" style="width: 180px;" />
                </div>
                <div class="row">
                    <span class="label-font" style="margin-top: 10px">{{ $t('label.startDay') }}</span>
                    <mg-datetime class="q-mr-lg"
                     mode="datetime"
                     :time.sync="start_time"
                     style="margin-left: 5px"
                     :max="end_time" />
                    <span class="label-font" style="margin-top: 10px">{{ $t('label.endDay') }}</span>
                    <mg-datetime class="q-mr-lg"
                     mode="datetime"
                     :time.sync="end_time"
                     style="margin-left: 5px"
                     :min="start_time" />
                </div>
            </div>
        </div>
        <div class="procedure row">
            <q-card class="procedureIndex"  v-for="(item,index) in procedureArr" style="margin-right: 50px">
               {{ index+1 }}.( {{ item.name }} )
                <!--<div class="deviceWrap column" v-for="(itemDevice,indexDevice) in item.device">-->
                    <!--<q-checkbox @input="checkDevice" v-model="selection[indexDevice]" :val="itemDevice.description" :label='itemDevice.description' color="secondary"/>-->
                <!--</div>-->
                <q-option-group
                    type="checkbox"
                    color="secondary"
                    v-model="item.checkbox"
                    :options="item.device"
                />
            </q-card>
        </div>
        <div style="text-align: center">
            <q-btn :loading="loading" color="secondary" label="确认派工" style="width: 600px" @click="submit"/>
        </div>
    </div>
</template>

<script>
import { date } from 'quasar'
import http from 'http/serverRequests'
export default {
    name: "layout",
    data() {
        return {
            product: '',
            selectOptions:[],
            worknum: '',
            start_time: '',
            end_time: '',
            ret: [],
            procedureArr: [],
            loading: false
        }
    },
    created() {
        const time = new Date()
        this.start_time = date.formatDate(date.addToDate(time, { days: 0 }), 'YYYY-MM-DD')
        this.end_time = date.formatDate(date.addToDate(time, { days: 7 }), 'YYYY-MM-DD')
    },
    mounted() {
        this.getProductInfo()
    },
    methods: {
        inputChange() {
            let procedureArr = []
            for(var i in this.ret){
                if(this.product == this.ret[i].code){
                    this.ret[i].procedure.map((value, index) => {
                        let deviceArr =[];
                        let checkboxArr=[];
                        deviceArr = value.device.concat([]);
                        deviceArr.map((val,ind)=>{
                            val.label=val.description;
                            val.value=val.code;
                        });
                        if(deviceArr.length===1){
                            checkboxArr.push(deviceArr[0].value);
                        }
                        procedureArr.push({
                            name:value.name,
                            device: deviceArr,
                            code: value.code,
                            checkbox:checkboxArr
                        });
                    })
                }
            }
            this.procedureArr = procedureArr;
            console.log(procedureArr);
        },
        checkDevice(e) {
            // console.log(e);
          console.log(this.procedureArr)
          console.log(this.selection)
        },
        getProductInfo() {
            var that = this
            http.productInfo(function (res) {
                console.log(res)
                that.ret = res.data
                that.ret.map((v,i) => {
                    that.selectOptions.push({
                        label: v.name,
                        value: v.code
                    })
                })
            })
        },
        submit() {
            let that = this
            let device = {}
            let arr = []
            for(var i in that.procedureArr){
                device[that.procedureArr[i].code] = that.procedureArr[i].checkbox
            }
            that.loading = true
            if(that.product!='' && that.worknum!=''){
                    http.worksheetHandler({
                    "code":that.product,
                    "count":that.worknum,
                    "start_time": that.start_time,
                    "end_time": that.end_time,
                    "device": device
                }, res=> {
                    if(res.code == 'success'){
                        console.log(res)
                        this.$q.notify({
                                type: 'positive',
                                position: 'top',
                                message: '已派工'
                            })
                        setTimeout(() => {
                            that.loading = false
                            location.reload();
                        },3000)
                    }
                })
            }else{
                this.$q.notify({
                        type: 'warning',
                        position: 'top',
                        message: '工单信息不完整'
                    })
                setTimeout(() => {
                        that.loading = false
                    },3000)
            }
        }
    }
}
</script>

<style lang="stylus" scoped>
.deliveryworksheet
    padding 20px
.order
    height 150px
    border 1px solid #ccc
    border-radius 2px
    overflow hidden
.procedure
    margin-top 10px
    height 320px
.procedureIndex
    height 50px
    line-height 42px
    padding 5px 10px
.deviceWrap
    margin-top 10px
</style>