import { reactive } from 'vue'

export function useCalculatorModel() {
  return reactive({
    num1: 0,
    num2: 0,
    result: 0
  })
}
