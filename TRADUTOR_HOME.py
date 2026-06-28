import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os

class CSVTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("HOME.CSV TRADUTOR by LOBO NINTENDISTA")
        self.root.geometry("500x350")
        self.root.configure(bg='#1a1a1a')
        
        # Estilo escuro
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Dark.TFrame', background='#1a1a1a')
        self.style.configure('Dark.TLabel', background='#1a1a1a', foreground='white', font=('Arial', 10))
        self.style.configure('Dark.TButton', background='#333333', foreground='white', font=('Arial', 10))
        self.style.configure('Dark.TCombobox', fieldbackground='#333333', background='#333333', foreground='white')
        self.style.map('Dark.TButton', background=[('active', '#555555')])
        
        # Frame principal
        main_frame = ttk.Frame(root, style='Dark.TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="Tradutor automático de HomeButton .CSV", style='Dark.TLabel', font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Frame para opções
        options_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        options_frame.pack(pady=10)
        
        # Seleção de codificação
        ttk.Label(options_frame, text="Codificação:", style='Dark.TLabel').grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.encoding_var = tk.StringVar(value='utf-8')
        self.encoding_combo = ttk.Combobox(options_frame, textvariable=self.encoding_var, 
                                           values=['ansi', 'utf-8', 'utf-16-le', 'utf-16-be', 'shift_jis'],
                                           state='readonly', width=15)
        self.encoding_combo.grid(row=0, column=1, padx=10, pady=10)
        
        # Seleção de idioma ("Todos os idiomas" removido daqui)
        ttk.Label(options_frame, text="Idioma de orígem:", style='Dark.TLabel').grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.language_var = tk.StringVar(value='Inglês')
        self.language_combo = ttk.Combobox(options_frame, textvariable=self.language_var,
                                           values=['Inglês', 'Francês', 'Espanhol', 'Japonês', 'Alemão', 'Italiano', 'Holandês', 'Chinês', 'Coreano'],
                                           state='readonly', width=15)
        self.language_combo.grid(row=1, column=1, padx=10, pady=10)
        
        # Botão para abrir múltiplos arquivos
        open_multiple_button = tk.Button(main_frame, text="Selecionar Arquivos CSV", command=self.open_multiple_files,
                                         bg='#333333', fg='white', font=('Arial', 12, 'bold'),
                                         activebackground='#555555', activeforeground='white',
                                         padx=20, pady=15, cursor='hand2')
        open_multiple_button.pack(pady=30)
        
        # Status
        self.status_var = tk.StringVar(value="Selecione um ou mais arquivos CSV para processar")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, style='Dark.TLabel')
        status_label.pack(pady=10)
        
        # Dicionários de tradução completos
        self.translations = {
            'Inglês': {
                "Simultaneously press ① and ②": "Aperte simultaneamente ① e ②",
                "on each Wii Remote in the": "em cada Wii Remote na ordem",
                "desired player order.": "desejada para jogar.",
                "Disconnecting...": "Desconectando...",
                "Return to the Wii Menu?": "Deseja retornar ao Menu do Wii?",
                "(Anything not saved will be lost.)": "(Dados sem salvar podem se perder)",
                "Reset the software?": "Deseja reiniciar?",
                "This will quit the game. Proceed?": "Isto encerrará o jogo. Continuar?"
            },
            'Espanhol': {
                "Para realizar una nueva": "Aperte simultaneamente ① e ②",
                "conexión, se deberán pulsar": "em cada Wii Remote na ordem",
                "a la vez los Botones ① y ②": "",
                "de cada mando de Wii en el": "",
                "orden de jugadores deseado.": "desejada para jogar.",
                "Disconnecting...": "Desconectando...",
                "Desconectando...": "Desconectando...",
                "¿Deseas volver al menú de Wii?": "Retornar ao Menu do Wii?",
                "Se perderán los datos": "(Dados sem salvar",
                "no guardados.": "podem se perder)",
                "¿Deseas reiniciar?": "Deseja reiniciar?",
                "Se perderán los datos": "(Dados sem salvar",
                "no guardados.": "podem se perder)",
                "¿Esto cerrará el juego. ¿Continuar?": "Isto encerrará o jogo. Continuar?",
                "Vas a salir del juego.": "Isto encerrará o jogo,",
                "¿Deseas continuar?": "Continuar?"
            },
            'Francês': {
                "Appuyez simultanément sur": "Aperte simultaneamente ① e ②",
                "① et ② sur chaque": "",
                "télécommande Wii pour les": "",
                "connecter dans l'ordre de": "em cada Wii Remote na ordem",
                "votre choix.": "desejada para jogar.",
                "Interruption des connexions...": "Desconectando...",
                "Voulez-vous retourner au menu Wii?": "Retornar ao Menu do Wii?",
                "(Tout ce qui n'a pas été": "(Dados sem salvar",
                "sauvegardé sera perdu.)": "(Dados sem salvar podem se perder)",
                "Voulez-vous réinitialiser?": "Deseja reiniciar?",
                "(Tout ce qui n'a pas été": "(Dados sem salvar",
                "sauvegardé sera perdu.)": "(Dados sem salvar podem se perder)",
                "Cela mettra fin au jeu. Souhaitez": "Isto encerrará o jogo.",
                "Zurück zum Wii-Menü?": "Retornar ao Menu do Wii?",
                "-vous continuer? (Tout ce qui n'a": "Continuar?"
            },
            'Japonês': {
                "接続する順番に": "Aperte simultaneamente ① e ②",
                "①ボタンと②ボタンを": "em cada Wii Remote na ordem",
                "同時に押してください。": "desejada para jogar.",
                "切断中・・・": "Desconectando...",
                "Wiiメニューにもどりますか？": "Retornar ao Menu do Wii?",
                "（保存していない内容は失われます）": "(Dados sem salvar podem se perder)",
                "リセットしますか？": "Deseja reiniciar?",
                "（保存していない内容は失われます）": "(Dados sem salvar podem se perder)",
                "ゲームを終了します。": "Isto encerrará o jogo.",
                "よろしいですか？": "Continuar?"
            },
            'Alemão': {
                "Bitte gleichzeitig ① und ②": "Aperte simultaneamente ① e ②",
                "jeder Wii-FB in der gewünschten": "em cada Wii Remote na ordem",
                "Spieler-Reihenfolge drücken.": "desejada para jogar.",
                "Verbindung wird getrennt...": "Desconectando...",
                "Zurück zum Wii-Menü?": "Retornar ao Menu do Wii?",
                "gespeicherte Daten gehen verloren.)": "(Dados sem salvar podem se perder)",
                "Zurücksetzen?": "Deseja reiniciar?",
                "Daten gehen verloren.)": "(Dados sem salvar podem se perder)"
            },
            'Italiano': {
                "Per reimpostare il collegamento": "Aperte simultaneamente ① e ②",
                "bisogna premere": "em cada Wii Remote na ordem",
                "contemporaneamente ① e ②": "desejada para jogar.",
                "su ciascun telecomando Wii": "",
                "nell'ordine dei giocatori": "",
                "desiderato.": "",
                "Interruzione collegamento": "Desconectando...",
                "in corso...": "",
                "Vuoi tornare al menu Wii?": "Retornar ao Menu do Wii?",
                "I dati non salvati andranno perduti.": "(Dados sem salvar podem se perder)",
                "Vuoi riavviare il software?": "Deseja reiniciar?",
                "I dati non salvati andranno perduti.": "(Dados sem salvar podem se perder)"
            },
            'Holandês': {
                "Druk tegelijk op ① en ② op": "Aperte simultaneamente ① e ②",
                "iedere Wii-afstandsbediening,": "em cada Wii Remote na ordem",
                "in de gewenste spelervolgorde.": "desejada para jogar.",
                "Bezig met het verbreken": "Desconectando...",
                "van de verbinding...": "",
                "Wil je terug naar het": "Retornar ao Menu do Wii?",
                "Wii-menu? Niet opgeslagen": "",
                "gegevens gaan verloren.": "(Dados sem salvar podem se perder)",
                "Wil je terug naar het": "Deseja reiniciar?",
                "titelscherm? Niet opgeslagen": "",
                "gegevens gaan verloren.": "(Dados sem salvar podem se perder)"
            },
            'Chinês': {
                "请按照您需要的连接顺序，": "Aperte simultaneamente ① e ②",
                "同时按Wii遥控器上的": "em cada Wii Remote na ordem",
                "①键和②键。": "desejada para jogar.",
                "正在断开连接……": "Desconectando...",
                "要返回Wii菜单吗？": "Retornar ao Menu do Wii?",
                "（未保存的内容将会丢失）": "(Dados sem salvar podem se perder)",
                "要重启吗？": "Deseja reiniciar?",
                "（未保存的内容将会丢失）": "(Dados sem salvar podem se perder)"
            },
            'Coreano': {
                "먼저 접속할": "Aperte simultaneamente ① e ②",
                "Wii 리모컨부터": "em cada Wii Remote na ordem",
                "차례대로 ① 버튼과": "desejada para jogar.",
                "② 버튼을 동시에": "",
                "눌러 주십시오.": "",
                "접속 해제 중...": "Desconectando...",
                "Wii 메뉴로 돌아가시겠습니까?": "Retornar ao Menu do Wii?",
                "(저장되지 않은 내용은 사라집니다)": "(Dados sem salvar podem se perder)",
                "리셋하시겠습니까?": "Deseja reiniciar?",
                "(저장되지 않은 내용은 사라집니다)": "(Dados sem salvar podem se perder)"
            }
        }
        
        # Linhas a excluir para cada idioma
        self.lines_to_delete = {
            'Espanhol': [
                "a la vez los Botones ① y ②",
                "de cada mando de Wii en el"
            ],
            'Francês': [
                "① et ② sur chaque",
                "télécommande Wii pour les",
                "(Tout ce qui n'a pas été"
            ],
            'Italiano': [
                "su ciascun telecomando Wii",
                "nell'ordine dei giocatori",
                "desiderato.",
                "in corso..."
            ],
            'Holandês': [
                "van de verbinding...",
                "Wii-menu? Niet opgeslagen",
                "titelscherm? Niet opgeslagen"
            ],
            'Coreano': [
                "② 버튼을 동시에",
                "눌러 주십시오."
            ],
            'Inglês': [],
            'Japonês': [],
            'Alemão': [],
            'Chinês': []
        }
    
    def get_encoding(self):
        encoding_map = {
            'ansi': 'cp1252',
            'utf-8': 'utf-8',
            'utf-16-le': 'utf-16-le',
            'utf-16-be': 'utf-16-be',
            'shift_jis': 'shift_jis'
        }
        return encoding_map.get(self.encoding_var.get(), 'utf-8')
    
    def should_delete_line(self, line_content, language):
        # Simplificado: checa apenas as linhas do idioma selecionado
        for delete_string in self.lines_to_delete.get(language, []):
            if delete_string in line_content:
                return True
        return False
    
    def translate_content(self, content, language):
        # Simplificado: aplica apenas o dicionário do idioma selecionado
        translations = self.translations.get(language, {})
        for original, translated in translations.items():
            if translated:  # Só substitui se a tradução não estiver vazia
                content = content.replace(original, translated)
        return content
    
    def process_file(self, file_path):
        """Processa um único arquivo CSV"""
        try:
            encoding = self.get_encoding()
            language = self.language_var.get()
            
            # Ler o arquivo
            with open(file_path, 'r', encoding=encoding, newline='') as file:
                lines = file.readlines()
            
            # Processar linhas
            processed_lines = []
            deleted_count = 0
            
            for line in lines:
                # Verificar se a linha deve ser excluída
                if self.should_delete_line(line, language):
                    deleted_count += 1
                    continue
                
                # Traduzir o conteúdo
                translated_line = self.translate_content(line, language)
                processed_lines.append(translated_line)
            
            # Criar novo nome do arquivo
            directory = os.path.dirname(file_path)
            filename = os.path.basename(file_path)
            new_filename = f"n_{filename}"
            new_file_path = os.path.join(directory, new_filename)
            
            # Salvar o arquivo
            with open(new_file_path, 'w', encoding=encoding, newline='') as file:
                file.writelines(processed_lines)
            
            return True, filename, deleted_count, new_filename
            
        except Exception as e:
            return False, os.path.basename(file_path), 0, str(e)
    
    def open_multiple_files(self):
        """Abre múltiplos arquivos CSV em massa"""
        file_paths = filedialog.askopenfilenames(
            title="Selecione um ou mais arquivos CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if not file_paths:
            return
        
        # Confirmar processamento em massa
        if not messagebox.askyesno("Confirmar", 
            f"Você selecionou {len(file_paths)} arquivo(s).\n\n"
            f"Idioma: {self.language_var.get()}\n"
            f"Codificação: {self.encoding_var.get()}\n\n"
            "Deseja processar todos os arquivos?"):
            return
        
        # Processar cada arquivo
        successful = []
        failed = []
        total_deleted = 0
        
        for file_path in file_paths:
            success, filename, deleted_count, result = self.process_file(file_path)
            if success:
                successful.append((filename, deleted_count, result))
                total_deleted += deleted_count
            else:
                failed.append((filename, result))
            
            # Atualizar status
            self.status_var.set(f"Processando... {len(successful) + len(failed)}/{len(file_paths)} arquivos")
            self.root.update()
        
        # Mostrar resultados
        status_msg = f"Processamento concluído!\n\n"
        status_msg += f"Arquivos processados: {len(successful)}\n"
        status_msg += f"Falhas: {len(failed)}\n"
        status_msg += f"Total de linhas excluídas: {total_deleted}\n\n"
        
        if successful:
            status_msg += "Arquivos processados com sucesso:\n"
            for filename, deleted, newname in successful[:5]:  # Mostrar até 5
                status_msg += f"  • {filename} → {newname} ({deleted} linhas excluídas)\n"
            if len(successful) > 5:
                status_msg += f"  ... e mais {len(successful) - 5} arquivo(s)\n"
        
        if failed:
            status_msg += "\nFalhas:\n"
            for filename, error in failed[:5]:
                status_msg += f"  • {filename}: {error}\n"
            if len(failed) > 5:
                status_msg += f"  ... e mais {len(failed) - 5} falha(s)\n"
        
        self.status_var.set(f"Processados {len(successful)} arquivos com sucesso")
        messagebox.showinfo("Resultado do Processamento", status_msg)

def main():
    root = tk.Tk()
    app = CSVTranslator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
