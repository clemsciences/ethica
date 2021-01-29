<template>
  <div id="app">
    <opus-text :url="ethicaUrl"/>
  </div>
</template>

<script>
import OpusText from "@/components/OpusText";

export default {
  name: 'App',
  components: {
    OpusText
  },
  data: function() {
    return {
      ethicaUrl: "/load/text"
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
