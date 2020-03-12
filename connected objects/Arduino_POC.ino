const int debit = 9600; // On défini le debit dans une variable
const int L1 = 8; // broche 8 du micro-contrôleur se nomme maintenant : L1

byte texte; // Variable pour contenir le texte reçu

void setup() { // Fonction d'initilisation de la carte
  pinMode(L1, OUTPUT); //L1 est une broche de sortie
  Serial.begin(debit); // On initialise la liaison série
}

void loop() // Fonction principale, elle se répète (s’exécute) à l'infini
{
  while (Serial.available()) // On attend des messages sur la liason série
  {
    while (Serial.available()) // On attend des messages sur la liason série
    {
      texte = Serial.read(); // Stockage des messages dans texte
      if(texte==72)
      {
        digitalWrite(L1, HIGH); //allumer L1
      }
      if(texte==76)
      {
        digitalWrite(L1, LOW); //allumer L1
      }
      //Serial.println(texte);
      delay(10);
    }
    /*
    if(texte=="ON")
    {
      digitalWrite(L1, HIGH); //allumer L1
    }
    delay(10);
    */

  }
}
