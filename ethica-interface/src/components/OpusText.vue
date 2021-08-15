<template>
  <b-container>
    <b-row>
          <h3>Textus Ethicae Spinozae</h3>
    </b-row>
    <b-row v-if="chapters.length === 0 && !networkError" class="mx-auto">
      <b-col align-self="center" class="my-5">
        <b-spinner label="Loading data..."/>
      </b-col>
    </b-row>
    <b-row align-h="center">
      <chapter :chapter="chapter" v-for="chapter in chapters" :key="chapter.id"/>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
import Chapter from "@/components/Chapter";

export default {
  name: "OpusText",
  components: {Chapter},
  data: function () {
    return {
      url: "/load/text",
      chapters: [],
      networkError: false
    }
  },
  methods: {
    retrieveText: function() {
      axios.get(this.url).then(
          (response) => {
            this.chapters = response.data.content;
          }
      ).catch(
          (reason) => {
            console.log(reason);
            this.networkError = true;
          }
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