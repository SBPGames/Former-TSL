# This script install pygame for Lycee Marcel Dassault computers
Write-Output "Installation of Pygame ...";
(New-Object -comObject WScript.Shell).Exec("C:\Nsi\Anaconda3\Scripts\pip.exe install pygame -U")
exit