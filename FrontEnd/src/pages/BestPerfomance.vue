<template>
  <main>
    <h2>Результаты поиска по запросу: лучшая производительность</h2>
    <br />
    <ResultCard v-for="option in options" :key="option.ID" :cow="option" />
  </main>
</template>

<script setup>
import ResultCard from '@/components/ResultCard.vue'

const options = [
  {
    ID: 1111,
    Milk_Contribution: 'Milk Contribution',
    Meat_Contribution: 'Meat Contribution',
    Interaction_Effect: 'Interaction Effect',
    Rank: 'Rank'
  },
  {
    ID: 2222,
    Milk_Contribution: 'Milk_Contribution',
    Meat_Contribution: 'Meat_Contribution',
    Interaction_Effect: 'Interaction_Effect',
    Rank: 'Rank'
  },
  {
    ID: 3222,
    Milk_Contribution: 'Milk_Contribution',
    Meat_Contribution: 'Meat_Contribution',
    Interaction_Effect: 'Interaction_Effect',
    Rank: 'Rank'
  },
  {
    ID: 43333,
    Milk_Contribution: 'Milk_Contribution',
    Meat_Contribution: 'Meat_Contribution',
    Interaction_Effect: 'Interaction_Effect',
    Rank: 'Rank'
  },
  {
    ID: 5444,
    Milk_Contribution: 'Milk_Contribution',
    Meat_Contribution: 'Meat_Contribution',
    Interaction_Effect: 'Interaction_Effect',
    Rank: 'Rank'
  },
  {
    ID: 6555,
    Milk_Contribution: 'Milk_Contribution',
    Meat_Contribution: 'Meat_Contribution',
    Interaction_Effect: 'Interaction_Effect',
    Rank: 'Rank'
  },
]
</script>