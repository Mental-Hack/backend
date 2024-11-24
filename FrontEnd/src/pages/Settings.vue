<template>
  <Layout :centered="true">
  <h1 v-if="isAdmin">Добавить новую особь</h1>
  <h1 v-else>Выберите признаки для отбора</h1>
  <br />
  <el-form :model="form" label-width="auto">
    <div v-if="isAdmin">
    <div class="input-wrapper">
      <span>ID особи</span>
      <el-input v-model="form.id"/>
    </div>
    <br />

    <div class="input-wrapper">
      <span>Пол</span>
      <el-select
        v-model="form.sex"
        size="large"
        placeholder="Пол животного"
      >
        <el-option
          v-for="item in sexOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
    </div>
    <br />

    <div class="input-wrapper">
      <span>Удой</span>
      <el-input v-model="form.milk" placeholder="Удой л/день"/>
      <!-- <el-slider v-model="form.milk" :format-tooltip="formatTooltip" /> -->
    </div>
    <br />
    </div>

    <div class="input-wrapper" v-else>
      <span class="demonstration">Отбор по признакам</span>
      <el-select
      v-model="value"
      placeholder="Укажите признак"
      size="large"
      multiple
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
    </div>

    <el-button v-if="isAdmin" class="green-button large-button" type="success" @click="onSubmit" :disabled="disabled">Добавить особь</el-button>
    <el-button v-else class="green-button large-button" type="success" @click="onSubmit">Поиск</el-button>
  </el-form>
</Layout>
</template>

<script setup>
import Layout from '@/layouts/Layout.vue';
import { ElNotification } from 'element-plus'
import { reactive, ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isAdmin = ref(false)
const disabled = ref(true)

onMounted(() => {
  if(localStorage.getItem('isAdmin')) {
    isAdmin.value = true
  }
})


const form = reactive({
  id: '',
  sex: '',
  milk: ''
})

const sexOptions = [
    {
      value: 'Самец'
    },
    {
      value: 'Самка'
    }
  ]

watch(form, (newVal) => {
  if(newVal.milk < 0 || newVal.milk > 120) {
    disabled.value = false
    ElNotification({
      title: 'Пожалуйста, укажите корректное значение поля. Удой не может быть отрицательным или быть больше 120 л/день',
      duration: 3000
    })
  }
  if(newVal.id && newVal.sex) {
    disabled.value = false
  } else {
    disabled.value = true
  }
})

const value = ref('')

const options = [
  {
    value: 'firtility',
    label: 'Фертильность',
  },
  {
    value: 'weight',
    label: 'Прирост веса',
  },
  {
    value: 'health',
    label: 'Здоровье',
  },
  {
    value: 'index',
    label: 'Коэффициент инбридинга',
  },
  {
    value: 'fantess',
    label: 'Упитанность',
  },
  {
    value: 'milk',
    label: 'Удой',
  },
  {
    value: 'value',
    label: 'Генетическая ценность',
  },
]

const formatTooltip = (val) => {
  return val
}

const formatTooltipFatness = (val) => {
  return val / 10
}

const formatTooltipIndex = (val) => {
  return val / 100
}

const handleChange = (value) => {
  console.log(value)
}


const onSubmit = () => {
  router.push({name: 'home'})
}
</script>

<style>
.el-input-number {
  width: 100%;
}
.input-wrapper {
  display: flex;
  flex-direction: column;
}
</style>