@echo off

:: Script para flashear y cargar archivos a la esp32
:: Autor: Carlos Tovar
:: Fecha: 19/11/24

:: Configuración Inicial
set PORT=COM3
set CHIP=esp32
set BAUD=460800
set BIN_PATH=.\ESP32_GENERIC-20241129-v1.24.1.bin

echo.
echo.
echo.
echo -------------------------
echo Activando Environment
echo -------------------------
call ..\..\venv\Scripts\activate.bat
echo.
echo.
echo.


echo ================================================
echo          Proceso de Configuracion del ESP32      
echo ================================================
echo.
echo.
echo.

echo [Paso 1] Borrando la flash...
echo.
esptool --chip %CHIP% --port %PORT% erase_flash
if %errorlevel% neq 0 (
    echo Error al borrar el flash. Verifica la conexion y vuelve a intentarlo.
    pause
    exit /b
)
echo.
echo.
echo.


echo [Paso 2] Flasheando el firmware...
echo.
esptool --chip %CHIP% --port %PORT% --baud %BAUD% write_flash -z 0x1000 %BIN_PATH%
if %errorlevel% neq 0 (
    echo Error al flashear el firmware. Verifica la conexion y vuelve a intentarlo.
    pause
    exit /b
)
echo.
echo.
echo.


echo [Paso 3] Subiendo archivos Python al ESP32...
echo.
cd src

ampy --port %PORT% put device_cert.crt
echo [Paso 3.1] device cert uploaded
ampy --port %PORT% put private.key
echo [Paso 3.2] private key uploaded
ampy --port %PORT% put root.pem
echo [Paso 3.2] root uploaded
ampy --port %PORT% put main.py
echo [Paso 3.4] main script uploaded
ampy --port %PORT% put simple.py
echo [Paso 3.5] simple.py uploaded
ampy --port %PORT% put mh_z19.py
echo [Paso 3.5] mh_z19.py uploaded


echo.
echo ================================================
echo       Proceso completado exitosamente.         
echo ================================================