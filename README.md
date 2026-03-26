# Automa-o-Testes
# Automação de testes
## 📊 Coverage (Cobertura de Testes)

Este projeto utiliza a ferramenta **coverage** para medir a cobertura dos testes automatizados.

### 📦 Instalação

Instale o coverage com o seguinte comando:

```bash
pip install coverage
```

Ou, caso necessário:

```bash
python -m pip install coverage
```
---

### ▶️ Executando os testes com coverage

Para rodar os testes e coletar dados de cobertura:

```bash
python -m coverage run -m pytest "nome do exercicio caso queira especificar"
```

---

### 📄 Gerando relatório HTML

Após executar os testes, gere o relatório com:

```bash
python -m coverage html
```

Isso criará uma pasta chamada:

```
htmlcov/
```

---

### 🌐 Visualizando o relatório

Abra o arquivo abaixo no navegador:

```
htmlcov/index.html
```

Ou, no Windows:

```bash
start htmlcov/index.html
```

---

### 💡 Observação

* Linhas em **verde** indicam código testado
* Linhas em **vermelho** indicam código não testado

---

### 🚀 Por que usar coverage?

* Ajuda a identificar partes do código sem testes
* Melhora a qualidade do software
* Facilita manutenção e evolução do projeto
