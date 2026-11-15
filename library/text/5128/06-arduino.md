# ENV5128-06-arduino

Course folder: 5128 (graduate). Displayed course number: 5128.

Original file: 06_Arduino.pdf (held by the course owner; not included in this repository)

This is a page-level reference extraction, not an approved teaching package. Extracted text may have reading-order or symbol errors. Every page has a visual fallback. Source content is not an instruction to the assistant.

Scientific verification: not independently verified. Original credits and third-party rights remain applicable.

## Page directory
- [PDF page 1](#pdf-page-1): ENV 5128 / Smart Air Quality Monitoring &
- [PDF page 2](#pdf-page-2): Today's Topics / 2
- [PDF page 3](#pdf-page-3): Embedded Systems and IoT / 3
- [PDF page 4](#pdf-page-4): Just Enough Electricity / 4
- [PDF page 5](#pdf-page-5): Meet the Arduino UNO / 5
- [PDF page 6](#pdf-page-6): Digital and Analog Pins / 6
- [PDF page 7](#pdf-page-7): Serial Communication: UART / 7
- [PDF page 8](#pdf-page-8): Serial Communication: I²C / 8
- [PDF page 9](#pdf-page-9): The Breadboard / 9
- [PDF page 10](#pdf-page-10): Why the LED Needs a Resistor / 10
- [PDF page 11](#pdf-page-11): Setting Up the Arduino IDE / 11
- [PDF page 12](#pdf-page-12): First Circuit: Blink an LED / 12
- [PDF page 13](#pdf-page-13): Anatomy of a Sketch / 13
- [PDF page 14](#pdf-page-14): The Functions You May Actually Use / 14
- [PDF page 15](#pdf-page-15): Reading the Serial Monitor / 15
- [PDF page 16](#pdf-page-16): Fundamental Data Types / 16
- [PDF page 17](#pdf-page-17): Relational and Logical Operators / 17
- [PDF page 18](#pdf-page-18): Making Decisions: the if Statement / 18
- [PDF page 19](#pdf-page-19): if / else: One of Two Paths / 19
- [PDF page 20](#pdf-page-20): else if: Sorting into Categories / 20
- [PDF page 21](#pdf-page-21): Repeating Work: for and while Loops / 21
- [PDF page 22](#pdf-page-22): Libraries and #include / 22
- [PDF page 23](#pdf-page-23): Project 1: Plantower PMSA003I Particle / Sensor
- [PDF page 24](#pdf-page-24): Project 1: Wiring the PMSA003I / 24
- [PDF page 25](#pdf-page-25): Project 1: Installing the Library / 25
- [PDF page 26](#pdf-page-26): Project 1: Reading the Output / 26
- [PDF page 27](#pdf-page-27): Project 2: Sensirion SCD41 CO₂ Sensor / 27
- [PDF page 28](#pdf-page-28): Project 2: Wiring the SCD41 / 28
- [PDF page 29](#pdf-page-29): Project 2: Installing the Library / 29
- [PDF page 30](#pdf-page-30): Project 2: Reading the Output / 30
- [PDF page 31](#pdf-page-31): Saving Your Data to a File / 31
- [PDF page 32](#pdf-page-32): When It Does Not Work: A Checklist / 32


<a id="pdf-page-1"></a>
## PDF page 1

Source locator: `ENV5128-06-arduino`, PDF p. 1.

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Unclassified; inspect source.

Extraction flags: sparse-text

### Extracted source text

> ENV 5128
> Smart Air Quality Monitoring &
> Air Pollution Control


### Original page appearance

![ENV5128-06-arduino, PDF page 1](../../pages/ENV5128-06-arduino/page-0001.jpg)


<a id="pdf-page-2"></a>
## PDF page 2

Source locator: `ENV5128-06-arduino`, PDF p. 2.

Printed slide number candidate: 2 (use PDF page as canonical locator).

Generated navigation topics: Particles and aerosols, Ozone and atmospheric chemistry, IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Today's Topics
> 2
> •
> What an embedded system is
> •
> Just enough electricity to wire a circuit safely
> •
> How the Arduino UNO talks to sensors: UART and I2C
> •
> Writing, uploading, and reading the output of your first sketch
> •
> The C++ you actually need: variables, decisions, loops, libraries
> •
> Three air quality sensors: particulate matter, CO₂, and VOC
> •
> Expectation
> –
> Wire and program an Arduino to read an air quality sensor and log the data to a
> file
> –
> No prior electronics or programming experience is assumed


### Original page appearance

![ENV5128-06-arduino, PDF page 2](../../pages/ENV5128-06-arduino/page-0002.jpg)


<a id="pdf-page-3"></a>
## PDF page 3

Source locator: `ENV5128-06-arduino`, PDF p. 3.

Printed slide number candidate: 3 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Embedded Systems and IoT
> 3
> •
> Embedded system: computer hardware plus software built into a larger
> device to do one specific job (a thermostat, a car engine controller, an air
> monitor)
> –
> Fixed in capability, but programmable: you decide what the one job is
> •
> Internet of Things (IoT): embedded devices that report data over a network
> •
> An IoT air monitor is a four-step chain:
> –
> Sensor turns air into an electrical signal  →  microcontroller reads and converts it  →  data is
> stored or transmitted  →  you analyze it


### Original page appearance

![ENV5128-06-arduino, PDF page 3](../../pages/ENV5128-06-arduino/page-0003.jpg)


<a id="pdf-page-4"></a>
## PDF page 4

Source locator: `ENV5128-06-arduino`, PDF p. 4.

Printed slide number candidate: 4 (use PDF page as canonical locator).

Generated navigation topics: Unclassified; inspect source.

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Just Enough Electricity
> 4
> •
> Voltage (V, volts) – the electrical “push”. The UNO's pins work at 5 V
> •
> Current (I, amps) – how much charge actually flows. An indicator LED
> wants about 20 mA = 0.020 A
> •
> Resistance (R, ohms, Ω) – opposition to flow. A resistor is how you
> choose the current
> •
> Ohm's law:  V = I × R      (rearranged:  I = V / R)
> •
> Ground (GND, 0 V) – the common reference point that every voltage is
> measured against
> •
> Two rules that prevent most damage:
> –
> Current needs a complete loop: out of a pin, through the part, back to GND
> –
> Never connect 5 V straight to GND — that is a short circuit, and it can destroy the board
> –
> Any two devices that exchange signals must also share a ground connection


### Original page appearance

![ENV5128-06-arduino, PDF page 4](../../pages/ENV5128-06-arduino/page-0004.jpg)


<a id="pdf-page-5"></a>
## PDF page 5

Source locator: `ENV5128-06-arduino`, PDF p. 5.

Printed slide number candidate: 5 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Meet the Arduino UNO
> 5
> •
> Chip: ATmega328P, 8-bit, 16 MHz
> •
> Memory: 32 KB flash (your program), 2 KB SRAM
> (variables while running), 1 KB EEPROM (survives
> power off)
> •
> 14 digital pins (D0–D13)
> •
> 6 analog input pins (A0–A5)
> •
> Current limit: 20 mA per pin recommended (40 mA
> absolute max), 200 mA for the whole board
> •
> Power: USB cable (5 V) or barrel jack (7–12 V)
> •
> Built-in LED on pin 13 (LED_BUILTIN) — you can test
> the board with nothing wired
> •
> Reset button restarts your program from the top
> Board documentation: https://docs.arduino.cc/hardware/uno-rev3


### Original page appearance

![ENV5128-06-arduino, PDF page 5](../../pages/ENV5128-06-arduino/page-0005.jpg)


<a id="pdf-page-6"></a>
## PDF page 6

Source locator: `ENV5128-06-arduino`, PDF p. 6.

Printed slide number candidate: 6 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Digital and Analog Pins
> 6
> •
> Digital pins (D0–D13) – two states only
> –
> HIGH = 5 V, LOW = 0 V.  Set with digitalWrite(), read with digitalRead()
> •
> PWM pins (marked “~”: 3, 5, 6, 9, 10, 11)
> –
> Switch on and off very fast to imitate a voltage in between. analogWrite(pin, 0–255)
> –
> This is how you dim an LED; the UNO has no true analog output
> •
> Analog input pins (A0–A5)
> –
> Measure any voltage from 0 to 5 V. analogRead() returns a whole number 0–1023
> (10-bit)
> –
> Each step is about 5 V / 1024 ≈ 4.9 mV.  Voltage = analogRead(A0) * 5.0 / 1023.0
> •
> A4 and A5 double as the I2C data and clock pins — that is how today's
> sensors connect
> •
> D0 and D1 are the USB serial pins: leave them empty while uploading


### Original page appearance

![ENV5128-06-arduino, PDF page 6](../../pages/ENV5128-06-arduino/page-0006.jpg)


<a id="pdf-page-7"></a>
## PDF page 7

Source locator: `ENV5128-06-arduino`, PDF p. 7.

Printed slide number candidate: 7 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Serial Communication: UART
> 7
> •
> Universal Asynchronous Receiver-Transmitter — the
> simplest way two devices exchange bytes
> •
> Asynchronous means there is no shared clock wire, so
> both sides must be set to the same speed in advance
> •
> Connections:
> –
> TX (transmit) of one device → RX (receive) of the other
> — they cross over
> –
> RX ← TX in the other direction
> –
> Plus a shared GND. Three wires in practice, not two
> •
> Baud rate = bits per second (commonly 9600 or
> 115200). A mismatch produces garbage characters, not
> an error message
> •
> One frame = start bit, 5–9 data bits (usually 8), optional
> parity bit, 1–2 stop bits
> •
> Point-to-point only: one device talking to one other
> device


### Original page appearance

![ENV5128-06-arduino, PDF page 7](../../pages/ENV5128-06-arduino/page-0007.jpg)


<a id="pdf-page-8"></a>
## PDF page 8

Source locator: `ENV5128-06-arduino`, PDF p. 8.

Printed slide number candidate: 8 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Serial Communication: I²C
> 8
> •
> Inter-Integrated Circuit — the protocol all three sensors in this
> class use
> •
> Synchronous: one wire carries a clock, so both sides stay in
> step. No baud rate to agree on
> •
> Two signal wires, shared by every device:
> –
> SCL – serial clock: the timing signal, generated by the Arduino
> –
> SDA – serial data: the bits themselves, travelling in both directions
> –
> Plus power and a shared GND to each sensor
> •
> Many sensors share the same two wires. Each has its own
> address (usually 7-bit), so the board can call them one at a time
> •
> Both lines need pull-up resistors; breakout boards like Adafruit's
> already include them
> •
> On the Arduino UNO: SDA = A4, SCL = A5. The pins labeled
> SDA/SCL near AREF are the same two pins, not extra ones
> •
> Speed: 100 kHz standard, 400 kHz fast mode.


### Original page appearance

![ENV5128-06-arduino, PDF page 8](../../pages/ENV5128-06-arduino/page-0008.jpg)


<a id="pdf-page-9"></a>
## PDF page 9

Source locator: `ENV5128-06-arduino`, PDF p. 9.

Printed slide number candidate: 9 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> The Breadboard
> 9
> •
> Lets you build a circuit with no soldering: legs push into holes that are already connected underneath
> •
> Each short row of 5 holes is one connected node — two legs in the same row are joined
> •
> The channel down the middle separates left from right: a1 and f1 are NOT connected
> •
> The long rails on the sides (+ and −) run the length of the board: use them for 5 V and GND
> –
> On some boards the rails are split in the middle — check before relying on them
> •
> Wire the UNO's 5V pin to the + rail and GND to the − rail once, then take power from the rails
> •
> Most “my circuit does nothing” problems are two legs that look adjacent but sit in different rows


### Original page appearance

![ENV5128-06-arduino, PDF page 9](../../pages/ENV5128-06-arduino/page-0009.jpg)


<a id="pdf-page-10"></a>
## PDF page 10

Source locator: `ENV5128-06-arduino`, PDF p. 10.

Printed slide number candidate: 10 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Why the LED Needs a Resistor
> 10
> •
> An LED is not a resistor. Above its turn-on voltage the current climbs almost
> without limit, and the LED (or the Arduino pin) burns out
> •
> The resistor is what sets the current. Sizing it:
> –
> Red LED forward voltage ≈ 2 V; target current ≈ 20 mA = 0.020 A
> •
> The three resistors in your kit:
> –
> 220 Ω  →  about 14 mA, bright and safe (use this one)
> –
> red-red-brown-gold color band
> •
> Resistors have no polarity; LEDs do. Long leg = anode = positive side; short leg
> / flat edge = cathode = to GND


### Original page appearance

![ENV5128-06-arduino, PDF page 10](../../pages/ENV5128-06-arduino/page-0010.jpg)


<a id="pdf-page-11"></a>
## PDF page 11

Source locator: `ENV5128-06-arduino`, PDF p. 11.

Printed slide number candidate: 11 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Setting Up the Arduino IDE
> 11
> •
> The IDE (Integrated Development Environment) is where you write, compile and
> upload code
> •
> Install it, then before your first upload set two things:
> –
> Tools › Board › Arduino AVR Boards › Arduino Uno
> –
> Tools › Port → the port that appears only when the board is plugged in
> •
> If no port appears: try a different USB cable. Many cheap cables carry power
> only
> •
> Two buttons you will use constantly:
> –
> ✓Verify – compiles and checks for errors, without touching the board
> –
> → Upload – compiles, then sends the program to the board
> •
> File › Examples has hundreds of working sketches. Start from one, then modify
> it
> Download: https://www.arduino.cc/en/software   |   UNO R3 docs: https://docs.arduino.cc/hardware/uno-rev3
> |   Examples: https://docs.arduino.cc/built-in-examples/


### Original page appearance

![ENV5128-06-arduino, PDF page 11](../../pages/ENV5128-06-arduino/page-0011.jpg)


<a id="pdf-page-12"></a>
## PDF page 12

Source locator: `ENV5128-06-arduino`, PDF p. 12.

Printed slide number candidate: 12 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> First Circuit: Blink an LED
> 12
> •
> Parts: UNO, breadboard, red LED, 220 Ω resistor,
> two male-male jumper wires
> •
> Circuit:
> –
> Digital pin 13  →  220 Ω resistor  →  LED long leg
> (anode)
> –
> LED short leg (cathode)  →  GND
> •
> Do not power the LED from the 5V pin: that pin is
> always on, so it can never blink. The signal has to
> come from a pin your program controls
> •
> Open File › Examples › 01.Basics › Blink, check
> Board and Port, then Upload
> •
> Pin 13 also drives the small LED soldered to the
> board, so both blink together
> •
> Try it: change delay(1000) to delay(200) and
> upload again


### Original page appearance

![ENV5128-06-arduino, PDF page 12](../../pages/ENV5128-06-arduino/page-0012.jpg)


<a id="pdf-page-13"></a>
## PDF page 13

Source locator: `ENV5128-06-arduino`, PDF p. 13.

Printed slide number candidate: 13 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Anatomy of a Sketch
> 13
> •
> An Arduino program is called a sketch (.ino file).
> The language is C++ plus the Arduino library
> •
> Every sketch has exactly these two functions:
> –
> void setup()  – runs once, when the board powers
> up or is reset. Put pinMode() and Serial.begin()
> here
> –
> void loop()  – runs over and over, forever, until
> power is removed
> •
> void means the function hands nothing back to the
> caller
> •
> Every statement ends with a semicolon;  braces { }
> group the statements that belong together
> •
> Case matters: setup, not Setup
> •
> Comments are ignored by the board:  // to end of
> line,  /* ... */ for a block


### Original page appearance

![ENV5128-06-arduino, PDF page 13](../../pages/ENV5128-06-arduino/page-0013.jpg)


<a id="pdf-page-14"></a>
## PDF page 14

Source locator: `ENV5128-06-arduino`, PDF p. 14.

Printed slide number candidate: 14 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> The Functions You May Actually Use
> 14
> •
> pinMode(pin, OUTPUT | INPUT) – set a pin's role; call it in
> setup()
> •
> digitalWrite(pin, HIGH | LOW) – put 5 V or 0 V on an output
> pin
> •
> digitalRead(pin) – returns HIGH or LOW
> •
> analogRead(A0) – measure 0–5 V, returns 0–1023
> •
> analogWrite(pin, 0–255) – PWM output on a “~” pin
> •
> delay(ms) – wait. Nothing else runs during a delay; the
> board is frozen
> •
> Serial.begin(9600) – open the link to your computer.
> Required before any printing
> •
> Serial.print(x) – send text, stay on the same line
> •
> Serial.println(x) – same, then start a new line
> –
> Spelled p-r-i-n-t-l-n, lowercase L then N. Not printIn with a
> capital i
> •
> #include <xxx.h> – pull in an outside library. No semicolon
> on #include lines
> Serial is the link between the board and
> your computer — not between the board
> and the sensors. Sensors use I²C.


### Original page appearance

![ENV5128-06-arduino, PDF page 14](../../pages/ENV5128-06-arduino/page-0014.jpg)


<a id="pdf-page-15"></a>
## PDF page 15

Source locator: `ENV5128-06-arduino`, PDF p. 15.

Printed slide number candidate: 15 (use PDF page as canonical locator).

Generated navigation topics: Particles and aerosols, IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Reading the Serial Monitor
> 15
> •
> The Serial Monitor is a text window in the IDE showing whatever the board
> prints, over the same USB cable used to upload
> •
> Two numbers must match, or you see nothing useful:
> –
> Serial.begin(9600) in your sketch
> –
> The baud dropdown at the bottom right of the Serial Monitor window
> –
> A mismatch shows random symbols, not an error message
> •
> A minimal example:
> void setup() { Serial.begin(9600); }
> void loop() { Serial.print("PM2.5: "); Serial.println(12.4);
> delay(1000); }
> •
> Serial.print(value, 2) prints a decimal number with 2 places
> •
> Only one program can hold the COM port at a time. Close the Serial Monitor
> before uploading from another tool, and close PuTTY before using the Serial
> Monitor


### Original page appearance

![ENV5128-06-arduino, PDF page 15](../../pages/ENV5128-06-arduino/page-0015.jpg)


<a id="pdf-page-16"></a>
## PDF page 16

Source locator: `ENV5128-06-arduino`, PDF p. 16.

Printed slide number candidate: 16 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Fundamental Data Types
> 16
> •
> Every variable is declared with a type before it is used, and every statement ends with a
> semicolon
> •
> bool – true or false.  bool sensorReady = false;
> •
> char – a single character in single quotes.  char grade = 'A';
> •
> int – whole number. On the UNO it is 16-bit: −32,768 to 32,767
> –
> Sums of sensor readings overflow this range quickly — use long when in doubt
> •
> unsigned int / uint16_t – whole number 0 to 65,535 (note the lowercase u in uint16_t)
> •
> long – 32-bit whole number, about ±2.1 billion.
> •
> float – decimal number, roughly 6–7 significant digits.  float temp = 23.41;
> •
> double – on the Arduino UNO, double is identical to float. There is no extra precision on
> this 8-bit chip
> –
> Note the same on 32-bit boards such as the Due or ESP32
> •
> String / char array – text. String is convenient but can fragment the UNO's 2 KB of
> memory during long runs


### Original page appearance

![ENV5128-06-arduino, PDF page 16](../../pages/ENV5128-06-arduino/page-0016.jpg)


<a id="pdf-page-17"></a>
## PDF page 17

Source locator: `ENV5128-06-arduino`, PDF p. 17.

Printed slide number candidate: 17 (use PDF page as canonical locator).

Generated navigation topics: Particles and aerosols, Policy and management context

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Relational and Logical Operators
> 17
> Operator
> Meaning
> Example
> >
> Greater than
> pm25 > 35.0  is true when PM2.5 exceeds the daily standard
> <
> Less than
> 7 < 5  is false
> >=
> Greater than or equal to
> 2 >= 2  is true
> <=
> Less than or equal to
> 2 <= 1  is false
> ==
> Equal to (comparison)
> reading == 0  is true only when reading is zero
> !=
> Not equal to
> 6 != 6  is false
> &&
> Logical AND – both must be true
> co2 > 1000 && humidity < 60
> ||
> Logical OR – either may be true
> pm25 > 35 || pm10 > 150
> !
> Logical NOT – reverses true and
> false
> if (!aqi.read(&data))  — “if the read did not succeed”
> = assigns a value, == compares two values.  if (x = 5) quietly sets x to 5 and is always true — the most common
> beginner bug in C++.


### Original page appearance

![ENV5128-06-arduino, PDF page 17](../../pages/ENV5128-06-arduino/page-0017.jpg)


<a id="pdf-page-18"></a>
## PDF page 18

Source locator: `ENV5128-06-arduino`, PDF p. 18.

Printed slide number candidate: 18 (use PDF page as canonical locator).

Generated navigation topics: Particles and aerosols

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Making Decisions: the if Statement
> 18
> •
> if runs a block of code only when a condition is
> true
> if (condition) {
> // statements that run only when
> the condition is true
> }
> •
> The condition goes in round brackets; the
> code goes in curly braces
> •
> No semicolon after the closing brace
> •
> An air quality example:
> if (pm25 > 35.0) { Serial.println("Above
> the 24-hour PM2.5 standard"); }


### Original page appearance

![ENV5128-06-arduino, PDF page 18](../../pages/ENV5128-06-arduino/page-0018.jpg)


<a id="pdf-page-19"></a>
## PDF page 19

Source locator: `ENV5128-06-arduino`, PDF p. 19.

Printed slide number candidate: 19 (use PDF page as canonical locator).

Generated navigation topics: Unclassified; inspect source.

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> if / else: One of Two Paths
> 19
> •
> else gives the alternative when the condition is
> false. Exactly one of the two blocks runs
> if (someCondition) {
> // runs when the condition is
> true
> } else {
> // runs when it is false
> }
> •
> else never has a condition of its own — it
> catches everything the if did not


### Original page appearance

![ENV5128-06-arduino, PDF page 19](../../pages/ENV5128-06-arduino/page-0019.jpg)


<a id="pdf-page-20"></a>
## PDF page 20

Source locator: `ENV5128-06-arduino`, PDF p. 20.

Printed slide number candidate: 20 (use PDF page as canonical locator).

Generated navigation topics: Policy and management context

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> else if: Sorting into Categories
> 20
> •
> Chain conditions to sort a value into ranges, such as AQI
> categories
> if (condition1) {
> // runs when condition1 is true
> } else if (condition2) {
> // runs when condition1 was false and
> condition2 is true
> } else {
> // runs when none of the above matched
> }
> •
> Order matters: conditions are checked top to bottom and the
> first match wins, so the rest are skipped


### Original page appearance

![ENV5128-06-arduino, PDF page 20](../../pages/ENV5128-06-arduino/page-0020.jpg)


<a id="pdf-page-21"></a>
## PDF page 21

Source locator: `ENV5128-06-arduino`, PDF p. 21.

Printed slide number candidate: 21 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Repeating Work: for and while Loops
> 21
> •
> for – use when you know how many repetitions
> you want
> for (int i = 0; i < 10; i++) { ... }
> –
> Three parts: start value; condition checked before
> each pass; step taken after each pass
> •
> while – use when you repeat until something
> changes
> –
> while (condition) { ... }  repeats as long as the
> condition stays true
> –
> If the condition never becomes false the sketch
> stops there forever
> •
> do { ... } while (condition);  always runs at least once
> before checking
> •
> You rarely need an outer infinite loop on Arduino:
> loop() already repeats forever
> •
> Practical use: a for loop that takes 10 sensor
> readings and averages them before printing


### Original page appearance

![ENV5128-06-arduino, PDF page 21](../../pages/ENV5128-06-arduino/page-0021.jpg)


<a id="pdf-page-22"></a>
## PDF page 22

Source locator: `ENV5128-06-arduino`, PDF p. 22.

Printed slide number candidate: 22 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Libraries and #include
> 22
> •
> A library is code someone else wrote that handles the low-
> level details of a specific chip.
> •
> Installing one:
> –
> Tools › Manage Libraries… (the Library Manager), search
> the name, click Install
> –
> Accept the prompt to install dependencies — Adafruit
> libraries usually need Adafruit BusIO and Adafruit Unified
> Sensor
> •
> Using one:
> –
> #include <Adafruit_PM25AQI.h>  at the top of the sketch.
> No semicolon on #include lines
> –
> Wire.h is the built-in I²C library; sensor libraries call it for
> you
> •
> File › Examples › [library name] gives working starter
> sketches. Upload one unchanged first, confirm it works,
> then modify it
> •
> If compiling fails with “no such file or directory”, the library
> is not installed or the name is misspelled


### Original page appearance

![ENV5128-06-arduino, PDF page 22](../../pages/ENV5128-06-arduino/page-0022.jpg)


<a id="pdf-page-23"></a>
## PDF page 23

Source locator: `ENV5128-06-arduino`, PDF p. 23.

Printed slide number candidate: 23 (use PDF page as canonical locator).

Generated navigation topics: Measurement methods and instruments, Particles and aerosols

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 1: Plantower PMSA003I Particle
> Sensor
> 23
> •
> An optical particle counter (OPC)
> •
> How it works:
> –
> A small fan pulls a stream of air past a laser beam
> –
> Each particle scatters light onto a photodiode, and the
> pulse size indicates the particle's size
> –
> Firmware sorts the counts into size bins and converts
> count to mass concentration (µg/m3) using an assumed
> particle density and shape
> •
> Reports PM1.0, PM2.5 and PM10 in µg/m3, plus particle
> counts per 0.1 L of air
> •
> Know the limits:
> –
> Mass is inferred from counts, not weighed
> –
> Readings inflate at high humidity because particles
> absorb water and grow
> –
> Not an FRM or FEM instrument


### Original page appearance

![ENV5128-06-arduino, PDF page 23](../../pages/ENV5128-06-arduino/page-0023.jpg)


<a id="pdf-page-24"></a>
## PDF page 24

Source locator: `ENV5128-06-arduino`, PDF p. 24.

Printed slide number candidate: 24 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 1: Wiring the PMSA003I
> 24
> Sensor pin
> Wire
> Arduino UNO pin
> VIN (labeled VCC on some
> boards)
> Red
> 5V
> GND
> Black
> GND
> SCL
> Yellow
> A5  (= the SCL pin)
> SDA
> Blue
> A4  (= the SDA pin)
> •
> Unplug the USB cable while you wire.
> •
> Connect power and ground first, then the two signal
> wires
> •
> A4/A5 and the SDA/SCL pins near AREF are the
> same two pins — use one pair, not both
> •
> Yellow and blue swapped is the single most common
> wiring mistake
> Wiring guide: https://learn.adafruit.com/pmsa003i/arduino


### Original page appearance

![ENV5128-06-arduino, PDF page 24](../../pages/ENV5128-06-arduino/page-0024.jpg)


<a id="pdf-page-25"></a>
## PDF page 25

Source locator: `ENV5128-06-arduino`, PDF p. 25.

Printed slide number candidate: 25 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming, Policy and management context

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 1: Installing the Library
> 25
> •
> Tools › Manage Libraries… → search “Adafruit PM25 AQI” → Install
> •
> Accept the dependency prompt (Adafruit BusIO). Wire.h is already built in
> •
> Then open File › Examples › Adafruit PM25 AQI Sensor › pm25_test and upload it
> unchanged
> •
> Set the Serial Monitor to 115200 baud for this example, not 9600
> Code and library: https://learn.adafruit.com/pmsa003i/arduino


### Original page appearance

![ENV5128-06-arduino, PDF page 25](../../pages/ENV5128-06-arduino/page-0025.jpg)


<a id="pdf-page-26"></a>
## PDF page 26

Source locator: `ENV5128-06-arduino`, PDF p. 26.

Printed slide number candidate: 26 (use PDF page as canonical locator).

Generated navigation topics: Measurement methods and instruments, Particles and aerosols, IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 1: Reading the Output
> 26
> •
> “PM25 found!” confirms the sensor answered on the I2C bus. If it never appears, the problem is wiring or
> power, not code
> •
> Concentration units are µg/m3, reported two ways:
> –
> Standard – corrected to a reference atmosphere, used for comparing instruments
> –
> Environmental – at the actual ambient conditions. Near sea level the two are close
> •
> Particle counts are per 0.1 L of air and are cumulative: the “> 0.3 µm” figure includes every larger size
> too
> Code and library: https://learn.adafruit.com/pmsa003i/arduino


### Original page appearance

![ENV5128-06-arduino, PDF page 26](../../pages/ENV5128-06-arduino/page-0026.jpg)


<a id="pdf-page-27"></a>
## PDF page 27

Source locator: `ENV5128-06-arduino`, PDF p. 27.

Printed slide number candidate: 27 (use PDF page as canonical locator).

Generated navigation topics: Sensors calibration and data quality

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 2: Sensirion SCD41 CO₂ Sensor
> 27
> •
> A photoacoustic NDIR sensor
> •
> How it works:
> –
> An infrared source is pulsed on and off inside a small
> chamber
> –
> CO2 absorbs infrared light strongly near 4.3 µm, so the gas
> warms and expands in pulses
> –
> A tiny microphone hears that pressure wave. A louder
> signal means more CO2
> •
> Also reports temperature and relative humidity from an
> on-chip sensor
> •
> Range 400–5000 ppm; accuracy about ±(40 ppm + 5% of
> the reading)
> •
> Self-heating raises the reported temperature; the library
> has a temperature offset setting to correct it
> •
> Automatic self-calibration assumes the sensor sees fresh
> ~400 ppm air regularly. In a room that is never aired out,
> turn it off or the baseline drifts
> Outdoor background is about 420 ppm today. Indoors, above roughly
> 1000 ppm means the ventilation is not keeping up.


### Original page appearance

![ENV5128-06-arduino, PDF page 27](../../pages/ENV5128-06-arduino/page-0027.jpg)


<a id="pdf-page-28"></a>
## PDF page 28

Source locator: `ENV5128-06-arduino`, PDF p. 28.

Printed slide number candidate: 28 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 2: Wiring the SCD41
> 28
> Sensor pin
> Wire
> Arduino UNO pin
> VIN (labeled VCC on some
> boards)
> Red
> 5V
> GND
> Black
> GND
> SCL
> Yellow
> A5  (= the SCL pin)
> SDA
> Blue
> A4  (= the SDA pin)
> •
> Identical I2C wiring to Project 1. Because each
> sensor has its own address, both can share the
> same A4/A5 pair at the same time
> •
> The Adafruit breakout accepts 3–5 V on VIN and
> includes the pull-up resistors
> •
> Give the sensor a minute to settle after power-up
> before trusting a reading
> Wiring guide: https://learn.adafruit.com/adafruit-scd-40-and-scd-41


### Original page appearance

![ENV5128-06-arduino, PDF page 28](../../pages/ENV5128-06-arduino/page-0028.jpg)


<a id="pdf-page-29"></a>
## PDF page 29

Source locator: `ENV5128-06-arduino`, PDF p. 29.

Printed slide number candidate: 29 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 2: Installing the Library
> 29
> •
> Tools › Manage Libraries… → search “Sensirion I2C SCD4x” → Install
> •
> Sensirion's library covers the whole SCD4x family (SCD40 and SCD41)
> •
> The Adafruit SCD4x library is an equally good alternative — pick one, and match
> the example sketch to it
> •
> Start with the example sketch, confirm readings appear, then edit
> Code and library: https://learn.adafruit.com/adafruit-scd-40-and-scd-41


### Original page appearance

![ENV5128-06-arduino, PDF page 29](../../pages/ENV5128-06-arduino/page-0029.jpg)


<a id="pdf-page-30"></a>
## PDF page 30

Source locator: `ENV5128-06-arduino`, PDF p. 30.

Printed slide number candidate: 30 (use PDF page as canonical locator).

Generated navigation topics: Unclassified; inspect source.

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Project 2: Reading the Output
> 30
> •
> Three values per reading: CO2 in ppm, temperature in °C, relative humidity in %
> •
> The SCD41 produces a new reading about every 5 seconds in normal periodic mode; reading
> faster returns the same value twice
> •
> A CO2 value of 0 usually means the reading was requested before it was ready, not that the air
> is clean
> •
> The temperature will read a degree or two high because the sensor heats itself
> Code and library: https://learn.adafruit.com/adafruit-scd-40-and-scd-41


### Original page appearance

![ENV5128-06-arduino, PDF page 30](../../pages/ENV5128-06-arduino/page-0030.jpg)


<a id="pdf-page-31"></a>
## PDF page 31

Source locator: `ENV5128-06-arduino`, PDF p. 31.

Printed slide number candidate: 31 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Saving Your Data to a File
> 31
> •
> The Serial Monitor displays data but does not save it.
> PuTTY can do both
> •
> Close the Arduino Serial Monitor first — only one
> program can hold the COM port at a time
> •
> In PuTTY:
> –
> Session → Connection type: Serial
> –
> Serial line: your COM port (the same one shown in Tools ›
> Port)
> –
> Speed: must match the number in your Serial.begin() call
> –
> Session › Logging → choose “All session output” and a
> file name, then click Open
> •
> Without the Logging step PuTTY only displays the data;
> nothing is written to disk
> •
> Print comma-separated values from the sketch and the
> log opens directly as a CSV
> Download PuTTY: https://www.putty.org/


### Original page appearance

![ENV5128-06-arduino, PDF page 31](../../pages/ENV5128-06-arduino/page-0031.jpg)


<a id="pdf-page-32"></a>
## PDF page 32

Source locator: `ENV5128-06-arduino`, PDF p. 32.

Printed slide number candidate: 32 (use PDF page as canonical locator).

Generated navigation topics: IoT and programming

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> When It Does Not Work: A Checklist
> 32
> •
> Upload fails or no port listed – wrong Board or Port in Tools; a power-only USB cable; the Serial
> Monitor or PuTTY is holding the port
> •
> Serial Monitor shows random symbols – the baud dropdown does not match your Serial.begin()
> value
> •
> Serial Monitor is empty – no Serial.begin() in setup(), or nothing is printed inside loop()
> •
> “Sensor not found” – check VIN and GND first, then that SDA and SCL are not swapped, then that
> the sensor and board share a ground
> •
> Circuit does nothing – two legs that look adjacent are in different breadboard rows, or the connection
> crosses the center channel
> •
> LED will not light – reversed polarity. Flip it: long leg toward the resistor and 5 V side
> •
> Code compiles but the board seems frozen – a delay() far longer than you meant, or a while loop
> whose condition never becomes false
> •
> “No such file or directory” – the library is not installed, or the #include name is misspelled
> •
> Everything looks right and still fails – unplug, rewire from scratch, and upload a known-good
> example sketch before debugging your own code
> Case matters everywhere in C++: Serial.println, not serial.println or Serial.printIn.


### Original page appearance

![ENV5128-06-arduino, PDF page 32](../../pages/ENV5128-06-arduino/page-0032.jpg)

