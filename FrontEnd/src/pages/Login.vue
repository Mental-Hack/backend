<template>
  <Layout>
    <h1>Здравствуйте, выберите вашу ферму и авторизуйтесь</h1>
    <br />
    <el-form :model="form" label-width="auto" style="max-width: 600px">
      <el-select
      v-model="form.farmName"
      placeholder="Выберите вашу ферму"
      size="large"
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
    <br />
    <br />
    <div class="input-wrapper">
      <label>Логин</label>
      <el-input v-model="form.login" />
    </div>
    <br />
    <div class="input-wrapper">
      <label>Пароль</label>
      <el-input v-model="form.password" type="password" show-password />
    </div>
    <br />
    <div>
      <el-switch class="switch" v-model="admin" />
      <label>Я администратор</label>
    </div>
    <br />
    <br />
    <el-button type="primary" class="green-button large-button" @click="onSubmit" :disabled="disabled">Авторизоваться</el-button>
    </el-form>
  </Layout>
</template>

<script setup>
import Layout from '@/layouts/Layout.vue'
import {useRouter} from 'vue-router'
import { reactive, ref, watch, computed, onMounted } from 'vue'

const router = useRouter()
const disabled = ref(true)

const admin = ref(false)

onMounted(() => {
  localStorage.removeItem('isAdmin')
})

watch(admin, (newVal) => {
  if(newVal) {
    localStorage.setItem('isAdmin', true)
  } else {
    localStorage.setItem('isAdmin', false)
  }
})

const options = [
  {
    value: 'fan cows',
    label: 'Весёлые коровки',
  },
  {
    value: 'meat',
    label: 'Мясное раздолье',
  },
]

const form = reactive({
  farmName: '',
  login: '',
  password: '',
})

watch(form, (newVal) => {
  if(newVal.farmName && newVal.login && newVal.password.length >= 6) {
    disabled.value = false
  } else {
    disabled.value = true
  }
})

const onSubmit = () => {
  router.push({name: 'control'})
}
</script>

<style lang="sass">
.switch
  margin-right: 10px

.form
  position: relative
  z-index: 2

.icon
  position: absolute
  top: 0
  right: 20px
  z-index: 1
</style>