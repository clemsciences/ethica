<template>
  <div>
    <text-entity :entity="entity" v-for="entity in chapter.content" :key="entity.id"/>
  </div>
</template>

<script>
import TextEntity from "@/components/TextEntity";
export default {
  name: "Chapter",
  components: {TextEntity},
  props: {
    chapter: Object
  }
}
</script>

<style scoped>

</style>