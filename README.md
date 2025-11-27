# 🧠 Análise Computacional da Convergência de Otimizadores de IA

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-green.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Trabalho de Conclusão de Curso (TCC)**  
> **Universidade Federal do Maranhão (UFMA)**  
> **Bacharelado Interdisciplinar em Ciência e Tecnologia**  
> **Autor:** João Victor Lima Azevedo  
> **Orientador:** Prof. Dr. Jadevilson Cruz Ribeiro

---

## 📋 Sobre o Projeto

Este projeto implementa e compara empiricamente dois algoritmos fundamentais de otimização matemática aplicados a problemas de Inteligência Artificial:

- **Gradiente Descendente (GD)** - Método de primeira ordem
- **Newton-Raphson (NR)** - Método de segunda ordem

### 🎯 Objetivo

Investigar quantitativamente as diferenças de **velocidade**, **eficiência** e **robustez** entre os métodos usando a **Função de Rosenbrock** como benchmark.

### 🏆 Resultado Principal

**Newton-Raphson foi 798x mais rápido** que Gradiente Descendente, convergindo em apenas **6 iterações** versus **32.076 iterações**.

---

## 📊 Resultados Visuais

### Superfície 3D com Trajetórias
![Superfície 3D](docs/images/preview_3d.png)
*Gradiente Descendente (vermelho) faz zig-zag; Newton-Raphson (azul) segue direto ao mínimo*

### Comparação de Desempenho
| Métrica | Gradiente Descendente | Newton-Raphson | Vantagem NR |
|---------|----------------------|----------------|-------------|
| **Iterações** | 32.076 | 6 | **5.346x** |
| **Tempo Total** | 214.79 ms | 0.27 ms | **798x** ⚡ |
| **Erro Final** | 2.50×10⁻⁶ | 1.89×10⁻¹¹ | **10.000x** |
| **Custo/Iteração** | 6.70 μs | 44.83 μs | 6.7x mais caro |

---

## 🚀 Início Rápido

### Pré-requisitos

```bash
Python 3.8+
```

### Instalação

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/tcc-otimizadores-ia.git
cd tcc-otimizadores-ia

# Instale as dependências
pip install -r requirements.txt
```

### Executar

```bash
# Rodar TUDO (experimentos + gráficos)
python executar_completo.py

# Ou rodar apenas os experimentos
python src/experiments.py

# Ou gerar apenas os gráficos (se já tem dados)
python src/visualization.py
```

### Saída

```
results/
├── data/
│   └── resultados_experimentos.json
└── plots/
    ├── grafico_1_superficie_3d.png
    ├── grafico_2_curvas_nivel.png
    ├── grafico_3_convergencia.png
    ├── grafico_4_comparacao_desempenho.png
    └── grafico_5_sensibilidade_alpha.png
```

---

## 📁 Estrutura do Projeto

```
tcc-otimizadores-ia/
│
├── README.md                      # Este arquivo
├── requirements.txt               # Dependências Python
├── LICENSE                        # Licença MIT
├── .gitignore                     # Arquivos ignorados pelo Git
│
├── executar_completo.py           # 🎯 SCRIPT PRINCIPAL
│
├── src/                           # Código-fonte
│   ├── __init__.py
│   ├── rosenbrock.py              # Função de teste + derivadas
│   ├── optimizers.py              # Implementação GD e NR
│   ├── experiments.py             # 4 experimentos do TCC
│   └── visualization.py           # Geração de gráficos
│
├── docs/                          # Documentação
│   ├── TCC_Completo.pdf           # (Opcional) PDF do TCC
│   └── images/                    # Imagens de exemplo
│
├── results/                       # Resultados (criado automaticamente)
│   ├── data/                      # Dados JSON
│   └── plots/                     # Gráficos PNG
│
└── tests/                         # (Futuro) Testes unitários
    └── test_rosenbrock.py
