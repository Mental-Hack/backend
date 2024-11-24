<template>
  <Layout :loading="loading">
    <h2>Больше мяса</h2>
    <br />
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="id" label="ID особи" />
      <el-table-column prop="value" label="Прирост веса кг/день"/>
    </el-table>
    <br />
    <a class="green-button large-button" v-if="showButton" type="success" href="https://etl.spb.ru/farm_meat_analysis.xlsx" download>
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
    data.value = tableData
    showButton.value = true
  }, 2000)
})

const tableData = [
  {
    id: 5152,
    value: 8.35,
  },
  {
    id: 3330,
    value: 7.61,
  },
]
</script>