# ESP32Features
Übersichtstabelle mit den aktuellen ESP32-Modellen basierend auf den offiziellen Espressif-Datasheets (Stand September 2025)


## Tabelle

| Modell     | Architektur (Kerne, Clock min/max, LP/ULP) | Embedded SRAM | Embedded Flash/PSRAM-Optionen (Kombos) | Max PSRAM (embedded/external, Future) | Max Flash (embedded/external, Future) | Radio (Varianten)                          | Interfaces (Auswahl: Anzahl, Typ) |
|------------|--------------------------------------------|---------------|----------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|-----------------------------------|
| ESP32     | Dual Xtensa LX6, 80-240 MHz, keine dedizierte LP; ULP-Co-Proc (FSM-basiert, für Deep-Sleep) | 520 KB       | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombos: z. B. U4WDH (2 MB Flash + 0 PSRAM), D0WDR2-V3 (4 MB Flash + 2 MB PSRAM) | 2 MB embedded / 8 MB external        | 4 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 4.2 (BR/EDR + LE) | 34 GPIOs; 4 SPI; 2 I2S; 2 I2C; 3 UART; Ethernet MAC; TWAI (CAN); ADC (18 ch., 12-bit); Touch (10); DAC (2, 8-bit) |
| ESP32-S2  | Mono Xtensa LX7, 40-240 MHz, keine dedizierte LP; ULP-Co-Procs (RISC-V + FSM, nicht simultan) | 320 KB + 16 KB RTC | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Kombos: z. B. FH2 (2 MB Flash + 0 PSRAM), FN4R2 (4 MB Flash + 2 MB PSRAM), R2 (0 Flash + 2 MB PSRAM) | 2 MB embedded / 1 GB external (typ. 64 MB) | 4 MB embedded / 1 GB external (typ. 128 MB) | Wi-Fi 2.4 GHz (802.11 b/g/n)              | 43 GPIOs; 4 SPI; 1 I2S; 2 I2C; 2 UART; USB OTG (FS); LCD (2: SPI/I2S); Camera (DVP 8/16-bit); ADC (20 ch., 12-bit); DAC (2, 8-bit); Touch (14); RMT (4 ch.); LED PWM (8 ch.) |
| ESP32-S3  | Dual Xtensa LX7, 40-240 MHz, keine dedizierte LP; ULP-Co-Procs (RISC-V + FSM, nicht simultan) | 512 KB + 16 KB RTC | Flash: 0/4/8/16 MB; PSRAM: 0/2/4/8/16 MB; Kombos: z. B. FN8 (8 MB Flash + 0 PSRAM), R2 (0 + 2 MB), R8 (0 + 8 MB), R16V (0 + 16 MB), FH4R2 (4 MB Flash + 2 MB PSRAM), FN4R8 (4 MB Flash + 8 MB PSRAM) | 16 MB embedded / 32 MB external (Future: 64 MB) | 16 MB embedded / 32 MB external (Future: 64 MB) | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE)   | 45 GPIOs; 4 SPI (2 mem., 2 gen.); 2 I2S; 2 I2C; 3 UART; USB OTG (FS); SD/MMC (2 slots); TWAI; LCD/Camera; ADC (20 ch., 12-bit); Touch (14); MCPWM; RMT; PCNT; LED PWM |
| ESP32-C3  | Mono RISC-V, 40-160 MHz, keine dedizierte LP/ULP | 400 KB (16 KB Cache) | Flash: 0/4 MB; PSRAM: 0 MB; Kombos: z. B. C3 (0 Flash + 0 PSRAM), FH4/C3FH4X (4 MB Flash + 0 PSRAM) – PSRAM external only | 0 MB embedded / 8 MB external (Future: 16 MB) | 4 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE)   | 22/16 GPIOs; 3 SPI; 1 I2S; 1 I2C; 2 UART; USB Serial/JTAG; TWAI; LED PWM (6 ch.); RMT (4 ch.); ADC (6 ch., 12-bit); Temp sensor |
| ESP32-C2  | Mono RISC-V, 20-120 MHz, keine dedizierte LP/ULP | 272 KB (16 KB Cache) | Flash: 0 MB (external only); PSRAM: 0 MB; Kombos: Keine embedded (z. B. C2FH4: 0 + 0, aber Modules wie ESP8684 integrieren 4 MB Flash external-style) | 0 MB embedded / 8 MB external (Future: 16 MB) | 0 MB embedded / 16 MB external       | Wi-Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE) | 14 GPIOs; 2 SPI; 1 I2S; 1 I2C; 2 UART; LED PWM; GDMA; SAR ADC (6 ch.); Temp sensor; USB Serial |
| ESP32-C5  | Dual RISC-V (HP/LP), HP 40-240 MHz / LP 20-48 MHz, dedizierte LP ja; kein separater ULP | 384 KB HP + 16 KB LP + 320 KB ROM | Flash: 0/4 MB; PSRAM: 0/8 MB; Kombos: z. B. C5HF4 (4 MB Flash + 0 PSRAM), C5HR8 (0 Flash + 8 MB PSRAM) | 8 MB embedded / 32 MB external (Future: 64 MB) | 4 MB embedded / 32 MB external (Future: 64 MB) | Wi-Fi dual-band 6 (2.4/5 GHz, 802.11 a/b/g/n/ac/ax), BT LE 5 (Core 6.0), 802.15.4 (Zigbee 3.0 / Thread 1.4) | 29 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 CAN FD; SDIO; LED PWM (6 ch.); MCPWM (6 ch.); RMT (4 ch.); PARLIO; PCNT (4); ADC (6 ch., 12-bit); Temp sensor; Analog Comparator (2 pads) |
| ESP32-C6  | Dual RISC-V (HP/LP), HP 40-160 MHz / LP 20 MHz, dedizierte LP ja; kein separater ULP | 512 KB HP + 16 KB LP | Flash: 0/4/8 MB; PSRAM: 0 MB; Kombos: z. B. C6 (0 + 0), C6FH4 (4 MB Flash + 0), C6FH8 (8 MB Flash + 0) – PSRAM external only | 0 MB embedded / 16 MB external (Future: 32 MB) | 8 MB embedded / 16 MB external (Future: 32 MB) | Wi-Fi 6 2.4 GHz (802.11 ax/b/g/n), BT 5.3 (LE + Mesh), 802.15.4 (Zigbee 3.0 / Thread 1.3) | 30/22 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 TWAI; SDIO; LED PWM (6 ch.); MCPWM (3); RMT (4 ch.); PARLIO; PCNT (4); ADC (7 ch., 12-bit); Temp sensor; GDMA; ETM |
| ESP32-P4  | Dual HP + Mono LP RISC-V, HP 40-360 MHz / LP 40 MHz, dedizierte LP ja; kein separater ULP | 768 KB HP L2MEM + 32 KB LP + 8 KB SPM | Flash: 0 MB; PSRAM: 0/16/32 MB; Kombos: z. B. P4NRW16 (0 Flash + 16 MB PSRAM), P4NRW32 (0 + 32 MB PSRAM) | 32 MB embedded / 64 MB external (Future: 128 MB) | 0 MB embedded / 64 MB external (Future: 128 MB) | Keine integrierten Radios (MCU-fokussiert, external möglich) | 55 GPIOs (16 LP); 4 SPI (+1 LP); 3 I2S (+1 LP); 3 I2C (+1 Analog +1 I3C); 6 UART (5 HP +1 LP); USB HS/FS OTG + Serial/JTAG; Ethernet (10/100 RMII); 3 TWAI; SD/MMC; LED PWM (8 ch.); MCPWM (2); RMT (8 ch.); PARLIO; Touch (14); 2 ADC; VAD; Image: JPEG Codec, ISP, H.264 Encoder, MIPI CSI/DSI (2-lane), LCD/Camera

## Referenzen

- ESP32 Series Datasheet (Version 4.3, abgerufen September 2025)
- ESP32-S2 Series Datasheet (Version 1.4, abgerufen September 2025)
- ESP32-S3 Series Datasheet (Version 1.3, abgerufen September 2025)
- ESP32-C3 Series Datasheet (Version 1.2, abgerufen September 2025)
- ESP32-C2 Technical Reference Manual (Version 1.0, abgerufen September 2025, Hinweis: Kein vollständiges Datasheet verfügbar, basierend auf Moduldaten wie ESP8684)
- ESP32-C5 Series Datasheet (Version 1.0, abgerufen September 2025)
- ESP32-C6 Series Datasheet (Version 1.1, abgerufen September 2025)
- ESP32-P4 Series Datasheet (Version 0.7, abgerufen September 2025)
- Espressif Product Selector (abgerufen September 2025)


ESP32 Module Reference (WROOM/WROVER) (Version 2.0, abgerufen September 2025)
