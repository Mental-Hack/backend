<template>
  <main>
    <h2>Результаты поиска по запросу: лучшая производительность</h2>
    <br />
    <CowCard v-for="option in options" :key="option.id" :cow="option" />
  </main>
</template>

<script setup>
import CowCard from '@/components/CowCard.vue'

const options = [
  {
    id: 1111,
    score: 4
  },
  {
    id: 2222,
    score: 4
  },
  {
    id: 3222,
    score: 4
  },
  {
    id: 43333,
    score: 4
  },
  {
    id: 5444,
    score: 4
  },
  {
    id: 6555,
    score: 4
  },
]
</script>