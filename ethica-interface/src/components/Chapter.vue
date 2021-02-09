<template>
  <div>
    <div class="accordion" role="tablist">
      <b-button class="toggle-button outline-primary" v-b-toggle="chapter.id" role="tab" @click="visible = !visible">Capita {{ chapter.id + 1 }}</b-button>
      <b-collapse accordion="my-accordion" role="tabpanel" v-model="visible">
        <text-entity :id="chapter.id" :entity="entity" v-for="entity in chapter.content" :key="entity.id" />
      </b-collapse>
    </div>
  </div>
</template>

<script>
import TextEntity from "@/components/TextEntity";
export default {
  name: "Chapter",
  components: {TextEntity},
  props: {
    chapter: Object
  },
  data: function() {
    return {
      visible: false
    }
  }
}
</script>

<style scoped>
.toggle-button {
  margin: 1em;
}

/*.btn-primary {*/
/*  color: black;*/
/*  background-color: #c0e3f5;*/
/*}*/

.btn-outline-primary {
    color: black;
  background-color: #c0e3f5;
}

</style>