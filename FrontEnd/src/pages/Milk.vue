<template>
  <Layout :loading="loading">
    <h2>Больше молока</h2>
    <br />
    <el-table :data="data" style="width: 100%">
      <el-table-column prop="id" label="ID особи" />
      <el-table-column prop="value" label="Удой л/день"/>
    </el-table>
    <br />
    <a class="green-button large-button" v-if="showButton" type="success" href="https://etl.spb.ru/farm_milk_analysis.xlsx" download>
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
    id: 6038,
    value: 7.840,
  },
  {
    id: 6804,
    value: 5.995,
  },
  {
    id: 508,
    value: 5.390,
  },
  {
    id: 6465,
    value: 5.175,
  },
  {
    id: 4094,
    value: 4.995,
  },
]
</script>