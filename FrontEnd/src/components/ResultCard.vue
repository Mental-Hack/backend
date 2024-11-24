<template>
  <el-card class="card">
    <header>
      <p>id: {{ cow.ID }}</p>
      <p>milk: {{ cow.Milk_Contribution }}</p>
      <p>meat: {{ cow.Meat_Contribution }}</p>
      <p>interaction effect: {{ cow.Interaction_Effect }}</p>
      <p>rank: {{ cow.Rank }}</p>
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