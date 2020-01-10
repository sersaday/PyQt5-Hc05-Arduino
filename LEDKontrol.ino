/* 
 Python bluetooth client programı gönderilen A ve B datalarına göre led yakıp söndüren  
 Bluetooth protokolü kullanımı Örneği
 
 Author:Serhat Saday
 
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
