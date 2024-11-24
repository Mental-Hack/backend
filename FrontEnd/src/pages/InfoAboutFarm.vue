<template>
  <Layout :centered="true">
    <h1>Посмотреть анализ по ферме</h1>
  <br />
  <br />
    <!-- <el-button class="green-button large-button" type="success" @click="handleResult" >
      Оценка генетического вклада в генотип
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleSearchBestPerfomance" >
      Выбрать лучшую производительность
    </el-button> -->
    <el-button class="green-button large-button" type="success" @click="handleResult" >
      Развернутый анализ
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleMilkPage" >
      Хочу больше молока
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleMeatPage" >
      Хочу больше мяса
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleMilkMeatPage" >
      Лучшее соотношение мясо/молоко
    </el-button>
  </Layout>
</template>

<script setup>
import { useRouter } from "vue-router"
import Layout from '@/layouts/Layout.vue'

const router = useRouter()

const handleResult = () => {
  router.push({name: 'evaluate'})
}

const handleMilkPage = () => {
  router.push({name: 'milk'})
}

const handleMeatPage = () => {
  router.push({name: 'meat'})
}

const handleMilkMeatPage = () => {
  router.push({name: 'correlation'})
}
</script>