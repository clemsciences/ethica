<template>
  <div>
    <chapter :chapter="chapter" v-for="chapter in chapters" :key="chapter.id"/>
  </div>
</template>

<script>
import axios from "axios";
import Chapter from "@/components/Chapter";

export default {
  name: "OpusText",
  components: {Chapter},
  props: {
      url: String,
    },
  data: function () {
    return {
      chapters: []
    }
  },
  methods: {
    retrieveText: function() {
      axios.get(this.url).then(
          (response) => {
            this.chapters = response.data.content;
          }
      ).catch(
          (reason => console.log(reason))
      )
    }
  },
  mounted() {
    this.retrieveText()
  }

}
</script>

<style scoped>

</style>