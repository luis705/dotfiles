cp ~/.bashrc .
cp ~/.profile .
cp ~/.gitconfig .
cp ~/.gtkrc-2.0 .
cp ~/.Xresources .

# Temas
cp -R ~/.themes .
rm -rf .themes/gruvbox-gtk/.git
cp -R ~/.icons .
rm -rf .icons/gruvbox-dark-icons-gtk/.git

# Config
cp -r ~/.config/i3 .config/
cp -r ~/.config/rofi .config/
cp -r ~/.config/terminator .config/


# Wallpapers
cp -r ~/wallpapers ./

# Packages
pacman -Qtdq | sudo pacman -Rns -
pacman -Qqen > install/pacman_all.txt
pip freeze > install/pip_install.txt
