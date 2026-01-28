<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import ControlPanel from "./components/ControlPanel.vue";
</script>

<template>
  <div
    class="grid grid-rows-[auto_1fr] grid-cols-[1fr_420px]
           w-screen h-screen bg-slate-850 text-slate-100"
  >
    <!-- Top control panel -->
    <header
      class="col-span-2 h-full flex items-center justify-between
             px-6 py-4 bg-slate-850"
    >
      <h2 class="text-lg font-semibold">
        PM Monitoring Digital Twin Platform
      </h2>
    </header>

    <!-- 3D Digital Twin -->
    <main class="overflow-hidden bg-slate-850">
      <BabylonCanvas />
    </main>

    <!-- PM legend + controls -->
    <aside class="bg-slate-850 px-4 space-y-4">
      <ControlPanel />
    </aside>
  </div>
</template>
