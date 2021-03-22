# Instalando programas e bibliotecas
sudo pacman -S --noconfirm - < pacman_all.txt
pip3 install -r pip_install.txt

# Configurações básicas
cp ../.bashrc ~/
cp ../.profile ~/
cp ../.gitconfig ~/
cp ../.gtkrc-2.0 ~/
cp ../.Xresources ~/

# Temas
cd -R ../.themes ~/
cp -R ../.icons ~/

# Pasta config
cp -r .config/* ~/.config

# Wallpapers
cp ../wallpapers ~/


# Utilitarios
cp xfce4-sccreenshoter ~/
