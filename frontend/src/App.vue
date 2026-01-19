<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import Legend from "./components/Legend.vue";
</script>

<template>
  <div class="app-root">
    <!-- Top control panel -->
    <header class="top-panel">
      <h2 class>PM Monitoring Digital Twin Platform</h2>
    </header>

    <!-- 3D Digital Twin -->
    <main class="viewer">
      <BabylonCanvas />
    </main>

    <!-- PM legend -->
    <aside class="legend-panel">
      <Legend />
    </aside>
  </div>
</template>

<style scoped>
.app-root {
  display: grid;
  grid-template-rows: auto 1fr;
  grid-template-columns: 1fr 240px;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background: #020617;
}


.top-panel {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 20px;
  color: azure;
  background: #020617;
}

.viewer {
  grid-row: 2;
  grid-column: 1;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background: #020617;
  overflow: hidden;
}


.legend-panel {
  grid-row: 2;
  grid-column: 2;
  padding: 12px;
  color: azure;
  background: #020617;
}

</style>
