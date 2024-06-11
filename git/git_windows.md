## Git windows

```
isort . | black -l 99 . | git add . | git commit -m 'commit' | git push
```

* install git
``` 
# get latest download url for git-for-windows 64-bit exe
$git_url = "https://api.github.com/repos/git-for-windows/git/releases/latest"
$asset = Invoke-RestMethod -Method Get -Uri $git_url | % assets | where name -like "*64-bit.exe"
# download installer
$installer = "$env:temp\$($asset.name)"
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $installer
# run installer
$git_install_inf = "<install inf file>"
$install_args = "/SP- /VERYSILENT /SUPPRESSMSGBOXES /NOCANCEL /NORESTART /CLOSEAPPLICATIONS /RESTARTAPPLICATIONS /LOADINF=""$git_install_inf"""
Start-Process -FilePath $installer -ArgumentList $install_args -Wait
```
* install colored brances, see instructions
```
https://github.com/dahlbyk/posh-git
```
* ssh
```
ssh-keygen -o
```
```
cat ~/.ssh/id_rsa.pub
```
* copy ssh public key and paste into github.com
```
rm ~/.ssh/known_hosts
```