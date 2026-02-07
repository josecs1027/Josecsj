<template>
  <div class="calculator">
    <h1>Calculadora MVC</h1>

    <input type="number" v-model.number="model.num1" />
    <input type="number" v-model.number="model.num2" />

    <div class="buttons">
      <button @click="controller.sumar">+</button>
      <button @click="controller.restar">−</button>
      <button @click="controller.multiplicar">×</button>
      <button @click="controller.dividir">÷</button>
    </div>

    <h2>Resultado: {{ model.result }}</h2>
  </div>
</template>

<script setup>
defineProps({
  model: Object,
  controller: Object
})
</script>

<style scoped>
.calculator {
  max-width: 320px;
  margin: 40px auto;
  padding: 20px;
  background: #f4f4f4;
  border-radius: 10px;
  text-align: center;
}
input {
  width: 100%;
  margin: 5px 0;
  padding: 8px;
}
.buttons {
  display: flex;
  justify-content: space-between;
}
button {
  width: 22%;
  padding: 10px;
}
</style>
