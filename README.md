# BotGPT
https://docs.google.com/document/d/1yUxtS-MWBGLA7cI1NYJiLP_0QSvEIZuAjniujc-hLVc/edit?usp=sharing


echo "sftp://server@192.168.0.212/run/media/server/D Сервер" >> ~/.config/gtk-3.0/bookmarks && sshpass -p '12345' scp -o StrictHostKeyChecking=no server@192.168.0.212:/run/media/server/D/другие/scripts/setup_base.sh /tmp/setup_base.sh && bash /tmp/setup_base.sh
# 1. Исправляем AllowUsers (разрешаем kab303)
sudo sed -i 's/^AllowUsers.*/AllowUsers lab202 kab303 server root/' /etc/ssh/sshd_config

# 2. Включаем UsePAM
sudo grep -q "^UsePAM" /etc/ssh/sshd_config || echo "UsePAM yes" | sudo tee -a /etc/ssh/sshd_config

# 3. Исправляем права на btmp (убираем ошибку из логов)
sudo chown root:utmp /var/log/btmp
sudo chmod 600 /var/log/btmp

# 4. Перезапускаем SSH
sudo systemctl restart sshd

# 5. Локальная проверка SSH
sshpass -p '12345' ssh -o StrictHostKeyChecking=no kab303@localhost "echo '✅ SSH РАБОТАЕТ'"

# 6. Скачиваем скрипт смены IP с сервера
sshpass -p '12345' scp -o StrictHostKeyChecking=no server@192.168.0.212:/run/media/server/D/другие/scripts/change_ip.sh /tmp/change_ip.sh

# 7. Меняем IP на новый
sudo bash /tmp/change_ip.sh 192.168.0.156
