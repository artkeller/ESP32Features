# ESP32Features
Übersichtstabelle mit den aktuellen ESP32-Modellen basierend auf den offiziellen Espressif-Datasheets (Stand September 2025)

- [Deep-Sleep](#deep-sleep)
  - [Details](#details)
- [Referenzen](#referenzen)
- [Vor-/Nachteile](#vor-nachteile)
  - [ESP32](#esp32-1)
  - [ESP32-S2](#esp32-s2-1)
  - [ESP32-S3](#esp32-s3-1)
  - [ESP32-C3](#esp32-c3-1)
  - [ESP32-C2](#esp32-c2-1)
  - [ESP32-C5](#esp32-c5-1)
  - [ESP32-C6](#esp32-c6-1)
  - [ESP32-H2](#esp32-h2-1)
  - [ESP32-P4](#esp32-p4-1)
- [Anwendungsbewertung](#anwendungsbewertung)


## Übersicht der wichtigsten Eigenschaften

| Modell     | Architektur (Kerne, Clock min/max, LP/ULP) | Embedded SRAM | Embedded Flash/PSRAM-Optionen (Kombos) | Max PSRAM (embedded/external, Future) | Max Flash (embedded/external, Future) | Radio (Varianten)                          | Interfaces (Auswahl: Anzahl, Typ) |
|------------|--------------------------------------------|---------------|----------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|-----------------------------------|
| ESP32     | Dual Xtensa LX6, 80-240 MHz, keine dedizierte LP; ULP-Co-Proc (FSM-basiert, für Deep-Sleep) | 520 KB       | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombos: z. B. U4WDH (2 MB Flash + 0 PSRAM), D0WDR2-V3 (4 MB Flash + 2 MB PSRAM) | 2 MB embedded / 8 MB external        | 4 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 4.2 (BR/EDR + LE) | 34 GPIOs; 4 SPI; 2 I2S; 2 I2C; 3 UART; Ethernet MAC; TWAI (CAN); ADC (18 ch., 12-bit); Touch (10); DAC (2, 8-bit) |
| ESP32-S2  | Mono Xtensa LX7, 40-240 MHz, keine dedizierte LP; ULP-Co-Procs (RISC-V + FSM, nicht simultan) | 320 KB + 16 KB RTC | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombos: z. B. FH2 (2 MB Flash + 0 PSRAM), FN4R2 (4 MB Flash + 2 MB PSRAM), R2 (0 Flash + 2 MB PSRAM) | 2 MB embedded / 1 GB external (typ. 64 MB) | 4 MB embedded / 1 GB external (typ. 128 MB) | Wi-Fi 2.4 GHz (802.11 b/g/n)              | 43 GPIOs; 4 SPI; 1 I2S; 2 I2C; 2 UART; USB OTG (FS); LCD (2: SPI/I2S); Camera (DVP 8/16-bit); ADC (20 ch., 12-bit); DAC (2, 8-bit); Touch (14); RMT (4 ch.); LED PWM (8 ch.) |
| ESP32-S3  | Dual Xtensa LX7, 40-240 MHz, keine dedizierte LP; ULP-Co-Procs (RISC-V + FSM, nicht simultan) | 512 KB + 16 KB RTC | Flash: 0/4/8/16 MB; PSRAM: 0/2/4/8/16 MB; Kombos: z. B. FN8 (8 MB Flash + 0 PSRAM), R2 (0 + 2 MB), R8 (0 + 8 MB), R16V (0 + 16 MB), FH4R2 (4 MB Flash + 2 MB PSRAM), FN4R8 (4 MB Flash + 8 MB PSRAM) | 16 MB embedded / 32 MB external (Future: 64 MB) | 16 MB embedded / 32 MB external (Future: 64 MB) | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE)   | 45 GPIOs; 4 SPI (2 mem., 2 gen.); 2 I2S; 2 I2C; 3 UART; USB OTG (FS); SD/MMC (2 slots); TWAI; LCD/Camera; ADC (20 ch., 12-bit); Touch (14); MCPWM; RMT; PCNT; LED PWM |
| ESP32-C3  | Mono RISC-V, 40-160 MHz, keine dedizierte LP/ULP | 400 KB (16 KB Cache) | Flash: 0/4 MB; PSRAM: 0 MB; Kombos: z. B. C3 (0 Flash + 0 PSRAM), FH4/C3FH4X (4 MB Flash + 0 PSRAM) – PSRAM external only | 0 MB embedded / 8 MB external (Future: 16 MB) | 4 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE)   | 22/16 GPIOs; 3 SPI; 1 I2S; 1 I2C; 2 UART; USB Serial/JTAG; TWAI; LED PWM (6 ch.); RMT (4 ch.); ADC (6 ch., 12-bit); Temp sensor |
| ESP32-C2  | Mono RISC-V, 20-120 MHz, keine dedizierte LP/ULP | 272 KB (16 KB Cache) | Flash: 0 MB (external only); PSRAM: 0 MB; Kombos: Keine embedded (z. B. C2FH4: 0 + 0, aber Modules wie ESP8684 integrieren 4 MB Flash external-style) | 0 MB embedded / 8 MB external (Future: 16 MB) | 0 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE) | 14 GPIOs; 2 SPI; 1 I2S; 1 I2C; 2 UART; LED PWM; GDMA; SAR ADC (6 ch.); Temp sensor; USB Serial |
| ESP32-C5  | Dual RISC-V (HP/LP), HP 40-240 MHz / LP 20-48 MHz, dedizierte LP ja; kein separater ULP | 384 KB HP + 16 KB LP + 320 KB ROM | Flash: 0/4 MB; PSRAM: 0/8 MB; Kombos: z. B. C5HF4 (4 MB Flash + 0 PSRAM), C5HR8 (0 Flash + 8 MB PSRAM) | 8 MB embedded / 32 MB external (Future: 64 MB) | 4 MB embedded / 32 MB external (Future: 64 MB) | Wi-Fi dual-band 6 (2.4/5 GHz, 802.11 a/b/g/n/ac/ax), BT LE 5 (Core 6.0), 802.15.4 (Zigbee 3.0 / Thread 1.4) | 29 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 CAN FD; SDIO; LED PWM (6 ch.); MCPWM (6 ch.); RMT (4 ch.); PARLIO; PCNT (4); ADC (6 ch., 12-bit); Temp sensor; Analog Comparator (2 pads) |
| ESP32-C6  | Dual RISC-V (HP/LP), HP 40-160 MHz / LP 20 MHz, dedizierte LP ja; kein separater ULP | 512 KB HP + 16 KB LP | Flash: 0/4/8 MB; PSRAM: 0 MB; Kombos: z. B. C6 (0 + 0), C6FH4 (4 MB Flash + 0), C6FH8 (8 MB Flash + 0) – PSRAM external only | 0 MB embedded / 16 MB external (Future: 32 MB) | 8 MB embedded / 16 MB external (Future: 32 MB) | Wi-Fi 6 2.4 GHz (802.11 ax/b/g/n), BT 5.3 (LE + Mesh), 802.15.4 (Zigbee 3.0 / Thread 1.3) | 30/22 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 TWAI; SDIO; LED PWM (6 ch.); MCPWM (3); RMT (4 ch.); PARLIO; PCNT (4); ADC (7 ch., 12-bit); Temp sensor; GDMA; ETM |
| ESP32-H2 | Mono RISC-V, 32 MHz (min typ. low-power) / 96 MHz, keine dedizierte LP/ULP; LP-Komponenten für Deep-Sleep | 320 KB HP + 4 KB LP | Flash: 0/2/4 MB; PSRAM: 0 MB; Kombos: z. B. H2FH2S (2 MB Flash + 0 PSRAM), H2FH4S (4 MB Flash + 0 PSRAM) – PSRAM external only | 0 MB embedded / 16 MB external (Future: 32 MB) | 4 MB embedded / 16 MB external (Future: 32 MB) | BT LE 5.3 (1/2 Mbps, Coded PHY, Long Range, Advertising Extensions), 802.15.4 (250 Kbps OQPSK, Thread/Zigbee 3.0/Matter) | 19 GPIOs; 2 SPI (Flash + gen.); 2 UART; 2 I2C; 1 I2S; RMT (2 tx/2 rx ch.); LED PWM (6 ch.); USB Serial/JTAG; TWAI (CAN); GDMA (3 tx/3 rx); PCNT; MCPWM; ADC (5 ch., 12-bit); Temp sensor; Timers (2 gen. 54-bit, 52-bit sys., 3 WDT) | 
| ESP32-P4  | Dual HP + Mono LP RISC-V, HP 40-360 MHz / LP 40 MHz, dedizierte LP ja; kein separater ULP | 768 KB HP L2MEM + 32 KB LP + 8 KB SPM | Flash: 0 MB; PSRAM: 0/16/32 MB; Kombos: z. B. P4NRW16 (0 Flash + 16 MB PSRAM), P4NRW32 (0 + 32 MB PSRAM) | 32 MB embedded / 64 MB external (Future: 128 MB) | 0 MB embedded / 64 MB external (Future: 128 MB) | Keine integrierten Radios (MCU-fokussiert, external möglich) | 55 GPIOs (16 LP); 4 SPI (+1 LP); 3 I2S (+1 LP); 3 I2C (+1 Analog +1 I3C); 6 UART (5 HP +1 LP); USB HS/FS OTG + Serial/JTAG; Ethernet (10/100 RMII); 3 TWAI; SD/MMC; LED PWM (8 ch.); MCPWM (2); RMT (8 ch.); PARLIO; Touch (14); 2 ADC; VAD; Image: JPEG Codec, ISP, H.264 Encoder, MIPI CSI/DSI (2-lane), LCD/Camera | 

## Referenzen

- ESP32 Series Datasheet (Version 4.3, abgerufen September 2025)
- ESP32-S2 Series Datasheet (Version 1.4, abgerufen September 2025)
- ESP32-S3 Series Datasheet (Version 1.3, abgerufen September 2025)
- ESP32-C3 Series Datasheet (Version 1.2, abgerufen September 2025)
- ESP32-C2 Technical Reference Manual (Version 1.0, abgerufen September 2025, Hinweis: Kein vollständiges Datasheet verfügbar, basierend auf Moduldaten wie ESP8684)
- ESP32-C5 Series Datasheet (Version 1.0, abgerufen September 2025)
- ESP32-C6 Series Datasheet (Version 1.1, abgerufen September 2025)
- ESP32-H2 Series Datasheet (Version 1.1, abgerufen September 2025)
- ESP32-P4 Series Datasheet (Version 0.7, abgerufen September 2025)
- Espressif Product Selector (abgerufen September 2025)-
- ESP32 Module Reference (WROOM/WROVER) (Version 2.0, abgerufen September 2025)


## Deep sleep

### Dtails

Alle ESP32-Modelle (ESP32, S2, S3, C3, C2, C5, C6, P4) unterstützen Deep-Sleep-Modus, und in den meisten Fällen sind speziellen Speicher (RTC SRAM oder vergleichbar) nutzbar, um Daten währened des Deep-Sleeps zu sichern. Allerdings gibt es Unterschiede in der Architektur (RTC SRAM, LP SRAM, oder andere Mechanismen), die beeinflussen, wie und welcher Speicher für diesen Zweck genutzt wird. 

### Übersicht: Deep-Sleep und Speicher zum Sichern von Daten

**Deep-Sleep-Modus:** Alle Modelle können in Deep-Sleep gehen, wodurch der Hauptprozessor (HP-Core) und die meisten Peripherien abgeschaltet werden, um Strom zu sparen. Bestimmte Speicherbereiche bleiben aktiv, um Daten zu sichern oder einfache Aufgaben auszuführen.

**RTC SRAM**: In Modellen ohne dedizierten LP-Core (ESP32, S2, S3, teilweise C3) ist der RTC SRAM der Hauptspeicher, der im Deep-Sleep aktiv bleibt, um Daten zu sichern oder ULP-Co-Prozessor-Code auszuführen.

**LP SRAM**: In Modellen mit dediziertem LP-Core (C5, C6, P4) übernimmt der LP SRAM oft diese Rolle, da der LP-Core im Deep-Sleep aktiv bleiben kann und eigene Daten/Code speichert. Beim H2 gibt es 4 KB LP SRAM, aber ohne LP-Core, nur für Datenspeicherung und LP-Peripherie.

**Spezialfälle:** C2 hat keinen dedizierten RTC SRAM oder LP SRAM, aber es gibt einen kleinen RTC-Bereich (nicht explizit spezifiziert), der ähnliche Funktionen bietet. C3 hat eingeschränkte Optionen. H2 ist für ultra-niedrigen Verbrauch (7 μA Deep-Sleep) optimiert, mit LP SRAM für passive Speicherung.


### Modell-spezifische Details

#### ESP32 (Classic):

- **Deep-Sleep:** Ja, unterstützt.
- **Speicher:** 520 KB SRAM, davon ein Teil (nicht separat als "RTC SRAM" spezifiziert, aber ca. 8 KB im RTC-Domain) bleibt im Deep-Sleep aktiv. Der ULP-Co-Prozessor (FSM-basiert) kann darauf zugreifen, um Daten zu sichern oder einfache Aufgaben auszuführen.
- **Nutzung:** Sicherung von Variablen im RTC-Speicherbereich (via RTC-Speicher-API) z. B. Zustandsdaten, Zähler, oder Sensorwerte. Der ULP kann diese Daten verarbeiten.
- **Limit:** Begrenzter Speicher im Vergleich zu neueren Modellen; ULP ist nicht so flexibel wie ein LP-Core.


#### ESP32-S2:

- **Deep-Sleep:** Ja, unterstützt.
- **Speicher:** 16 KB RTC SRAM explizit im Datasheet, bleibt im Deep-Sleep aktiv. Zwei ULP-Co-Procs (RISC-V + FSM, nicht simultan) können darauf zugreifen.
- **Nutzung:** RTC SRAM kann für Daten (z. B. Zustände, Konfigurationsdaten) genutzt werden. Der RISC-V-ULP erlaubt komplexere Berechnungen als beim klassischen ESP32.
- **Limit:** 16 KB ist nicht riesig, aber ausreichend für die meisten Sensor- oder Zustandsdaten.


#### ESP32-S3:

- **Deep-Sleep:** Ja, unterstützt.
- **Speicher:** 16 KB RTC SRAM, bleibt im Deep-Sleep aktiv. ULP-Co-Procs (RISC-V + FSM) können diesen Speicher nutzen.
- **Nutzung:** Ähnlich wie S2, ideal für Daten wie Konfigurationen, Sensorwerte, oder kleine Zustandsmaschinen. Der ULP-RISC-V ist programmierbar für komplexere Deep-Sleep-Logik.
- **Limit:** Wie S2, 16 KB RTC SRAM begrenzt die Datenmenge.


#### ESP32-C3:

- **Deep-Sleep:** Ja, unterstützt.
- **Speicher:** Kein expliziter RTC SRAM, aber ein Teil der 400 KB SRAM (ca. 8 KB im RTC-Domain, ähnlich ESP32) bleibt im Deep-Sleep aktiv. Kein ULP-Co-Prozessor, daher kein Programmieren im Deep-Sleep.
- **Nutzung:** Du kannst Daten im RTC-Bereich sichern (via ESP-IDF RTC-Speicher-APIs), aber ohne ULP nur statische Speicherung, keine aktive Verarbeitung.
- **Limit:** Kein ULP oder LP-Core schränkt die Flexibilität ein; kleinerer Speicherbereich.


#### ESP32-C2:

- **Deep-Sleep:** Ja, unterstützt.
- **Speicher:** Kein expliziter RTC SRAM oder LP SRAM. Ein kleiner RTC-Bereich (nicht im Datasheet quantifiziert, geschätzt <8 KB) bleibt aktiv, ähnlich wie bei C3.
- **Nutzung:** Begrenzte Datenspeicherung im RTC-Bereich möglich (z. B. Zustandsvariablen), aber keine aktive Verarbeitung, da kein ULP oder LP-Core.
- **Limit:** Sehr eingeschränkt, da kein dedizierter Speicher oder Co-Prozessor vorhanden.


#### ESP32-C5:

- **Deep-Sleep:** Ja, unterstützt (HP-Core aus, LP-Core kann aktiv bleiben).
- **Speicher:** 16 KB LP SRAM für den dedizierten LP-Core (RISC-V), bleibt im Deep-Sleep aktiv. Kein separater RTC SRAM, da der LP-Core diese Aufgaben übernimmt.
- **Nutzung:** LP SRAM kann für Daten und Code des LP-Cores genutzt werden, der im Deep-Sleep läuft. Ideal für komplexe Low-Power-Logik oder Datenspeicherung.
- **Limit:** 16 KB LP SRAM ist ausreichend, aber nicht riesig; LP-Core bietet mehr Flexibilität als ULP.


#### ESP32-C6:

- **Deep-Sleep:** Ja, unterstützt (ähnlich wie C5).
- **Speicher:** 16 KB LP SRAM für den LP-Core, bleibt im Deep-Sleep aktiv. Kein separater RTC SRAM.
- **Nutzung:** Wie C5, LP SRAM für Daten/Code des LP-Cores, geeignet für komplexe Deep-Sleep-Aufgaben.
- **Limit:** 16 KB LP SRAM, aber flexibler durch LP-Core.


#### ESP32-H2: 

- **Deep-Sleep:** Ja, unterstützt (optimiert für ultra-niedrigen Verbrauch, 7 μA).
- **Speicher:** 4 KB LP SRAM, bleibt im Deep-Sleep aktiv. Kein separater RTC SRAM oder dedizierter LP-Core.
- **Nutzung:** LP SRAM für passive Datenspeicherung (z. B. Zustandsvariablen, Sensor-Daten) im Deep-Sleep; LP-Peripherie (z. B. Timer, Sensoren) unterstützt einfache Aufgaben.
- **Limit:** 4 KB LP SRAM ist klein; kein LP-Core, daher keine komplexe Verarbeitung im Deep-Sleep.


#### ESP32-P4:

- **Deep-Sleep:** Ja, unterstützt (HP-Cores aus, LP-Core aktiv).
- **Speicher:** 32 KB LP SRAM für den LP-Core, bleibt im Deep-Sleep aktiv. Kein RTC SRAM, da LP-Core die Low-Power-Aufgaben übernimmt.
- **Nutzung:** LP SRAM für Daten und Code des LP-Cores, ideal für anspruchsvolle Low-Power-Anwendungen (z. B. Bildverarbeitung, Sensor-Logik).
- **Limit:** 32 KB ist großzügiger als bei C5/C6, keine wesentlichen Einschränkungen.



## Zusammenfassung

- Alle ESP32-Modelle unterstützen Deep-Sleep.
- RTC-Speicher (oder Äquivalent) zum Sichern von Daten bei allen Modellen
- **ESP32, S2, S3:** RTC SRAM (16 KB bei S2/S3, kleinerer Bereich beim klassischen ESP32) für Datenspeicherung, unterstützt durch ULP-Co-Procs.
- **C3, C2:** Kleiner RTC-Bereich (nicht explizit spezifiziert, <8 KB), nur für statische Datenspeicherung, kein ULP/LP-Core.
- **C5, C6, P4:** LP SRAM (16 KB bei C5/C6, 32 KB bei P4) für Datenspeicherung und LP-Core-Aufgaben, flexibler als RTC SRAM.
- Unterschiede: Modelle mit ULP (ESP32, S2, S3) oder LP-Core (C5, C6, P4) bieten mehr Flexibilität, da sie im Deep-Sleep aktiv Code ausführen können. C3 und C2 sind eingeschränkt (nur Speicherung, keine Verarbeitung).
- **C5, C6, P4** können zusätzlich den LP-Core nutzen, um **im Deep-Sleep** aktiv zu sein.

### Gründliche Bewertung jedes Modells

Basierend auf den offiziellen Espressif-Datasheets (Stand September 2025) und den gesammelten Details aus den Quellen wird jedes ESP32-Modell hinsichtlich seiner Vor- und Nachteile analysiert. Der Fokus liegt auf der **Schwerpunkt-Nutzbarkeit**, d.h. wie die Ausstattung (Architektur, Memory, Radios, Interfaces, Power) das Modell für bestimmte Anwendungsbereiche optimiert. Die Bewertung berücksichtigt Faktoren wie Leistung, Energieeffizienz, Kosten, Kompatibilität (z.B. RISC-V vs. Xtensa), Wireless-Optionen und Peripherie. Modelle mit RISC-V sind zukunftsorientiert (besser für Open-Source), während Xtensa etabliert ist. Neuere Modelle (C-Serie, H2, P4) betonen Low-Power und Multi-Protocol (z.B. Matter), ältere (Classic, S2, S3) sind allgemeiner, aber verbrauchsintensiver.

#### ESP32 (Classic)
- **Schwerpunkt**: Allrounder für drahtlose Netzwerke und Legacy-Anwendungen; stark in Wi-Fi + BT Classic/LE-Kombinationen mit Ethernet/CAN.
- **Vorteile**: Dual-Core Xtensa für parallele Tasks (z.B. Wi-Fi + BT), etablierte Ökosystem (viel Code verfügbar), Ethernet MAC und TWAI (CAN) für industrielle Netzwerke, günstig und robust, ULP-Co-Proc für einfache Low-Power-Tasks.
- **Nachteile**: Höherer Stromverbrauch (Deep-Sleep ~10 μA, Active >100 mA), Xtensa-Architektur weniger zukunftsweisend (weniger Open-Source-Tools), kein Wi-Fi 6/BT 5, begrenzte Memory-Optionen (max 4 MB embedded Flash), veraltet (NRND für einige Varianten), kein dedizierter LP-Core.
- **Gesamtbewertung**: Gut für kostengünstige, etablierte Projekte mit gemischter Connectivity, aber nicht ideal für ultra-low-power oder moderne Protokolle.

#### ESP32-S2
- **Schwerpunkt**: USB- und Multimedia-fokussiert (LCD/Camera/Touch), für Wi-Fi-only Geräte mit Low-Power.
- **Vorteile**: USB OTG (FS) für HID/Storage, LCD/Camera-Interfaces für Displays, 14 Touch-Sensoren, ULP-Co-Procs (RISC-V + FSM) für flexible Deep-Sleep, große external Memory-Support (bis 1 GB), kompakt und energieeffizient für Wi-Fi-Apps.
- **Nachteile**: Kein BT, Mono-Core Xtensa (weniger Leistung), kein Ethernet/CAN, Touch nicht CS-zertifiziert (Einschränkungen in noisy Umgebungen), höherer Verbrauch als C-Serie (Deep-Sleep ~5-7 μA), veraltet im Vergleich zu S3.
- **Gesamtbewertung**: Stark für USB-basierte oder Display/Touch-Geräte (z.B. Smart Panels), aber limitiert ohne BT/Multi-Core.

#### ESP32-S3
- **Schwerpunkt**: AI und Multimedia (Vector/AI-Extensions, LCD/Camera), für Edge-Computing mit Wi-Fi/BT LE.
- **Vorteile**: Dual-Core Xtensa mit AI/DSP-Extensions (z.B. 128-bit Vector), USB OTG/SD für Storage, LCD/Camera für Video, ULP-Co-Procs für Low-Power, große Memory (bis 16 MB embedded PSRAM), BT 5 LE für moderne Apps.
- **Nachteile**: Kein Wi-Fi 6, höherer Verbrauch (Deep-Sleep ~7 μA, Active >100 mA), Xtensa statt RISC-V, ADC/Wi-Fi-Konflikte, teurer als C-Serie, kein 802.15.4.
- **Gesamtbewertung**: Ideal für AI/Multimedia (z.B. Voice/Image Recognition), aber nicht optimal für ultra-low-power oder Multi-Protocol-IoT.

#### ESP32-C3
- **Schwerpunkt**: Low-Cost Low-Power Wireless (Wi-Fi + BT LE), für einfache Sensoren.
- **Vorteile**: RISC-V Mono-Core (zukunftsweisend), Wi-Fi + BT 5 LE, TWAI (CAN), USB Serial/JTAG, günstig und kompakt, externe Memory bis 16 MB.
- **Nachteile**: Kein ULP/LP-Core (eingeschränkte Deep-Sleep-Verarbeitung, ~5 μA), begrenzte GPIOs (22/16), kein Ethernet/USB OTG, Mono-Core limitiert Leistung, einige Varianten EOL/NRND.
- **Gesamtbewertung**: Perfekt für kostengünstige, batteriebetriebene Sensoren, aber schwach in Multimedia/High-Perf.

#### ESP32-C2
- **Schwerpunkt**: Ultra-Low-Cost Minimalist für Low-Power Wireless.
- **Vorteile**: Sehr günstig und klein, RISC-V Mono-Core, Wi-Fi + BT 5 LE, Low-Power (Deep-Sleep <8 μA), externe Memory-Support.
- **Nachteile**: Kein embedded Flash/PSRAM (external only), wenige GPIOs (14), minimal Interfaces (kein USB OTG/Ethernet/CAN), kein ULP/LP-Core, begrenzte SRAM (272 KB).
- **Gesamtbewertung**: Für massenproduzierte, einfache Wireless-Geräte (z.B. Tags), aber zu limitiert für komplexe Apps.

#### ESP32-C5
- **Schwerpunkt**: Modern Multi-Protocol Wireless (Dual-Band Wi-Fi 6 + BT LE 5 + 802.15.4), für Low-Power IoT mit LP-Core.
- **Vorteile**: Dual-Band Wi-Fi 6 (2.4/5 GHz), BT LE 5 (inkl. Direction Finding), 802.15.4 (Zigbee/Thread), dedizierter LP-Core (RISC-V, bis 48 MHz), CAN FD, Low-Power (Deep-Sleep ~12 μA), RISC-V Dual-Core.
- **Nachteile**: Weniger GPIOs (29), begrenzte embedded Memory (4 MB Flash/8 MB PSRAM), höherer Preis, neu (weniger etabliert).
- **Gesamtbewertung**: Stark für smarte Home/IoT-Netzwerke (Matter-kompatibel), aber nicht für High-Perf ohne Wireless.

#### ESP32-C6
- **Schwerpunkt**: Low-Power Multi-Protocol (Wi-Fi 6 2.4GHz + BT 5.3 + 802.15.4), für Batterie-IoT mit LP-Core.
- **Vorteile**: Wi-Fi 6 (2.4 GHz), BT 5.3 (Mesh), 802.15.4 (Zigbee/Thread), dedizierter LP-Core (RISC-V, 20 MHz), Low-Power (Deep-Sleep 7 μA), RISC-V Dual-Core, TWAI.
- **Nachteile**: Kein 5 GHz Wi-Fi, begrenzte embedded PSRAM (external only), 30/22 GPIOs, kein USB OTG/Ethernet.
- **Gesamtbewertung**: Optimal für energieeffiziente Smart Devices (z.B. Sensor-Netzwerke), besser als C5 in Power, aber ohne Dual-Band.

#### ESP32-H2
- **Schwerpunkt**: Ultra-Low-Power Non-Wi-Fi Wireless (BT LE 5.3 + 802.15.4), für Thread/Zigbee/Matter.
- **Vorteile**: BT LE 5.3 (Long Range, Mesh), 802.15.4 (Zigbee/Thread), RISC-V Mono-Core (96 MHz), Ultra-Low-Power (Deep-Sleep 7 μA), USB Serial/JTAG, kompakt.
- **Nachteile**: Kein Wi-Fi, kleiner SRAM (320 KB + 4 KB LP), wenige GPIOs (19), kein dedizierter LP-Core (nur LP-Komponenten), begrenzte Interfaces.
- **Gesamtbewertung**: Ideal für batteriebetriebene Mesh-Netzwerke (z.B. Smart Lighting), aber ungeeignet für Wi-Fi-Apps.

#### ESP32-P4
- **Schwerpunkt**: High-Performance MCU ohne Radios, für AI/Multimedia (JPEG/H.264/MIPI) mit Wired Connectivity.
- **Vorteile**: Dual-HP + Mono-LP RISC-V (bis 360 MHz), AI/DSP-Extensions, Multimedia (JPEG Codec, H.264 Encoder, MIPI CSI/DSI), USB HS/FS OTG, Ethernet, 55 GPIOs (16 LP), große Memory (bis 32 MB embedded PSRAM), VAD/Touch.
- **Nachteile**: Keine integrierten Radios (external nötig), kein embedded Flash, höherer Verbrauch (Deep-Sleep 0.025 mA), teurer, neu (weniger Support).
- **Gesamtbewertung**: Perfekt für High-Perf Wired/AI-Geräte (z.B. HMI Panels), aber nicht für Wireless ohne Add-ons.

### Liste typischer Anwendungen

Nachfolgend sind 35 typische Anwendungen für ESP32-Modelle zusammengestellt, basierend auf Espressif-Empfehlungen (z.B. Smart Home, IoT, Industrial). Diese decken Bereiche wie Low-Power Sensoren, Multimedia, AI, Industrial und Wearables ab. Die Liste ist nummeriert und beschreibt kurz den Fokus.

1. Smart Home Hub (z.B. Zentrale Steuerung mit Multi-Protocol).
2. Wi-Fi Access Point/Extender (z.B. Netzwerk-Erweiterung).
3. Bluetooth Audio Device (z.B. Speaker/Headset).
4. Low-Power Sensor Node (z.B. Umweltsensor mit Batterie).
5. AI Edge Computing (z.B. Voice Recognition).
6. Security Camera (z.B. Video-Überwachung mit Streaming).
7. Wearable Fitness Tracker (z.B. Schrittzähler mit BT).
8. Industrial IoT Gateway (z.B. Daten-Sammlung mit CAN/Ethernet).
9. Zigbee/Thread Smart Lighting (z.B. Lampen-Steuerung).
10. USB HID Device (z.B. Maus/Tastatur).
11. Ethernet-Connected Controller (z.B. Wired Automation).
12. CAN-Bus Vehicle Monitor (z.B. Auto-Diagnose).
13. LCD Display Panel (z.B. HMI Interface).
14. Touch Screen Device (z.B. Bedienpanel).
15. Battery-Powered Remote Control (z.B. IR/Fernbedienung).
16. Matter-Compatible Smart Plug (z.B. Steckdose mit Multi-Protocol).
17. Wi-Fi 6 Mesh Network (z.B. Home Mesh).
18. Bluetooth Mesh Sensor Network (z.B. Gebäudemonitoring).
19. 802.15.4 Low-Power Mesh (z.B. Thread-Netzwerk).
20. Robotics Controller (z.B. Motor-Steuerung mit PWM).
21. Barcode Scanner (z.B. Image Processing).
22. Voice Assistant (z.B. Sprachsteuerung).
23. Secure IoT Device (z.B. mit Encryption/Boot).
24. Environmental Monitoring Station (z.B. Wetterstation).
25. SD Card Data Logger (z.B. Logging mit Storage).
26. PWM Motor Driver (z.B. DC-Motoren).
27. Analog Sensor Reader (z.B. Temp/Druck mit ADC).
28. Asset Tracking Tag (z.B. BT LE Beacon).
29. Smart Thermostat (z.B. Heizungssteuerung).
30. POS Terminal (z.B. Zahlungsterminal mit Display).
31. Service Robot Brain (z.B. Navigation mit AI).
32. Audio Streaming Device (z.B. Musik-Player).
33. Health Monitoring Wearable (z.B. Puls-Sensor).
34. Agricultural Sensor (z.B. Bodenfeuchte mit Low-Power).
35. Vending Machine Controller (z.B. Zahlung/Display).

### Bewertungstabelle

Die Tabelle bewertet die Eignung jedes Modells für die Anwendungen mit ++ (sehr gut, optimal), + (gut, machbar), 0 (neutral, mit Einschränkungen), - (schlecht, ungeeignet), -- (sehr schlecht, unmöglich). Bewertung basiert auf Ausstattung (z.B. Radios für Wireless, LP-Core für Low-Power, Interfaces für Multimedia). Optionaler Text in Klammern erklärt Schlüsselgründe.

| Anwendung | ESP32 | ESP32-S2 | ESP32-S3 | ESP32-C3 | ESP32-C2 | ESP32-C5 | ESP32-C6 | ESP32-H2 | ESP32-P4 |
|-----------|-------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1. Smart Home Hub | ++ (Wi-Fi/BT + Ethernet) | + (Wi-Fi, aber kein BT) | ++ (AI/Multimedia + BT LE) | + (Low-Cost Wi-Fi/BT) | 0 (Minimal, aber Wi-Fi/BT) | ++ (Multi-Protocol Wi-Fi 6) | ++ (Wi-Fi 6 + 802.15.4) | + (802.15.4/BT, kein Wi-Fi) | + (High-Perf, aber externe Radios) |
| 2. Wi-Fi Access Point/Extender | ++ (Dual-Core Wi-Fi) | ++ (Wi-Fi + USB) | ++ (Wi-Fi + Memory) | + (Low-Power Wi-Fi) | + (Minimal Wi-Fi) | ++ (Dual-Band Wi-Fi 6) | ++ (Wi-Fi 6) | -- (Kein Wi-Fi) | - (Keine Radios) |
| 3. Bluetooth Audio Device | ++ (BT Classic/LE) | -- (Kein BT) | ++ (BT LE + I2S) | + (BT LE) | + (BT LE) | ++ (BT LE 5 + I2S) | ++ (BT 5.3 Mesh) | ++ (BT LE 5.3) | + (I2S/LP, aber externe BT) |
| 4. Low-Power Sensor Node | + (ULP, aber verbrauchsintensiv) | + (ULP-Co-Procs) | + (ULP-Co-Procs) | ++ (Low-Power RISC-V) | ++ (Ultra-Low-Cost/Power) | ++ (LP-Core + Low-Verbrauch) | ++ (LP-Core + 7μA Deep-Sleep) | ++ (Ultra-Low-Power 7μA) | + (LP-Core, aber kein Wireless) |
| 5. AI Edge Computing | + (Dual-Core) | 0 (Mono-Core) | ++ (Vector/AI Extensions) | - (Mono-Core, wenig SRAM) | -- (Minimal) | + (Dual-Core RISC-V) | + (Dual-Core) | - (Mono-Core, wenig SRAM) | ++ (AI/DSP Extensions) |
| 6. Security Camera | + (Wi-Fi/BT) | ++ (LCD/Camera + Wi-Fi) | ++ (LCD/Camera + AI) | 0 (Kein Camera-Interface) | - (Minimal Interfaces) | + (Wi-Fi 6, aber kein Camera) | + (Wi-Fi 6) | - (Kein Wi-Fi/Camera) | ++ (MIPI CSI/DSI + H.264) |
| 7. Wearable Fitness Tracker | + (BT + Touch) | + (Touch + Low-Power) | ++ (BT LE + Touch/AI) | ++ (BT LE + Low-Power) | ++ (Low-Power BT LE) | ++ (BT LE 5 + LP-Core) | ++ (BT 5.3 + LP-Core) | ++ (BT LE 5.3 Low-Power) | + (Touch + LP, aber groß) |
| 8. Industrial IoT Gateway | ++ (Ethernet/CAN + Dual-Core) | + (USB/TWAI) | ++ (TWAI + SD) | + (TWAI + Low-Cost) | 0 (Minimal) | ++ (CAN FD + Multi-Protocol) | ++ (TWAI + Wi-Fi 6) | + (802.15.4 + TWAI) | ++ (Ethernet + CAN) |
| 9. Zigbee/Thread Smart Lighting | 0 (Kein 802.15.4) | 0 (Kein 802.15.4) | 0 (Kein 802.15.4) | 0 (Kein 802.15.4) | 0 (Kein 802.15.4) | ++ (802.15.4 + Zigbee/Thread) | ++ (802.15.4 + Thread 1.3) | ++ (802.15.4 + Zigbee/Thread) | - (Keine Radios) |
| 10. USB HID Device | + (UART/USB Serial) | ++ (USB OTG FS) | ++ (USB OTG FS) | + (USB Serial) | + (USB Serial) | + (USB Serial) | + (USB Serial) | + (USB Serial) | ++ (USB HS/FS OTG) |
| 11. Ethernet-Connected Controller | ++ (Ethernet MAC) | - (Kein Ethernet) | - (Kein Ethernet) | - (Kein Ethernet) | - (Kein Ethernet) | - (Kein Ethernet) | - (Kein Ethernet) | - (Kein Ethernet) | ++ (Ethernet 10/100) |
| 12. CAN-Bus Vehicle Monitor | ++ (TWAI/CAN) | + (TWAI) | + (TWAI) | ++ (TWAI) | - (Kein CAN) | ++ (2x CAN FD) | ++ (2x TWAI) | + (TWAI) | ++ (3x TWAI) |
| 13. LCD Display Panel | + (I2S/SPI) | ++ (LCD Interface) | ++ (LCD/Camera) | 0 (Kein LCD) | - (Minimal) | 0 (Kein LCD) | 0 (Kein LCD) | 0 (Kein LCD) | ++ (MIPI DSI + LCD) |
| 14. Touch Screen Device | ++ (10 Touch) | ++ (14 Touch) | ++ (14 Touch) | - (Kein Touch) | - (Kein Touch) | - (Kein Touch) | - (Kein Touch) | - (Kein Touch) | ++ (14 Touch) |
| 15. Battery-Powered Remote | + (BT + Low-Power) | + (Wi-Fi + RMT) | + (BT LE) | ++ (BT LE Low-Power) | ++ (BT LE Minimal) | ++ (BT LE 5 LP-Core) | ++ (BT 5.3 LP-Core) | ++ (BT LE 5.3 Low-Power) | + (RMT + LP-Core) |
| 16. Matter-Compatible Smart Plug | + (Wi-Fi/BT) | + (Wi-Fi) | + (Wi-Fi/BT LE) | + (Wi-Fi/BT LE) | + (Wi-Fi/BT LE) | ++ (Multi-Protocol) | ++ (Wi-Fi 6 + 802.15.4) | ++ (802.15.4/BT LE) | - (Keine Radios) |
| 17. Wi-Fi 6 Mesh Network | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | ++ (Dual-Band Wi-Fi 6) | ++ (Wi-Fi 6 2.4GHz) | -- (Kein Wi-Fi) | - (Keine Radios) |
| 18. Bluetooth Mesh Network | + (BT LE) | -- (Kein BT) | ++ (BT 5 LE Mesh) | + (BT 5 LE) | + (BT 5 LE) | ++ (BT LE 5) | ++ (BT 5.3 Mesh) | ++ (BT LE 5.3 Mesh) | - (Keine Radios) |
| 19. 802.15.4 Low-Power Mesh | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | ++ (802.15.4) | ++ (802.15.4) | ++ (802.15.4) | - (Keine Radios) |
| 20. Robotics Controller | ++ (Dual-Core + PWM) | + (Mono-Core + PWM) | ++ (Dual-Core + MCPWM) | + (Mono-Core + PWM) | 0 (Minimal PWM) | ++ (MCPWM + Dual-Core) | ++ (MCPWM + Dual-Core) | + (MCPWM) | ++ (MCPWM + High-Perf) |
| 21. Barcode Scanner | + (Wi-Fi/BT) | ++ (Camera) | ++ (Camera + AI) | 0 (Kein Camera) | - (Kein Camera) | 0 (Kein Camera) | 0 (Kein Camera) | 0 (Kein Camera) | ++ (ISP + MIPI CSI) |
| 22. Voice Assistant | + (Dual-Core + I2S) | + (I2S + USB) | ++ (I2S + AI) | 0 (I2S, aber Mono) | 0 (I2S Minimal) | + (I2S + Dual-Core) | + (I2S + Dual-Core) | + (I2S) | ++ (VAD + I2S/LP) |
| 23. Secure IoT Device | ++ (Crypto Accel) | ++ (Crypto + Secure Boot) | ++ (Crypto + Secure Boot) | ++ (Crypto) | + (Crypto) | ++ (Crypto + XTS-AES) | ++ (Crypto + XTS-AES) | ++ (Crypto) | ++ (Crypto + DSA) |
| 24. Environmental Monitoring Station | + (ADC + Wireless) | + (ADC + Touch) | + (ADC + Touch) | ++ (ADC + Low-Power) | ++ (ADC + Low-Power) | ++ (ADC + LP-Core) | ++ (ADC + LP-Core) | ++ (ADC + Low-Power) | + (ADC + Touch) |
| 25. SD Card Data Logger | + (SPI) | + (SPI) | ++ (SD/MMC) | + (SPI) | + (SPI) | ++ (SDIO) | ++ (SDIO) | 0 (Kein SD) | ++ (SD/MMC) |
| 26. PWM Motor Driver | ++ (PWM) | ++ (LED PWM) | ++ (MCPWM) | ++ (LED PWM) | ++ (LED PWM) | ++ (MCPWM 6 ch.) | ++ (MCPWM 3 ch.) | ++ (LED PWM) | ++ (MCPWM 2) |
| 27. Analog Sensor Reader | ++ (ADC 18 ch.) | ++ (ADC 20 ch.) | ++ (ADC 20 ch.) | ++ (ADC 6 ch.) | ++ (ADC 6 ch.) | ++ (ADC 6 ch.) | ++ (ADC 7 ch.) | ++ (ADC 5 ch.) | ++ (2 ADC) |
| 28. Asset Tracking Tag | + (BT LE) | - (Kein BT) | + (BT LE) | ++ (BT LE Low-Power) | ++ (BT LE Low-Power) | ++ (BT LE 5 Direction) | ++ (BT 5.3) | ++ (BT LE 5.3 Long Range) | - (Keine Radios) |
| 29. Smart Thermostat | ++ (Wi-Fi/BT + Touch) | ++ (Wi-Fi + Touch) | ++ (Wi-Fi/BT + Touch) | + (Wi-Fi/BT) | + (Wi-Fi/BT) | ++ (Multi-Protocol) | ++ (Wi-Fi 6 + 802.15.4) | + (802.15.4/BT) | + (Touch, externe Radios) |
| 30. POS Terminal | + (Ethernet + Display) | ++ (USB + LCD) | ++ (SD + LCD) | 0 (Kein USB OTG) | - (Minimal) | 0 (Kein USB OTG) | 0 (Kein USB OTG) | 0 (Kein USB) | ++ (USB HS + SD/MMC) |
| 31. Service Robot Brain | ++ (Dual-Core + Ethernet) | + (Mono-Core + USB) | ++ (Dual-Core + AI) | + (Mono-Core) | - (Minimal) | ++ (Dual-Core + CAN) | ++ (Dual-Core) | + (Mono-Core) | ++ (High-Perf + AI) |
| 32. Audio Streaming Device | ++ (I2S + BT) | ++ (I2S + Wi-Fi) | ++ (I2S + BT LE) | + (I2S + BT LE) | + (I2S + BT LE) | ++ (I2S + BT LE 5) | ++ (I2S + BT 5.3) | ++ (I2S + BT LE 5.3) | ++ (I2S/LP + VAD) |
| 33. Health Monitoring Wearable | + (BT + ADC) | + (ADC + Touch) | ++ (BT LE + Touch/AI) | ++ (BT LE + ADC) | ++ (BT LE + ADC) | ++ (BT LE 5 + ADC) | ++ (BT 5.3 + ADC) | ++ (BT LE 5.3 + ADC) | + (ADC + Touch) |
| 34. Agricultural Sensor | + (Wi-Fi/BT + ADC) | + (Wi-Fi + ADC) | + (Wi-Fi/BT + ADC) | ++ (Wi-Fi/BT + Low-Power) | ++ (Wi-Fi/BT + Low-Power) | ++ (Multi-Protocol + ADC) | ++ (Wi-Fi 6 + ADC) | ++ (802.15.4/BT + ADC) | + (ADC, externe Radios) |
| 35. Vending Machine Controller | ++ (Ethernet + Display) | ++ (USB + LCD/Touch) | ++ (SD + LCD/Touch) | + (SPI) | 0 (Minimal) | + (SDIO) | + (SDIO) | 0 (Kein SD) | ++ (SD/MMC + Ethernet) |
