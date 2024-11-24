<template>
  <Layout :centered="true">
    <img class="logo" src="/cow.png" />
    <h1>Cattle Cupid</h1>
    <el-button class="green-button" type="success" @click="handleLogin">breeding automation</el-button>
  </Layout>
</template>

<script setup>
import Layout from '@/layouts/Layout.vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const handleLogin = () => {
  router.push({name: 'login'})
}
</script>

<style lang="sass" scoped>
p
  text-align: center

.logo
  margin-top: 20px
  width: 100%
  height: 160px
  object-fit: contain
</style>