```

---

## 🧪 Experimentos Implementados

### Experimento 1: Convergência Básica
Compara comportamento padrão dos dois métodos partindo de `(-1.2, 1.0)`.

**Resultado:** NR converge em 6 iterações vs GD em 32.076.

### Experimento 2: Sensibilidade ao Learning Rate
Testa GD com 6 valores de α ∈ `{0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1}`.

**Resultado:** Apenas α=0.001 converge adequadamente; valores fora dessa janela divergem ou são lentos.

### Experimento 3: Robustez a Pontos Iniciais
Avalia convergência de 5 pontos iniciais diferentes.

**Resultado:** NR converge de todos (100%); GD falha em 1 ponto (80%).

### Experimento 4: Trade-off Computacional
Mede tempo de execução com precisão.

**Resultado:** NR 6.7x mais caro por iteração, mas 798x mais rápido no total.

---

## 📈 Gráficos Gerados

### 1. Superfície 3D (`grafico_1_superficie_3d.png`)
Superfície tridimensional da função de Rosenbrock com trajetórias dos algoritmos.

### 2. Curvas de Nível (`grafico_2_curvas_nivel.png`)
Vista superior evidenciando o "zig-zag" do GD vs caminho direto do NR.

### 3. Convergência (`grafico_3_convergencia.png`)
Análise quantitativa: erro e valor da função vs iteração (escala log).

### 4. Comparação de Desempenho (`grafico_4_comparacao_desempenho.png`)
4 subplots comparando iterações, tempo, erro e custo por iteração.

### 5. Sensibilidade ao α (`grafico_5_sensibilidade_alpha.png`)
Mostra janela estreita de valores de α que funcionam para GD.

---

## 🔬 Metodologia

### Função de Teste: Rosenbrock

```python
f(x, y) = (1 - x)² + 100(y - x²)²
```

- **Mínimo global:** `(1, 1)` com `f(1,1) = 0`
- **Característica:** Vale estreito e curvo ("banana valley")
- **Número de condição:** κ ≈ 2500 (mal condicionado)

### Implementação

- **Linguagem:** Python 3.8+
- **Bibliotecas:** NumPy, Matplotlib
- **Abordagem:** Implementação *from scratch* (sem bibliotecas prontas de otimização)
- **Derivadas:** Analíticas (não numéricas)

### Critério de Convergência

```python
||∇f(x)|| < 10⁻⁶  ou  max_iterações atingido
```

---

## 📚 Fundamentação Teórica

### Gradiente Descendente

```python
x_{k+1} = x_k - α·∇f(x_k)
```

- **Taxa de convergência:** Linear (geométrica)
- **Custo por iteração:** O(n)
- **Vantagem:** Simples, baixo custo
- **Desvantagem:** Convergência lenta, sensível a α

### Newton-Raphson

```python
H(x_k)·d = -∇f(x_k)
x_{k+1} = x_k + d
```

- **Taxa de convergência:** Quadrática
- **Custo por iteração:** O(n³)
- **Vantagem:** Convergência dramática
- **Desvantagem:** Caro computacionalmente, requer Hessiana

---

## 🎓 Conclusões

### 3 Insights Fundamentais

1. **Convergência Quadrática é Poderosa**  
   798x de vantagem não é marginal - é transformacional.

2. **Curvatura Vale o Custo**  
   6.7x mais caro por iteração, mas 5.346x menos iterações = vantagem líquida massiva.

3. **Contexto Determina Escolha**  
   - **Use NR:** Baixa dimensão (n < 1000), Hessiana tratável, precisão crítica
   - **Use GD:** Alta dimensão (n > 1000), memória limitada, Deep Learning

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação
- **NumPy 1.24+** - Computação numérica
- **Matplotlib 3.7+** - Visualização de dados
- **JSON** - Armazenamento de resultados

---

## 🤝 Como Contribuir

1. Fork este repositório
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. Push para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

### Ideias para Contribuição

- [ ] Implementar métodos Quasi-Newton (BFGS, L-BFGS)
- [ ] Adicionar otimizadores modernos (Adam, RMSprop)
- [ ] Estender para Rosenbrock N-dimensional
- [ ] Testar em problemas reais de ML
- [ ] Adicionar testes unitários
- [ ] Criar interface web interativa

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**João Victor Lima Azevedo**

- GitHub: [@jvictorlima](https://github.com/jvictorlima)
- LinkedIn: [linkedin.com/in/joaovictorlima](https://linkedin.com/in/joaovictorlima)
- Email: joao.victor@discente.ufma.br

**Orientador:** Prof. Dr. Jadevilson Cruz Ribeiro  
**Instituição:** Universidade Federal do Maranhão (UFMA)  
**Curso:** Bacharelado Interdisciplinar em Ciência e Tecnologia  
**Ano:** 2025

---

## 🙏 Agradecimentos

- Prof. Dr. Jadevilson Cruz Ribeiro pela orientação fundamental
- UFMA pelo suporte institucional
- Comunidade open-source (Python, NumPy, Matplotlib)

---

## 📖 Citação

Se você usar este código em sua pesquisa, por favor cite:

```bibtex
@misc{azevedo2025otimizadores,
  author = {Azevedo, João Victor Lima},
  title = {Análise Computacional da Convergência de Otimizadores de IA: 
           Newton-Raphson vs. Gradiente Descendente},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jvictorlima/tcc-otimizadores-ia}}
}
```

---

## 📞 Contato

Para dúvidas, sugestões ou colaborações, abra uma [Issue](https://github.com/jvictorlima/tcc-otimizadores-ia/issues) ou envie um email.

---

<div align="center">

**⭐ Se este projeto foi útil, deixe uma estrela! ⭐**

Desenvolvido com 💙 por [João Victor Lima Azevedo](https://github.com/jvictorlima)

</div>
