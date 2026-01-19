<script setup lang="ts">
import { computed } from "vue";
import { usePMStore } from "../store/pmStore";

type PMType = "pm1" | "pm25" | "pm10";

const pmStore = usePMStore();

const selectedPM = computed<PMType>({
  get: () => pmStore.pmType as PMType,
  set: (val) => pmStore.setPMType(val),
});
</script>


<template>
  <div class="pm-selector">
    <label for="pm">PM Type:</label>
    <select id="pm" v-model="selectedPM">
      <option value="pm1">PM1.0</option>
      <option value="pm25">PM2.5</option>
      <option value="pm10">PM10</option>
    </select>
  </div>
</template>

<style scoped>
.pm-selector {
  display: flex;
  align-items: center;
  gap: 8px;
}

select {
  background: #020617;
  color: #e5e7eb;
  border: 1px solid #1e293b;
  padding: 4px 6px;
}
</style>
