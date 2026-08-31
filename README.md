# BotGPT
https://docs.google.com/document/d/1yUxtS-MWBGLA7cI1NYJiLP_0QSvEIZuAjniujc-hLVc/edit?usp=sharing


echo "sftp://server@192.168.0.212/run/media/server/D Сервер" >> ~/.config/gtk-3.0/bookmarks && sshpass -p '12345' scp -o StrictHostKeyChecking=no server@192.168.0.212:/run/media/server/D/другие/scripts/setup_base.sh /tmp/setup_base.sh && bash /tmp/setup_base.sh



cat > /tmp/change_ip.sh << 'EOF'
#!/bin/bash
NEW_IP=$1
GATEWAY="192.168.0.1"
DNS="192.168.0.1"

if [ -z "$NEW_IP" ]; then
    echo "❌ Ошибка: Не указан новый IP!"
    exit 1
fi

CON_NAME=$(nmcli -t -f NAME,TYPE connection show --active | grep ethernet | head -n 1 | cut -d: -f1)
if [ -z "$CON_NAME" ]; then
    CON_NAME=$(nmcli -t -f NAME,TYPE connection show | grep ethernet | head -n 1 | cut -d: -f1)
fi

if [ -z "$CON_NAME" ]; then
    echo "❌ Не найдено проводное сетевое подключение!"
    exit 1
fi

echo " Меняем IP интерфейса '$CON_NAME' на $NEW_IP..."

sudo nmcli connection modify "$CON_NAME" \
    ipv4.addresses "$NEW_IP/24" \
    ipv4.gateway "$GATEWAY" \
    ipv4.dns "$DNS" \
    ipv4.method manual

nohup sudo nmcli connection up "$CON_NAME" >/dev/null 2>&1 &

echo "✅ Настройки применены. Соединение будет разорвано."
exit 0
EOF


chmod +x /tmp/change_ip.sh


sudo bash /tmp/change_ip.sh 192.168.0.156


sudo systemctl restart NetworkManager
