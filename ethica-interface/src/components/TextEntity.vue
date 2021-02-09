<template>
  <div>
    <p :style="entityStyle" class="text-element"
       @mouseover="setStyle" @mouseout="unsetStyle">
      {{ entity.content}}
    </p>
  </div>
</template>

<script>
export default {
name: "TextEntity",
  props: {
    entity: Object
  },
  data: function() {
    return {
      entityStyle: {}
    }
  },
  methods: {
    setStyle: function() {
      console.log(this.entity);
      switch (this.entity.entityType) {
        case "Definitio":
          this.entityStyle = {
            'background-color': '#29708d',
          };
          break;
        case "Axioma":
          this.entityStyle = {
            'background-color': '#61d9cf',
          };
          break;
        case "Propositio":
          this.entityStyle = {
            'background-color': '#e95a5a',
          };
          break;
        case "Demonstratio":
          this.entityStyle = {
            'background-color': '#d0693d',
          };
          break;
        case "Aliter":
          this.entityStyle = {
            'background-color': '#ff6947',
          };
          break;
        case "Explicatio":
          this.entityStyle = {
            'background-color': '#7aa06a',
          };
          break;
        case "Corollarium":
          this.entityStyle = {
            'background-color': '#28be7d',
          };
          break;
        case "Scholium":
          this.entityStyle = {
            'background-color': '#8e80c3',
          };
          break;
        case "Appendix":
          this.entityStyle = {
            'background-color': '#ac7599',
          };
          break;
        case "Caput":
          this.entityStyle = {
            'background-color': '#bc9c83',
          };
          break;
        case "Lemma":
          this.entityStyle = {
            'background-color': '#ff8f8f',
          };
          break;
        case "Postula":
          this.entityStyle = {
            'background-color': '#e8ff8e',
          };
          break;
        case "Praefatio":
          this.entityStyle = {
            'background-color': '#e6ffb9',
          };
          break;
        case "Titulus":
          this.entityStyle = {
            'background-color': '#faffa2',
          };
          break;
        case "Finis":
          this.entityStyle = {
            'background-color': '#92b0ff',
          };
          break;

      }
    },
    unsetStyle: function () {
      this.entityStyle = {};
    }
  },
}
</script>

<style scoped>

.text-element {
  text-align: justify;
  margin-left: 2%;
  margin-right: 2%;
}

</style>