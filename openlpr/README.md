REFERENCE:
http://doc.openalpr.com/opensource.html

UBUNTU REQUIREMENTS:
$ wget -O - https://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
$ echo "deb https://deb.openalpr.com/master/ trusty main" | sudo tee /etc/apt/sources.list.d/openalpr.list
$ sudo apt-get update
$ sudo apt-get install openalpr openalpr-daemon openalpr-utils libopenalpr-dev
$ sudo cp br.conf /usr/share/openalpr/runtime_data/config/

USAGE:
$ alpr -c br ../imgs/5.jpg

FIX PROBLEMS:
For te error:
Error opening data file /usr/share/openalpr/runtime_data/ocr/lus.traineddata
Please make sure the TESSDATA_PREFIX environment variable is set to your "tes
Failed loading language 'lus'
Tesseract couldn't load any languages!
Segmentation fault (core dumped)

Execute the following command:
sudo cp /usr/share/openalpr/runtime_data/ocr/tessdata/*.traineddata /usr/share/openalpr/runtime_data/ocr/


GITHUB ISSUE:
https://github.com/openalpr/openalpr/issues/124
