<template class="bkacground">
  <div class="md-layout">
    <div class="md-layout-item"></div>
    <div class="md-layout-item">
      <div class="components">
        <ListComponent v-if="currentRender == 'List'"/>
        <AddComponent v-if="currentRender == 'Add'"/>
      </div>
      <div class="phone-viewport">
        <md-bottom-bar md-type="shift">
          <md-bottom-bar-item id="bottom-bar-item-home" 
          v-on:click="setRender('List')" md-label="Inicio" md-icon="home">
          </md-bottom-bar-item>
          <md-bottom-bar-item id="bottom-bar-item-pages" 
          v-on:click="setRender('Add')" md-label="Adição" md-icon="add">
          </md-bottom-bar-item>
        </md-bottom-bar>
      </div>
    </div>
    <div class="md-layout-item"></div>
  </div>
</template>

<script>
import AddComponent from './components/AddComponent'
import ListComponent from './components/ListComponent';
export default {
  name: 'App',
  data: function () {
    return {
      currentRender: "List" 
    }
  },
  components: {
    ListComponent,
    AddComponent,
  },
  methods: {
    setRender: function (newRender) {
      this.currentRender = newRender;
    },

  }
}
</script>

<style>
.phone-viewport {
    width: 400px;
    /* height: 100px; */
    display: inline-flex;
    align-items: flex-end;
    overflow: hidden;
    /* border: 1px solid rgba(#000, .26); */
    background: rgba(#000, .06);
  }
  .components{
    width: 400px;
    height: 400px;
    overflow-y: scroll;
    overflow-x: hidden;
    background-color: white;

  }
</style>
