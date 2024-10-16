## Configuración de git
git config

### Configuración del nombre del autor
git config --global user.name "Charly Mercury"

### Configuración del email del autor
git config --global user.email "carlos.mercury92@gmail.com"

### Configuración de la rama master a main
git config --global init.defaultBranch main

## Repositorio
Tres áreas: untracked files -> staging area -> git repository

## Inicializar un repositorio de git
git init

## Estado del repositorio
git status

## Agregar todos los archivos untracked al área de staging
git add -A

## Agregar un commit del área de staging a la base de datos de git
git commit -m " Message "



…or create a new repository on the command line
echo "# upv_clases" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:CharlyMercury/upv_clases.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin git@github.com:CharlyMercury/upv_clases.git
git branch -M main
git push -u origin main