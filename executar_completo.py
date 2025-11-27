#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXECUTAR COMPLETO - TCC Otimizadores de IA

Este script executa todo o pipeline do projeto:
1. Cria estrutura de diretórios
2. Executa os 4 experimentos
3. Gera todos os 5 gráficos
4. Salva dados em JSON

Autor: João Victor Lima Azevedo
TCC - UFMA - BICT - 2025
Orientador: Prof. Dr. Jadevilson Cruz Ribeiro
"""

import os
import sys
import json
import numpy as np
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar módulos
from rosenbrock import calcular_rosenbrock, calcular_gradiente, calcular_hessiana
from optimizers import executar_gradiente_descendente, executar_newton_raphson
from experiments import (
    executar_experimento_1,
    executar_experimento_2,
    executar_experimento_3,
    executar_experimento_4
)
from visualization import (
    gerar_grafico_superficie_3d,
    gerar_grafico_curvas_nivel,
    gerar_grafico_convergencia,
    gerar_grafico_comparacao_desempenho,
    gerar_grafico_sensibilidade_alpha
)


def criar_diretorios():
    """Cria estrutura de diretórios para resultados"""
    diretorios = [
        'results',
        'results/data',
        'results/plots'
    ]
    
    for dir_name in diretorios:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
    
    print("✅ Diretórios criados: results/data e results/plots")


def exibir_banner():
    """Exibe banner inicial"""
    print("=" * 80)
    print("🎓 TCC: ANÁLISE COMPUTACIONAL DE OTIMIZADORES DE IA")
    print("=" * 80)
    print()
    print("📚 Universidade Federal do Maranhão (UFMA)")
    print("👤 Autor: João Victor Lima Azevedo")
    print("🎯 Orientador: Prof. Dr. Jadevilson Cruz Ribeiro")
    print()
    print("=" * 80)
    print()


def executar_experimentos():
    """Executa todos os 4 experimentos"""
    print("🧪 EXECUTANDO EXPERIMENTOS")
    print("-" * 80)
    
    print("\n1️⃣  Experimento 1: Convergência Básica...")
    resultado_exp1_gd, resultado_exp1_nr = executar_experimento_1()
    print(f"   ✓ GD: {resultado_exp1_gd['iteracoes_totais']:,} iterações em {resultado_exp1_gd['tempo_total']*1000:.2f} ms")
    print(f"   ✓ NR: {resultado_exp1_nr['iteracoes_totais']:,} iterações em {resultado_exp1_nr['tempo_total']*1000:.2f} ms")
    speedup_iter = resultado_exp1_gd['iteracoes_totais'] / resultado_exp1_nr['iteracoes_totais']
    speedup_tempo = resultado_exp1_gd['tempo_total'] / resultado_exp1_nr['tempo_total']
    print(f"   🚀 Speedup: {speedup_iter:.1f}x iterações | {speedup_tempo:.0f}x tempo")
    
    print("\n2️⃣  Experimento 2: Sensibilidade ao Learning Rate...")
    resultado_exp2 = executar_experimento_2()
    num_convergiu = sum(1 for r in resultado_exp2['resultados'].values() if r['convergiu'])
    print(f"   ✓ Testados {len(resultado_exp2['valores_alpha'])} valores de α")
    print(f"   ✓ Convergiram: {num_convergiu}/{len(resultado_exp2['valores_alpha'])}")
    
    print("\n3️⃣  Experimento 3: Robustez a Pontos Iniciais...")
    resultado_exp3 = executar_experimento_3()
    print(f"   ✓ Testados {len(resultado_exp3['pontos_iniciais'])} pontos iniciais")
    gd_sucesso = sum(1 for r in resultado_exp3['resultados_gd'].values() if r['convergiu'])
    nr_sucesso = sum(1 for r in resultado_exp3['resultados_nr'].values() if r['convergiu'])
    print(f"   ✓ GD: {gd_sucesso}/{len(resultado_exp3['pontos_iniciais'])} sucesso ({gd_sucesso/len(resultado_exp3['pontos_iniciais'])*100:.0f}%)")
    print(f"   ✓ NR: {nr_sucesso}/{len(resultado_exp3['pontos_iniciais'])} sucesso ({nr_sucesso/len(resultado_exp3['pontos_iniciais'])*100:.0f}%)")
    
    print("\n4️⃣  Experimento 4: Trade-off Computacional...")
    resultado_exp4_gd, resultado_exp4_nr = executar_experimento_4()
    print(f"   ✓ GD médio: {resultado_exp4_gd['tempo_total_medio']*1000:.2f} ms ({resultado_exp4_gd['tempo_por_iteracao']*1e6:.2f} μs/iter)")
    print(f"   ✓ NR médio: {resultado_exp4_nr['tempo_total_medio']*1000:.2f} ms ({resultado_exp4_nr['tempo_por_iteracao']*1e6:.2f} μs/iter)")
    
    return {
        'exp1_gd': resultado_exp1_gd,
        'exp1_nr': resultado_exp1_nr,
        'exp2': resultado_exp2,
        'exp3': resultado_exp3,
        'exp4_gd': resultado_exp4_gd,
        'exp4_nr': resultado_exp4_nr
    }


def salvar_dados(resultados):
    """Salva dados dos experimentos em JSON"""
    print("\n💾 Salvando dados dos experimentos...")
    
    # Preparar dados para serialização (remover arrays numpy grandes)
    dados_completos = {
        'experimento_1': {
            'gd': {k: v for k, v in resultados['exp1_gd'].items() 
                   if k not in ['historico_trajetoria', 'valores_convergencia', 'normas_gradiente']},
            'nr': {k: v for k, v in resultados['exp1_nr'].items() 
                   if k not in ['historico_trajetoria', 'valores_convergencia', 'normas_gradiente']}
        },
        'experimento_2': resultados['exp2'],
        'experimento_3': resultados['exp3'],
        'experimento_4': {
            'gd': resultados['exp4_gd'],
            'nr': resultados['exp4_nr']
        }
    }
    
    # Converter arrays numpy para listas
    def converter_numpy(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {k: converter_numpy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [converter_numpy(item) for item in obj]
        else:
            return obj
    
    dados_completos = converter_numpy(dados_completos)
    
    # Salvar JSON
    with open('results/data/resultados_experimentos.json', 'w', encoding='utf-8') as f:
        json.dump(dados_completos, f, indent=2, ensure_ascii=False)
    
    print("   ✓ Dados salvos em results/data/resultados_experimentos.json")


def gerar_graficos(resultados):
    """Gera todos os gráficos"""
    print("\n" + "=" * 80)
    print("📊 GERANDO GRÁFICOS")
    print("=" * 80)
    
    print("\n🎨 Gráfico 1: Superfície 3D...")
    gerar_grafico_superficie_3d(
        resultados['exp1_gd'],
        resultados['exp1_nr'],
        'results/plots/grafico_1_superficie_3d.png'
    )
    
    print("\n🎨 Gráfico 2: Curvas de Nível...")
    gerar_grafico_curvas_nivel(
        resultados['exp1_gd'],
        resultados['exp1_nr'],
        'results/plots/grafico_2_curvas_nivel.png'
    )
    
    print("\n🎨 Gráfico 3: Análise de Convergência...")
    gerar_grafico_convergencia(
        resultados['exp1_gd'],
        resultados['exp1_nr'],
        'results/plots/grafico_3_convergencia.png'
    )
    
    print("\n🎨 Gráfico 4: Comparação de Desempenho...")
    dados_exp1 = {
        'gd': resultados['exp1_gd'],
        'nr': resultados['exp1_nr']
    }
    dados_exp4 = {
        'gd': resultados['exp4_gd'],
        'nr': resultados['exp4_nr']
    }
    gerar_grafico_comparacao_desempenho(
        dados_exp1,
        dados_exp4,
        'results/plots/grafico_4_comparacao_desempenho.png'
    )
    
    print("\n🎨 Gráfico 5: Sensibilidade ao Learning Rate...")
    gerar_grafico_sensibilidade_alpha(
        resultados['exp2'],
        'results/plots/grafico_5_sensibilidade_alpha.png'
    )


def exibir_resumo_final(resultados):
    """Exibe resumo final dos resultados"""
    print("\n" + "=" * 80)
    print("✅ EXECUÇÃO COMPLETA!")
    print("=" * 80)
    print()
    print("📂 Arquivos gerados:")
    print("   • results/data/resultados_experimentos.json")
    print("   • results/plots/grafico_1_superficie_3d.png")
    print("   • results/plots/grafico_2_curvas_nivel.png")
    print("   • results/plots/grafico_3_convergencia.png")
    print("   • results/plots/grafico_4_comparacao_desempenho.png")
    print("   • results/plots/grafico_5_sensibilidade_alpha.png")
    print()
    print("🎯 RESULTADO PRINCIPAL:")
    print(f"   • Newton-Raphson: {resultados['exp1_nr']['iteracoes_totais']} iterações")
    print(f"   • Gradiente Descendente: {resultados['exp1_gd']['iteracoes_totais']:,} iterações")
    speedup = resultados['exp1_gd']['iteracoes_totais'] / resultados['exp1_nr']['iteracoes_totais']
    speedup_tempo = resultados['exp1_gd']['tempo_total'] / resultados['exp1_nr']['tempo_total']
    print(f"   • Speedup iterações: {speedup:.1f}x")
    print(f"   • Speedup tempo: {speedup_tempo:.0f}x ⚡")
    print()
    print("=" * 80)
    print()


def main():
    """Função principal"""
    try:
        # Banner
        exibir_banner()
        
        # Criar diretórios
        print("📁 Criando estrutura de diretórios...")
        criar_diretorios()
        print()
        
        # Executar experimentos
        resultados = executar_experimentos()
        
        # Salvar dados
        salvar_dados(resultados)
        
        # Gerar gráficos
        gerar_graficos(resultados)
        
        # Resumo final
        exibir_resumo_final(resultados)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Execução interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
