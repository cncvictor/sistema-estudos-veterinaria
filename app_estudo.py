import streamlit as st
import os
import markdown
import json
from pathlib import Path
import random
import time
import base64
from PIL import Image
import io
import fitz  # PyMuPDF
import re

# Configuração da página
st.set_page_config(
    page_title="Sistema de Estudos Veterinária",
    page_icon="🐾",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .main-title {
        color: #2196F3;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #666;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🐾 Sistema de Estudos Veterinária")
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #666;'>Desenvolvido por Victor Rodrigues</p>", unsafe_allow_html=True)

# Função para ler e exibir conteúdo markdown
def exibir_conteudo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            st.markdown(conteudo)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {str(e)}")

# Função para listar arquivos markdown em um diretório
def listar_arquivos_md(diretorio):
    return sorted([f for f in os.listdir(diretorio) if f.endswith('.md')])

# Diretório base dos resumos
diretorio_resumos = "Resumos_IA"

# Dicionários para organizar os arquivos
arquivos_farmacologia = {
    "Fundamentos de Farmacologia": [],
    "Fármacos do Sistema Nervoso": [],
    "Fármacos Cardiovasculares": [],
    "Anti-inflamatórios e Analgésicos": [],
    "Anestésicos": [],
    "Outros Fármacos": []
}

arquivos_sistemas = {
    "Sistema Nervoso": [],
    "Sistema Cardiovascular": [],
    "Sistema Respiratório": [],
    "Sistema Digestivo": [],
    "Sistema Urinário": [],
    "Sistema Endócrino": [],
    "Sistema Imune": [],
    "Sistema Reprodutor": [],
    "Sistema Tegumentar": [],
    "Sistema Musculoesquelético": [],
    "Sistema Sensorial": [],
    "Sistema Hematopoiético": [],
    "Sistema Linfático": []
}

# Classificar os arquivos
for arquivo in listar_arquivos_md(diretorio_resumos):
    caminho_completo = os.path.join(diretorio_resumos, arquivo)
    nome_arquivo = arquivo.replace('.md', '').lower()
    
    # Classificação de Farmacologia
    if any(termo in nome_arquivo for termo in ['farmaco', 'farmacocinetica', 'farmacodinamica']):
        arquivos_farmacologia["Fundamentos de Farmacologia"].append((arquivo, caminho_completo))
    elif any(termo in nome_arquivo for termo in ['nervoso', 'neural', 'neuro']) and 'farmaco' in nome_arquivo:
        arquivos_farmacologia["Fármacos do Sistema Nervoso"].append((arquivo, caminho_completo))
    elif any(termo in nome_arquivo for termo in ['cardio', 'vascular']) and 'farmaco' in nome_arquivo:
        arquivos_farmacologia["Fármacos Cardiovasculares"].append((arquivo, caminho_completo))
    elif any(termo in nome_arquivo for termo in ['anti', 'analgesic', 'dor']):
        arquivos_farmacologia["Anti-inflamatórios e Analgésicos"].append((arquivo, caminho_completo))
    elif 'anestesic' in nome_arquivo:
        arquivos_farmacologia["Anestésicos"].append((arquivo, caminho_completo))
    elif 'farmaco' in nome_arquivo:
        arquivos_farmacologia["Outros Fármacos"].append((arquivo, caminho_completo))
    
    # Classificação de Sistemas
    elif 'nervoso' in nome_arquivo or 'neural' in nome_arquivo:
        arquivos_sistemas["Sistema Nervoso"].append((arquivo, caminho_completo))
    elif 'cardiovascular' in nome_arquivo or 'cardio' in nome_arquivo:
        arquivos_sistemas["Sistema Cardiovascular"].append((arquivo, caminho_completo))
    elif 'respiratorio' in nome_arquivo:
        arquivos_sistemas["Sistema Respiratório"].append((arquivo, caminho_completo))
    elif 'digestivo' in nome_arquivo:
        arquivos_sistemas["Sistema Digestivo"].append((arquivo, caminho_completo))
    elif 'urinario' in nome_arquivo:
        arquivos_sistemas["Sistema Urinário"].append((arquivo, caminho_completo))
    elif 'endocrino' in nome_arquivo:
        arquivos_sistemas["Sistema Endócrino"].append((arquivo, caminho_completo))
    elif 'imune' in nome_arquivo:
        arquivos_sistemas["Sistema Imune"].append((arquivo, caminho_completo))
    elif 'reprodut' in nome_arquivo:
        arquivos_sistemas["Sistema Reprodutor"].append((arquivo, caminho_completo))
    elif 'tegumentar' in nome_arquivo:
        arquivos_sistemas["Sistema Tegumentar"].append((arquivo, caminho_completo))
    elif 'musculo' in nome_arquivo:
        arquivos_sistemas["Sistema Musculoesquelético"].append((arquivo, caminho_completo))
    elif 'sensorial' in nome_arquivo:
        arquivos_sistemas["Sistema Sensorial"].append((arquivo, caminho_completo))
    elif 'hematop' in nome_arquivo:
        arquivos_sistemas["Sistema Hematopoiético"].append((arquivo, caminho_completo))
    elif 'linfatico' in nome_arquivo:
        arquivos_sistemas["Sistema Linfático"].append((arquivo, caminho_completo))

# Interface principal com três abas
tab1, tab2, tab3 = st.tabs(["📚 Farmacologia", "🔬 Sistemas", "📊 Estatísticas"])

with tab1:
    st.markdown("<h2 class='section-title'>📚 Farmacologia</h2>", unsafe_allow_html=True)
    
    for categoria, arquivos in arquivos_farmacologia.items():
        if arquivos:  # Só mostra categorias com arquivos
            st.markdown(f"<h3 class='subsection-title'>{categoria}</h3>", unsafe_allow_html=True)
            for arquivo, caminho in sorted(arquivos):
                with st.expander(f"📖 {arquivo.replace('.md', '').replace('_', ' ').title()}"):
                    exibir_conteudo(caminho)

with tab2:
    st.markdown("<h2 class='section-title'>🔬 Sistemas</h2>", unsafe_allow_html=True)
    
    for categoria, arquivos in arquivos_sistemas.items():
        if arquivos:  # Só mostra categorias com arquivos
            st.markdown(f"<h3 class='subsection-title'>{categoria}</h3>", unsafe_allow_html=True)
            for arquivo, caminho in sorted(arquivos):
                with st.expander(f"📖 {arquivo.replace('.md', '').replace('_', ' ').title()}"):
                    exibir_conteudo(caminho)

with tab3:
    st.markdown("<h2 class='section-title'>📊 Estatísticas do Material</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📚 Farmacologia")
        for categoria, arquivos in arquivos_farmacologia.items():
            if arquivos:
                st.metric(categoria, len(arquivos))
    
    with col2:
        st.markdown("### 🔬 Sistemas")
        for categoria, arquivos in arquivos_sistemas.items():
            if arquivos:
                st.metric(categoria, len(arquivos))
    
    # Total geral
    st.markdown("### 📈 Total Geral")
    total_farmacologia = sum(len(arquivos) for arquivos in arquivos_farmacologia.values())
    total_sistemas = sum(len(arquivos) for arquivos in arquivos_sistemas.values())
    total_geral = total_farmacologia + total_sistemas
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Farmacologia", total_farmacologia)
    col2.metric("Total Sistemas", total_sistemas)
    col3.metric("Total Geral", total_geral)

# Barra lateral com busca
with st.sidebar:
    st.markdown("### 🔍 Busca")
    termo_busca = st.text_input("Buscar conteúdo:")
    if termo_busca:
        st.markdown("#### Resultados da busca:")
        termo_lower = termo_busca.lower()
        encontrados = False
        
        # Busca em Farmacologia
        st.markdown("##### 📚 Em Farmacologia:")
        for categoria, arquivos in arquivos_farmacologia.items():
            for arquivo, caminho in arquivos:
                if termo_lower in arquivo.lower():
                    st.markdown(f"- {arquivo.replace('.md', '').replace('_', ' ').title()}")
                    encontrados = True
        
        # Busca em Sistemas
        st.markdown("##### 🔬 Em Sistemas:")
        for categoria, arquivos in arquivos_sistemas.items():
            for arquivo, caminho in arquivos:
                if termo_lower in arquivo.lower():
                    st.markdown(f"- {arquivo.replace('.md', '').replace('_', ' ').title()}")
                    encontrados = True
        
        if not encontrados:
            st.info("Nenhum resultado encontrado.")
    
    # Informações do sistema
    st.markdown("---")
    st.markdown("### ℹ️ Sobre")
    st.markdown("""
    Sistema de estudos para Medicina Veterinária com:
    - 📚 Material organizado por temas
    - 🔍 Busca integrada
    - 📊 Estatísticas do material
    """)
    
    st.markdown("---")
    st.markdown("Desenvolvido com ❤️ para estudantes de Veterinária") 