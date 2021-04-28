<template>
    <div>
        <md-list v-show="render == 'List'">
            <md-list-item v-for="(item, index) in elements" :key="item.id">
                <md-icon>directions_car</md-icon>
                <span class="md-list-item-text">{{item.model}}</span>
                <md-button class="md-icon-button md-primary"
                v-on:click="openVehicle('Eddit', index)">
                <md-icon >build</md-icon>
                </md-button>
            </md-list-item>
        </md-list>
        <div v-if="render == 'Eddit'">
            <EdditComponent v-bind:entry="this.selected"
            @close="closeVehicle($event)"/>
        </div>
        
    </div>
</template>

<script>
import axios from "axios"
import EdditComponent from "./EditComponent"

export default ({

    data: function(){
        return {
            elements: [],
            render: "List",
            selected: {
                id:Number,
                model: String,
                brand: String,
                price: Number,
                note: String,
            },
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
        },
        openVehicle: function (newRender, index) {
            this.selected = this.elements[index]
            this.render = newRender;
        },
        closeVehicle($event){
            if($event != -1){
                console.log($event)
                this.elements = this.elements.filter(function (element){return element.id != $event})
            }
            this.render = 'List';

        }

    },
    setup() {
        
    },
    components: {
        EdditComponent,
    },
})
</script>


<style lang="stylus" scoped>


</style>
