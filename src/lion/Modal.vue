<template>
  <div>
    <div
      class="modal-overlay"
      ref="overlay"
      :class="{ 'state-show': overlayVisible }"
      @click="closeModal"
    ></div>
    <div
      class="modal-frame"
      @click="closeModal"
      :class="{ 'state-appear': modalVisible }"
    >
      <div class="modal-inset">
        <div class="modal-body">
          <p v-for="item in data.paras">
            {{ item }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, reactive } from "vue";

export default {
  setup() {
    const data = reactive({
      paras: []
    });
    const overlayVisible = ref(false);
    const modalVisible = ref(false);
    const modalLeaving = ref(false);
    const overlayRef = ref(null);

    const openModal = (context) => {
      overlayVisible.value = true;
      modalVisible.value = true;
      modalLeaving.value = false;
      data.paras = context;
    };

    const closeModal = () => {
      overlayVisible.value = false;
      modalVisible.value = false;
    };
    return {
      data,
      overlayVisible,
      overlayRef,
      modalVisible,
      modalLeaving,
      openModal,
      closeModal
    };
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

@font-face {
  font-family: "MYSXT";
  src: url("./mysxt.ttf");
  font-weight: normal;
  font-style: normal;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  background-color: #fff;
  opacity: 0;
  visibility: hidden;
  z-index: 40;
  -moz-transition: opacity 0.25s ease 0s, visibility 0.35s linear;
  -o-transition: opacity 0.25s ease 0s, visibility 0.35s linear;
  -webkit-transition: opacity 0.25s ease, visibility 0.35s linear;
  -webkit-transition-delay: 0s, 0s;
  transition: opacity 0.25s ease 0s, visibility 0.35s linear;
}
.modal-overlay.state-show {
  opacity: 0.7;
  visibility: visible;
  -moz-transition-delay: 0s;
  -o-transition-delay: 0s;
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
  -moz-transition-duration: 0.2s, 0s;
  -o-transition-duration: 0.2s, 0s;
  -webkit-transition-duration: 0.2s, 0s;
  transition-duration: 0.2s, 0s;
}

.modal-frame {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  z-index: 50;

  /*     display: table; */
  display: -webkit-flex;
  display: flex;
  -webkit-align-items: center;
  align-items: center;
  -moz-box-align: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -moz-box-pack: center;
  -ms-flex-pack: center;
  width: 100%;
  visibility: hidden;
}
.modal-frame.state-appear {
  visibility: visible;
}
.modal-frame.state-appear .modal-inset {
  -moz-animation: modalComeIn 0.25s ease;
  -webkit-animation: modalComeIn 0.25s ease;
  animation: modalComeIn 0.25s ease;
  visibility: visible;
  /* to keep @ final state */
}
.modal-frame.state-appear .modal-body {
  opacity: 1;
  -moz-transform: translateY(0) scale(1, 1);
  -ms-transform: translateY(0) scale(1, 1);
  -webkit-transform: translateY(0) scale(1, 1);
  transform: translateY(0) scale(1, 1);
}
.modal-frame.state-leave {
  visibility: visible;
}
.modal-frame.state-leave .modal-inset {
  -moz-animation: modalHeadOut 0.35s ease 0.1s;
  -webkit-animation: modalHeadOut 0.35s ease 0.1s;
  animation: modalHeadOut 0.35s ease 0.1s;
  visibility: visible;
}
.modal-frame.state-leave .modal-body {
  opacity: 0;
  -moz-transition-delay: 0s;
  -o-transition-delay: 0s;
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
  -moz-transition-duration: 0.35s;
  -o-transition-duration: 0.35s;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -moz-transition-timing-function: ease;
  -o-transition-timing-function: ease;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
  -moz-transform: translateY(25px);
  -ms-transform: translateY(25px);
  -webkit-transform: translateY(25px);
  transform: translateY(25px);
}

@-moz-document url-prefix() {
  .modal-frame {
    height: calc(100% - 55px);
  }
}
.modal {
  display: block;
  vertical-align: middle;
}

.modal-inset {
  position: relative;
  padding: 30px;
  background-color: rgba(34, 34, 34, 0.8);
  border-radius: 8px;
  color: #fff;
  width: 520px;
  min-height: 50px;
  margin: auto;
  visibility: hidden;
  -moz-box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  -moz-backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -moz-transform: translate3d(0, 0, 0);
  -ms-transform: translate3d(0, 0, 0);
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  -moz-transform-style: preserve-3d;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
}

.modal-body {
  margin: auto;
  opacity: 0;
  -moz-transform: translateY(0) scale(0.8, 0.8);
  -ms-transform: translateY(0) scale(0.8, 0.8);
  -webkit-transform: translateY(0) scale(0.8, 0.8);
  transform: translateY(0) scale(0.8, 0.8);
  -moz-transition-property: opacity, -moz-transform;
  -o-transition-property: opacity, -o-transform;
  -webkit-transition-property: opacity, -webkit-transform;
  transition-property: opacity, transform;
  -moz-transition-duration: 0.25s;
  -o-transition-duration: 0.25s;
  -webkit-transition-duration: 0.25s;
  transition-duration: 0.25s;
  -moz-transition-delay: 0.1s;
  -o-transition-delay: 0.1s;
  -webkit-transition-delay: 0.1s;
  transition-delay: 0.1s;
}
.modal-body p {
  padding-top: 10px;
  padding-bottom: 10px;
  margin: 0;
  /* font-family: "MYSXT"; */
  /* font-family: "Kaiti SC"; */
  font-weight: 200;
  font-size: 0.9rem;
  -webkit-font-smoothing: antialiased;
}

@-webkit-keyframes modalComeIn {
  0% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: scale(0.8, 0.8);
    -ms-transform: scale(0.8, 0.8);
    -webkit-transform: scale(0.8, 0.8);
    transform: scale(0.8, 0.8);
  }
  65.5% {
    -moz-transform: scale(1.03, 1.03);
    -ms-transform: scale(1.03, 1.03);
    -webkit-transform: scale(1.03, 1.03);
    transform: scale(1.03, 1.03);
  }
  100% {
    visibility: visible;
    opacity: 1;
    -moz-transform: scale(1, 1);
    -ms-transform: scale(1, 1);
    -webkit-transform: scale(1, 1);
    transform: scale(1, 1);
  }
}
@-moz-keyframes modalComeIn {
  0% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: scale(0.8, 0.8);
    -ms-transform: scale(0.8, 0.8);
    -webkit-transform: scale(0.8, 0.8);
    transform: scale(0.8, 0.8);
  }
  65.5% {
    -moz-transform: scale(1.03, 1.03);
    -ms-transform: scale(1.03, 1.03);
    -webkit-transform: scale(1.03, 1.03);
    transform: scale(1.03, 1.03);
  }
  100% {
    visibility: visible;
    opacity: 1;
    -moz-transform: scale(1, 1);
    -ms-transform: scale(1, 1);
    -webkit-transform: scale(1, 1);
    transform: scale(1, 1);
  }
}
@keyframes modalComeIn {
  0% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: scale(0.8, 0.8);
    -ms-transform: scale(0.8, 0.8);
    -webkit-transform: scale(0.8, 0.8);
    transform: scale(0.8, 0.8);
  }
  65.5% {
    -moz-transform: scale(1.03, 1.03);
    -ms-transform: scale(1.03, 1.03);
    -webkit-transform: scale(1.03, 1.03);
    transform: scale(1.03, 1.03);
  }
  100% {
    visibility: visible;
    opacity: 1;
    -moz-transform: scale(1, 1);
    -ms-transform: scale(1, 1);
    -webkit-transform: scale(1, 1);
    transform: scale(1, 1);
  }
}
@-webkit-keyframes modalHeadOut {
  0% {
    visibility: visible;
    opacity: 1;
    -moz-transform: translateY(0) scale(1, 1);
    -ms-transform: translateY(0) scale(1, 1);
    -webkit-transform: translateY(0) scale(1, 1);
    transform: translateY(0) scale(1, 1);
  }
  100% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(35px) scale(0.97, 0.97);
    -ms-transform: translateY(35px) scale(0.97, 0.97);
    -webkit-transform: translateY(35px) scale(0.97, 0.97);
    transform: translateY(35px) scale(0.97, 0.97);
  }
}
@-moz-keyframes modalHeadOut {
  0% {
    visibility: visible;
    opacity: 1;
    -moz-transform: translateY(0) scale(1, 1);
    -ms-transform: translateY(0) scale(1, 1);
    -webkit-transform: translateY(0) scale(1, 1);
    transform: translateY(0) scale(1, 1);
  }
  100% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(35px) scale(0.97, 0.97);
    -ms-transform: translateY(35px) scale(0.97, 0.97);
    -webkit-transform: translateY(35px) scale(0.97, 0.97);
    transform: translateY(35px) scale(0.97, 0.97);
  }
}
@keyframes modalHeadOut {
  0% {
    visibility: visible;
    opacity: 1;
    -moz-transform: translateY(0) scale(1, 1);
    -ms-transform: translateY(0) scale(1, 1);
    -webkit-transform: translateY(0) scale(1, 1);
    transform: translateY(0) scale(1, 1);
  }
  100% {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(35px) scale(0.97, 0.97);
    -ms-transform: translateY(35px) scale(0.97, 0.97);
    -webkit-transform: translateY(35px) scale(0.97, 0.97);
    transform: translateY(35px) scale(0.97, 0.97);
  }
}
</style>
