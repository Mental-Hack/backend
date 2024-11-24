<template>
  <el-card class="card" @click="emit('action', cow.id)">
    <header>
      <el-checkbox v-if="choice" class="header-checkbox" v-model="checked1" size="large" />
      <p>{{ cow.id }}</p>
    </header>
    <!-- <p>{{ cow.description }}</p>
    <el-rate v-model="cow.rate"  disabled /> -->
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
  },
  action: {
    type: Function
  }
})
const emit = defineEmits(['action'])
</script>

<style scoped lang="sass">
header
  display: flex
  align-items: center


.header-checkbox
  margin-right: 10px

</style>