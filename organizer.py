#создано на Python 3
#Создает в текущую папку с пустыми файлами
from pathlib import Path

def create_empty_portfolio():
    
    # Создает папку в папке, в которой запущен срипт, куда сохраняются все проекты и файлы в них
    portfolio_path = Path("Моё портфолио")
    portfolio_path.mkdir(exist_ok=True)
    
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
    
    # Здесь создаются файлы для проекта
    file_templates = {
        'python': ['main.py', 'config.py', 'utils.py', 'README.txt'],
        'web': ['index.html', 'style.css', 'script.js', 'README.txt'],
        'data': ['analysis.py', 'data.csv', 'config.json', 'README.txt'],
        'documents': ['нужноеt.pdf', 'то как реализовал.txt', 'план.txt']
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
            
            
            # Создает файлы(Пустой)
            for filename in file_templates[category]:
                file_path = project_path / filename
                file_path.touch()  # Создает файл(Пустой)
                print(f"{filename}")
                total_files += 1
            
            total_projects += 1
    
    # Результат
    print(f"Создано: {total_projects} проектов, {total_files} файлов")
    print(f"Папка: {portfolio_path.absolute()}")

if __name__ == "__main__":
    create_empty_portfolio()