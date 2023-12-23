<template>
  <div>
    <div
      class="modal-overlay"
      ref="overlay"
      :class="{ 'state-show': overlayVisible }"
    ></div>
    <div class="modal-frame" :class="{ 'state-appear': modalVisible }">
      <div class="modal-inset">
        <div class="modal-body">
          <textarea v-model="data.text" id="T_TRANS"></textarea>
          <button @click="closeModal">关闭</button>
          <button @click="handleText">格式转换</button>
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
      paras: [],
      text: ""
    });
    const overlayVisible = ref(false);
    const modalVisible = ref(false);
    const modalLeaving = ref(false);
    const overlayRef = ref(null);

    const handleText = () => {
      const lines = data.text.split("\n");
      const result = [];
      data.text = "";
      lines.forEach((line) => {
        if (!line.trim()) {
          return; // 如果文本为空，直接跳过不处理
        }
        if (line.startsWith("## ")) {
          result.push({ t: "h2", c: line.substring(3) });
        } else if (line.startsWith("### ")) {
          result.push({ t: "h3", c: line.substring(4) });
        } else if (line.startsWith("**")) {
          result.push({ t: "h4", c: line.substring(2) });
        } else {
          result.push({ t: "p", c: line.trim() });
        }
      });
      result.forEach((item) => {
        const { t, c } = item;
        const element = createHTMLElement(t, c);
        data.text += element.outerHTML;
      });
    };

    const createHTMLElement = (tag, content) => {
      const element = document.createElement(tag);
      if (content.includes("<") && content.includes(">")) {
        element.innerHTML = content;
      } else {
        element.textContent = content;
      }
      return element;
    };

    const openModal = (context) => {
      data.text = "";
      overlayVisible.value = true;
      modalVisible.value = true;
      modalLeaving.value = false;
      data.paras = context;
    };

    const closeModal = () => {
      data.text = "";
      overlayVisible.value = false;
      modalVisible.value = false;
    };
    return {
      data,
      handleText,
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
  src: url("/lion/mysxt.ttf");
  font-weight: normal;
  font-style: normal;
}
button {
  width: 100px;
  height: 40px;
  margin: auto;
  box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  border: none;
  margin-right: 20px;
  margin-top: 20px;
  cursor: pointer;
}
button:hover {
  background-color: rgba(50, 50, 50, 0.1);
}
textarea {
  width: 100%;
  height: 85vh;
  outline: none;
  border: none;
  box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  padding: 20px;
  font-family: "MYSXT";
  font-size: 15px;
  letter-spacing: 2;
  -webkit-font-smoothing: antialiased;
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
}
.modal-overlay.state-show {
  opacity: 0.7;
  visibility: visible;
  transition-delay: 0s;
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
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 100%;
  visibility: hidden;
}
.modal-frame.state-appear {
  visibility: visible;
}
.modal-frame.state-appear .modal-inset {
  animation: modalComeIn 0.25s ease;
  visibility: visible;
  /* to keep @ final state */
}
.modal-frame.state-appear .modal-body {
  opacity: 1;
  transform: translateY(0) scale(1, 1);
}
.modal-frame.state-leave {
  visibility: visible;
}
.modal-frame.state-leave .modal-inset {
  animation: modalHeadOut 0.35s ease 0.1s;
  visibility: visible;
}
.modal-frame.state-leave .modal-body {
  opacity: 0;
  transition-delay: 0s;
  transition-duration: 0.35s;
  transition-timing-function: ease;
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
  position: absolute;
  padding: 30px;
  background-color: #fff;
  color: #fff;
  width: 520px;
  height: 100vh;
  margin: auto;
  visibility: hidden;
  box-shadow: 2px 2px 8px 1px rgba(0, 0, 0, 0.2);
  backface-visibility: hidden;
  transform: translate3d(0, 0, 0);
  transform-style: preserve-3d;
}

.modal-body {
  margin: auto;
}
.modal-body p {
  padding-top: 10px;
  padding-bottom: 10px;
  margin: 0;
  /* font-family: "MYSXT"; */
  /* font-family: "Kaiti SC"; */
  font-weight: 200;
  font-size: 0.9rem;
  font-smoothing: antialiased;
}
</style>
