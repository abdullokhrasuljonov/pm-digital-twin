import { defineStore } from "pinia";

export const useEnvStore = defineStore("env", {
  state: () => ({
    timeRange: {
      start: "",
      end: "",
    },

    humidity: 50,       // %
    windSpeed: 2.0,     // m/s
    windDirection: 0,   // degrees (0 = North)
  }),

  actions: {
    setTimeRange(start: string, end: string) {
      this.timeRange.start = start;
      this.timeRange.end = end;
    },

    setHumidity(value: number) {
      this.humidity = value;
    },

    setWindSpeed(value: number) {
      this.windSpeed = value;
    },

    setWindDirection(value: number) {
      this.windDirection = value;
    },
  },
});
