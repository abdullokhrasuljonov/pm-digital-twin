<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, watch } from "vue";
import {
  Engine,
  Scene,
  ArcRotateCamera,
  Vector3,
  HemisphericLight,
  SceneLoader,
} from "@babylonjs/core";
import "@babylonjs/loaders";
import { useEnvStore } from "../store/envStore";

/* =========================
   Store
========================= */
const env = useEnvStore();

/* =========================
   Canvas & Babylon refs
========================= */
const canvasRef = ref<HTMLCanvasElement | null>(null);

let engine: Engine | null = null;
let scene: Scene | null = null;

/* =========================
   React to environment changes
========================= */
watch(
  () => [
    env.timeRange.start,
    env.timeRange.end,
    env.humidity,
    env.windSpeed,
    env.windDirection,
  ],
  () => {
    console.log("Simulation updated:", {
      time: env.timeRange,
      humidity: env.humidity,
      windSpeed: env.windSpeed,
      windDirection: env.windDirection,
    });
  }
);

/* =========================
   Resize
========================= */
function handleResize() {
  engine?.resize();
}

/* =========================
   Babylon lifecycle
========================= */
onMounted(async () => {
  if (!canvasRef.value) return;

  engine = new Engine(canvasRef.value, true);
  scene = new Scene(engine);

  const camera = new ArcRotateCamera(
    "camera",
    Math.PI / 2,
    Math.PI / 3,
    50,
    Vector3.Zero(),
    scene
  );

  camera.attachControl(canvasRef.value, true);

  new HemisphericLight("light", new Vector3(0, 1, 0), scene);

  // Load site model
  await SceneLoader.AppendAsync("/models/", "site.glb", scene);

  camera.zoomOn(scene.meshes);

  engine.runRenderLoop(() => {
    scene?.render();
  });

  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
  engine?.dispose();
});
</script>

<template>
  <canvas
    ref="canvasRef"
    class="
      w-full
      h-full
      block
      outline-none
      border-0
      bg-slate-950
      select-none
    "
  />
</template>
