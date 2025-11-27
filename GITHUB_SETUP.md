# 📤 Como Fazer Upload para o GitHub

## 🎯 Passo a Passo

### 1️⃣ Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em **"New repository"** (botão verde)
3. Configure:
   - **Repository name:** `tcc-otimizadores-ia`
   - **Description:** `Análise Computacional da Convergência de Otimizadores de IA: Newton-Raphson vs. Gradiente Descendente`
   - **Public** (recomendado) ou Private
   - ❌ **NÃO** marque "Initialize with README" (já temos!)
   - ❌ **NÃO** adicione .gitignore (já temos!)
   - ❌ **NÃO** adicione licença (já temos!)
4. Clique em **"Create repository"**

### 2️⃣ Conectar Repositório Local ao GitHub

Após criar o repositório, o GitHub mostrará comandos. Use estes:

```bash
cd /caminho/para/tcc-otimizadores-ia

# Adicionar remote (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/tcc-otimizadores-ia.git

# Renomear branch para main (opcional, mas recomendado)
git branch -M main

# Fazer push
git push -u origin main
```

### 3️⃣ Autenticação

O GitHub pedirá autenticação. Você tem 2 opções:

#### Opção A: Personal Access Token (Recomendado)

1. Vá para GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Clique **"Generate new token (classic)"**
3. Marque escopo: `repo` (acesso completo a repositórios)
4. Clique **"Generate token"**
5. **COPIE O TOKEN** (você não verá novamente!)
6. Ao fazer `git push`, use:
   - **Username:** seu_usuario_github
   - **Password:** cole_o_token_aqui

#### Opção B: SSH (Avançado)

```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu_email@exemplo.com"

# Adicionar ao ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# Adicionar no GitHub: Settings → SSH and GPG keys → New SSH key
```

Depois, use URL SSH:
```bash
git remote set-url origin git@github.com:SEU_USUARIO/tcc-otimizadores-ia.git
```

---

## 🔄 Atualizações Futuras

Após o primeiro push, para atualizar:

```bash
# Fazer alterações no código...

# Adicionar mudanças
git add .

# Commit com mensagem descritiva
git commit -m "✨ Adiciona otimizador Adam"

# Push
git push
```

---

## 📝 Boas Práticas de Commit

### Mensagens de Commit

Use emojis e seja descritivo:

```bash
git commit -m "🎨 Melhora visualização 3D"
git commit -m "🐛 Corrige bug na Hessiana quando x=0"
git commit -m "✅ Adiciona testes para convergência"
git commit -m "📝 Atualiza documentação do README"
git commit -m "⚡ Otimiza cálculo de gradiente"
git commit -m "✨ Adiciona implementação do Adam"
```

### Emojis Úteis

- 🎉 `:tada:` - Commit inicial
- ✨ `:sparkles:` - Nova funcionalidade
- 🐛 `:bug:` - Correção de bug
- 📝 `:memo:` - Documentação
- 🎨 `:art:` - Melhora estrutura/formato
- ⚡ `:zap:` - Performance
- ✅ `:white_check_mark:` - Testes
- 🔧 `:wrench:` - Configuração
- 🚀 `:rocket:` - Deploy

---

## 🌐 Acessar no Replit

### Opção 1: Importar do GitHub

1. Acesse [replit.com](https://replit.com)
2. Clique **"+ Create Repl"**
3. Escolha **"Import from GitHub"**
4. Cole URL: `https://github.com/SEU_USUARIO/tcc-otimizadores-ia`
5. Clique **"Import from GitHub"**

### Opção 2: Git Clone

No Replit Shell:

```bash
git clone https://github.com/SEU_USUARIO/tcc-otimizadores-ia.git
cd tcc-otimizadores-ia
pip install -r requirements.txt
python executar_completo.py
```

---

## 🎯 Checklist Final

Antes de fazer push, verifique:

- [ ] README.md está atualizado
- [ ] requirements.txt lista todas as dependências
- [ ] .gitignore exclui arquivos sensíveis
- [ ] Código está funcionando (`python executar_completo.py`)
- [ ] Commits têm mensagens descritivas
- [ ] Não há dados sensíveis (senhas, tokens) no código

---

## 🆘 Troubleshooting

### Erro: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/tcc-otimizadores-ia.git
```

### Erro: "failed to push some refs"

```bash
git pull origin main --rebase
git push origin main
```

### Esqueci meu token

Gere um novo em GitHub → Settings → Developer settings → Personal access tokens

---

## 📞 Suporte

Se tiver problemas:

1. Consulte [GitHub Docs](https://docs.github.com)
2. Abra uma issue no repositório
3. Email: joao.victor@discente.ufma.br

---

**Pronto! Seu projeto está no GitHub! 🎉**
