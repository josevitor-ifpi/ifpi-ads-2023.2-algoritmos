// Definindo a classe Banqueiro
class Banqueiro {
    constructor(recursosDisponiveis, processos) {
      this.recursosDisponiveis = recursosDisponiveis.slice(); // Copia dos recursos disponíveis
      this.recursosMaximos = processos.map(p => p.recursosMaximos.slice()); // Copia dos recursos máximos necessários para cada processo
      this.recursosAlocados = processos.map(p => p.recursosAlocados.slice()); // Copia dos recursos já alocados para cada processo
      this.recursosNecessarios = processos.map(p => p.recursosNecessarios.slice()); // Copia dos recursos necessários para cada processo
      this.processosConcluidos = processos.map(() => false); // Inicialmente nenhum processo concluído
    }
  
    // Verifica se é seguro alocar recursos para um determinado processo
    isAlocacaoSegura(processo) {
      for (let i = 0; i < this.recursosDisponiveis.length; i++) {
        if (this.recursosNecessarios[processo][i] > this.recursosDisponiveis[i]) {
          return false;
        }
      }
      return true;
    }
  
    // Aloca recursos para um determinado processo
    alocarRecursos(processo) {
      if (!this.processosConcluidos[processo] && this.isAlocacaoSegura(processo)) {
        // Alocar recursos
        for (let i = 0; i < this.recursosDisponiveis.length; i++) {
          this.recursosDisponiveis[i] += this.recursosAlocados[processo][i];
          this.recursosAlocados[processo][i] = 0;
          this.recursosMaximos[processo][i] = 0;
          this.recursosNecessarios[processo][i] = 0;
        }
        this.processosConcluidos[processo] = true;
        return true;
      }
      return false;
    }
  
    // Executa o algoritmo Banqueiro
    executarAlgoritmo() {
      let processoConcluido;
      do {
        processoConcluido = false;
        for (let i = 0; i < this.processosConcluidos.length; i++) {
          if (!this.processosConcluidos[i] && this.isAlocacaoSegura(i)) {
            this.alocarRecursos(i);
            processoConcluido = true;
          }
        }
      } while (processoConcluido);
    }
  }
  
  // Exemplo de uso
  const recursosDisponiveis = [2, 1, 0, 0];
  const processos = [
    { recursosMaximos: [7, 5, 3], recursosAlocados: [0, 0, 1, 0], recursosNecessarios: [2, 0, 0, 1] },
    { recursosMaximos: [3, 2, 2], recursosAlocados: [2, 0, 0, 1], recursosNecessarios: [1, 0, 1, 0] },
    { recursosMaximos: [9, 0, 2], recursosAlocados: [0, 1, 2, 0], recursosNecessarios: [2, 1, 0, 0] }
  ];
  
  const banqueiro = new Banqueiro(recursosDisponiveis, processos);
  banqueiro.executarAlgoritmo();
  
  // Verifica se todos os processos foram concluídos
  const todosConcluidos = banqueiro.processosConcluidos.every(concluido => concluido);
  console.log("Todos os processos foram concluídos:", todosConcluidos);
