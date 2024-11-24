<template>
  <el-card class="card">
    <header>
      <p>{{ cow.id }}</p>
    </header>
    <p>score: {{ cow.score }}</p>
    <!-- <el-rate v-model="cow.score"  disabled /> -->
  </el-card>
</template>

<script setup>
import { ref } from 'vue'

const checked1 = ref(false)

const props = defineProps({
  cow: {
    type: Object,
    required: true
  },
  choice: {
    type: Boolean,
    default: true
  }
})
</script>

<style scoped lang="sass">
header
  display: flex
  align-items: center

</style>