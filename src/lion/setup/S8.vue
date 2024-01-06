<template>
  <article>
    <h2>
      <div>世界观</div>
      <div>南城四夷坊·叁</div>
    </h2>
    <h4>吴人坊、燕人坊、西埯坊、扶桑坊</h4>
    <p>
      洛阳有二百二十六座里坊，其中四夷坊<span class="tip">（游民社区）</span
      >其面积最广，人口最稠密，民族成分最纷杂。四夷坊最初规划时，为圈禁番邦异族之所，但因诸般原由，又吸引了大量来自本土的底层百姓<span
        class="tip"
        >（时局困顿，贫者想入庄园为奴而不得，因为庄园也要裁减人手，走投无路的人只能来四夷坊闯一闯）</span
      >。时至今日，四夷坊早已脱离「夷坊」之标谱，洛阳人民九十万，四夷坊独据十万。
      <span class="desc" @click="handlePaper(0)">【碎片*】</span>
    </p>
    <h4>鹩儿巷</h4>
    <p>
      鹩儿巷位于吴人坊和西埯坊的交界地带，虽是四夷坊的一部分，但这里却是个雅致风流的高级娼寮<span
        class="tip"
        >（另有城西白马寺里巷和城东小市糖水巷）</span
      >。而其所受青睐之因，在于这里不仅有白皙婉约的鲜卑佳丽，还有善歌妙舞的东胡美女。
    </p>
    <p>
      鹩儿巷的另一大特色，是这里高度系统化的商业模式。它的幕后老板，有说是琅琊王的<span
        class="tip"
        >（太子党）</span
      >，也有人说是赵王<span class="tip">（皇后党）</span
      >。鹩儿巷的门槛主要在于礼节繁琐，这里有一套完整的隐语体系和行为准则，一旦言行失误，则被视为乡野村夫，非但会招致耻笑，还会被人千方百计地掏空钱袋。<span
        class="desc"
        @click="handlePaper(1)"
        >【碎片*】</span
      >
    </p>
    <p>四夷坊内不止有鹩儿巷，更有诸多下品娼寮，被狎客们统称为腌肉庄。</p>

    <h4>四通市</h4>
    <p>
      位于四夷坊北部，是洛阳八大集市之一<span class="tip"
        >（四通市，大市，东市，金市，鬼市，白马寺集，七里桥集，东华门集）</span
      >，由于四夷坊人多，所以从某种意义上说，四通市就是洛阳的江湖，是消息最灵通的所在。
      <span class="desc" @click="handlePaper(2)">【碎片*】</span>
    </p>
    <p>
      四通市又叫胡人集，因为这里是胡人商队的聚集所，胡人商队里，粟特国商队是最有牌面的，他们就像中古版本的犹太人，拥有遍布全球的商业网络，东至洛阳，西至君士坦丁堡，只要找他们，就没有买不到的东西。
    </p>
    <h4>吴人坊</h4>
    <p>
      吴人坊里有几个大户，建邺刘氏<span class="tip">（渔帮）</span
      >，会稽王氏<span class="tip">（拐子帮）</span>，江东陆氏<span class="tip"
        >（名士家族）</span
      >。江东陆氏和其他两家的区别在于辐射范围不同，两者不在一个层面上。所以无论陆小乙如何乱搞，他在吴人坊里永远都有光环。
    </p>
    <h4>学坊</h4>
    <p>
      学坊在洛水河北岸，四夷坊在南岸，它们就像洛阳的两面，一个是象牙塔，一个是修罗场。学坊士子把洛水河上的「永康桥」称作「两界桥」，走没走过两界桥，去没去过四夷坊，是成年人和小朋友的区别。
    </p>
  </article>
  <Modal ref="S8Modal" />
  <Tools />
</template>
<script setup>
import Modal from "../Modal.vue";
import Tools from "./Tools.vue";
import * as PAPER from "./Paper.js";
import { ref } from "vue";
const S8Modal = ref(null);

function handlePaper(index) {
  const data = PAPER[`S${8}_PAPER`][parseInt(index)];
  S8Modal.value.openModal(data.paras); // 调用子组件方法
}
</script>
