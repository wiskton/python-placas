wget -O - https://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
echo "deb https://deb.openalpr.com/master/ trusty main" | sudo tee /etc/apt/sources.list.d/openalpr.list
sudo apt-get update
sudo apt-get install openalpr openalpr-daemon openalpr-utils libopenalpr-dev
sudo cp br.conf /usr/share/openalpr/runtime_data/config/