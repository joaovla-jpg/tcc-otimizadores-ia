# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com este projeto! Este documento fornece diretrizes para contribuições.

## 📋 Como Contribuir

### 1. Reportar Bugs

Se encontrar um bug, abra uma [Issue](https://github.com/jvictorlima/tcc-otimizadores-ia/issues) com:

- **Título claro:** Ex: "Erro na função de Hessiana quando x=0"
- **Descrição detalhada:** Passos para reproduzir o erro
- **Ambiente:** Versão do Python, SO, etc
- **Código de exemplo:** Mínimo necessário para reproduzir

### 2. Sugerir Melhorias

Abra uma [Issue](https://github.com/jvictorlima/tcc-otimizadores-ia/issues) com:

- **Motivação:** Por que essa melhoria é útil?
- **Proposta:** Como implementá-la?
- **Alternativas:** Outras abordagens consideradas?

### 3. Contribuir com Código

1. **Fork** o repositório
2. Crie uma **branch** descritiva:
   ```bash
   git checkout -b feature/adiciona-adam-optimizer
   ```
3. Faça suas alterações
4. **Teste** seu código:
   ```bash
   python -m pytest tests/
   ```
5. **Commit** com mensagens claras:
   ```bash
   git commit -m "Adiciona implementação do otimizador Adam"
   ```
6. **Push** para seu fork:
   ```bash
   git push origin feature/adiciona-adam-optimizer
   ```
7. Abra um **Pull Request**

## 📝 Estilo de Código

- **PEP 8:** Siga as convenções de estilo Python
- **Docstrings:** Documente todas as funções
- **Type hints:** Use quando apropriado
- **Comentários:** Explique o "porquê", não o "como"

### Exemplo:

```python
def calcular_gradiente(ponto: np.ndarray) -> np.ndarray:
    """
    Calcula o gradiente da função de Rosenbrock.
    
    Args:
        ponto: Ponto (x, y) onde calcular o gradiente.
        
    Returns:
        Vetor gradiente [∂f/∂x, ∂f/∂y].
        
    Raises:
        ValueError: Se ponto não tiver dimensão 2.
    """
    if ponto.shape[0] != 2:
        raise ValueError("Ponto deve ter dimensão 2")
    
    x, y = ponto
    df_dx = -2*(1 - x) - 400*x*(y - x**2)
    df_dy = 200*(y - x**2)
    
    return np.array([df_dx, df_dy])
```

## 🧪 Testes

- Adicione testes para novas funcionalidades
- Mantenha cobertura de código > 80%
- Use `pytest` para rodar testes:

```bash
pip install pytest
python -m pytest tests/ -v
```

## 📚 Documentação

- Atualize o `README.md` se necessário
- Adicione exemplos de uso
- Documente parâmetros e retornos

## 🎯 Áreas para Contribuição

### Implementação de Novos Otimizadores

- [ ] BFGS (Broyden-Fletcher-Goldfarb-Shanno)
- [ ] L-BFGS (Limited-memory BFGS)
- [ ] Adam (Adaptive Moment Estimation)
- [ ] RMSprop
- [ ] Adagrad

### Novas Funções de Benchmark

- [ ] Função de Himmelblau
- [ ] Função de Rastrigin
- [ ] Função Sphere
- [ ] Função de Ackley

### Melhorias

- [ ] Suporte a Rosenbrock N-dimensional
- [ ] Testes unitários completos
- [ ] Interface CLI (argparse)
- [ ] Logging estruturado
- [ ] Paralelização de experimentos

### Visualização

- [ ] Gráficos interativos (Plotly)
- [ ] Animações de trajetórias
- [ ] Dashboard web (Streamlit)

## 💬 Comunicação

- **Issues:** Para bugs e sugestões
- **Pull Requests:** Para contribuições de código
- **Discussions:** Para perguntas gerais
- **Email:** joao.victor@discente.ufma.br

## 📜 Código de Conduta

Este projeto segue o [Contributor Covenant](https://www.contributor-covenant.org/). Seja respeitoso e inclusivo.

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [Licença MIT](LICENSE).

---

**Obrigado por contribuir! 🎉**
