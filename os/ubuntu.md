* удобный терминал tilix
```
sudo apt install tilix
```
* ветка git в терминале
```
nano .bashrc
```
удалить
```
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
```
* заменить на
```
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
 PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\] $(parse_git_branch)\[\033[00m\]\$ '
else
 PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi
```
* сервера обновлений удалить ru.
```
cd etc/apt && sudo nano sources.list
```
* системный монитор в углу экрана
```
https://github.com/corecoding/Vitals
```
* смена раскладки клавиатуры
```
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Shift>Alt_L']"
```
```
Open Settings > Keyboard > Keyboard Shortcuts (View and Customise Shortcuts) > Typing to confirm changes.
```
* chrome
```
https://www.google.com/chrome/?platform=linux
```
```
sudo dpkg -i [version].deb
```
```
sudo apt --fix-broken install
```
