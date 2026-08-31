# BotGPT
https://docs.google.com/document/d/1yUxtS-MWBGLA7cI1NYJiLP_0QSvEIZuAjniujc-hLVc/edit?usp=sharing


echo "sftp://server@192.168.0.212/run/media/server/D Сервер" >> ~/.config/gtk-3.0/bookmarks && sshpass -p '12345' scp -o StrictHostKeyChecking=no server@192.168.0.212:/run/media/server/D/другие/scripts/setup_base.sh /tmp/setup_base.sh && bash /tmp/setup_base.sh



# Исправленная команда для sshd_config
sudo sed -i 's/^AllowUsers.*/AllowUsers lab202 kab303 server root/' /etc/ssh/sshd_config

# Правильная проверка UsePAM
if ! sudo grep -q "^UsePAM" /etc/ssh/sshd_config; then
    echo "UsePAM yes" | sudo tee -a /etc/ssh/sshd_config
fi

# Раздельные команды для chown и chmod
sudo chown root:utmp /var/log/btmp
sudo chmod 600 /var/log/btmp

# Перезапуск SSH
sudo systemctl restart sshd

# Проверка SSH
sshpass -p '12345' ssh -o StrictHostKeyChecking=no kab303@localhost "echo '✅ SSH РАБОТАЕТ'"
