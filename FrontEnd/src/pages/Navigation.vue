<template>
  <Layout :centered="true">
    <h1>Выберите действие</h1>
  <br />
  <br />
    <el-button class="green-button large-button" type="success" @click="handleFindAnimal">
      Найти пару
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleShowAssay" >
      Посмотреть анализ по ферме
    </el-button>
  </Layout>
</template>

<script setup>
import { useRouter } from "vue-router"
import Layout from '@/layouts/Layout.vue'

const router = useRouter()
const handleFindAnimal = () => {
  router.push({name: 'cows'})
}

const handleShowAssay = () => {
  router.push({name: 'info'})
}
</script>