<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import Legend from "./components/Legend.vue";
</script>

<template>
  <div class="app-root">
    <!-- Top control panel -->
    <header class="top-panel">
      <h2>PM Monitoring Digital Twin Platform</h2>
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
  background: #020617;
}

.top-panel h1 {
  margin: 0;
  color: #f8fafc;
  font-size: 18px;
  font-weight: 600;
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
  background: #020617;
  border-left: 1px solid #1e293b;
}

</style>
