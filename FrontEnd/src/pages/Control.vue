<template>
  <Layout :centered="true">
    <h1>Выберите действие</h1>
  <br />
  <br />
    <el-button class="green-button large-button" type="success" @click="handleSettings">
      Добавление новых данных
    </el-button>
    <el-button class="green-button large-button" type="success" @click="handleWorkCurrentBase" >
      Работать с текущей базой данных
    </el-button>
  </Layout>
</template>

<script setup>
import Layout from '@/layouts/Layout.vue'
import {useRouter} from 'vue-router'

const router = useRouter()
const handleSettings = () => {
  router.push({name: 'settings'})
}

const handleWorkCurrentBase = () => {
  router.push({name: 'home'})
}
</script>