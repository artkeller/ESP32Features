# ESP32-Funktionen

[![CRA-Status](https://img.shields.io/badge/CRA-Exempt%20(pure%20OSS)-informational)](./CRA-EXEMPTION.md)
[![Lizenz](https://img.shields.io/badge/License-CC--BY--4.0-blue?style=flat-square)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-2026.07-brightgreen?style=flat-square)](./README-DE.md)

Willkommen bei ESP32Features, einem Leitfaden und Repository für die aktuelle ESP32-SoC-Familie von Espressif Systems. Diese README-Datei enthält eine Übersichtstabelle der relevanten ESP32-Modelle, basierend auf den offiziellen Datenblättern und der Dokumentation von Espressif (Stand: Juli 2026). Die ESP32-Serie umfasst eine breite Palette an Mikrocontrollern, die für IoT-Anwendungen, Edge-Computing, Sensoren mit geringem Stromverbrauch und industrielle Systeme optimiert sind – von bewährten Allroundern wie dem klassischen ESP32 bis hin zu modernen RISC-V-basierten Chips mit Wi-Fi 6, Bluetooth 5.4 und Unterstützung für mehrere Protokolle (z. B. Zigbee/Thread für Matter-kompatible Smart Homes).

## Warum ESP32Features?

- **Umfassende Abdeckung:** Alle Modelle (ESP32, S2, S3, C3, C2, C5, C6, C61, H2, H4, P4, **E22, H21, S31**) mit Schwerpunkt auf Architektur, Speicher (SRAM, Flash, PSRAM), Funkmodule, Schnittstellen und Low-Power-Funktionen.
- **Praktische Analyse:** Ergänzt durch Details zum Deep-Sleep-Modus, Vor- und Nachteile, Anwendungsbewertungen sowie Kombinationsvorschläge für Hybridsysteme (z. B. P4 + C6 für Industrie 4.0).
- **Aktuell und quellbasiert:** Basierend auf dem Produkt-Selektor und den Datenblättern von Espressif (z. B. ESP32-C5 seit 2025 in Serienproduktion, ESP32-C6 mit PSA-Level-2-Sicherheitszertifizierung, ESP32-E22 seit Juni 2026 Wi-Fi 6E-zertifiziert).
- **Für Entwickler:** Integriert mit ESP-IDF, Arduino und Tools für das Rapid Prototyping – ideal für Smart Devices, KI am Netzwerkrand und IIoT.

Die folgende Tabelle fasst die wichtigsten Funktionen zusammen. Detaillierte Analysen finden Sie in den Unterabschnitten: [Espressif-SoC-Produktportfolio](#espressif-soc-product-portfolio), [Deep Sleep](#deep-sleep), [Vor- und Nachteile](#thorough-evaluation-of-each-model), [Anwendungen](#list-of-typical-applications), [Kombinationen](#useful-combinations-of-esp32-models) und [Literaturhinweise](#references--further-reading)

### Haftungsausschluss 2026

> **Hinweis:** Die obige Abbildung des Espressif-Produktportfolios (Stand: September 2025) enthält **nicht** die seitdem angekündigten Varianten **ESP32‑E22**, **ESP32‑H21** und **ESP32‑S31**. Diese wurden zu einem späteren Zeitpunkt in die Tabelle aufgenommen.

Die folgenden Modelle wurden seit September 2025 von Espressif angekündigt und sind **bereits in der obigen Tabelle enthalten**:
- **ESP32‑E22** – Tri‑Band-Wi‑Fi 6E + Dual‑Mode-Bluetooth 5.4-Konnektivitäts-Coprozessor (RCP) – erhältlich seit Januar 2026, Wi‑Fi 6E‑zertifiziert seit Juni 2026
- **ESP32‑H21** – Ultra-Low-Power-BLE-5- und 802.15.4-SoC – seit März 2026 mit Preview-Unterstützung in ESP-IDF v6.0 verfügbar
- **ESP32‑S31** – Dual-Core-RISC-V-SoC mit Wi-Fi 6, BT 5.4, 802.15.4, Gigabit-Ethernet und erweiterten HMI-Funktionen – im März 2026 angekündigt, Markteinführung steht noch aus

**Weitere zukünftige Modelle** (über die oben aufgeführten hinaus) wurden von Espressif zum jetzigen Zeitpunkt **noch nicht** angekündigt. Diese Liste wird aktualisiert, sobald neue Produkte angekündigt werden.

## Übersichtstabelle der ESP32-Modelle

| Modell | Architektur (Kerne, Taktfrequenz min./max., LP/ULP) | Integriertes SRAM | Integrierte Flash-/PSRAM-Optionen (Kombinationen) | Max. PSRAM (integriert/extern, zukünftig) | Max. Flash (integriert/extern, zukünftig) | Funkmodul (Varianten) | Schnittstellen (Auswahl: Anzahl, Typ) |
|------------|--------------------------------------------|---------------|----------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|-----------------------------------|
| ESP32 | Dual Xtensa LX6, 80–240 MHz, kein dedizierter LP; ULP-Coprozessor (FSM-basiert, für Tiefschlaf) | 520 KB | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombinationen: z. B. U4WDH (2 MB Flash + 0 PSRAM), D0WDR2‑V3 (4 MB Flash + 2 MB PSRAM) | 2 MB integriert / 8 MB extern | 4 MB integriert / 16 MB extern | WLAN 2,4 GHz (802.11 b/g/n), BT 4.2 (BR/EDR + LE) | 34 GPIOs; 4 SPI; 2 I2S; 2 I2C; 3 UART; Ethernet-MAC; TWAI (CAN); ADC (18 Kanäle, 12 Bit); Touch (10); DAC (2, 8 Bit) |
| ESP32‑S2 | Mono Xtensa LX7, 40–240 MHz, kein dedizierter LP; ULP-Coprozessoren (RISC-V + FSM, nicht gleichzeitig) | 320 KB + 16 KB RTC | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombinationen: z. B. FH2 (2 MB Flash + 0 PSRAM), FN4R2 (4 MB Flash + 2 MB PSRAM), R2 (0 Flash + 2 MB PSRAM) | 2 MB integriert / 1 GB extern (typ. 64 MB) | 4 MB integriert / 1 GB extern (typ. 128 MB) | WLAN 2,4 GHz (802.11 b/g/n) | 43 GPIOs; 4 SPI; 1 I2S; 2 I2C; 2 UART; USB OTG (FS); LCD (2: SPI/I2S); Kamera (DVP 8/16-Bit); ADC (20 Kanäle, 12-Bit); DAC (2, 8-Bit); Touch (14); RMT (4 Kanäle); LED-PWM (8 Kanäle) |
| ESP32‑S3 | Zwei Xtensa LX7, 40–240 MHz, kein dedizierter LP; ULP-Coprozessoren (RISC‑V + FSM, nicht gleichzeitig) | 512 KB + 16 KB RTC | Flash: 0/4/8/16 MB; PSRAM: 0/2/4/8/16 MB; Kombinationen: z. B. FN8 (8 MB Flash + 0 PSRAM), R2 (0 + 2 MB), R8 (0 + 8 MB), R16V (0 + 16 MB), FH4R2 (4 MB Flash + 2 MB PSRAM), FN4R8 (4 MB Flash + 8 MB PSRAM) | 16 MB integriert / 32 MB extern (zukünftig: 64 MB) | 16 MB integriert / 32 MB extern (zukünftig: 64 MB) | WLAN 2,4 GHz (802.11 b/g/n), BT 5 (LE) | 45 GPIOs; 4 SPI (2 Speicher, 2 Generatoren); 2 I2S; 2 I2C; 3 UART; USB OTG (FS); SD/MMC (2 Steckplätze); TWAI; LCD/Kamera; ADC (20 Kanäle, 12 Bit); Touch (14); MCPWM; RMT; PCNT; LED-PWM |
| ESP32-C3 | Mono-RISC-V, 40–160 MHz, kein dedizierter LP/ULP-Modus | 400 KB (16 KB Cache) | Flash: 0/4 MB; PSRAM: 0 MB; Kombinationen: z. B. C3 (0 Flash + 0 PSRAM), FH4/C3FH4X (4 MB Flash + 0 PSRAM) – PSRAM nur extern | 0 MB integriert / 8 MB extern (zukünftig: 16 MB) | 4 MB integriert / 16 MB extern | WLAN 2,4 GHz (802.11 b/g/n), BT 5 (LE) | 22/16 GPIOs; 3 SPI; 1 I2S; 1 I2C; 2 UART; USB-Seriell/JTAG; TWAI; LED-PWM (6 Kan.); RMT (4 Kan.); ADC (6 Kan., 12 Bit); Temperatursensor |
| ESP32-C2 | Mono-RISC-V, 20–120 MHz, kein dedizierter LP/ULP-Modus | 272 KB (16 KB Cache) | Flash: 0 MB (nur extern); PSRAM: 0 MB; Kombinationen: Keine integriert (z. B. C2FH4: 0 + 0, aber Module wie das ESP8684 integrieren 4 MB Flash im externen Stil) | 0 MB integriert / 8 MB extern (zukünftig: 16 MB) | 0 MB integriert / 16 MB extern | WLAN 2,4 GHz (802.11 b/g/n), BT 5 (LE) | 14 GPIOs; 2 SPI; 1 I2S; 1 I2C; 2 UART; LED-PWM; GDMA; SAR-ADC (6 Kan.); Temperatursensor; USB-Seriell |
| ESP32‑C5 | Dual-RISC‑V (HP/LP), HP 40–240 MHz / LP 20–48 MHz, dedizierter LP-Modus ja; kein separater ULP-Modus | 384 KB HP + 16 KB LP + 320 KB ROM | Flash: 0/4 MB; PSRAM: 0/8 MB; Kombinationen: z. B. C5HF4 (4 MB Flash + 0 PSRAM), C5HR8 (0 Flash + 8 MB PSRAM) | 8 MB integriert / 32 MB extern (zukünftig: 64 MB) | 4 MB integriert / 32 MB extern (zukünftig: 64 MB) | Wi-Fi Dualband 6 (2,4/5 GHz, 802.11 a/b/g/n/ac/ax), BT LE 5 (Core 6.0), 802.15.4 (Zigbee 3.0 / Thread 1.4) | 29 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB-Seriell/JTAG; 2 CAN FD; SDIO; LED-PWM (6 Kan.); MCPWM (6 Kan.); RMT (4 Kan.); PARLIO; PCNT (4); ADC (6 Kan., 12 Bit); Temperatursensor; Analogkomparator (2 Pads) |
| ESP32‑C6 | Dual-RISC‑V (HP/LP), HP 40–160 MHz / LP 20 MHz, dedizierter LP ja; kein separater ULP | 512 KB HP + 16 KB LP | Flash: 0/4/8 MB; PSRAM: 0 MB; Kombinationen: z. B. C6 (0 + 0), C6FH4 (4 MB Flash + 0), C6FH8 (8 MB Flash + 0) – PSRAM nur extern | 0 MB integriert / 16 MB extern (zukünftig: 32 MB) | 8 MB integriert / 16 MB extern (zukünftig: 32 MB) | Wi-Fi 6 2,4 GHz (802.11 ax/b/g/n), BT 5.3 (LE + Mesh), 802.15.4 (Zigbee 3.0 / Thread 1.3) | 30/22 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB-Seriell/JTAG; 2 TWAI; SDIO; LED-PWM (6 Kan.); MCPWM (3); RMT (4 Kan.); PARLIO; PCNT (4); ADC (7 Kan., 12 Bit); Temperatursensor; GDMA; ETM |
| ESP32-C61 | Mono-RISC-V, 40–160 MHz, LP/ULP ja (Energieverwaltungsmodi) | 320 KB | Flash: 0/4 MB; PSRAM: 0/2/8 MB; Kombinationen: z. B. C61HF4 (4 MB Flash + 0 PSRAM), C61HR2 (0 Flash + 2 MB PSRAM), C61HR8 (0 Flash + 8 MB PSRAM) – Quad-SPI | 8 MB integriert / 32 MB extern (zukünftig) | 4 MB integriert / 32 MB extern (zukünftig) | Wi-Fi 6 2,4 GHz (802.11 ax), BT 5 (LE) | 30 GPIOs; 2 SPI; 1 I2S; 1 I2C; 3 UART; USB-Seriell/JTAG; SDIO 2.0-Slave; LED-PWM; RMT; TWAI; ADC (1 Kanal, 12 Bit); Temperatursensor |
| ESP32‑H2 | Mono-RISC‑V, 32 MHz (min., typ., Low-Power) / 96 MHz, kein dedizierter LP/ULP-Modus; LP-Komponenten für Tiefschlaf | 320 KB HP + 4 KB LP | Flash: 0/2/4 MB; PSRAM: 0 MB; Kombinationen: z. B. H2FH2S (2 MB Flash + 0 PSRAM), H2FH4S (4 MB Flash + 0 PSRAM) – PSRAM nur extern | 0 MB integriert / 16 MB extern (zukünftig: 32 MB) | 4 MB integriert / 16 MB extern (zukünftig: 32 MB) | BT LE 5.3 (1/2 Mbit/s, codierte PHY, große Reichweite, Advertising-Erweiterungen), 802.15.4 (250 kbit/s OQPSK, Thread/Zigbee 3.0/Matter) | 19 GPIOs; 2 SPI (Flash + generisch); 2 UART; 2 I2C; 1 I2S; RMT (2 Sende-/2 Empfangskanäle); LED-PWM (6 Kanäle); USB-Seriell/JTAG; TWAI (CAN); GDMA (3 Sende-/3 Empfangskanäle); PCNT; MCPWM; ADC (5 Kanäle, 12 Bit); Temperatursensor; Timer (2 Generatoren, 54-Bit, 52-Bit-System, 3 WDT) |
| ESP32-H4 | Dual-RISC-V, max. 96 MHz, dedizierter LP ja (ausgewählte Peripheriegeräte) | 320 KB | Flash: 0 MB; PSRAM: 0/4 MB; Kombinationen: z. B. H4 (0 Flash + 0 PSRAM), H4R4 (0 Flash + 4 MB PSRAM) – Unterstützung für externen Flash-Speicher | 0 MB integriert / 4 MB extern (zukünftig: 16 MB) | 0 MB integriert / 16 MB extern (Zukunft) | BT LE 5.4 (LE), 802.15.4 (Zigbee/Thread/Matter) | 35 GPIOs; I2C; I2S; SPI; UART; LED-PWM; ADC; Timer; DMA; TWAI; USB OTG; MCPWM; Touch (14); Ereignis-Task-Matrix |
| ESP32‑P4 | Dual-HP + Mono-LP-RISC‑V, HP 40‑360 MHz / LP 40 MHz, dedizierter LP-Modus ja; kein separater ULP-Modus | 768 KB HP L2MEM + 32 KB LP + 8 KB SPM | Flash: 0 MB; PSRAM: 0/16/32 MB; Kombinationen: z. B. P4NRW16 (0 Flash + 16 MB PSRAM), P4NRW32 (0 + 32 MB PSRAM) | 32 MB integriert / 64 MB extern (zukünftig: 128 MB) | 0 MB integriert / 64 MB extern (zukünftig: 128 MB) | Keine integrierten Funkmodule (MCU-fokussiert, extern möglich) | 55 GPIOs (16 LP); 4 SPI (+1 LP); 3 I2S (+1 LP); 3 I2C (+1 Analog +1 I3C); 6 UART (5 HP +1 LP); USB HS/FS OTG + Seriell/JTAG; Ethernet (10/100 RMII); 3 TWAI; SD/MMC; LED-PWM (8 Kan.); MCPWM (2); RMT (8 Kan.); PARLIO; Touch (14); 2 ADC; VAD; Bild: JPEG-Codec, ISP, H.264-Encoder, MIPI CSI/DSI (2-Lane), LCD/Kamera |
| **ESP32-E22** | Zwei RISC-V-HP-Kerne mit **500 MHz**, RCP-Architektur (Radio-Coprozessor) | **1 MB** | Kein integrierter Speicher (RCP-Design) | 0 MB integriert / extern über Host-System | 0 MB integriert / extern über Host-System | **Tri-Band Wi-Fi 6E** (2,4/5/6 GHz), 160 MHz Kanalbandbreite, 2×2 MU-MIMO, Beamforming, 1024-QAM, Datenrate bis zu 2,4 Gbit/s; **Bluetooth Classic (BR/EDR) + BLE 5.4**; Wi-Fi CERTIFIED 6E™ (Juni 2026) | **30 GPIOs**; **PCIe 2.1**; **SDIO 3.0**; **USB 2.0**; Linux-Treiber Open Source (Kernel 5.4+) |
| **ESP32‑H21** | Mono RISC‑V, bis **96 MHz** | 320 KB SRAM + 128 KB ROM | Kein integrierter Speicher (extern über SPI‑Flash) | 0 MB integrierter / externer Speicher (über SPI‑Flash) | 0 MB integrierter / externer Speicher (über SPI‑Flash) | **BT LE 5.0** (BLE 5.3-zertifiziert) + **802.15.4** (Thread/Zigbee/Matter); **20 dBm Sendeleistung**; **On-Chip-DC-DC-Wandler** | **19 GPIOs**; UART, SPI, I²C, I²S, PWM, ADC, Timer, DMA; USB-Seriell/JTAG |
| **ESP32-S31** | Dual-RISC-V, **320 MHz**, **128-Bit-SIMD-Datenpfad** | **512 KB SRAM** | S31 (0 + 0), externer Flash/PSRAM über Oktal-SPI | extern: bis zu 64 MB (250 MHz 8-Bit-DDR-PSRAM) | extern: bis zu 64 MB (Octal-SPI) | **Wi-Fi 6** (2,4 GHz, 802.11ax); **BT 5.4** (LE + Classic BR/EDR); **IEEE 802.15.4** (Thread/Zigbee); **1000 Mbit/s Ethernet-MAC** | **60 GPIOs**; DVP-Kamera (8–16 Bit); LCD (8–24 Bit parallel); 14× Touch; JPEG-Codec; 2D-Grafikbeschleunigung (PPA); 2D-DMA; 2× I2S; USB OTG; SD/MMC; TWAI; SPI; I2C; UART; **Trusted Execution Environment (TEE)** mit APM; **RAM-basierte PUF** |

### Anmerkungen zur Tabelle:

- **Architektur:** Berücksichtigt Kerne (HP/LP), Taktbereiche und Low-Power-Funktionen (ULP/LP).
- **Speicher:** Embedded-Optionen mit Variantenkombinationen; Maximalwerte inkl. zukünftiger Unterstützung (z. B. bis zu 128 MB für P4).
- **Funkmodule:** Alle Varianten, einschließlich Multiprotokoll (z. B. Wi-Fi 6 für C5/C6, 802.15.4 für C5/C6/H2 für Matter, Tri-Band für E22).
- **Schnittstellen:** Wichtige Peripheriegeräte mit Stückzahlen; Schwerpunkt auf GPIOs, Relevanz für den drahtlosen Bereich und besonderen Funktionen (z. B. MIPI für P4, PCIe für E22).
- **Quellen:** Direkt aus den Datenblättern von Espressif; keine neuen Modelle über die Liste hinaus (Stand 2025, z. B. C5 in Serienproduktion; C61/H4 neu im Portfolio; E22/H21/S31 im Jahr 2026 hinzugefügt).

### Espressif SoC-Produktportfolio

![Espressif-SoC-Produktportfolio](res/4de262290804bb22f2a6272d7fc53db0.jpg „Espressif-SoC-Produktportfolio“)

> **Hinweis:** Die obige Abbildung des Espressif-Produktportfolios (Stand: September 2025) enthält **nicht** die Varianten **ESP32‑E22**, **ESP32‑H21** und **ESP32‑S31**, die seitdem angekündigt wurden. Diese wurden zu einem späteren Zeitpunkt in die Tabelle aufgenommen.

## Tiefschlaf

Die Informationen basieren auf dem Espressif-SoC-Produktportfolio und den offiziellen Datenblättern (Stand: Juli 2026). Die Struktur berücksichtigt die spezifischen Eigenschaften der neuen Modelle (z. B. C61 als Single-Core-Wi-Fi-6-Low-Power-Modell, H4 als Dual-Core-Low-Power-Modell mit 802.15.4, E22 als RCP mit hostgesteuertem Energiemanagement, H21 als Ultra-Low-Power-BLE/802.15.4-SoC). Da die genauen Werte für den Stromverbrauch im Deep-Sleep-Modus für C61 und H4 im Portfolio nicht explizit angegeben sind, werden diese auf der Grundlage ähnlicher Modelle (C6/H2) geschätzt und entsprechend gekennzeichnet.

### Details

**Alle** ESP32-Modelle (ESP32, S2, S3, C3, C2, C5, C6, C61, H2, H4, P4, **E22, H21, S31**) unterstützen den Deep-Sleep-Modus, und in den meisten Fällen kann spezieller Speicher (RTC-SRAM oder vergleichbar) zur Sicherung von Daten während des Deep-Sleep-Modus verwendet werden. Es gibt jedoch Unterschiede in der Architektur (RTC-SRAM, LP-SRAM oder andere Mechanismen), die beeinflussen, wie und welcher Speicher für diesen Zweck verwendet wird.

### Überblick: Tiefschlaf und Speicher zur Datensicherung

**Tiefschlafmodus:** Alle Modelle können in den Tiefschlafmodus wechseln, bei dem der Hauptprozessor (HP-Kern) und die meisten Peripheriegeräte abgeschaltet werden, um Strom zu sparen. Bestimmte Speicherbereiche bleiben aktiv, um Daten zu sichern oder einfache Aufgaben auszuführen.

**RTC-SRAM**: Bei Modellen ohne dedizierten LP-Kern (ESP32, S2, S3, einige C3) ist das RTC-SRAM der Hauptspeicher, der im Tiefschlafmodus aktiv bleibt, um Daten zu sichern oder ULP-Coprozessor-Code auszuführen.

**LP-SRAM**: Bei Modellen mit einem dedizierten LP-Kern (C5, C6, H4, P4, **S31**) übernimmt das LP-SRAM diese Rolle, da der LP-Kern im Tiefschlafmodus aktiv bleiben kann. Das H2/C61 verfügt über LP-SRAM, jedoch ohne LP-Kern, und dient ausschließlich der Datenspeicherung.

**Sonderfälle:** C2/C3 verfügen über kleine RTC-Bereiche (<8 KB) ohne ULP-/LP-Kern, was Einschränkungen mit sich bringt. H2/C61 sind für extrem niedrigen Stromverbrauch (ca. 7–10 μA) optimiert und verfügen über LP-Peripheriegeräte. H4 verfügt über einen dedizierten LP-Kern für flexiblere Aufgaben im Niedrigstrombetrieb. **E22** als RCP wird typischerweise von einem Host gesteuert; das Low-Power-Management wird vom Host übernommen. **H21** bietet einen Tiefschlafmodus mit 5 µA Verbrauch dank eines integrierten DC-DC-Wandlers. Die Spezifikationen für den Tiefschlafmodus des **S31** sind noch nicht vollständig veröffentlicht.

### Modellspezifische Details

#### ESP32:

- **Tiefschlaf:** Ja, unterstützt.
- **Speicher:** 520 KB SRAM, von dem ein Teil (nicht separat als „RTC-SRAM“ spezifiziert, aber ca. 8 KB im RTC-Bereich) im Tiefschlaf aktiv bleibt. Der ULP-Coprozessor (FSM-basiert) kann darauf zugreifen, um Daten zu speichern oder einfache Aufgaben auszuführen.
- **Verwendung:** Speichern von Variablen im RTC-Speicherbereich (über die RTC-Speicher-API), z. B. Statusdaten, Zähler oder Sensorwerte. Der ULP kann diese Daten verarbeiten.
- **Einschränkung:** Begrenzter Speicher im Vergleich zu neueren Modellen; der ULP ist nicht so flexibel wie ein LP-Kern.

#### ESP32‑S2:

- **Deep Sleep:** Ja, unterstützt.
- **Speicher:** 16 KB RTC-SRAM, ausdrücklich im Datenblatt angegeben, bleibt im Deep Sleep aktiv. Zwei ULP-Coprozessoren (RISC-V + FSM, nicht gleichzeitig) können darauf zugreifen.
- **Verwendung:** Das RTC-SRAM kann für Daten (z. B. Zustände, Konfigurationsdaten) genutzt werden. Der RISC-V-ULP ermöglicht komplexere Berechnungen als der klassische ESP32.
- **Einschränkung:** 16 KB sind nicht besonders viel, reichen aber für die meisten Sensor- oder Statusdaten aus.

#### ESP32‑S3:

- **Deep Sleep:** Ja, unterstützt.
- **Speicher:** 16 KB RTC-SRAM, bleibt im Deep Sleep aktiv. ULP-Coprozessoren (RISC‑V + FSM) können diesen Speicher nutzen.
- **Verwendung:** Ähnlich wie beim S2, ideal für Daten wie Konfigurationen, Sensorwerte oder kleine Zustandsmaschinen. Der ULP-RISC-V ist für komplexere Deep-Sleep-Logik programmierbar.
- **Einschränkung:** Wie beim S2 begrenzt das 16-KB-RTC-SRAM die Datenmenge.

#### ESP32‑C3:

- **Tiefschlaf:** Ja, unterstützt.
- **Speicher:** Kein expliziter RTC-SRAM, aber ein Teil des 400-KB-SRAM (ca. 8 KB im RTC-Bereich, ähnlich wie beim ESP32) bleibt im Tiefschlaf aktiv. Kein ULP-Coprozessor, daher keine Programmierung im Tiefschlaf.
- **Verwendung:** Sie können Daten im RTC-Bereich speichern (über die ESP-IDF-RTC-Speicher-APIs), jedoch ohne ULP nur statische Speicherung, keine aktive Verarbeitung.
- **Einschränkung:** Das Fehlen eines ULP- oder LP-Kerns schränkt die Flexibilität ein; kleinerer Speicherbereich.

#### ESP32‑C2:

- **Tiefschlaf:** Ja, unterstützt.
- **Speicher:** Kein expliziter RTC-SRAM oder LP-SRAM. Ein kleiner RTC-Bereich (im Datenblatt nicht quantifiziert, geschätzt <8 KB) bleibt aktiv, ähnlich wie beim C3.
- **Nutzung:** Begrenzte Datenspeicherung im RTC-Bereich möglich (z. B. Zustandsvariablen), jedoch keine aktive Verarbeitung, da kein ULP- oder LP-Kern vorhanden ist.
- **Einschränkung:** Sehr begrenzt, da kein dedizierter Speicher oder Koprozessor vorhanden ist.

#### ESP32‑C5:

- **Deep Sleep:** Ja, unterstützt (HP-Kern ausgeschaltet, LP-Kern kann aktiv bleiben).
- **Speicher:** 16 KB LP-SRAM für den dedizierten LP-Kern (RISC-V), bleibt im Deep Sleep aktiv. Kein separater RTC-SRAM, da der LP-Kern diese Aufgaben übernimmt.
- **Verwendung:** Das LP-SRAM kann für Daten und Code des im Tiefschlaf laufenden LP-Kerns verwendet werden. Ideal für komplexe Low-Power-Logik oder Datenspeicherung.
- **Einschränkung:** 16 KB LP-SRAM sind ausreichend, aber nicht riesig; der LP-Kern bietet mehr Flexibilität als der ULP-Kern.

#### ESP32-C6:

- **Deep-Sleep-Modus:** Ja, unterstützt (ähnlich wie beim C5).
- **Speicher:** 16 KB LP-SRAM für den LP-Kern, bleibt im Tiefschlaf aktiv. Kein separates RTC-SRAM.
- **Verwendung:** Wie beim C5, LP-SRAM für Daten/Code des LP-Kerns, geeignet für komplexe Aufgaben im Tiefschlaf.
- **Einschränkung:** 16 KB LP-SRAM, aber dank des LP-Kerns flexibler.

#### ESP32‑C61:

- **Tiefschlaf:** Ja, unterstützt (optimiert für stromsparendes Wi-Fi 6, geschätzt ~10 μA).
- **Speicher:** 4 KB LP-SRAM, bleibt im Tiefschlaf aktiv. Kein separater RTC-SRAM oder dedizierter LP-Kern.
- **Verwendung:** LP-SRAM zur passiven Datenspeicherung (z. B. Zustandsvariablen, Sensordaten) im Tiefschlaf; LP-Peripheriegeräte (z. B. Timer, ADC) unterstützen einfache Aufgaben.
- **Einschränkung:** 4 KB LP-SRAM sind wenig; kein LP-Kern, daher keine komplexen Verarbeitungsvorgänge im Tiefschlaf.

#### ESP32‑H2:

- **Tiefschlaf:** Ja, unterstützt (optimiert für extrem niedrigen Stromverbrauch, 7 μA).
- **Speicher:** 4 KB LP-SRAM, bleibt im Tiefschlaf aktiv. Kein separates RTC-SRAM und kein dedizierter LP-Kern.
- **Verwendung:** LP-SRAM zur passiven Datenspeicherung (z. B. Zustandsvariablen, Sensordaten) im Tiefschlaf; LP-Peripheriegeräte (z. B. Timer, Sensoren) unterstützen einfache Aufgaben.
- **Einschränkung:** 4 KB LP-SRAM sind wenig; kein LP-Kern, daher keine komplexen Verarbeitungsvorgänge im Tiefschlaf.

#### ESP32‑H4:

- **Tiefschlaf:** Ja, unterstützt (optimiert für extrem niedrigen Stromverbrauch mit ausgewählten Peripheriegeräten, geschätzt ~7 μA).
- **Speicher:** 16 KB LP-SRAM für den LP-Kern, bleibt im Tiefschlaf aktiv. Kein separates RTC-SRAM.
- **Verwendung:** LP-SRAM für Daten/Code des LP-Kerns, geeignet für komplexe Deep-Sleep-Aufgaben (z. B. Mesh-Netzwerke, Sensorverarbeitung).
- **Einschränkung:** 16 KB LP-SRAM, jedoch flexibel dank dediziertem LP-Kern.

#### ESP32‑P4:

- **Tiefschlaf:** Ja, unterstützt (HP-Kerne ausgeschaltet, LP-Kern aktiv).
- **Speicher:** 32 KB LP-SRAM für den LP-Kern, bleibt im Tiefschlaf aktiv. Kein RTC-SRAM, da der LP-Kern Aufgaben mit geringem Stromverbrauch übernimmt.
- **Verwendung:** LP-SRAM für Daten und Code des LP-Kerns, ideal für anspruchsvolle Anwendungen mit geringem Stromverbrauch (z. B. Bildverarbeitung, Sensorlogik).
- **Einschränkung:** 32 KB sind großzügiger bemessen als bei C5/C6, keine nennenswerten Einschränkungen.

#### ESP32-E22:

- **Tiefschlaf:** Ja (als RCP in einem hostbasierten System).
- **Speicher:** Kein dediziertes LP-SRAM (RCP-Design).
- **Verwendung:** Als Radio-Coprozessor (RCP) wird der ESP32‑E22 typischerweise von einem Host-SoC gesteuert. Das Strommanagement wird vom Host-Prozessor übernommen. Der ESP32-E22 selbst kann in einen Energiesparzustand versetzt werden, während der Host den Tiefschlaf verwaltet. Genaue Stromwerte im Tiefschlaf sind im Datenblatt noch nicht angegeben.
- **Einschränkung:** RCP-Architektur – kein eigenständiger Betrieb im Energiesparmodus ohne Host.

#### ESP32‑H21:

- **Tiefschlaf:** Ja – **5 µA** im Tiefschlaf.
- **Speicher:** 4 KB LP-SRAM (wie H2).
- **Verwendung:** LP-SRAM für passive Datenspeicherung im Tiefschlaf; LP-Peripheriegeräte unterstützen einfache Aufgaben. Der integrierte DC-DC-Wandler verbessert den Wirkungsgrad während des Empfangsbetriebs (ca. 8,2 mA bei aktivem Empfang).
- **Einschränkung:** 4 KB – keine komplexen Verarbeitungsvorgänge im Tiefschlaf (kein dedizierter LP-Kern).

#### ESP32‑S31:

- **Tiefschlaf:** Ja (Spezifikationen noch nicht vollständig veröffentlicht).
- **Speicher:** Voraussichtlich mit RTC/LP-SRAM (ähnlich wie beim S3).
- **Verwendung:** Als Nachfolger der S-Serie (S2/S3) wird der ESP32‑S31 voraussichtlich über ULP-Coprozessoren (RISC‑V + FSM) und RTC-SRAM für den Tiefschlafbetrieb verfügen. Genaue Werte zum Stromverbrauch liegen noch nicht vor.
- **Grenzwert:** Spezifikationen noch nicht vollständig veröffentlicht.

### Zusammenfassung

- **Alle** ESP32-Modelle unterstützen den Deep-Sleep-Modus.
- **RTC-Speicher** (oder gleichwertig) zur Datensicherung bei allen Modellen
- **ESP32, S2, S3:** RTC-SRAM (16 KB bei S2/S3, geringerer Speicherumfang beim klassischen ESP32) zur Datenspeicherung, unterstützt durch ULP-Coprozessoren.
- **C3, C2:** Kleiner RTC-Bereich (nicht explizit angegeben, <8 KB), nur für die Speicherung statischer Daten, kein ULP-/LP-Kern.
- **C5, C6, H2, P4:** LP-SRAM (16 KB bei C5/C6, 32 KB bei P4) für die Datenspeicherung und LP-Kernaufgaben, flexibler als RTC-SRAM.
- **E22:** RCP-Architektur – Low-Power-Modus wird vom Host gesteuert.
- **H21:** 5 µA im Deep-Sleep-Modus, 4 KB LP-SRAM, kein LP-Kern.
- **S31:** Wird voraussichtlich über RTC-SRAM und ULP-Coprozessoren verfügen (Spezifikationen stehen noch aus).
- **Unterschiede:** Modelle mit ULP- (ESP32, S2, S3) oder LP-Kern (C5, C6, H2, P4, **S31**) bieten mehr Flexibilität, da sie im Tiefschlaf aktiv Code ausführen können. C3 und C2 sind eingeschränkt (nur Speicher, keine Verarbeitung).
- **C5, C6, H2, P4** können den LP-Kern ebenfalls nutzen, um **im Tiefschlaf** aktiv zu sein.

## Gründliche Bewertung der einzelnen Modelle

Auf der Grundlage der offiziellen Espressif-Datenblätter (Stand: Juli 2026) und der aus den Quellen gesammelten Details wird jedes ESP32-Modell hinsichtlich seiner Vor- und Nachteile analysiert. Der Fokus liegt auf der **entscheidenden Praxistauglichkeit**, d. h. darauf, wie die Merkmale (Architektur, Speicher, Funkmodule, Schnittstellen, Stromversorgung) das Modell für bestimmte Anwendungsbereiche optimieren. Die Bewertung berücksichtigt Faktoren wie Leistung, Energieeffizienz, Kosten, Kompatibilität (z. B. RISC‑V vs. Xtensa), Funkoptionen und Peripheriegeräte. Modelle mit RISC‑V sind zukunftsorientiert (besser für Open Source), während Xtensa etabliert ist. Neuere Modelle (C-Serie, H2, P4, **E22, H21, S31**) legen den Schwerpunkt auf geringen Stromverbrauch und Multi-Protokoll-Unterstützung (z. B. Matter), während ältere Modelle (Classic, S2, S3) allgemeiner einsetzbar sind, aber mehr Strom verbrauchen.

#### ESP32-
 – **Schwerpunkt**: Allrounder für drahtlose Netzwerke und Legacy-Anwendungen; stark bei Kombinationen aus Wi-Fi + BT Classic/LE mit Ethernet/CAN.
- **Vorteile**: Dual-Core-Xtensa für parallele Aufgaben (z. B. WLAN + BT), etabliertes Ökosystem (viel verfügbarer Code), Ethernet-MAC und TWAI (CAN) für industrielle Netzwerke, kostengünstig und robust, ULP-Coprozessor für einfache Aufgaben mit geringem Stromverbrauch.
- **Nachteile**: Höherer Stromverbrauch (Deep-Sleep ~10 μA, im aktiven Betrieb >100 mA), Xtensa-Architektur weniger zukunftsorientiert (weniger Open-Source-Tools), kein Wi-Fi 6/BT 5, begrenzte Speicheroptionen (max. 4 MB Embedded-Flash), veraltet (NRND für einige Varianten), kein dedizierter LP-Kern.
- **Gesamtbewertung**: Gut geeignet für kostengünstige, etablierte Projekte mit gemischter Konnektivität, jedoch nicht ideal für Anwendungen mit extrem geringem Stromverbrauch oder modernen Protokollen.

#### ESP32-S2
- **Schwerpunkt**: USB- und multimedienorientiert (LCD/Kamera/Touch), für reine WLAN-Geräte mit geringem Stromverbrauch.
- **Vorteile**: USB-OTG (FS) für HID/Speicher, LCD-/Kamera-Schnittstellen für Displays, 14 Touch-Sensoren, ULP-Coprozessoren (RISC-V + FSM) für flexiblen Tiefschlaf, Unterstützung für großen externen Speicher (bis zu 1 GB), kompakt und energieeffizient für WLAN-Anwendungen.
- **Nachteile**: Kein BT, Single-Core-Xtensa (geringere Leistung), kein Ethernet/CAN, Touch nicht CS-zertifiziert (Einschränkungen in störungsreichen Umgebungen), höherer Stromverbrauch als die C-Serie (Tiefschlaf ~5–7 μA), im Vergleich zum S3 veraltet.
- **Gesamtbewertung**: Stark geeignet für USB-basierte oder Display-/Touch-Geräte (z. B. Smart Panels), aber eingeschränkt ohne BT/Multi-Core.

#### ESP32-S3
- **Schwerpunkt**: KI und Multimedia (Vektor-/KI-Erweiterungen, LCD/Kamera), für Edge-Computing mit WLAN/BT LE.
- **Vorteile**: Dual-Core-Xtensa mit KI-/DSP-Erweiterungen (z. B. 128-Bit-Vektor), USB-OTG/SD für Speicher, LCD/Kamera für Video, ULP-Coprozessoren für geringen Stromverbrauch, großer Speicher (bis zu 16 MB eingebettetes PSRAM), BT 5 LE für moderne Apps.
- **Nachteile**: Kein Wi-Fi 6, höherer Stromverbrauch (Deep-Sleep ~7 μA, im Betrieb >100 mA), Xtensa statt RISC-V, Konflikte zwischen ADC und Wi-Fi, teurer als die C-Serie, kein 802.15.4.
- **Gesamtbewertung**: Ideal für KI/Multimedia (z. B. Sprach-/Bilderkennung), jedoch nicht optimal für IoT-Anwendungen mit extrem geringem Stromverbrauch oder mehreren Protokollen.

#### ESP32-C3
- **Schwerpunkt**: Kostengünstige, stromsparende Drahtlostechnik (Wi-Fi + BT LE) für einfache Sensoren.
- **Vorteile**: RISC-V-Mono-Core (zukunftsorientiert), Wi-Fi + BT 5 LE, TWAI (CAN), USB-Seriell/JTAG, preiswert und kompakt, externer Speicher bis zu 16 MB.
- **Nachteile**: Kein ULP-/LP-Kern (eingeschränkte Verarbeitung im Deep-Sleep-Modus, ~5 μA), begrenzte GPIOs (22/16), kein Ethernet/USB-OTG, Single-Core schränkt die Leistung ein, einige Varianten EOL/NRND.
- **Gesamtbewertung**: Perfekt für kostengünstige, batteriebetriebene Sensoren, aber schwach bei Multimedia und hoher Leistung.

#### ESP32‑C2
- **Schwerpunkt**: Extrem kostengünstige, minimalistische Lösung für drahtlose Anwendungen mit geringem Stromverbrauch.
- **Vorteile**: Sehr preiswert und klein, RISC‑V-Single-Core, Wi‑Fi + BT 5 LE, geringer Stromverbrauch (Deep Sleep <8 μA), Unterstützung für externen Speicher.
- **Nachteile**: Kein integrierter Flash-/PSRAM-Speicher (nur extern), wenige GPIOs (14), minimale Schnittstellen (kein USB-OTG/Ethernet/CAN), kein ULP-/LP-Kern, begrenzter SRAM (272 KB).
 – **Gesamtbewertung**: Für einfach gehaltene, in Massenproduktion gefertigte Funkgeräte (z. B. Tags), für komplexe Anwendungen jedoch zu eingeschränkt.

#### ESP32-C5
- **Schwerpunkt**: Moderne Multiprotokoll-Funktechnologie (Dualband-Wi-Fi 6 + BT LE 5 + 802.15.4) für energiesparendes IoT mit LP-Kern.
- **Vorteile**: Dualband-Wi-Fi 6 (2,4/5 GHz), BT LE 5 (inkl. Peilung), 802.15.4 (Zigbee/Thread), dedizierter LP-Kern (RISC-V, bis zu 48 MHz), CAN FD, geringer Stromverbrauch (Deep Sleep ~12 μA), RISC-V-Dual-Core.
- **Nachteile**: Weniger GPIOs (29), begrenzter integrierter Speicher (4 MB Flash/8 MB PSRAM), höherer Preis, neu (noch nicht so etabliert).
- **Gesamtbewertung**: Stark für Smart-Home-/IoT-Netzwerke (Matter-kompatibel), jedoch nicht für hohe Leistung ohne Funk.

#### ESP32-C6
- **Schwerpunkt**: Multiprotokoll mit geringem Stromverbrauch (Wi-Fi 6 2,4 GHz + BT 5.3 + 802.15.4), für batteriebetriebenes IoT mit LP-Kern.
- **Vorteile**: Wi-Fi 6 (2,4 GHz), BT 5.3 (Mesh), 802.15.4 (Zigbee/Thread), dedizierter LP-Kern (RISC-V, 20 MHz), geringer Stromverbrauch (Deep Sleep 7 μA), RISC-V-Dual-Core, TWAI.
- **Nachteile**: Kein 5-GHz-Wi-Fi, begrenzter integrierter PSRAM (nur extern), 30/22 GPIOs, kein USB-OTG/Ethernet.
- **Gesamtbewertung**: Ideal für energieeffiziente Smart-Geräte (z. B. Sensornetzwerke), in puncto Stromverbrauch besser als C5, jedoch ohne Dualband.

#### ESP32-H2
- **Schwerpunkt**: Extrem stromsparende drahtlose Kommunikation ohne WLAN (BT LE 5.3 + 802.15.4), für Thread/Zigbee/Matter.
- **Vorteile**: BT LE 5.3 (große Reichweite, Mesh), 802.15.4 (Zigbee/Thread), RISC-V-Single-Core (96 MHz), extrem geringer Stromverbrauch (Deep Sleep 7 μA), USB-Seriell/JTAG, kompakt.
- **Nachteile**: Kein WLAN, kleines SRAM (320 KB + 4 KB LP), wenige GPIOs (19), kein dedizierter LP-Kern (nur LP-Komponenten), begrenzte Schnittstellen.
- **Gesamtbewertung**: Ideal für batteriebetriebene Mesh-Netzwerke (z. B. Smart Lighting), jedoch ungeeignet für WLAN-Anwendungen.

#### ESP32-P4
- **Schwerpunkt**: Hochleistungs-MCU ohne Funkmodule, für KI/Multimedia (JPEG/H.264/MIPI) mit kabelgebundener Konnektivität.
- **Vorteile**: Dual-HP + Mono-LP-RISC-V (bis zu 360 MHz), KI-/DSP-Erweiterungen, Multimedia (JPEG-Codec, H.264-Encoder, MIPI CSI/DSI), USB HS/FS OTG, Ethernet, 55 GPIOs (16 LP), großer Speicher (bis zu 32 MB eingebettetes PSRAM), VAD/Touch.
- **Nachteile**: Keine integrierten Funkmodule (extern erforderlich), kein eingebetteter Flash-Speicher, höherer Stromverbrauch (Deep-Sleep-Modus 0,025 mA), teurer, neu (weniger Support).
- **Gesamtbewertung**: Perfekt für leistungsstarke kabelgebundene/KI-Geräte (z. B. HMI-Panels), jedoch nicht für drahtlose Anwendungen ohne Zusatzkomponenten.

#### ESP32-E22
- **Schwerpunkt**: Hochleistungs-Koprozessor (RCP) für drahtlose Konnektivität mit Tri-Band-Wi-Fi 6E + Dual-Mode-Bluetooth.
- **Vorteile**:
 - **Erster Tri-Band-Wi-Fi-6E-SoC von Espressif** (2,4 / 5 / 6 GHz)
 - **160-MHz-Kanalbandbreite + 2×2 MU-MIMO + Beamforming** für hohen Durchsatz und geringe Latenz
 - **Dual-Core-RISC-V mit 500 MHz**
 - **Datenrate bis zu 2,4 Gbit/s**
 - **Bluetooth Classic (BR/EDR) + BLE 5.4** in einem Chip
 - **RCP-Architektur** – entlastet den Host von Netzwerkstacks
 - **Flexible Host-Schnittstellen**: PCIe 2.1, SDIO 3.0, USB 2.0
 - **Open-Source-Linux-Treiber** (Kernel 5.4+) – senkt die Integrationshürde
 - **Wi-Fi CERTIFIED 6E™** – garantiert Interoperabilität
- **Nachteile**:
 - **Kein eigenständiger MCU-Betrieb** – immer auf den Host-Prozessor angewiesen (RCP-Design)
 - **Kein integrierter Flash-/PSRAM-Speicher** – Speicher über den Host
 - **Kein dedizierter LP-Kern** – Low-Power-Steuerung erfolgt über den Host
 - **Höherer Preis** – Positionierung im High-End-Bereich
 - **Neu** – Ökosystem noch nicht so gut etabliert (der Linux-Treiber ist jedoch Open Source)
- **Gesamtbewertung**: Ideal für **Anwendungen mit hoher Bandbreite** wie 4K/8K-Videostreaming, AR/VR-Zubehör, industrielle Brückenlösungen und Smart-Home-Hubs der nächsten Generation. Nicht geeignet für eigenständige, batteriebetriebene Sensoren mit geringem Stromverbrauch.

#### ESP32-H21
- **Schwerpunkt**: Ultra-Low-Power-Wireless-SoC für batteriebetriebene IoT-Geräte auf Basis von Thread, Matter, Zigbee und BLE.
- **Vorteile**:
 - **Extrem geringer Stromverbrauch**: Deep Sleep 5 µA, Light Sleep 9 µA
 - **On-Chip-DC-DC-Wandler** – reduziert den Betriebsstrom (RX: 8,2 mA)
 - **20 dBm Sendeleistung** – verbesserte Reichweite und Verbindungsstabilität
 - **ESP-Matter-SDK-kompatibel** – nahtlose Matter-over-Thread-Entwicklung
 - **ESP-BLE-MESH-Unterstützung** – skalierbare Netzwerke mit mehreren Knoten
 - **ESP-IDF vollständig unterstützt** – inkl. ESP‑IDF v6.0
 - **RISC‑V-Architektur** – zukunftsorientiert
- **Nachteile**:
 - **Kein WLAN** – nur BT LE + 802.15.4
 - **Kein dedizierter LP-Kern** – nur LP-Komponenten (wie H2)
 - **Begrenztes SRAM** (320 KB) – weniger als bei H4 (384 KB)
 - **Kein USB-OTG** – nur USB-Serial/JTAG
 - **Inkrementelles Update gegenüber H2** – keine radikalen Änderungen
- **Gesamtbewertung**: Ideal für **extrem stromsparende, batteriebetriebene Mesh-Netzwerke** (Smart-Home-Sensoren, Gebäudeautomation, Wearables). Bessere Energieeffizienz als H2 dank DC-DC-Wandler. Nicht für WLAN-Anwendungen geeignet.

#### ESP32-S31
- **Schwerpunkt**: Hochleistungsfähiger Dual-Core-RISC-V-SoC mit Wi-Fi 6, BT 5.4, 802.15.4, Gigabit-Ethernet und erweiterten HMI-Funktionen.
- **Vorteile**:
 - **Erster RISC-V-SoC der S-Serie** – ersetzt Xtensa (S2/S3)
 - **Wi-Fi 6 + BT 5.4 (LE + Classic) + 802.15.4 + Gigabit-Ethernet** – All-in-One-Konnektivitäts
 - **128-Bit-SIMD-Datenpfad** – beschleunigt KI-/ML-Workloads
 - **Umfassende HMI-Funktionen**: DVP-Kamera, LCD (8–24 Bit), 14× Touch, JPEG-Codec, 2D-Grafik
 - **60 GPIOs** – sehr flexibel
 - **RAM-basiertes PUF + TEE + APM** – höchstes Sicherheitsniveau
 - **Matter-kompatibel** (Wi-Fi + Thread)
- **Nachteile**:
 - **Angekündigt, aber noch nicht vollständig verfügbar**
 - **Keine genauen Werte zum Stromverbrauch** bekannt
 - **Komplexität** – viele Funktionen erhöhen den Entwicklungsaufwand
 - **Positionierung** – zwischen S3 (KI/Multimedia) und P4 (Hochleistung) → mögliche Überschneidungen
- **Gesamtbewertung**: Der ESP32-S31 ist der **Nachfolger des S2/S3 mit RISC-V-Architektur** und einem erweiterten Funktionsumfang. Er kombiniert **Wi-Fi 6, BT 5.4, 802.15.4 und Gigabit-Ethernet** mit **fortschrittlichen HMI- und Sicherheitsfunktionen**. Ideal für **anspruchsvolle IoT-Anwendungen** mit hohen Anforderungen an Konnektivität, Multimedia und Sicherheit.

## Liste typischer Anwendungen

Nachfolgend finden Sie eine Liste mit **50** typischen Anwendungen für ESP32-Modelle, basierend auf den Empfehlungen von Espressif (z. B. Smart Home, IoT, Industrie). Diese decken Bereiche wie Sensoren mit geringem Stromverbrauch, Multimedia, KI, Industrie und Wearables ab. Die Liste ist nummeriert und beschreibt kurz den jeweiligen Schwerpunkt.

1. Smart-Home-Hub (z. B. zentrale Steuerung mit Multi-Protokoll).
2. WLAN-Access-Point/Extender (z. B. Netzwerkverlängerung).
3. Bluetooth-Audiogerät (z. B. Lautsprecher/Headset).
4. Energiesparender Sensorknoten (z. B. Umgebungssensor mit Batterie).
5. KI-Edge-Computing (z. B. Spracherkennung).
6. Überwachungskamera (z. B. Videoüberwachung mit Streaming).
7. Tragbarer Fitness-Tracker (z. B. Schrittzähler mit BT).
8. Industrielles IoT-Gateway (z. B. Datenerfassung mit CAN/Ethernet).
9. Zigbee/Thread-Smart-Lighting (z. B. Lampensteuerung).
10. USB-HID-Gerät (z. B. Maus/Tastatur).
11. Ethernet-verbundener Controller (z. B. kabelgebundene Automatisierung).
12. CAN-Bus-Fahrzeugmonitor (z. B. Fahrzeugdiagnose).
13. LCD-Display (z. B. HMI-Schnittstelle).
14. Touchscreen-Gerät (z. B. Bedienfeld).
15. Batteriebetriebene Fernbedienung (z. B. IR-Fernbedienung).
16. Matter-kompatibler Smart Plug (z. B. Steckdose mit Multi-Protokoll).
17. Wi-Fi 6-Mesh-Netzwerk (z. B. Heim-Mesh).
18. Bluetooth-Mesh-Sensornetzwerk (z. B. Gebäudeüberwachung).
19. 802.15.4 Low-Power-Mesh (z. B. Thread-Netzwerk).
20. Robotik-Steuerung (z. B. Motorsteuerung mit PWM).
21. Barcode-Scanner (z. B. Bildverarbeitung).
22. Sprachassistent (z. B. Sprachsteuerung).
23. Sicheres IoT-Gerät (z. B. mit Verschlüsselung/Boot).
24. Umweltmessstation (z. B. Wetterstation).
25. SD-Karten-Datenlogger (z. B. Protokollierung mit Speicherung).
26. PWM-Motortreiber (z. B. Gleichstrommotoren).
27. Analoger Sensorleser (z. B. Temperatur/Druck mit ADC).
28. Ortungs-Tag (z. B. BT-LE-Beacon).
29. Intelligenter Thermostat (z. B. Heizungssteuerung).
30. POS-Terminal (z. B. Zahlungsterminal mit Display).
31. Steuerungssystem für Serviceroboter (z. B. Navigation mit KI).
32. Audio-Streaming-Gerät (z. B. Musikplayer).
33. Wearable zur Gesundheitsüberwachung (z. B. Pulssensor).
34. Landwirtschaftssensor (z. B. Bodenfeuchte mit geringem Stromverbrauch).
35. Verkaufsautomaten-Steuerung (z. B. Bezahlung/Display).
36. **4K/8K-Video-Streaming-Gerät** (E22: hohe Bandbreite).
37. **AR/VR-Zubehör** (E22: geringe Latenz).
38. **Drahtloser Netzwerkadapter (M.2-Format)** (E22: PCIe/SDIO).
39. **Industrielle Bridging-Lösung** (E22: robustes Wi-Fi 6E).
40. **Set-Top-Box-/Laptop-Konnektivität** (E22: PCIe/SDIO-Integration).
41. **Matter-over-Thread-Sensor** (H21: ESP-Matter-SDK, 5 µA im Tiefschlafmodus).
42. **Bluetooth-Mesh-Beleuchtung** (H21: ESP-BLE-MESH, 20 dBm).
43. **Anwesenheits-/Umgebungssensor** (H21: extrem geringer Stromverbrauch, 5 µA).
44. **Tag zur Bestandsverfolgung** (H21: 5 µA im Tiefschlaf, 20 dBm Reichweite).
45. **Tragbarer Gesundheitsmonitor** (H21: extrem geringer Stromverbrauch, kompakte GPIOs).
46. **Smart Speaker / Sprachassistent** (S31: BT 5.4 LE Audio + I2S + KI-Beschleunigung).
47. **Industrielles HMI-Panel** (S31: 24-Bit-LCD, 14×-Touch, Ethernet).
48. **Sicherheitskamera mit Edge-KI** (S31: DVP-Kamera + JPEG-Codec + KI-Beschleunigung).
49. **Matter-Gateway (Wi-Fi + Thread)** (S31: Wi-Fi 6 + 802.15.4 + Ethernet).
50. **Kassenterminal** (S31: USB OTG + SD/MMC + Sicherheitsfunktionen).

### Bewertungstabelle

Die Tabelle bewertet die Eignung der einzelnen Modelle für die Anwendungen mit ++ (sehr gut, optimal), + (gut, machbar), 0 (neutral, mit Einschränkungen), - (schlecht, ungeeignet), -- (sehr schlecht, unmöglich). Die Bewertung basiert auf den Funktionen (z. B. Funkmodule für drahtlose Verbindungen, LP-Core für geringen Stromverbrauch, Schnittstellen für Multimedia). Optionaler Text in Klammern erläutert die wichtigsten Gründe.

| Anwendung | ESP32 | ESP32‑S2 | ESP32‑S3 | ESP32‑C3 | ESP32‑C2 | ESP32‑C5 | ESP32‑C6 | ESP32‑H2 | ESP32‑P4 | **ESP32‑E22** | **ESP32‑H21** | **ESP32‑S31** |
|-----------|-------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1. Smart-Home-Hub | ++ (WLAN/BT + Ethernet) | + (WLAN, aber kein BT) | ++ (KI/Multimedia + BT LE) | + (kostengünstiges WLAN/BT) | 0 (minimal, aber WLAN/BT) | ++ (Multi-Protokoll-WLAN 6) | ++ (WLAN 6 + 802.15.4) | + (802.15.4/Bluetooth, kein WLAN) | + (hohe Leistung, aber externe Funkmodule) | ++ (Tri-Band-WLAN 6E + Bluetooth Classic/BLE) | + (802.15.4/Bluetooth, kein WLAN) | ++ (WLAN 6 + 802.15.4 + Ethernet) |
| 2. WLAN-Zugangspunkt/Repeater | ++ (Dual-Core-WLAN) | ++ (WLAN + USB) | ++ (WLAN + Speicher) | + (Stromsparendes WLAN) | + (Minimales WLAN) | ++ (Dualband-WLAN 6) | ++ (WLAN 6) | -- (Kein WLAN) | - (Keine Funkmodule) | ++ (Tri-Band-WLAN 6E) | -- (Kein WLAN) | ++ (WLAN 6) |
| 3. Bluetooth-Audiogerät | ++ (BT Classic/LE) | -- (Kein BT) | ++ (BT LE + I2S) | + (BT LE) | + (BT LE) | ++ (BT LE 5 + I2S) | ++ (BT 5.3 Mesh) | ++ (BT LE 5.3) | + (I2S/LP, aber externes BT) | ++ (BT Classic + BLE 5.4) | ++ (BT LE 5.3 + I2S) | ++ (BT 5.4 LE Audio + Classic) |
| 4. Sensor-Knoten mit geringem Stromverbrauch | + (ULP, aber stromintensiv) | + (ULP-Coprozessoren) | + (ULP-Coprozessoren) | ++ (RISC-V mit geringem Stromverbrauch) | ++ (ultra-kostengünstig/stromsparend) | ++ (LP-Kern + geringer Stromverbrauch) | ++ (LP-Kern + 7 μA im Tiefschlaf) | ++ (ultra-geringer Stromverbrauch 7 μA) | + (LP-Kern, jedoch ohne Funk) | – (kein eigenständiger Low-Power-Modus) | ++ (5 µA im Tiefschlafmodus) | + (LP-Kern erwartet, Spezifikationen stehen noch aus) |
| 5. KI-Edge-Computing | + (Dual-Core) | 0 (Single-Core) | ++ (Vektor-/KI-Erweiterungen) | – (Single-Core, wenig SRAM) | -- (minimal) | + (Dual-Core-RISC-V) | + (Dual-Core) | - (Single-Core, wenig SRAM) | ++ (KI-/DSP-Erweiterungen) | 0 (RCP, keine KI) | – (Single-Core, keine KI) | ++ (128-Bit-SIMD + KI/DSP) |
| 6. Überwachungskamera | + (Wi-Fi/BT) | ++ (LCD/Kamera + Wi-Fi) | ++ (LCD/Kamera + KI) | 0 (keine Kameraschnittstelle) | - (Minimale Schnittstellen) | + (Wi-Fi 6, aber keine Kamera) | + (Wi-Fi 6) | - (Kein Wi-Fi/keine Kamera) | ++ (MIPI CSI/DSI + H.264) | 0 (Keine Kamera) | - (Kein Wi-Fi/keine Kamera) | ++ (DVP + JPEG + KI) |
| 7. Tragbarer Fitness-Tracker | + (BT + Touch) | + (Touch + geringer Stromverbrauch) | ++ (BT LE + Touch/KI) | ++ (BT LE + geringer Stromverbrauch) | ++ (BT LE mit geringem Stromverbrauch) | ++ (BT LE 5 + LP-Kern) | ++ (BT 5.3 + LP-Kern) | ++ (BT LE 5.3 mit geringem Stromverbrauch) | + (Touch + LP, aber groß) | 0 (kein BT LE) | ++ (BT LE 5.3 mit geringem Stromverbrauch) | ++ (BT 5.4 + Touch) |
| 8. Industrielles IoT-Gateway | ++ (Ethernet/CAN + Dual-Core) | + (USB/TWAI) | ++ (TWAI + SD) | + (TWAI + kostengünstig) | 0 (minimal) | ++ (CAN FD + Multi-Protokoll) | ++ (TWAI + Wi-Fi 6) | + (802.15.4 + TWAI) | ++ (Ethernet + CAN) | + (RCP, kein CAN) | + (TWAI) | ++ (Gigabit-Ethernet + TWAI) |
| 9. Zigbee/Thread-Smart-Lighting | 0 (kein 802.15.4) | 0 (kein 802.15.4) | 0 (kein 802.15.4) | 0 (kein 802.15.4) | 0 (kein 802.15.4) | ++ (802.15.4 + Zigbee/Thread) | ++ (802.15.4 + Thread 1.3) | ++ (802.15.4 + Zigbee/Thread) | – (keine Funkmodule) | 0 (kein 802.15.4) | ++ (802.15.4 + Thread/Zigbee/Matter) | ++ (802.15.4 + Thread/Zigbee) |
| 10. USB-HID-Gerät | + (UART/USB-Seriell) | ++ (USB-OTG-FS) | ++ (USB-OTG-FS) | + (USB-Seriell) | + (USB-Seriell) | + (USB-Seriell) | + (USB-Seriell) | + (USB-Seriell) | ++ (USB-HS/FS-OTG) | + (USB 2.0) | + (USB-Seriell) | ++ (USB OTG) |
| 11. Ethernet-verbundener Controller | ++ (Ethernet-MAC) | - (kein Ethernet) | - (kein Ethernet) | - (kein Ethernet) | - (kein Ethernet) | - (kein Ethernet) | - (kein Ethernet) | – (kein Ethernet) | ++ (Ethernet 10/100) | 0 (kein Ethernet-MAC – über Host) | – (kein Ethernet) | ++ (Gigabit-Ethernet-MAC) |
| 12. CAN-Bus-Fahrzeugmonitor | ++ (TWAI/CAN) | + (TWAI) | + (TWAI) | ++ (TWAI) | - (kein CAN) | ++ (2x CAN FD) | ++ (2x TWAI) | + (TWAI) | ++ (3x TWAI) | 0 (kein CAN) | + (TWAI) | ++ (TWAI) |
| 13. LCD-Display | + (I2S/SPI) | ++ (LCD-Schnittstelle) | ++ (LCD/Kamera) | 0 (kein LCD) | – (Minimal) | 0 (kein LCD) | 0 (kein LCD) | 0 (kein LCD) | ++ (MIPI DSI + LCD) | 0 (kein LCD) | 0 (kein LCD) | ++ (24-Bit-Parallel-LCD + 2D-Grafik) |
| 14. Touchscreen-Gerät | ++ (10-Punkt-Touch) | ++ (14-Punkt-Touch) | ++ (14-Punkt-Touch) | - (kein Touch) | - (kein Touch) | - (kein Touch) | - (kein Touchscreen) | - (kein Touchscreen) | ++ (14-Finger-Touch) | - (kein Touchscreen) | - (kein Touchscreen) | ++ (14×-Touch) |
| 15. Batteriebetriebene Fernbedienung | + (BT + Low-Power) | + (Wi-Fi + RMT) | + (BT LE) | ++ (BT LE Low-Power) | ++ (BT LE Minimal) | ++ (BT LE 5 LP-Core) | ++ (BT 5.3 LP-Core) | ++ (BT LE 5.3 Low-Power) | + (RMT + LP-Core) | 0 (kein BT LE) | ++ (BT LE 5.3 + 5 µA) | ++ (BT 5.4 + LP-Core) |
| 16. Matter-kompatibler Smart Plug | + (Wi-Fi/BT) | + (Wi-Fi) | + (Wi-Fi/BT LE) | + (Wi-Fi/BT LE) | + (Wi-Fi/BT LE) | ++ (Multi-Protokoll) | ++ (Wi-Fi 6 + 802.15.4) | ++ (802.15.4/BT LE) | - (Keine Funkmodule) | + (Wi-Fi/BT, kein 802.15.4) | ++ (802.15.4/BT LE + Matter) | ++ (Wi-Fi 6 + 802.15.4) |
| 17. Wi-Fi 6-Mesh-Netzwerk | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | - (Kein Wi-Fi 6) | – (Kein Wi-Fi 6) | ++ (Dualband-Wi-Fi 6) | ++ (Wi-Fi 6 2,4 GHz) | -- (Kein Wi-Fi) | – (Keine Funkmodule) | ++ (Tri-Band-Wi-Fi 6E) | -- (Kein Wi-Fi) | ++ (Wi-Fi 6) |
| 18. Bluetooth-Mesh-Netzwerk | + (BT LE) | -- (Kein BT) | ++ (BT 5 LE Mesh) | + (BT 5 LE) | + (BT 5 LE) | ++ (BT LE 5) | ++ (BT 5.3 Mesh) | ++ (BT LE 5.3 Mesh) | - (Keine Funkmodule) | ++ (BT Classic + BLE 5.4) | ++ (BT LE 5.3 Mesh) | ++ (BT 5.4 Mesh 1.1) |
| 19. 802.15.4 Low-Power-Mesh | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | - (Kein 802.15.4) | ++ (802.15.4) | ++ (802.15.4) | ++ (802.15.4) | - (keine Funkmodule) | 0 (kein 802.15.4) | ++ (802.15.4) | ++ (802.15.4) |
| 20. Robotik-Steuerung | ++ (Dual-Core + PWM) | + (Single-Core + PWM) | ++ (Dual-Core + MCPWM) | + (Mono-Core + PWM) | 0 (Minimale PWM) | ++ (MCPWM + Dual-Core) | ++ (MCPWM + Dual-Core) | + (MCPWM) | ++ (MCPWM + hohe Leistung) | 0 (RCP, keine PWM) | + (PWM) | ++ (MCPWM) |
| 21. Barcode-Scanner | + (Wi-Fi/BT) | ++ (Kamera) | ++ (Kamera + KI) | 0 (keine Kamera) | – (keine Kamera) | 0 (keine Kamera) | 0 (keine Kamera) | 0 (keine Kamera) | ++ (ISP + MIPI CSI) | 0 (keine Kamera) | 0 (keine Kamera) | ++ (DVP + JPEG) |
| 22. Sprachassistent | + (Dual-Core + I2S) | + (I2S + USB) | ++ (I2S + KI) | 0 (I2S, aber Mono) | 0 (I2S minimal) | + (I2S + Dual-Core) | + (I2S + Dual-Core) | + (I2S) | ++ (VAD + I2S/LP) | 0 (kein I2S/KI) | + (I2S) | ++ (BT 5.4 LE Audio + I2S + KI) |
| 23. Sicheres IoT-Gerät | ++ (Krypto-Beschleunigung) | ++ (Krypto + Secure Boot) | ++ (Krypto + Secure Boot) | ++ (Krypto) | + (Krypto) | ++ (Krypto + XTS-AES) | ++ (Krypto + XTS-AES) | ++ (Kryptografie) | ++ (Kryptografie + DSA) | ++ (Volle WPA3-Sicherheit in RCP) | ++ (Kryptografie) | ++ (PUF + TEE + APM) |
| 24. Umweltüberwachungsstation | + (ADC + Wireless) | + (ADC + Touch) | + (ADC + Touch) | ++ (ADC + Low-Power) | ++ (ADC + Low-Power) | ++ (ADC + LP-Core) | ++ (ADC + LP-Core) | ++ (ADC + Low-Power) | + (ADC + Touch) | 0 (kein ADC) | ++ (ADC + 5 µA) | ++ (ADC) |
| 25. SD-Karten-Datenlogger | + (SPI) | + (SPI) | ++ (SD/MMC) | + (SPI) | + (SPI) | ++ (SDIO) | ++ (SDIO) | 0 (keine SD) | ++ (SD/MMC) | 0 (keine SD) | 0 (keine SD) | ++ (SD/MMC) |
| 26. PWM-Motortreiber | ++ (PWM) | ++ (LED-PWM) | ++ (MCPWM) | ++ (LED-PWM) | ++ (LED-PWM) | ++ (MCPWM 6 Kan.) | ++ (MCPWM 3 Kan.) | ++ (LED-PWM) | ++ (MCPWM 2) | 0 (kein PWM) | ++ (PWM) | ++ (MCPWM) |
| 27. Analog-Sensor-Lesegerät | ++ (ADC 18 Kan.) | ++ (ADC 20 Kan.) | ++ (ADC 20 Kan.) | ++ (ADC 6 Kan.) | ++ (ADC 6 Kan.) | ++ (ADC 6 Kan.) | ++ (ADC 7 Kan.) | ++ (ADC 5 Kan.) | ++ (2 ADC) | 0 (kein ADC) | ++ (ADC) | ++ (ADC) |
| 28. Asset-Tracking-Tag | + (BT LE) | - (kein BT) | + (BT LE) | ++ (BT LE Low-Power) | ++ (BT LE Low-Power) | ++ (BT LE 5-Richtungs-Ortung) | ++ (BT 5.3) | ++ (BT LE 5.3 Long Range) | - (Keine Funkmodule) | 0 (kein BT LE) | ++ (BT LE 5.3 + 5 µA + 20 dBm) | ++ (BT 5.4 Peilung) |
| 29. Smart-Thermostat | ++ (WLAN/BT + Touch) | ++ (WLAN + Touch) | ++ (WLAN/BT + Touch) | + (WLAN/BT) | + (WLAN/BT) | ++ (Multi-Protokoll) | ++ (WLAN 6 + 802.15.4) | + (802.15.4/BT) | + (Touch, externe Funkmodule) | + (Wi-Fi/BT, kein 802.15.4) | ++ (802.15.4/BT + 5 µA) | ++ (Wi-Fi 6 + 802.15.4 + Touch) |
| 30. POS-Terminal | + (Ethernet + Display) | ++ (USB + LCD) | ++ (SD + LCD) | 0 (kein USB-OTG) | - (Minimal) | 0 (kein USB-OTG) | 0 (kein USB-OTG) | 0 (kein USB) | ++ (USB-HS + SD/MMC) | 0 (kein USB-OTG) | 0 (kein USB-OTG) | ++ (USB-OTG + SD/MMC + Sicherheit) |
| 31. Service-Roboter-Steuerung | ++ (Dual-Core + Ethernet) | + (Mono-Core + USB) | ++ (Dual-Core + KI) | + (Mono-Core) | - (Minimal) | ++ (Dual-Core + CAN) | ++ (Dual-Core) | + (Mono-Core) | ++ (High-Perf + KI) | 0 (RCP, keine KI) | - (Single-Core, keine KI) | ++ (High-Perf + KI + Ethernet) |
| 32. Audio-Streaming-Gerät | ++ (I2S + BT) | ++ (I2S + WLAN) | ++ (I2S + BT LE) | + (I2S + BT LE) | + (I2S + BT LE) | ++ (I2S + BT LE 5) | ++ (I2S + BT 5.3) | ++ (I2S + BT LE 5.3) | ++ (I2S/LP + VAD) | ++ (BT Classic + BLE 5.4) | ++ (I2S + BT LE 5.3) | ++ (BT 5.4 LE Audio + I2S) |
| 33. Wearable zur Gesundheitsüberwachung | + (BT + ADC) | + (ADC + Touch) | ++ (BT LE + Touch/KI) | ++ (BT LE + ADC) | ++ (BT LE + ADC) | ++ (BT LE 5 + ADC) | ++ (BT 5.3 + ADC) | ++ (BT LE 5.3 + ADC) | + (ADC + Touch) | 0 (kein BT LE) | ++ (BT LE 5.3 + ADC + 5 µA) | ++ (BT 5.4 + ADC + Touch) |
| 34. Landwirtschaftssensor | + (Wi-Fi/BT + ADC) | + (Wi-Fi + ADC) | + (Wi-Fi/BT + ADC) | ++ (Wi-Fi/BT + Low-Power) | ++ (Wi-Fi/BT + Low-Power) | ++ (Multi-Protokoll + ADC) | ++ (Wi-Fi 6 + ADC) | ++ (802.15.4/Bluetooth + ADC) | + (ADC, externe Funkmodule) | + (WLAN/Bluetooth, kein 802.15.4) | ++ (802.15.4/BT + ADC + 5 µA) | ++ (Wi-Fi 6 + 802.15.4 + ADC) |
| 35. Automaten-Steuerung | ++ (Ethernet + Display) | ++ (USB + LCD/Touch) | ++ (SD + LCD/Touch) | + (SPI) | 0 (Minimal) | + (SDIO) | + (SDIO) | 0 (kein SD) | ++ (SD/MMC + Ethernet) | 0 (kein SD/Ethernet) | 0 (kein SD) | ++ (SD/MMC + Ethernet) |
| 36. 4K/8K-Videostreaming | – | – | – | – | – | – | – | – | – | ++ (2,4 Gbit/s, 160 MHz) | – | + (Wi-Fi 6, jedoch geringere Bandbreite) |
| 37. AR/VR-Zubehör | - | - | - | - | - | - | - | - | - | ++ (geringe Latenz) | - | + |
| 38. WLAN-Adapter | - | - | - | - | - | - | - | - | - | ++ (PCIe/SDIO) | - | - |
| 39. Industrielle Brückenlösung | + | 0 | 0 | 0 | 0 | + | + | 0 | ++ | ++ (Robustes Wi-Fi 6E) | 0 | ++ (Gigabit-Ethernet) |
| 40. Set-Top-Box / Laptop | - | - | - | - | - | - | - | - | - | ++ (PCIe/SDIO) | - | - |
| 41. Matter-over-Thread-Sensor | - | - | - | - | - | + | + | ++ | - | - | ++ (ESP-Matter-SDK, 5 µA) | ++ |
| 42. Bluetooth-Mesh-Beleuchtung | + | - | + | + | + | + | ++ | ++ | - | + | ++ (ESP-BLE-MESH, 20 dBm) | ++ |
| 43. Anwesenheitssensor | + | + | + | ++ | ++ | ++ | ++ | ++ | + | - | ++ (5 µA) | ++ |
| 44. Ortungs-Tag | + | - | + | ++ | ++ | ++ | ++ | ++ | - | - | ++ (5 µA + 20 dBm) | ++ |
| 45. Tragbarer Gesundheitsmonitor | + | + | ++ | ++ | ++ | ++ | ++ | ++ | + | - | ++ (5 µA + kompakt) | ++ |
| 46. Smart Speaker | + | + | ++ | 0 | 0 | + | + | + | ++ | - | - | ++ (BT 5.4 LE Audio + KI) |
| 47. Industrielles HMI | + | ++ | ++ | 0 | - | 0 | 0 | 0 | ++ | - | - | ++ (LCD 24-Bit + Touch + Ethernet) |
| 48. Sicherheitskamera mit Edge-KI | + | ++ | ++ | 0 | - | 0 | 0 | - | ++ | - | - | ++ (DVP + JPEG + KI) |
| 49. Matter-Gateway | + | + | + | + | + | ++ | ++ | ++ | - | + | ++ | ++ (Wi-Fi 6 + 802.15.4 + Ethernet) |
| 50. POS-Terminal | + | ++ | ++ | 0 | - | 0 | 0 | 0 | ++ | 0 | - | ++ (USB OTG + SD/MMC + Sicherheit) |

### Sinnvolle Kombinationen von ESP32-Modellen

Auf der Grundlage der vorangegangenen Analysen (Architektur, Funkmodule, Schnittstellen, Vor- und Nachteile sowie Anwendungsbereiche) wurden mögliche Kombinationen identifiziert, die die Stärken der Modelle ergänzen. Beispielsweise wird ein Modell ohne Funkmodule (z. B. P4) durch ein Modell mit Funkmodulen (z. B. C6) ergänzt, oder ein Modell mit geringem Stromverbrauch (z. B. H2) erweitert ein Hochleistungsmodell (z. B. S3). Der Fokus liegt auf sinnvollen Paaren/Trios (nicht auf allen möglichen, da beispielsweise „Classic“ + „S2“ redundant wäre), wobei Komplementarität (z. B. Rechenleistung + Konnektivität) im Vordergrund steht. Für jede Kombination: Beschreibung, warum sie sinnvoll ist, sowie Anwendungsbereiche (von einfach bis anspruchsvoll, einschließlich Industrie 4.0 mit Schwerpunkt auf Edge-Computing, vorausschauender Wartung, sicheren Gateways und Multiprotokoll-Netzwerken).

#### 1. ESP32-P4 + ESP32-C6
- **Beschreibung**: P4 als leistungsstarke MCU (Dual-HP-RISC-V mit bis zu 360 MHz, KI/DSP, Multimedia-Schnittstellen wie MIPI CSI/DSI, Ethernet, USB HS) kombiniert mit C6 als Funkmodul (Wi-Fi 6 2,4 GHz, BT 5.3 Mesh, 802.15.4 für Zigbee/Thread, dedizierter LP-Kern für geringen Stromverbrauch).
- **Warum das sinnvoll ist**: P4 verfügt über keine Funkmodule, C6 ergänzt dies durch Multi-Protokoll-Funk und einen LP-Kern für energieeffiziente Edge-Aufgaben; die gemeinsame RISC-V-Architektur erleichtert die Software-Integration (z. B. über SPI/I2C/UART-Verbindung).
- **Anwendungen**:
 - Einfach: Smart-Home-Gateway (P4 für Display-/USB-Verarbeitung, C6 für WLAN-/Thread-Konnektivität).
 - Mittel: AR-Brille für Schulungszwecke (P4 für H.264-Kodierung/MIPI-Kamera, C6 für BT-Mesh-Verbindung zu Sensoren).
 - Anspruchsvoll (Industrie 4.0): Vorausschauendes Wartungssystem in Fabriken (P4 für Edge-KI-Analyse von Schwingungen/Bildern, C6 für sichere drahtlose Übertragung in die Cloud; ermöglicht Echtzeit-Fehlererkennung in Maschinennetzwerken).

#### 2. ESP32-P4 + ESP32-C5-
- **Beschreibung**: P4 (Hochleistungs-MCU mit KI, Ethernet, USB HS/FS, großem Speicher) + C5 (Dualband-Wi-Fi 6 2,4/5 GHz, BT LE 5, 802.15.4, LP-Core, CAN FD).
- **Warum es sinnvoll ist**: C5 bietet Dualband-WLAN für höhere Bandbreite (z. B. Videostreaming), P4 ergänzt dies durch kabelgebundene Konnektivität (Ethernet) und Multimedia-Verarbeitung; beide basieren auf RISC-V und ermöglichen so eine nahtlose Integration.
- **Anwendungen**:
 - Einfach: Video-Türklingel (P4 für JPEG/H.264, C5 für WLAN-Upload).
 - Mittel: Smart-Factory-Monitor (P4 für VAD/Sprachsteuerung, C5 für Dualband-Netzwerk).
 - Anspruchsvoll (Industrie 4.0): Robotersteuerung in Automatisierungslinien (P4 für MCPWM-Motorsteuerung und KI-Navigation, C5 für CAN FD + Wi-Fi 6 zur Koordination mehrerer Roboter; unterstützt Echtzeit-Datenaggregation zur Optimierung der Lieferkette).

#### 3. ESP32-S3 + ESP32-C6
- **Beschreibung**: S3 (Dual-Xtensa mit KI-/Vektorerweiterungen, LCD/Kamera, USB-OTG, BT 5 LE) + C6 (Wi-Fi 6, BT 5.3, 802.15.4, LP-Kern).
- **Warum das sinnvoll ist**: S3 bietet KI/Multimedia, C6 erweitert die Funktionen um Wi-Fi 6/802.15.4 für bessere IoT-Interoperabilität (z. B. Matter); ULP-Coprozessoren von S3 + LP-Kern von C6 für hybride Energiesparmodi.
- **Anwendungen**:
 - Einfach: KI-Sprachassistent (S3 für Spracherkennung, C6 für Mesh-Konnektivität).
 - Mittel: Sicherheitskameranetzwerk (S3 für Bildverarbeitung, C6 für Wi-Fi 6-Streaming).
 - Anspruchsvoll (Industrie 4.0): Qualitätskontrolle in der Produktion (S3 für KI-basierte Fehlererkennung per Kamera, C6 für 802.15.4-Mesh zu Sensoren; ermöglicht adaptive Fertigung mit Echtzeit-Feedback).

#### 4. ESP32-S3 + ESP32-P4-
- **Beschreibung**: S3 (KI/Multimedia, WLAN/BT LE) + P4 (leistungsstarker RISC-V, MIPI CSI/DSI, Ethernet, VAD/Touch).
- **Warum es sinnvoll ist**: S3 für Wireless/KI am Netzwerkrand, P4 für fortgeschrittene Verarbeitung/Multimedia (z. B. H.264-Encoder); Kombination für skalierbare Systeme mit kabelgebundener/kabelloser Hybridlösung.
- **Anwendungen**:
 - Einfach: Interaktives Display (S3 für WLAN, P4 für Touch/LCD).
 - Mittel: VR-Schulungstool (S3 für BT-LE-Sensoren, P4 für ISP/Bildverarbeitung).
 - Anspruchsvoll (Industrie 4.0): Augmented Reality für die Instandhaltung (S3 für WLAN-Datenabruf, P4 für MIPI-Kamera und H.264-Streaming; unterstützt kollaborative AR in Fabriken für Fernunterstützung).

#### 5. ESP32-C6 + ESP32-H2-
- **Beschreibung**: C6 (Wi-Fi 6, BT 5.3, 802.15.4, LP-Kern) + H2 (BT LE 5.3 mit großer Reichweite, 802.15.4, extrem geringer Stromverbrauch).
- **Warum es sinnvoll ist**: Beide sind Multiprotokoll-fähig (802.15.4/BT), H2 für Endknoten mit extrem geringem Stromverbrauch (7 μA im Tiefschlafmodus), C6 als Gateway mit WLAN; ideale Mesh-Erweiterung.
- **Anwendungen**:
 - Einfach: Smart-Lighting-Mesh (H2 für Lampen, C6 als Hub).
 - Mittel: Umgebungssensornetzwerk (H2 für Batteriesensoren, C6 für WLAN-Aggregation).
 - Anspruchsvoll (Industrie 4.0): Bestandsverfolgung in Lagerhäusern (H2 für Tags mit großer Reichweite, C6 als WLAN-6-Gateway; ermöglicht Echtzeit-Lokalisierung und Bestandsverwaltung mit prädiktiver Analyse).

#### 6. ESP32-C3 + ESP32-P4
- **Beschreibung**: C3 (kostengünstiges WLAN/BT LE, TWAI, RISC-V) + P4 (leistungsstarke MCU, Ethernet, USB HS, großer Speicher).
- **Warum es sinnvoll ist**: C3 als kostengünstiger Sensor/Endgerät, P4 als zentrale Steuerung; RISC-V-Kompatibilität für die Wiederverwendung von Software.
- **Anwendungen**:
 - Einfach: Kostengünstiger Sensorcluster (C3 für die Datenerfassung, P4 für die Verarbeitung).
 - Mittel: Sicheres Türschloss (C3 für BT LE, P4 für Verschlüsselung/USB).
 - Anspruchsvoll (Industrie 4.0): IIoT-Gateway für Maschinen (C3 für CAN-Bus-Sensoren, P4 für Ethernet + KI-basierte Anomalieerkennung; unterstützt sichere Datenaggregation in cyber-physischen Systemen).

#### 7. ESP32-C2 + ESP32-C6
- **Beschreibung**: C2 (extrem kostengünstig, minimalistisch, Wi-Fi/BT LE) + C6 (Multiprotokoll, LP-Kern).
- **Warum es sinnvoll ist**: C2 für Endknoten in großer Stückzahl (z. B. Tags), C6 als Hub mit erweiterter Konnektivität; beide RISC-V-basiert und stromsparend.
- **Anwendungen**:
 - Einfach: Beacon-Netzwerk (C2 für Tags, C6 als Gateway).
 - Mittel: Batteriesensor-Array (C2 für einfache Sensoren, C6 für Mesh).
 - Anspruchsvoll (Industrie 4.0): Zustandsüberwachung in Lieferketten (C2 für kostengünstige Vibrationssensoren auf Paletten, C6 für Wi-Fi 6/802.15.4-Übertragung; ermöglicht skalierbare prädiktive Logistik).

#### 8. ESP32-S2 + ESP32-H2
- **Beschreibung**: S2 (Wi-Fi, USB-OTG, LCD/Kamera, Touch) + H2 (BT LE/802.15.4, extrem geringer Stromverbrauch).
- **Warum es sinnvoll ist**: S2 für WLAN/Multimedia, H2 für Low-Power-Mesh; ergänzt die fehlenden Funktionen BT/802.15.4 des S2.
- **Anwendungen**:
 - Einfach: Touchpanel mit Mesh (S2 für Display, H2 für BT-Sensoren).
 - Mittel: Tragbarer Scanner (S2 für Kamera/USB, H2 für Bluetooth mit großer Reichweite).
 - Anspruchsvoll (Industrie 4.0): Handheld-Prüfgerät (S2 für LCD/Touchscreen/Kamera, H2 für 802.15.4-Konnektivität zu Maschinen; unterstützt mobile Qualitätskontrolle mit Echtzeit-Datensynchronisation).

#### 9. ESP32 (Classic) + ESP32-C5
- **Beschreibung**: Classic (Dual-Xtensa, Ethernet, BT Classic/LE, CAN) + C5 (Dual-Band-Wi-Fi 6, 802.15.4, LP-Core).
- **Warum das sinnvoll ist**: Classic für Abwärtskompatibilität (BT Classic/Ethernet), C5 für moderne Funkverbindungen; Hybrid für Upgrades.
- **Anwendungen**:
 - Einfach: Hybridnetzwerk (Classic für Ethernet, C5 für Wi-Fi 6).
 - Mittel: Fahrzeugortung (Classic für CAN, C5 für BT/802.15.4).
 - Anspruchsvoll (Industrie 4.0): Automotive IIoT (Classic für den CAN-Bus in Fahrzeugen, C5 für Dualband-WLAN zur Cloud; ermöglicht Flottenmanagement mit vorausschauender Wartung).

#### 10. ESP32-C5 + ESP32-H2 + ESP32-P4 (Trio)
- **Beschreibung**: C5 (Dualband-WLAN 6/802.15.4), H2 (Low-Power-Mesh), P4 (Hochleistungsverarbeitung).
- **Warum es sinnvoll ist**: Komplettsystem: H2 für Endknoten, C5 für drahtlose Gateway-Verbindung, P4 für zentrale Rechenleistung; skalierbar für große Netzwerke.
- **Anwendungen**:
 - Einfach: Fortgeschrittenes Smart Home (H2 für Sensoren, C5 für WLAN, P4 für Hub).
 - Mittel: Mesh-Überwachung (H2 für Tags, C5 für Streaming, P4 für KI).
 - Anspruchsvoll (Industrie 4.0): Smart-Factory-Ökosystem (H2 für batteriebetriebene Mitarbeiter-Tags, C5 für Wi-Fi-6-Netzwerk, P4 für Edge-KI und Ethernet-Integration; ermöglicht die autonome Optimierung von Produktionslinien durch Mensch-Maschine-Zusammenarbeit).

#### 11. ESP32-P4 + ESP32-E22-
- **Beschreibung**: P4 (Hochleistungs-MCU mit KI, Ethernet, USB HS/FS) + E22 (Tri-Band-Wi-Fi 6E + Dual-Mode-Bluetooth RCP).
- **Warum es sinnvoll ist**: P4 bietet leistungsstarke Rechenleistung und kabelgebundene Konnektivität, E22 ergänzt dies um modernste drahtlose Technologien (Wi-Fi 6E, BT Classic/BLE 5.4) über PCIe oder SDIO. Ideal für bandbreitenintensive Anwendungen.
- **Anwendungen**:
 - Einfach: High-End-Smart-Home-Hub mit 4K-Streaming.
 - Mittel: AR/VR-Headset mit Edge-KI.
 - Anspruchsvoll (Industrie 4.0): Echtzeit-Videoanalyse in Fabriken (P4 für KI-Verarbeitung, E22 für drahtlosen Video-Uplink mit geringer Latenz).

#### 12. ESP32-C6 + ESP32-H21
- **Beschreibung**: C6 (Wi-Fi 6, BT 5.3, 802.15.4, LP-Kern) + H21 (BLE 5 mit extrem geringem Stromverbrauch + 802.15.4 mit 5 µA im Tiefschlafmodus, 20 dBm Sendeleistung).
- **Warum es sinnvoll ist**: H21 erweitert das Mesh-Netzwerk mit noch geringerem Stromverbrauch (5 µA im Tiefschlafmodus) und höherer Sendeleistung (20 dBm) im Vergleich zu H2. C6 fungiert als Gateway mit Wi-Fi 6.
- **Anwendungen**:
 - Einfach: Smart-Lighting-Mesh mit extrem geringem Stromverbrauch.
 - Mittel: Asset-Tracking mit großer Reichweite mit 20-dBm-Tags.
 - Anspruchsvoll (Industrie 4.0): Batteriebetriebene Sensornetzwerke in rauen Industrieumgebungen mit erweiterter Reichweite.

Diese Kombinationen erweitern die individuellen Stärken zu robusten Systemen, insbesondere in der Industrie 4.0, wo Sicherheit, Skalierbarkeit und Echtzeitverarbeitung entscheidend sind. Zur Implementierung: Anschluss über SPI/UART/I2C/PCIe/SDIO; ESP-IDF unterstützt Konfigurationen mit mehreren Geräten.

## Referenzen & Weiterführende Literatur

- Datenblatt zur ESP32-Serie (Version 4.3, abgerufen im Juli 2026)
- Datenblatt zur ESP32-S2-Serie (Version 1.4, abgerufen im Juli 2026)
- Datenblatt zur ESP32-S3-Serie (Version 1.3, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑C3-Serie (Version 1.2, abgerufen im Juli 2026)
- Technisches Referenzhandbuch zur ESP32‑C2-Serie (Version 1.0, abgerufen im Juli 2026; Hinweis: kein vollständiges Datenblatt verfügbar, basierend auf Moduldaten wie denen des ESP8684)
- Datenblatt zur ESP32‑C5-Serie (Version 1.2, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑C6-Serie (Version 1.5, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑C61-Serie (Version 1.0, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑H2-Serie (Version 1.5, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑H4-Serie (Version 0.6, abgerufen im Juli 2026)
- Datenblatt zur ESP32‑P4-Serie (Version 1.0, abgerufen im Juli 2026)
- **Datenblatt zur ESP32‑E22-Serie** (Version 1.0, abgerufen im Juli 2026)
- **Datenblatt zur ESP32‑H21-Serie** (Version 1.0, abgerufen im Juli 2026)
- **Datenblatt zur ESP32‑S31-Serie** (Version 0.2, abgerufen im Juli 2026)
- Espressif-Produktwähler (abgerufen im Juli 2026)
- ESP32-Modul-Referenz (WROOM/WROVER) (Version 2.0, abgerufen im Juli 2026)
- ESP‑IDF: Für die Entwicklung mit allen Modellen. (ESP‑IDF v6.0.1 stabil für C5, E22, H21, S31-Unterstützung)

Beitrag: Pull-Anfragen sind willkommen! Mit „Star“ markieren und forken, um über Aktualisierungen auf dem Laufenden zu bleiben.

## Lizenz

[CC-BY-4.0](LICENSE)
