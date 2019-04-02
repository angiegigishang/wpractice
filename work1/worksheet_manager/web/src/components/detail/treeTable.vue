<template>
    <div>
        <div class="product" 
             v-for="item of list"
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
            
        }
    },
    computed: {
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
        width 30% 
        height 4.5em
        top 1em
        margin-left 2.6%
        display inline-block
        
        .product-title 
            position absolute
            height 1.3em
            line-height 1.3em
            width 100%
            top 0
            left 0
            background #192f3f;
            color #ecffff
            text-align center
            
        .middle-target
            position absolute
            height 1.5em
            line-height 1.7em
            width 100%
            top 40%
            left 0
            text-align center
            .target-title
                color #62b0c9
                letter-spacing 0.1em
                font-size 0.7em
            .target-number 
                font-family led-number
                font-size 1.3em
                color white
                background black
                margin-left 6%
                margin-right 4%
                letter-spacing 0.1em
                border 0.2px solid #6dabb9
                box-shadow 0px 0px 0.1px 0.8px #6dabb9
                border-radius 3px
            .unit 
                color white
                font-weight bold
                font-size 0.8em
            p
                display inline-block
        
</style>