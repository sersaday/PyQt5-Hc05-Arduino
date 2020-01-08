/* 
 Processing ile Android İşletim Sistemi Üzerinde
 Bluetooth protokolü kullanımı Örneği - 1
 
 Processing üzerinden gelen verilerle
 Arduino 8,9,10,11 nolu pinlere bağlı
 4 adet LED Kontrol ediliyor.
 A,C,E,G karakterleri geldiğinde LED'ler yakılıyor
 B,D,F,H karakterleri geldiğinde ise LED'ler söndürülüyor
 
 */

// LED bağlatı pinleri
int led = 8;
char gelenVeri;
void setup()
{
  pinMode(led,OUTPUT);


  Serial.begin(9600);
}

void loop()
{
  while(Serial.available()>0)
  {
    gelenVeri = Serial.read();
    switch(gelenVeri)
    {
    case 'A':
      digitalWrite(led,HIGH);
      break;
    case 'B':
      digitalWrite(led,LOW);
      break;
    
    }
  }
}
