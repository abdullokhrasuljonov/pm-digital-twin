import { defineStore } from "pinia";

function toLocalISOString(date: Date) {
  return date.toISOString().slice(0, 16); // YYYY-MM-DDTHH:mm
}

export const useEnvStore = defineStore("env", {
  state: () => ({
    timeRange: {
      // default: last 2 hours → now
      start: toLocalISOString(new Date(Date.now() - 2 * 60 * 60 * 1000)),
      end: toLocalISOString(new Date()),
    },

    humidity: 50,        // %
    windSpeed: 2.0,      // m/s
    windDirection: 0,    // degrees (0 = North)
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
