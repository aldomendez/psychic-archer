title "Programando Rutinas"
@echo off
cls
echo "Programando..."
at 15:15 powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\notify.wav").PlaySync();
echo "Programado"
::pause>null
