<script setup lang="ts">
import BabylonCanvas from "./components/BabylonCanvas.vue";
import ControlPanel from "./components/ControlPanel.vue";
</script>

<template>
  <div
    class="grid grid-rows-[auto_1fr] grid-cols-[1fr_360px]
           w-screen h-screen bg-slate-950 text-slate-100"
  >
    <!-- Top control panel -->
    <header
      class="col-span-2 flex items-center justify-between
             px-6 h-14 bg-slate-950"
    >
      <h2 class="text-lg font-semibold">
        PM Monitoring Digital Twin Platform
      </h2>
    </header>

    <!-- 3D Digital Twin -->
    <main class="overflow-hidden bg-slate-950">
      <BabylonCanvas />
    </main>

    <!-- PM legend + controls -->
    <aside class="bg-slate-950 p-6 space-y-6">
      <ControlPanel />
    </aside>
  </div>
</template>
