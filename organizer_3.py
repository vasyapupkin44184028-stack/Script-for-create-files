#создано на Python 3
#Создает в выбраную или текущую папку с символосодержащими файлами
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_folder():
    root = tk.Tk()
    root.withdraw() 
    
    print("Выберите папку")
    
    # Показываем диалог выбора папки
    selected_folder = filedialog.askdirectory(
        title="Выберите папку"
    )
    
    if not selected_folder:
        return Path(".")
    # Делает сохранение в текущую папку, если дурагая папка не выбрана
    
    return Path(selected_folder)

def create_portfolio_with_content():
    
    # Выбирает папку для сохранения
    base_path = select_folder()
    
    # Создает папку портфолио в выбранной папке
    portfolio_path = base_path / "Моё портфолио"
    portfolio_path.mkdir(exist_ok=True)
    
    print(f"📂 Сохраняю в: {portfolio_path.absolute()}")
    
    # Здесь создаются проекты
    projects = {
        'python': [
            'калькулятор', 
            'бот_для_телеграм',
            'парсер_сайта'
        ],
        'web': [
            'личный_сайт',
            'интернет_магазин',
            'блог',
        ],
        'documents': [
            'резюме',
            'доклады',
            'отчеты',
            'презентации'
        ]
    }
    
    # Содержимое для разных типов файлов
    file_contents = {
        'python': {
            'main.py': '#разработано на Python 3\n\nprint("Здесь будет ваш код, который вы напишите")',
            'config.py': '#разработано на Python 3\n\n# Настройки проекта\nDEBUG = True',
            'utils.py': '#разработано на Python 3\n\n# Вспомогательные функции',
            'README.txt': 'Описание вашего условного проекта на Python'
        },
        'web': {
            'index.html': '<!-- сюда можно добавить код -->',
            'style.css': '/* сюда можно добавить код */',
            'script.js': '// сюда можно добавить код',
            'README.txt': 'Описание вашего условного веб-проекта'
        },
        'documents': {
            'нужное.pdf': 'ваши документы или данные',
            'то как реализовал.txt': 'ваши документы или данные',
            'план.txt': 'ваши документы или данные'
        }
    }
    
    total_projects = 0
    total_files = 0
    
    # Создает проекты
    for category, project_list in projects.items():
        category_path = portfolio_path / category
        category_path.mkdir(exist_ok=True)
        
        for project_name in project_list:
            project_path = category_path / project_name
            project_path.mkdir(exist_ok=True)
            
            print(f"Создаю проект: {category}/{project_name}")
            
            # Создает файлы с содержимым
            for filename, content in file_contents[category].items():
                file_path = project_path / filename
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  📄 {filename}")
                total_files += 1
            
            total_projects += 1
            print()
    
    # Результат
    print(f"✅ Создано: {total_projects} проектов, {total_files} файлов")
    print(f"📁 Папка: {portfolio_path.absolute()}")
    
    # Показываеn сообщение об успехе
    messagebox.showinfo(f"Портфолио создано!\n\nПроектов: {total_projects}\nФайлов: {total_files}\n\nПапка: {portfolio_path}")

if __name__ == "__main__":
    create_portfolio_with_content()