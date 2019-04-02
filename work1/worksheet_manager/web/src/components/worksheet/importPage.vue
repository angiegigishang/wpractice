<template>
    <div class="importFile">
        <q-btn color="secondary" >
            <label for="fileInput" icon="cloud_upload">
                <q-icon name="cloud_upload" style="margin-bottom: 5px;margin-right: 5px"/>
                <span>导入</span>
            </label>
            <input type="file" label="导入" id="fileInput" @change="importXLS"></input>
        </q-btn>
    </div>
</template>

<script>
    import http from 'http/serverRequests'
    export default {
        name: "importPage",
        data() {
            return {

            }
        },
        methods: {
            importXLS(e){
                var formData = new FormData();
                formData.append("file",e.target.files[0])
                http.importExcel(formData, (res) => {
                    console.log(res)
                    if(res.code == 'success'){
                        this.$q.notify({
                            type: 'positive',
                            position: 'top',
                            timeout: 2000,
                            message: '导入成功'
                        })
                    }
                })
            }
        }
    }
</script>

<style lang="stylus" scoped>
.importFile
    padding 10px 20px
#fileInput
    display none
label
    display inline-block
    width 80px
    height 20px
.q-btn
    padding 0px!important
</style>