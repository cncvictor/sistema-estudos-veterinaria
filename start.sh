#!/bin/bash
# Script para iniciar o sistema de estudos web

echo "🐾 Iniciando Sistema de Estudo Veterinária..."

# Verifica se o Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3."
    exit 1
fi

# Verifica se o pip3 está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale o pip3."
    exit 1
fi

# Cria diretório de configuração do Streamlit se não existir
mkdir -p .streamlit

# Verifica se as dependências estão instaladas
echo "📦 Verificando dependências..."
if ! pip3 freeze | grep -q "streamlit"; then
    echo "📥 Instalando dependências..."
    pip3 install -r requirements.txt
fi

# Verifica se o modelo spaCy em português está instalado
echo "🔍 Verificando modelo spaCy em português..."
if ! python3 -c "import spacy; spacy.load('pt_core_news_sm')" 2>/dev/null; then
    echo "📥 Instalando modelo spaCy em português..."
    python3 -m spacy download pt_core_news_sm
fi

# Cria diretório para outputs se não existir
mkdir -p outputs

# Obtém o IP da máquina
IP_ADDRESS=$(hostname -I | awk '{print $1}')

# Inicia a aplicação
echo "🚀 Iniciando aplicação..."
echo "📱 Você poderá acessar o sistema em:"
echo "   • Local: http://localhost:8501"
echo "   • Rede: http://$IP_ADDRESS:8501"
streamlit run app_estudo.py --server.address 0.0.0.0 --server.port 8501 