<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch } from "vue";
import {
  Engine,
  Scene,
  ArcRotateCamera,
  Vector3,
  HemisphericLight,
  SceneLoader,
  MeshBuilder,
  StandardMaterial,
  Color3,
  Mesh,
} from "@babylonjs/core";
import "@babylonjs/loaders";

import { useEnvStore } from "../store/envStore";
import { fetchPmData } from "../services/pmApi";

/* =====================================================
   Store
===================================================== */
const env = useEnvStore();

/* =====================================================
   Canvas & Babylon refs
===================================================== */
const canvasRef = ref<HTMLCanvasElement | null>(null);

let engine: Engine | null = null;
let scene: Scene | null = null;
let pmMeshes: Mesh[] = [];

/* =====================================================
   PM color mapping
===================================================== */
function pmColor(value: number): Color3 {
  if (value <= 30) return Color3.Green();
  if (value <= 80) return Color3.Yellow();
  else return Color3.Red();
}

/* =====================================================
   Render PM dots
===================================================== */
function renderPmDots(
  scene: Scene,
  data: Array<{ x: number; y: number; z: number; value: number }>
) {
  // Clear previous dots
  pmMeshes.forEach((m) => m.dispose());
  pmMeshes = [];

  data.forEach((p) => {
    const sphere = MeshBuilder.CreateSphere(
      "pm-dot",
      { diameter: 2 },
      scene
    );

    // sphere.position.set(p.x, p.y + 0.5, p.z);
    sphere.position.set(p.x, p.y, p.z);

    const mat = new StandardMaterial("pm-mat", scene);
    mat.diffuseColor = pmColor(p.value);
    mat.emissiveColor = mat.diffuseColor.scale(0.3);

    sphere.material = mat;
    pmMeshes.push(sphere);
  });
}

/* =====================================================
   Fetch + update PM scene
===================================================== */
async function updatePmScene() {
  if (!scene) return;

  try {
    const res = await fetchPmData();
    console.log("PM data received:", res.data.data);

    renderPmDots(scene, res.data.data);
  } catch (err) {
    console.error("Failed to update PM scene:", err);
  }
}

/* =====================================================
   React to simulation changes
===================================================== */
watch(
  () => [
    env.timeRange.start,
    env.timeRange.end,
    env.humidity,
    env.windSpeed,
    env.windDirection,
  ],
  () => {
    console.log("Simulation updated → re-render PM");
    updatePmScene();
  }
);

/* =====================================================
   Resize
===================================================== */
function handleResize() {
  engine?.resize();
}

/* =====================================================
   BabylonJS lifecycle
===================================================== */
onMounted(async () => {
  if (!canvasRef.value) return;

  engine = new Engine(canvasRef.value, true);
  scene = new Scene(engine);

  // Camera
  const camera = new ArcRotateCamera(
    "camera",
    Math.PI / 2,
    Math.PI / 3,
    60,
    new Vector3(0, 50, 0),
    scene
  );
  
  camera.attachControl(canvasRef.value, true);
  camera.wheelDeltaPercentage = 0.01;

  // Light
  const light = new HemisphericLight(
    "light",
    new Vector3(0, 1, 0),
    scene
  );
  light.intensity = 0.8
  

  // Load site model
  await SceneLoader.AppendAsync("/models/", "site.glb", scene);
  camera.zoomOn(scene.meshes);

  // Initial PM render
  await updatePmScene();

  // Render loop
  engine.runRenderLoop(() => {
    scene?.render();
  });

  window.addEventListener("resize", handleResize);
});

/* =====================================================
   Cleanup
===================================================== */
onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);

  pmMeshes.forEach((m) => m.dispose());
  pmMeshes = [];

  engine?.stopRenderLoop();
  engine?.dispose();

  scene = null;
  engine = null;
});
</script>

<template>
  <canvas
    ref="canvasRef"
    class="block w-full h-full bg-slate-950 outline-none select-none"
  />
</template>
