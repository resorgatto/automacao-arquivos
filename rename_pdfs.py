import os
import re
import zipfile
import subprocess
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def find_winrar():
    
    possible_paths = [
        "C:\\Program Files\\WinRAR\\WinRAR.exe",
        "C:\\Program Files (x86)\\WinRAR\\WinRAR.exe"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def extract_archive(archive_path):
    
    extract_to = os.path.splitext(archive_path)[0] 

    if archive_path.endswith(".zip"):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    elif archive_path.endswith(".rar"):
        winrar_path = find_winrar()

        if not winrar_path:
            messagebox.showerror("Erro", "WinRAR não encontrado! Instale o WinRAR para extrair arquivos .rar.")
            return None

       
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        try:
            
            command = f'"{winrar_path}" x "{archive_path}" "{extract_to}\\" -y"'
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                messagebox.showerror("Erro", f"Falha ao extrair o arquivo RAR.\n\nSaída do WinRAR:\n{result.stdout}\n\nErro:\n{result.stderr}")
                return None

        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado ao executar o WinRAR:\n{e}")
            return None
    else:
        messagebox.showerror("Erro", "Formato de arquivo não suportado. Selecione um ZIP ou RAR.")
        return None

    return extract_to


def rename_pdfs(folder_path):
    current_year = datetime.now().year  
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):  
            
            match_main_date = re.search(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', filename)
            match_venc_date = re.search(r'VENC\. (\d{2})\.(\d{2})', filename)
            
            if match_main_date:
                day, month, year = match_main_date.groups()
                date = f"{year}-{month}-{day}" 
                
                
                if match_venc_date:
                    venc_day, venc_month = match_venc_date.groups()
                    venc_date = f"{current_year}-{venc_month}-{venc_day}"  
                else:
                    venc_date = date  
                
                parts = filename.replace(".pdf", "").split(" ")  
                
               
                date_index = parts.index(match_main_date.group(0))
                
                
                company_name = " ".join(parts[:date_index])
                
                
                company_name = re.sub(r'\bBRAVEND\b', '', company_name, flags=re.IGNORECASE).strip()
                
                
                company_name = re.sub(r'\b[A-Z0-9-]{8,}\b', '', company_name).strip()
                
                
                description = " ".join(parts[date_index+1:])
                
                
                description = re.sub(r'VENC\. \d{2}\.\d{2}', '', description).strip()
                
                
                if "MEMORIA DE CALCULO" in description.upper():
                    description = description.replace("MEMORIA DE CALCULO", "").strip()
                    new_filename = f"{venc_date} - MEMORIA DE CALCULO - {company_name}.pdf"
                else:
                    new_filename = f"{venc_date} - {company_name} - {description}.pdf"
                
                
                new_filename = re.sub(r'\s+', ' ', new_filename).strip()
                new_filename = re.sub(r'\s*-\s*-', '-', new_filename).strip()
                
                # Caminhos completos
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                
                # Renomeia o arquivo apenas se o nome for diferente
                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f"Renomeado: {filename} -> {new_filename}")
    
    messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

def select_file_or_folder():
    path = filedialog.askopenfilename(title="Selecione um arquivo ZIP, RAR ou PDF", filetypes=[("Arquivos ZIP/RAR/PDF", "*.zip;*.rar;*.pdf")])
    if not path:
        path = filedialog.askdirectory(title="Ou selecione uma pasta com PDFs")
    
    if path:
        if os.path.isfile(path) and path.lower().endswith(('.zip', '.rar')):
            extract_folder = extract_archive(path)
            if extract_folder:
                rename_pdfs(extract_folder)
                messagebox.showinfo("Sucesso", f"Arquivos renomeados e extraídos para: {extract_folder}")
        elif os.path.isdir(path):
            rename_pdfs(path)
            messagebox.showinfo("Sucesso", "Arquivos na pasta foram renomeados com sucesso!")

def main():
    root = tk.Tk()
    root.title("Renomeador de PDFs")
    root.geometry("400x200")
    
    tk.Label(root, text="Selecione um arquivo ZIP, RAR, PDF ou uma pasta:").pack(pady=20)
    tk.Button(root, text="Selecionar Arquivo/Pasta", command=select_file_or_folder).pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()