<template>
  <Layout :loading="loading">
    <h2>Лучшее соотношение молока/мяса</h2>
    <br />
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="id" label="ID особи" />
      <el-table-column prop="value" label="Удой л/день"/>
      <el-table-column prop="weight" label="Прирост веса кг/день"/>
      <el-table-column prop="rank" label="Ранг"/>
    </el-table>
    <br />
    <a class="green-button large-button" v-if="showButton" type="success" href="https://etl.spb.ru/milk_meat_full.csv" download>
      Скачать данные по всей ферме
    </a>
  </Layout>
</template>

<script lang="ts" setup>
import Layout from '@/layouts/Layout.vue'
import {onMounted, ref} from 'vue'

const loading = ref(true)
const data = ref()
const showButton = ref(false)

onMounted(() => {
  setTimeout(() => {
    loading.value = false
    showButton.value = true
    data.value = tableData
  }, 2000)
})

const tableData = [
  {
    id: 5427,
    value: 21.3,
    weight: 1.26,
    rank: 1.0
  },
  {
    id: 9114,
    value: 30.5,
    weight: 1.42,
    rank: 2.0
  },
  {
    id: 4752,
    value: 29.5,
    weight: 0.81,
    rank: 3.0
  },
  {
    id: 5718,
    value: 30.9,
    weight: 1.06,
    rank: 4.0
  },
  {
    id: 2796,
    value: 37.4,
    weight: 0.84,
    rank: 5.0
  },
]
</script>