import { defineStore } from "pinia";


export const useEnvStore = defineStore("env", {
  state: () => ({
    timeRange: {
      start: "2026-10-01T14:00",
      end: "2026-10-01T16:00",
    },

    humidity: 50,        // %
    windSpeed: 2.0,      // m/s
    windDirection: 0,    // degrees (0 = North)
  }),

  actions: {
    setTimeRange() {
      this.timeRange.start = '2026-10-01T14:00:00Z';
      this.timeRange.end = '2026-10-01T16:00:00Z';
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
