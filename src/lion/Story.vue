<template>
  <main class="story">
    <S1 v-if="parseInt(id) === 1" />
    <S2 v-if="parseInt(id) === 2" />
    <S3 v-if="parseInt(id) === 3" />
    <S4 v-if="parseInt(id) === 4" />
    <S5 v-if="parseInt(id) === 5" />
    <S6 v-if="parseInt(id) === 6" />
    <S7 v-if="parseInt(id) === 7" />
    <S8 v-if="parseInt(id) === 8" />
    <S9 v-if="parseInt(id) === 9" />
    <S10 v-if="parseInt(id) === 10" />
    <S11 v-if="parseInt(id) === 11" />
    <S12 v-if="parseInt(id) === 12" />
    <S13 v-if="parseInt(id) === 13" />
    <S14 v-if="parseInt(id) === 14" />
    <S15 v-if="parseInt(id) === 15" />
    <S16 v-if="parseInt(id) === 16" />
    <S17 v-if="parseInt(id) === 17" />
    <S18 v-if="parseInt(id) === 18" />
    <S19 v-if="parseInt(id) === 19" />
    <div class="pagination">
      <a v-if="id > 1" :href="`/lion/${id - 1}`">上一页</a>
      <a href="/lion">返回目录</a>
      <a v-if="id < 19" :href="`/lion/${id + 1}`">下一页</a>
    </div>
  </main>
</template>

<script setup>
import S1 from "./setup/S1.vue";
import S2 from "./setup/S2.vue";
import S3 from "./setup/S3.vue";
import S4 from "./setup/S4.vue";
import S5 from "./setup/S5.vue";
import S6 from "./setup/S6.vue";
import S7 from "./setup/S7.vue";
import S8 from "./setup/S8.vue";
import S9 from "./setup/S9.vue";
import S10 from "./setup/S10.vue";
import S11 from "./setup/S11.vue";
import S12 from "./setup/S12.vue";
import S13 from "./setup/S13.vue";
import S14 from "./setup/S14.vue";
import S15 from "./setup/S15.vue";
import S16 from "./setup/S16.vue";
import S17 from "./setup/S17.vue";
import S18 from "./setup/S18.vue";
import S19 from "./setup/S19.vue";
const { id } = defineProps(["id"]);
</script>

<style lang="scss">
body {
  margin: 0;
  padding: 0;
}
@font-face {
  font-family: "MYSXT";
  src: url("/lion/mysxt.ttf");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "LXGW";
  src: url("/lion/LXGW.ttf");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "JZXF";
  src: url("/lion/JZXF.ttf");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "FKH";
  src: url("/lion/FKH.ttf");
  font-weight: normal;
  font-style: normal;
}

main.story {
  max-width: 600px;
  margin: 0 auto;
  position: relative;
  // left: 85px;
  // font-family: "LXGW";
  // font-family: "JZXF";
  font-family: "MYSXT";
  // font-family: "SongTi SC";
  -webkit-font-smoothing: antialiased;
  font-size: 15px;
  letter-spacing: 1.7px;
  line-height: 1.4;
  text-align: justify;
  padding: 60px 0 0px;
  box-sizing: border-box;
  position: relative;

  article {
    // width: 60%;
    margin-bottom: 30px;
    position: relative;
    left: 10px;
  }
  .article {
    width: 600px;
    margin: 0 auto;
  }

  .desc {
    position: absolute;
    top: 5px;
    right: -100px;
    font-size: 0.8rem;
    font-weight: 400;
    color: rgba(45, 36, 63, 0.7);
    box-sizing: border-box;
    border-radius: 4px;
    background: rgba(97, 46, 61, 0.1);
    padding: 3px 10px 0px;
    border-bottom: 2px solid rgba(97, 46, 61, 0.2);
    cursor: pointer;
  }

  .pagination {
    display: flex;
    width: 300px;
    align-items: center;
    justify-content: space-around;
    margin: 50px auto;
  }
  .pagination > div {
    position: absolute;
  }
  a {
    color: #000;
    margin-bottom: 50px;
  }

  h2 {
    font-size: 1.5rem;
    margin: 30px 0;
    font-family: "LXGW";
  }

  h1 {
    font-size: 2.5rem;
    margin: 30px 0;
    position: fixed;
    font-family: "LXGW";
  }
  h1 > div {
    position: absolute;
    top: 5px;
    left: -130px;
    width: 2.5rem;
    font-size: 2.5rem;
    font-weight: 900;
    line-height: 1.5;
    color: rgba(97, 46, 61, 0.5);
  }
  h1 > .story-h2 {
    position: absolute;
    top: -35px;
    left: -150px;
    width: 2.5rem;
    font-size: 2.5rem;
    font-weight: 900;
    line-height: 1.5;
    color: rgba(97, 46, 61, 0.5);
  }

  h3 {
    font-size: 1.3rem;
    margin: 30px 0 15px;
    position: relative;
    font-weight: 400;
  }

  a.mark {
    color: inherit;
    background: url("data:image/svg+xml;charset=utf-8,%3Csvg preserveAspectRatio='none' width='120' height='5' viewBox='0 0 120 6' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M119 0.8C60 4 50-0.5 1 1.5' stroke='%23612e3d80' stroke-width='2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")
      bottom left/100% 0.3em no-repeat;
    text-decoration: none;
    padding-bottom: 0.3em;
  }

  h4 {
    position: relative;
    display: inline-block;
    margin: 5px -0.4em 0px;
    padding: 0.1em 0.4em;
    border-radius: 0.3em 0.2em;
    background: transparent;
    background-image: linear-gradient(
      to right,
      rgba(131, 63, 61, 0.1),
      rgba(131, 63, 61, 0.3) 30%,
      rgba(131, 63, 83, 0.1)
    );
    -webkit-box-decoration-break: clone;
    color: rgb(18, 18, 18);
    font-weight: 500;
  }

  p {
    width: 100%;
    line-height: 1.6;
    margin: 15px 0;
    position: relative;
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 0.4px;
    text-decoration-color: rgb(221, 216, 223);
  }
  p.label {
    margin: 12px 0;
  }

  span.tip {
    // font-family: "KaiTi SC";
    color: rgba(0, 0, 0, 0.4);
    font-size: 12px;
  }

  aside {
    border-radius: 4px;
    color: #2d243f;
    box-sizing: border-box;
    background: rgb(241, 241, 239);
    padding: 6px 16px 13px 12px;
    position: relative;
    font-family: "LXGW";
    // font-style: italic;
    margin: 35px 0;
    width: 100%;
    &::before {
      content: "“";
      font-family: "MYSXT";
      font-size: 2rem;
      position: absolute;
      top: 50%;
      left: -50px;
      transform: translateY(-100%);
      color: rgba(97, 46, 61, 0.3);
    }
    &::after {
      content: "”";
      font-family: "MYSXT";
      font-size: 2rem;
      position: absolute;
      top: 50%;
      right: -50px;
      transform: translateY(50%);
      color: rgba(97, 46, 61, 0.3);
    }
    .aside-title {
      font-size: 1.5rem;
      letter-spacing: 1.5px;
      color: rgba(97, 46, 61, 0.5);
      padding-left: 10px;
    }
    .aside-para {
      font-size: 14px;
      padding-left: 10px;
      box-sizing: border-box;
      color: rgba(0, 0, 0, 0.7);
    }
  }
}
@media (max-width: 900px) {
  main.story {
    max-width: 540px;
    .desc {
      display: none;
    }
  }
}
@media (max-width: 400px) {
  main.story {
    max-width: 90%;
    margin: 0 auto;
  }
}
</style>
