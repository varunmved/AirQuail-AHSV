int dht = D2;
int rh = 0;
int temp = 0;

void setup() 
{
  Spark.variable("rh", &rh, INT);
  Spark.variable("temp", &temp, INT);
  pinMode(dht, INPUT_PULLUP);
}

void loop() 
{
  delay(10000);
  rh = read_dht(dht, &temp);
}

int read_dht(int pin, int *temperature)
{
    uint8_t data[5] = {0, 0, 0, 0, 0};

    noInterrupts();
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
    delay(20);
    pinMode(pin, INPUT_PULLUP);
    while (digitalRead(pin) == HIGH) {
        delayMicroseconds(10);
    }
    while (digitalRead(pin) == LOW) {
        delayMicroseconds(10);
    }
    while (digitalRead(pin) == HIGH) {
        delayMicroseconds(10);
    }
    for (uint8_t i = 0; i < 40; i++) {
        uint8_t counter = 0;
        while (digitalRead(pin) == LOW) {
            delayMicroseconds(10);
        }
        while (digitalRead(pin) == HIGH) {
            delayMicroseconds(10);
            counter++;
        }

        data[i/8] <<= 1;
        if (counter > 4) {
            data[i/8] |= 1;
        }
    }
    interrupts();

    if (data[4] != ((data[0] + data[1] + data[2] + data[3]) & 0xFF)) {
        *temperature = -254;
        return -1;
    }

    *temperature = data[2];
    return data[0];
}
