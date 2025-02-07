# 🚀 Pipeline Data

Este repositório contém um pipeline de processamento de dados, incluindo coleta, transformação e análise. O objetivo do projeto é processar e integrar dados de duas empresas que passaram por um processo de fusão, visando criar um pipeline de dados automatizado para integrar e processar os dados das duas empresas, garantindo a consistência e a qualidade dos dados.
## 📂 Estrutura do Projeto

```
📦 pipeline-data
├── 📁 data_raw          # Dados brutos
├── 📁 data_processed    # Dados processados
├── 📁 notebooks         # Notebooks Jupyter para análise
├── 📁 scripts           # Scripts Python para processamento
└── 📄 requirements.txt  # Bibliotecas necessárias
```

## 🛠️ Configuração do Ambiente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/vitor-akira/pipeline-data.git
cd pipeline-data
```

### 2️⃣ Criar um ambiente virtual (WSL/Linux)
```bash
sudo apt install python3.12-venv  # Caso o venv não esteja disponível
python3 -m venv venv
source venv/bin/activate  # Ativar o ambiente virtual
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
