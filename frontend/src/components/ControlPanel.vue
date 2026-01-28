<script setup lang="ts">
import { ref } from "vue";
import HistoricalControls from "./controls/HistoricalControls.vue";
import PredictionControls from "./controls/PredictionControls.vue";

const activeTab = ref<"history" | "prediction">("history");
</script>

<template>
  <div class="w-full text-slate-300">
    <!-- Tabs -->
    <div class="flex bg-slate-900 rounded-xl mb-4">
      <button
        class="flex-1 py-2 text-md font-medium text-center"
        :class="activeTab === 'history'
          ? 'text-white bg-slate-800 rounded-xl'
          : 'text-slate-400 hover:text-slate-200'"
        @click="activeTab = 'history'"
      >
        Historical Data
      </button>

      <button
        class="flex-1 py-2 text-md font-medium text-center"
        :class="activeTab === 'prediction'
          ? 'text-white  bg-slate-800 rounded-xl'
          : 'text-slate-400 hover:text-slate-200'"
        @click="activeTab = 'prediction'"
      >
        Prediction
      </button>
    </div>

    <!-- Content -->
    <div>
      <HistoricalControls v-if="activeTab === 'history'" />
      <PredictionControls v-else />
    </div>
  </div>
</template>
