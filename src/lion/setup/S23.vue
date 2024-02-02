<template>
  <article data-chapter="1"></article>
  <Modal ref="S1Modal" />
  <Tools />
</template>
<script setup>
import Modal from "../Modal.vue";
import Tools from "./Tools.vue";
import * as PAPER from "./Paper.js";
import { ref } from "vue";
const S1Modal = ref(null);

function handlePaper(index) {
  const data = PAPER[`S${1}_PAPER`][parseInt(index)];
  S1Modal.value.openModal(data.paras); // 调用子组件方法
}
</script>
