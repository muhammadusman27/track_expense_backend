import os
BASE_DIR = os.getcwd()  # current working directory of your shell_plus session
for app_name in os.listdir(BASE_DIR):
    app_path = os.path.join(BASE_DIR, app_name)
    migrations_path = os.path.join(app_path, 'migrations')
    if os.path.isdir(migrations_path):
        for file_name in os.listdir(migrations_path):
            file_path = os.path.join(migrations_path, file_name)
            if file_name != '__init__.py' and (file_name.endswith('.py') or file_name.endswith('.pyc')):
                os.remove(file_path)
                print(f"Deleted: {file_path}")