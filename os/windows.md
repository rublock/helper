## Windows settings
* git branch in PowerShell
```
(new-object Net.WebClient).DownloadString("https://raw.githubusercontent.com/psget/psget/master/GetPsGet.ps1") | iex
```
```
Install-Module posh-git
```
```
Add-PoshGitToProfile
```


* install WSL virtual linux terminal on windows
* open PowerShell
```
wsl --install
```
> enjoy bash terminal
