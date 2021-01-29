<template>
  <div>
    <p :style="entityStyle" @mouseover="setStyle" @mouseout="unsetStyle">
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
            'background-color': '#4bbe28',
          };
          break;
        case "Axioma":
          this.entityStyle = {
            'background-color': '#4bbe28',
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
            'background-color': '#4bbe28',
          };
          break;
        case "Explicatio":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Corollarium":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Scholium":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Appendix":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Caput":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Lemma":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Postula":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Praefatio":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Titulus":
          this.entityStyle = {
            'background-color': '#4bbe28',
          };
          break;
        case "Finis":
          this.entityStyle = {
            'background-color': '#4bbe28',
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

</style>