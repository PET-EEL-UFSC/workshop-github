# Workshop de Git & GitHub — PET EEL

Material de apoio do workshop de Git e GitHub do PET EEL (UFSC). Use este README durante e depois da aula como referência rápida.

> 📄 Guia completo (com explicações, exemplos e o roteiro da aula): [link a adicionar]

---

## Preparação antes de começar

Abra o terminal e confira se as ferramentas já estão instaladas:

```bash
git --version
python --version
gcc --version
```

Se algo não responder, avise o monitor(a) antes de começar o exercício.

**Configuração inicial do Git** (só precisa fazer uma vez por computador):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## Cheat sheet — comandos essenciais

### Ciclo básico local

```bash
git init                    # cria um repositório novo na pasta atual
git status                  # mostra o estado atual (o comando mais usado!)
git add arquivo.txt         # manda um arquivo pro staging
git add .                   # manda todas as mudanças pro staging
git commit -m "mensagem"    # registra o commit
git log --oneline           # histórico de commits, resumido
git diff                    # o que mudou e ainda não foi commitado
```

### Branches

```bash
git branch                  # lista as branches
git checkout -b nova-branch # cria e muda pra uma branch nova
git checkout main           # volta pra branch main
git merge nova-branch       # traz as mudanças da branch pra branch atual
```

### GitHub (remoto)

```bash
git clone <url>             # copia um repositório do GitHub pra sua máquina
git push                    # envia seus commits pro GitHub
git pull                    # traz as mudanças do GitHub pra sua máquina
```

### Desfazer coisas

```bash
git restore arquivo.txt         # descarta mudanças não commitadas
git restore --staged arquivo.txt # tira do staging (mantém o conteúdo)
git commit --amend              # edita o último commit
git revert <hash-do-commit>     # desfaz um commit já enviado, criando um commit novo
```

### Emergência

```bash
git stash        # guarda mudanças temporariamente sem commitar
git reflog        # mostra tudo que aconteceu — "botão de pânico"
git merge --abort # cancela um merge em andamento
```

---

## Exercício: subindo um código pro GitHub

1. No GitHub, clique em **New repository**, dê um nome (ex: `meu-primeiro-repo`), marque **Add a README file** e crie.
2. Clone pra sua máquina:
   ```bash
   git clone https://github.com/SEU-USUARIO/meu-primeiro-repo.git
   cd meu-primeiro-repo
   ```
3. Crie um arquivo `ola.py` (ou `ola.c`) com um programa simples.
4. Suba pro GitHub:
   ```bash
   git add ola.py
   git commit -m "feat: adiciona programa de saudação"
   git push
   ```
5. Confira no site do GitHub que o arquivo apareceu.
6. Faça uma segunda mudança no código, repita `add` → `commit` → `push`, e veja o histórico crescer em `git log --oneline` e na aba de commits do repositório.

---

## Fork — quando usar

Fork é uma cópia do repositório de outra pessoa, feita na sua própria conta do GitHub. Use quando você **não tem** permissão de escrita no projeto original (ex: contribuir em um projeto open source). Quando você **já tem** acesso de escrita (projetos do próprio PET EEL, por exemplo), não precisa de fork — trabalhe direto com uma branch.

```bash
# depois de clicar em "Fork" no site:
git clone https://github.com/SEU-USUARIO/repo-forkado.git
cd repo-forkado
git checkout -b minha-contribuicao
# ... faça commits ...
git push origin minha-contribuicao
# abra um Pull Request do seu fork pro repositório original, pelo site do GitHub
```

---

## Links úteis

- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet oficial do GitHub (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)
