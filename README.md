         Ubuntu işletim sistemi için bluetooth istemcisi örneğidir. 









1-Ubuntu için bluetooth python kütüphanesi pybluez'dir.

		pip install PyBluez

2-PyQt5 kütüphanesi conda veya pip yardımı ile python'a yüklenir.

		conda install -c anaconda pyqt

3-Blueman bluetooth yönetimi programı ubuntuya yüklenir.
		sudo apt-get update -y

		sudo apt-get install -y blueman

4-blueman bluetooth yöneticinde Hc05 bulunur şifresi yazılır.Eşleştirme sağlanır.(genellikle şifre :1234'dür.)


5 LedKontrol.ino adlı dosya arduino programı yolu ile arduinoya yüklenir. 


5-Uç birim komut satırından aynı dizinde olmak üzere ( python PyQt5_Hc05.py )yazılıp entere basılır.  




# PyQt5-Hc05-Arduino 
