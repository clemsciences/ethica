<template>
  <div id="app">
    <b-container>
      <b-row align-h="start">
        <h1><b>Spinozae Ethica</b></h1>
      </b-row>

      <b-row>
        <b-col><b-button to="/text">Text</b-button></b-col>
<!--        <b-col><b-button to="/lexicon">Lexicon</b-button></b-col>-->
<!--        <b-col><b-button to="/statistica">Statistica</b-button></b-col>-->
    </b-row>
      <b-row align-h="center">
        <router-view/>
<!--        <opus-text :url="ethicaUrl"/>-->
      </b-row>
      <b-row align-h="start">
        <p class="m-3">Clement Besnier - 2021 <a href="https://www.clementbesnier.eu">clementbesnier.eu</a></p>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// import OpusText from "@/components/OpusText";

export default {
  name: 'App',
  components: {
    // OpusText
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
  margin-top: 20px;
}
</style>
