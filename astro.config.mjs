import { defineConfig } from "astro/config";
import vue from "@astrojs/vue";
import astroI18next from "astro-i18next";

// https://astro.build/config
export default defineConfig({
  integrations: [astroI18next(), vue()]
});
