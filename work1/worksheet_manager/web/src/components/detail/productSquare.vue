<template>
    <div>
        <div class="product" 
             v-for="item of finishnumbers"
             :key="item.id"
        >
            <div class="product-title">
                {{item.name}}
            </div>
            <div class="middle-target">
                    <p class="target-title">任务数<p>
                    <p class="target-number">{{item.targetnum}}</p>
                    <p class="unit">个</p>
            </div>
            <div class="middle-finish">
                <p class="finish-title">完成数</p>
                <p class="finish-number">{{item.finishnum}}</p>
                <p class="unit">个</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "productSquare",
    props: {
        list: Array
    },
    data () {
        return {
            finishnumber: 200
        }
    },
    computed: {
        finishnumbers () {
            var self = this
            for(var key in this.list) {
                var item = this.list[key] 
                var targetlength = String(item.targetnum).length;
                var finishlength = String(item.finishnum).length;
                if (targetlength !== finishlength) {
                    item.finishnum = (Array(targetlength).join('0') + item.finishnum).slice(-targetlength)
                    //self.changeNum(item.finishnum, targetlength)
                }            
            }
            return this.list
        }
    },
    methods: {
        // changeNum (num, length) {
        //     return (Array(length).join('0') + num).slice(-length); 
        //     console.log(1)
        // }
    }
}

</script>

<style lang="stylus" scoped>
    @font-face
      font-family:led-number;
      src:url("~assets/led-number.ttf");
      
    .product 
        position relative
        border 1px solid #6dabb9
        box-shadow 0px 0px 0.1px 0.8px #6dabb9
        border-radius 3px
        width 18.81% 
        height 10em
        top 3em
        margin-left 1%
        display inline-block
        
        .product-title 
            position absolute
            height 2.3em
            line-height 2.3em
            width 100%
            top 0
            left 0
            background #1f5972
            color #ecffff
            text-align center
            
        .middle-target
            position absolute
            height 2em
            line-height 2em
            width 100%
            top 32%
            left 0
            text-align center
            .target-title
                color #62b0c9
                letter-spacing 0.1em
            .target-number 
                font-family led-number
                font-size 2.3em
                color white
                background black
                margin-left 4%
                margin-right 3%
                letter-spacing 0.2em
                border 0.2px solid #6dabb9
                box-shadow 0px 0px 0.1px 0.8px #6dabb9
                border-radius 3px
            .unit 
                color white
                font-weight bold
            p
                display inline-block
        
        .middle-finish
            position absolute
            height 2em
            line-height 2em
            width 100%
            top 64%
            left 0
            text-align center
            .finish-title
                color #62b0c9
                letter-spacing 0.2em
            .finish-number 
                font-family led-number
                font-size 2.3em
                color white
                background black
                margin-left 4%
                margin-right 3%
                letter-spacing 0.2em
                border 0.2px solid #6dabb9
                box-shadow 0px 0px 0.1px 0.8px #6dabb9
                border-radius 3px
            .unit 
                color white
                font-weight bold
            p
                display inline-block
</style>