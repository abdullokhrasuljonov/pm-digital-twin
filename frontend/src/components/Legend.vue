<script setup lang="ts">
import PMSelector from "../components/PMSelector.vue";
</script>


<template>
  <div class="legend">
    <main class="">
      <PMSelector />
    </main>
  </div>
</template>


<style scoped>
.legend {
  font-size: 14px;
}

.legend ul {
  list-style: none;
  padding: 0;
  margin: 8px 0 0;
}

.legend li {
  display: flex;
  align-items: center;
  margin-bottom: 6px;
}
</style>
