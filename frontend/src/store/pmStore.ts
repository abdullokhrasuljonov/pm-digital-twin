import { defineStore } from "pinia";

export type PMType = "pm1" | "pm25" | "pm10";

export const usePMStore = defineStore("pm", {
  state: () => ({
    pmType: "pm25" as PMType,
  }),

  actions: {
    setPMType(type: PMType) {
      this.pmType = type;
    },
  },
});
