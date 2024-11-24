<template>
  <Layout :loading="loading">
    <h2>Подходящие пары для особи {{ currentCow }}</h2>
    <br />
    <PartnerCard v-for="option in options" :key="option.id" :cow="option" />
  </Layout>
</template>

<script setup>
import PartnerCard from '@/components/PartnerCard.vue'
import Layout from '@/layouts/Layout.vue'
import { ref, computed, onMounted } from 'vue'

const loading = ref(true)
const currentCow = ref(localStorage.getItem('selectedCow'))
const options = ref()

onMounted(() => {
  setTimeout(() => {
    options.value = getOptions()
    loading.value = false
  }, 3000)
})

const getOptions = () => {
  if(localStorage.getItem('selectedCow') === '1895') {
    return options1
  } else if(localStorage.getItem('selectedCow') === '2468') {
    return options2
  } else if(localStorage.getItem('selectedCow') === '3555') {
    return options3
  }
}

const options1 = [
  {
    id: 9023,
    score: 84.006767
  },
  {
    id: 3569,
    score: 84.006767
  },
  {
    id: 1173,
    score: 84.006767
  },
  {
    id: 6455,
    score: 84.006615
  },
  {
    id: 1225,
    score: 84.006615
  },
]

const options2 = [
  {
    id: 9023,
    score: 92.011345
  },
  {
    id: 3569,
    score: 92.011345
  },
  {
    id: 1173,
    score: 92.011345
  },
  {
    id: 6455,
    score: 92.011192
  },
  {
    id: 1225,
    score: 92.011192
  },
]

const options3 = [
  {
    id: 9023,
    score: 87.511086
  },
  {
    id: 3569,
    score: 87.511086
  },
  {
    id: 1173,
    score: 87.511086
  },
  {
    id: 6455,
    score: 87.510918
  },
  {
    id: 1225,
    score: 87.510918
  },
]

</script>
