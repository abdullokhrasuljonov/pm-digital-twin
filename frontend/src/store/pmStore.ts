import { defineStore } from "pinia";

export type PMType = "pm1" | "pm2_5" | "pm10";

export const usePMStore = defineStore("pm", {
  state: () => ({
    pmType: "pm2_5" as PMType,
  }),

  actions: {
    setPMType(type: PMType) {
      this.pmType = type;
    },
  },
});
