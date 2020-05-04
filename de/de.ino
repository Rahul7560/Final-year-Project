char serialdata;

int green_one=13,yellow_one=2,red_one=3,green_two=4,yellow_two=5,red_two=6;
int green_th=7,yellow_th=8,red_th=9,green_fr=10,yellow_fr=11,red_fr=12;

void setup()
{
  pinMode(green_one,OUTPUT);
  pinMode(green_two,OUTPUT);
  pinMode(green_th,OUTPUT);
  pinMode(green_fr,OUTPUT);
  pinMode(yellow_one,OUTPUT);
  pinMode(yellow_two,OUTPUT);
  pinMode(yellow_th,OUTPUT);
  pinMode(yellow_fr,OUTPUT);
  pinMode(red_one,OUTPUT);
  pinMode(red_two,OUTPUT);
  pinMode(red_th,OUTPUT);
  pinMode(red_fr,OUTPUT);
  
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()>0)
  {
    serialdata=Serial.read();
    Serial.print(serialdata);
    
    if (serialdata=='A')
    {
      digitalWrite(green_one,HIGH);
    }
    else if(serialdata=='B')
    {
      digitalWrite(green_one,LOW);
    }
    else if (serialdata=='C')
    {
      digitalWrite(yellow_one,HIGH);
    }
    else if(serialdata=='D')
    {
      digitalWrite(yellow_one,LOW);
    }
    else if (serialdata=='E')
    {
      digitalWrite(red_one,HIGH);
    }
    else if(serialdata=='F')
    {
      digitalWrite(red_one,LOW);
    }
    
    
    
    else if (serialdata=='G')
    {
      digitalWrite(green_two,HIGH);
    }
    else if(serialdata=='H')
    {
      digitalWrite(green_two,LOW);
    }
     else if (serialdata=='I')
    {
      digitalWrite(yellow_two,HIGH);
    }
    else if(serialdata=='J')
    {
      digitalWrite(yellow_two,LOW);
    }
      else if (serialdata=='K')
    {
      digitalWrite(red_two,HIGH);
    }
    else if(serialdata=='L')
    {
      digitalWrite(red_two,LOW);
    }
    
    
    
    
    
    
    else if (serialdata=='M')
    {
      digitalWrite(green_th,HIGH);
    }
    else if(serialdata=='N')
    {
      digitalWrite(green_th,LOW);
    }
     else if (serialdata=='O')
    {
      digitalWrite(yellow_th,HIGH);
    }
    else if(serialdata=='P')
    {
      digitalWrite(yellow_th,LOW);
    }
      else if (serialdata=='Q')
    {
      digitalWrite(red_th,HIGH);
    }
    else if(serialdata=='R')
    {
      digitalWrite(red_th,LOW);
    }
    
    
    
    
    
    
    
    else if (serialdata=='S')
    {
      digitalWrite(green_fr,HIGH);
    }
    else if(serialdata=='T')
    {
      digitalWrite(green_fr,LOW);
    }
     else if (serialdata=='U')
    {
      digitalWrite(yellow_fr,HIGH);
    }
    else if(serialdata=='V')
    {
      digitalWrite(yellow_fr,LOW);
    }
      else if (serialdata=='W')
    {
      digitalWrite(red_fr,HIGH);
    }
    else if(serialdata=='X')
    {
      digitalWrite(red_fr,LOW);
    }
  }
}
