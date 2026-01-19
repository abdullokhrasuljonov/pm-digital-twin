<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from "vue";
import {
  Engine,
  Scene,
  ArcRotateCamera,
  Vector3,
  HemisphericLight,
} from "@babylonjs/core";
import "@babylonjs/loaders";

const canvasRef = ref<HTMLCanvasElement | null>(null);

let engine: Engine | null = null;
let scene: Scene | null = null;

onMounted(() => {
  if (!canvasRef.value) return;

  engine = new Engine(canvasRef.value, true);
  scene = new Scene(engine);

  // Camera
  const camera = new ArcRotateCamera(
    "camera",
    Math.PI / 2,
    Math.PI / 3,
    30,
    Vector3.Zero(),
    scene
  );
  camera.attachControl(canvasRef.value, true);

  // Light
  new HemisphericLight("light", new Vector3(0, 1, 0), scene);

  // Render loop
  engine.runRenderLoop(() => {
    scene?.render();
  });

  // Resize handling
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
}
</style>
