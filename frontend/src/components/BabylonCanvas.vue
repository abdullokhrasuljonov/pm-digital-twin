<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from "vue";
import {
  Engine,
  Scene,
  ArcRotateCamera,
  Vector3,
  HemisphericLight,
  SceneLoader,
} from "@babylonjs/core";
import "@babylonjs/loaders";
import { watch } from "vue";
import { useEnvStore } from "../store/envStore";

const env = useEnvStore();


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

    // 🔜 later:
    // - re-fetch PM data
    // - update heatmap
    // - adjust particle flow direction
  }
);



const canvasRef = ref<HTMLCanvasElement | null>(null);

let engine: Engine | null = null;
let scene: Scene | null = null;

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

  // Load 3D site model
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

function handleResize() {
  engine?.resize();
}
</script>

<template>
  <canvas ref="canvasRef" class="babylon-canvas"></canvas>
</template>

<style scoped>
.babylon-canvas {
  width: 100%;
  height: 100%;
  display: block;
  outline: none;
  border: none;
}
</style>
