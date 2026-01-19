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
}
</style>
