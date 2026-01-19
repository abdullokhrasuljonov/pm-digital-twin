<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import PMSelector from "./components/PMSelector.vue";
import Legend from "./components/Legend.vue";
</script>

<template>
  <div class="app-root">
    <!-- Top control panel -->
    <header class="top-panel">
      <h1>Construction Site PM Digital Twin</h1>
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
  backgrou
