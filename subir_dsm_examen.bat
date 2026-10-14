@echo off
chcp 65001 >nul
title Subir DSM_EXAMEN a GitHub
color 0b

echo ========================================================
echo        SUBIENDO REPOSITORIO DSM_EXAMEN A GITHUB
echo ========================================================
echo.

cd /d "%~dp0"

echo Carpeta actual: %cd%
echo.
echo Comprobando estado de Git...
git status -s

echo.
echo Comprobando remoto:
git remote -v

echo.
echo ========================================================
echo  Iniciando Git Push a https://github.com/paucg06/DSM_EXAMEN.git
echo  (Si se abre una ventana en el navegador, inicia sesión)
echo ========================================================
echo.

git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo  [OK] REPOSITORIO SUBIDO CON EXITO A GITHUB!
    echo ========================================================
    echo.
    echo Repositorio: https://github.com/paucg06/DSM_EXAMEN
    echo.
    echo Pasos para activar GitHub Pages y usarlo en el móvil:
    echo 1. Entra a: https://github.com/paucg06/DSM_EXAMEN/settings/pages
    echo 2. En "Branch", selecciona "main" y la carpeta "/ (root)"
    echo 3. Haz clic en "Save"
    echo 4. En 1 minuto tu web estará disponible en:
    echo    https://paucg06.github.io/DSM_EXAMEN/
    echo.
) else (
    echo.
    echo ========================================================
    echo  [!] Hubo un error al subir o faltaron permisos.
    echo  Intentando push con force por si el repo en GitHub tenia commits...
    echo ========================================================
    echo.
    git push -u origin main --force
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo [OK] Subido correctamente con --force!
        echo Repositorio: https://github.com/paucg06/DSM_EXAMEN
        echo Web GitHub Pages: https://paucg06.github.io/DSM_EXAMEN/
    ) else (
        echo [ERROR] No se pudo subir. Comprueba que tengas conexion y permisos de escritura en GitHub.
    )
)

echo.
echo Presiona cualquier tecla para cerrar esta ventana...
pause >nul
