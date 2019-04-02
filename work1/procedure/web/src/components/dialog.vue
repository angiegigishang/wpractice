<template>
    <q-dialog
    v-model="value"
    @ok="onOk"
    @cancel="onCancel"
    @hide="onHide"
  >
    <span slot="title">提示</span>

    <div slot="body" style="min-width:300px">
      <q-field
        label="员工号"
        :label-width="4"
      >
        <q-input v-model="person_id" :disable="mode ? false : true"/>
      </q-field>
      <q-field
        label="员工名称"
        :label-width="4"
      >
        <q-input v-model="person_name" :disable="mode ? false : true"/>
      </q-field>
    </div>

    <template slot="buttons" slot-scope="props">
      <q-btn color="primary" :label="`${mode ? '签入 开始加工' : '签出 停止加工'}`" @click="choose(props.ok)" />
      <q-btn color="primary" label="取消" @click="props.cancel" />
    </template>
  </q-dialog>
</template>

<script lang="ts">
    import { Vue, Component, Prop, Watch, Model } from "vue-property-decorator"

    @Component({
        name: 'dialog'
    })
    export default class Dialog extends Vue {
        @Prop({ type: Boolean, default: true }) mode?: boolean
        @Prop({ type: Function}) ok?: { ():any }
        @Prop({ type: String }) worksheet_id!: string
        @Prop({ type: String }) id!: string
        @Prop({ type: String }) name!: string
        @Model('change', { type: Boolean, default: false }) diaFlag!: boolean
        @Watch('id', { immediate: true })
        watchId (val: string): void {
          this.person_id = val
        }
        @Watch('name', { immediate: true })
        watchName (val: string): void {
          this.person_name = val
        }
        public person_id: string = ''
        public person_name: string = ''
        onOk (data) { }
        onCancel () { }
        onHide () { this.$emit('change', false) }
        get value () {
            return this.$props.diaFlag
        }
        async choose (ok): Promise<any> {
            if (!this['person_id'].trim() || !this['person_name'].trim()) {
                this['$q'].dialog({
                    title: '请输入完整',
                    message: `必须填写完整！`
                })
            } else if (!(escape(this['person_id']).indexOf("%u") < 0)) {
                this['$q'].dialog({
                    title: '格式错误',
                    message: `员工号不允许出现中文`
                })
            } else {
                await ok()
                typeof this.$props.ok === 'function' && (_ => {
                  let arg: {
                    worksheet_id: string,
                    person_id?: string,
                    person_name?: string
                  } = {
                    worksheet_id: this.$props.worksheet_id
                  }
                  if (this.$props.mode) {
                    arg['person_id'] = this['person_id']
                    arg['person_name'] = this['person_name']
                  }
                  this.$props.ok(arg, this.$props.mode ? 'startOp' : 'stopOp')
                })()
            }
        }
    }
</script>

