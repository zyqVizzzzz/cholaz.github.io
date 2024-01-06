<template>
  <div class="tool-container">
    <div class="tools" @click="openTextOpt"><div>碎片机器</div></div>
  </div>

  <text-trans ref="TModal" />
</template>
<script setup>
import TextTrans from "./TextTrans.vue";
import { ref } from "vue";
const TModal = ref(null);
function openTextOpt() {
  TModal.value.openModal(1); // 调用子组件方法
}
</script>
<style scoped>
@font-face {
  font-family: "MYSXT";
  src: url("/lion/mysxt.ttf");
  font-weight: normal;
  font-style: normal;
}
.tool-container {
  background: #000;
  position: fixed;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  width: 40px;
  background: #fff;
  border-radius: 10px;
}
@media (max-width: 900px) {
  .tool-container {
    display: none;
  }
}
.tools {
  width: 40px;
  /* height: 50px; */
  padding: 10px 0;
  border-radius: 10px;
  background: rgba(97, 46, 61, 0.1);
  color: rgba(45, 36, 63, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;

  font-family: "MYSXT";
  font-weight: 400;
  letter-spacing: 2px;
  line-height: 1.5;
}
div {
  width: 15px;
}
</style>
