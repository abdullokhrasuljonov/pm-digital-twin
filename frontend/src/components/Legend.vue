<script setup lang="ts">
import PMSelector from "../components/PMSelector.vue";
</script>

<template>
  <div class="legend">
    <main class="">
      <PMSelector />
    </main>
    <ul>
      <li><span class="box pm1"></span> PM1.0</li>
      <li><span class="box pm25"></span> PM2.5</li>
      <li><span class="box pm10"></span> PM10</li>
    </ul>
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

.box {
  width: 14px;
  height: 14px;
  margin-right: 8px;
  border-radius: 0px;
}

.pm1 { background: #22c55e; }   /* green */
.pm25 { background: #f59e0b; }  /* orange */
.pm10 { background: #ef4444; }  /* red */
</style>
