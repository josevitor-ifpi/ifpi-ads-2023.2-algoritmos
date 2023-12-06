class Processo {
    constructor(nome, tempoExecucao) {
      this.nome = nome
      this.tempoExecucao = tempoExecucao
    }
  }
  
  function roundRobin(processos, quantum) {
    let tempoTotal = 0
    let fila = [...processos]
  
    while (fila.length > 0) {
      const processoAtual = fila.shift()
      const tempoExecucaoAtual = Math.min(quantum, processoAtual.tempoExecucao)
  
      console.log(`Executando ${processoAtual.nome} por ${tempoExecucaoAtual} unidades de tempo.`)
  
      tempoTotal += tempoExecucaoAtual
      processoAtual.tempoExecucao -= tempoExecucaoAtual
  
      if (processoAtual.tempoExecucao > 0) {
        fila.push(processoAtual) // Processo ainda não concluído, adiciona de volta à fila
      }
    }
  
    console.log(`Tempo total de execução: ${tempoTotal}`)
    console.log(`${tempoTotal/processos.length}`)
  }
  
  // Exemplo de uso
  const processos = [
    new Processo('P1', 10),
    new Processo('P2', 30),
    new Processo('P3', 20),
    new Processo('P4', 40)
  ]
  
  const quantum = 15
  
  roundRobin(processos, quantum)
  