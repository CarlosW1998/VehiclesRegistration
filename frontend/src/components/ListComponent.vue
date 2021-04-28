<template>
    <md-list>
        <md-list-item v-for="item in elements" :key="item.id">
            <md-icon>directions_car</md-icon>
            <span class="md-list-item-text">{{item.model}}</span>
            <md-button class="md-icon-button md-primary">
                <md-icon>build</md-icon>
            </md-button>
        </md-list-item>
    </md-list>
</template>

<script>
import axios from "axios"

export default ({

    data: function(){
        return {
            elements: []
        }
    },
    created() {
        this.getVehicles()

    },
    methods: {
        getVehicles(){
            axios.get('http://localhost:8000/api/vehicle/', {crossdomain: true}).then(response=>{
                this.elements = response['data']['results']
            })
        }

    },
    setup() {
        
    },
})
</script>


<style lang="stylus" scoped>


</style>
