<template>
  <div class="loader"
        v-loading="loading">
    <div class="container" v-if="centered">
      <slot />
    </div>
    <main v-else>
      <slot />
    </main>
  </div>
</template>

<script setup>
defineProps(['centered', 'loading'])
</script>

<style>
.container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 500px;
  padding: 20px 20px 30px;
}
</style>