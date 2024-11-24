<template>
  <main>
    <h1>Выберите животное, для которого необходимо подобрать пару</h1>
  <br />
  <ul style="overflow: auto">
    <li v-for="option in options" :key="option.id" class="infinite-list-item">
      <CowCard :cow="option" :choice="true" @action="getCowId" />
    </li>
  </ul>
  <el-button class="green-button large-button" type="success" @click="handleResult" >
      Найти пару
    </el-button>
  </main>
</template>

<script setup>
import CowCard from '@/components/CowCard.vue';
import { useRouter } from 'vue-router';

const getCowId = (id) => {
  localStorage.setItem('selectedCow', id)
}

const router = useRouter()

const handleResult = () => {
  router.push({name: 'match'})
}

const options = [
  {
    id: 1895,
    description: 'Лучшее совпадение',
    rate: 5,
  },
  {
    id: 2468,
    description: 'Тоже хорошее совпадение',
    rate: 4.5
  },
  {
    id: 3555,
    description: 'Тут какая-то полезная инфа',
    rate: 4.2
  },
]
</script>