<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import PMSelector from "./components/PMSelector.vue";
import Legend from "./components/Legend.vue";
</script>

<template>
  <div class="app-root">
    <!-- Top control panel -->
    <header class="top-panel">
      <h1>PM Monitoring Digital Twin Platform</h1>
      <PMSelector />
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
  grid-template-columns: 1fr auto;
  height: 100vh;
  background: #0f172a; /* dark, professional */
  color: #e5e7eb;
}

.top-panel {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: #020617;
  border-bottom: 1px solid #1e293b;
}

.viewer {
  grid-row: 2;
  grid-column: 1;
  position: relative;
}

.legend-panel {
  grid-row: 2;
  grid-column: 2;
  width: 220px;
  padding: 12px;
  background: #020617;
  border-left: 1px solid #1e293b;
}
</style>
