<template>
  <Layout :centered="false" :loading="loading">
    <h2>Развернутый анализ</h2>
    <br />
    <el-select
      v-model="value"
      placeholder="Выберите id особи"
      size="large"
      @change="handleSelect"
    >
      <el-option
        v-for="item in options"
        :key="item.id"
        :label="item.id"
        :value="item.id"
      />
    </el-select>
    <br />
    <br />
      <EvaluateCard :cow="option" v-if="option" />
    <a class="green-button large-button" type="success" v-if="showButton" href="https://etl.spb.ru/farm_analysis.xlsx" download>
      Скачать файл по всей ферме
    </a>
  </Layout>
</template>

<script setup>
import EvaluateCard from '@/components/EvaluateCard.vue'
import Layout from '@/layouts/Layout.vue'
import {ref} from 'vue'

const loading = ref(false)
const showButton = ref(false)

const option = ref()

const handleSelect = (id) => {
  // option.value = {}

  loading.value = true
  setTimeout(() => {
    loading.value = false
    option.value = options.find(option => option.id === id)

    showButton.value = true
  }, 2000)
}

const options = [
  {
    id: 2017,
    weight: 9.065, // прирост веса
    health: null,
    value: null, //генетическая ценность
    fatness: null,
    f: null // коэффициент инбридинга
  },
  {
    id: 2427,
    weight: 6.57,
    health: 0.00,
    value: null, //генетическая ценность
    fatness: null,
    f: null // коэффициент инбридинга
  },
  {
    id: 4846,
    weight: null,
    health: null,
    value: 6.095, //генетическая ценность
    fatness: 0.000,
    f: -0.260 // коэффициент инбридинга
  },
]
</script>
