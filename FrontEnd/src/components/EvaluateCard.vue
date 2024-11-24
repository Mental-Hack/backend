<template>
  <el-card class="card">
    <header>
      <p>ID особи: {{ cow.id }}</p>
      <p v-if="cow.weight">Прирост веса кг/день: {{ cow.weight}}</p>
      <p v-if="cow.health">Здоровье: {{ cow.health }}</p>
      <p v-if="cow.value">Генетическая ценность: {{ cow.value }}</p>
      <p v-if="cow.fatness">Упитанность: {{ cow.fatness }}</p>
      <p v-if="cow.f">Коэффициент инбридинга (F): {{ cow.f }}</p>
    </header>
  </el-card>
</template>

<script setup>
const props = defineProps({
  cow: {
    type: Object,
    required: true
  },
})
</script>