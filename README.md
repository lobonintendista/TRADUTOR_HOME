# 🛠️ HOME.CSV TRADUTOR

O **HOME.CSV TRADUTOR** (desenvolvido por *LOBO NINTENDISTA*) é uma ferramenta automatizada com interface gráfica (GUI) minimalista, projetada para facilitar e agilizar a tradução e a limpeza de arquivos `.csv` do menu HomeButton do Nintendo Wii.

Com suporte a múltiplos idiomas e diferentes tipos de codificação de texto (encoding), o programa automatiza o processo de substituição de strings e a remoção de linhas redundantes específicas de cada idioma sem quebrar a estrutura binária própria do arquivo csv.


<img width="499" height="383" alt="image" src="https://github.com/user-attachments/assets/498734b2-adc0-4324-81b6-1b14279ab9e4" />


## Estrutura do homeBtn.arc

| Arquivo/Pasta | Descrição |
|---------------|-----------|
| `anim/` | Arquivos `.brlan` com animações e transições do Menu HOME. |
| `blyt/` | Arquivo `.brlyt` responsável pelo layout como posição e tamanho dos elementosda na interface. |
| `font/` | Fontes `.brfnt` utilizadas pelo menu pelo arquivo home.csv. |
| `timg/` | Texturas `.tpl` Texturas .tpl com gráficos em png (botões, ícones, fundo, bateria, volume, etc.). |
| `home.csv` | Arquivo com textos exibidos pelo Menu HOME, ao qual o programa irá traduzir |


OBS: Link com gráficos traduzidos do arquivo `timg/`: https://github.com/lobonintendista/Gr-ficos-homeBtn-straps-BR/blob/main/README.md


---

### 📂 Como usar:
1. Baixe o arquivo executável na seção **new release**.
2. Abra o programa, escolha a codificação correta e o idioma de origem do seu arquivo `.csv` (Geralmente os jogos de wii usam muito a codificação UTF-16 BE)
3. Clique em **"Selecionar Arquivos CSV"**, escolha seus arquivos e confirme. Os novos arquivos traduzidos serão gerados na mesma pasta com o prefixo `n_`.

---

## ✨ Funcionalidades

* 📂 **Processamento em Massa:** Selecione e traduza múltiplos arquivos `.csv` de uma única vez.
* 🌍 **Suporte Multi-idioma:** Dicionários embutidos para Inglês, Espanhol, Francês, Japonês, Alemão, Italiano, Holandês, Chinês e Coreano.
* 🔤 **Gerenciamento de Codificação:** Suporte nativo para `ANSI (CP1252)`, `UTF-8`, `UTF-16-LE`, `UTF-16-BE` e `Shift_JIS`.
* 🧹 **Limpeza Automática:** Remove linhas de quebra de texto específicas que tornam-se desnecessárias após a tradução para o Português.
* 🖥️ **Interface Moderna:** Desenvolvida em Tkinter com um tema escuro confortável.

---

## 🚀 Download e Compatibilidade

Na aba **Releases**, você encontrará o executável (`.exe`) pronto para uso.

⚠️ **Informação Importante sobre Arquitetura:**
* O executável oficial disponibilizado está compilado em **64-bits** (compatível com a grande maioria dos computadores modernos com Windows 10 e 11).
* **Precisa da versão 32-bits?** Se você utiliza um sistema operacional de 32-bits (x86), o executável padrão não irá abrir. Neste caso, será necessário realizar a compilação manual a partir do código-fonte utilizando um ambiente Python de 32-bits.

---

## 🛠️ Como Compilar (Para 32-bits ou Modificações)

Caso queira gerar sua própria versão (seja para suporte a 32-bits ou para aplicar modificações no código), siga os passos abaixo:

1. **Instale o Python:** Certifique-se de ter o Python instalado. *(Se o objetivo for gerar a versão de 32-bits, certifique-se de baixar e instalar a versão **32-bit (x86)** do Python em sua máquina).*
2. **Instale o PyInstaller:** Abra o Prompt de Comando (CMD) e execute:
   ```bash
   pip install pyinstaller

Organize os arquivos: Deixe o script do tradutor e o ícone (icon.ico) na mesma pasta.

Compile o projeto: Execute o seguinte comando no terminal para gerar um executável único:

Bash:
pyinstaller --onefile --windowed --icon=icon.ico TRADUTOR_HOME.py

O arquivo final estará disponível dentro da pasta criada chamada dist/.



Sinta-se livre para clonar, abrir Issues ou enviar Pull Requests para melhorar os dicionários de tradução!

📝 Licença e Créditos
Desenvolvedor: LOBO NINTENDISTA
