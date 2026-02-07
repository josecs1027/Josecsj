export function useCalculatorController(model) {

  const toNumber = (v) => isNaN(Number(v)) ? 0 : Number(v)

  const sumar = () => {
    model.result = toNumber(model.num1) + toNumber(model.num2)
  }

  const restar = () => {
    model.result = toNumber(model.num1) - toNumber(model.num2)
  }

  const multiplicar = () => {
    model.result = toNumber(model.num1) * toNumber(model.num2)
  }

  const dividir = () => {
    if (toNumber(model.num2) === 0) {
      model.result = 'Error: división entre 0'
    } else {
      model.result = toNumber(model.num1) / toNumber(model.num2)
    }
  }

  return {
    sumar,
    restar,
    multiplicar,
    dividir
  }
}
