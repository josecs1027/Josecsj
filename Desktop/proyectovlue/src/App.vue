<template>
  <CalculatorView
    :model="model"
    :controller="controller"
  />
</template>

<script setup>
import CalculatorView from './views/CalculatorView.vue'
import { useCalculatorModel } from './models/calculatorModel'
import { useCalculatorController } from './controllers/calculatorController'

const model = useCalculatorModel()
const controller = useCalculatorController(model)
</script>
