# ESP32Features

[![CRA Status](https://img.shields.io/badge/CRA-Exempt%20(pure%20OSS)-informational)](./CRA-EXEMPTION.md)
[![License](https://img.shields.io/badge/License-CC--BY--4.0-blue?style=flat-square)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-2026.07-brightgreen?style=flat-square)](./README.md)

Welcome to ESP32Features, a guide and repository for the current ESP32 SoC family from Espressif Systems. This README provides an overview table of the relevant ESP32 models, based on the official Espressif datasheets and documentation (as of July 2026). The ESP32 series includes a wide range of microcontrollers optimized for IoT applications, edge computing, low-power sensors, and industrial systems—from legacy all-rounders like the classic ESP32 to modern RISC‑V‑based chips with Wi‑Fi 6, Bluetooth 5.4, and multi-protocol support (e.g., Zigbee/Thread for Matter-compatible smart homes).

## Why ESP32Features?

- **Complete coverage:** All models (ESP32, S2, S3, C3, C2, C5, C6, C61, H2, H4, P4, **E22, H21, S31**) with a focus on architecture, memory (SRAM, Flash, PSRAM), radios, interfaces, and low-power features.
- **Practical analysis:** Supplemented by deep sleep details, pros and cons, application evaluations, and combination suggestions for hybrid systems (e.g., P4 + C6 for Industry 4.0).
- **Up‑to‑date & source‑based:** Based on Espressif's Product Selector and datasheets (e.g., ESP32‑C5 in mass production since 2025, ESP32‑C6 with PSA Level 2 security certification, ESP32‑E22 Wi‑Fi 6E certified since June 2026).
- **For developers:** Integrated with ESP‑IDF, Arduino, and tools for rapid prototyping – ideal for smart devices, AI edge, and IIoT.

The table below summarizes the core features. For detailed analyses, see the subsections: [Espressif SoC Product Portfolio](#espressif-soc-product-portfolio), [Deep Sleep](#deep-sleep), [Advantages and Disadvantages](#thorough-evaluation-of-each-model), [Applications](#list-of-typical-applications), [Combinations](#useful-combinations-of-esp32-models), [Cryptographic Security & Post‑Quantum Readiness](#cryptographic-security--post‑quantum-readiness), and [References](#references--further-reading)

### Disclaimer 2026

The following models have been announced by Espressif since September 2025 and are **already included in the table below**:
- **ESP32‑E22** – Tri‑Band Wi‑Fi 6E + Dual‑Mode Bluetooth 5.4 Connectivity Co‑Processor (RCP) – available since Jan 2026, Wi‑Fi 6E‑certified since Jun 2026
- **ESP32‑H21** – Ultra‑Low‑Power BLE 5 + 802.15.4 SoC – available with preview support in ESP‑IDF v6.0 since March 2026
- **ESP32‑S31** – Dual‑Core RISC‑V SoC with Wi‑Fi 6, BT 5.4, 802.15.4, Gigabit Ethernet, and advanced HMI features – announced in March 2026, release pending

**Additional future models** (beyond those listed above) have **not** been announced by Espressif at this time. This list will be updated as new products are announced.

## Overview table of ESP32 models

| Model | Architecture (cores, Clock min/max, LP/ULP) | Embedded SRAM | Embedded Flash/PSRAM options (combos) | Max PSRAM (embedded/external, Future) | Max Flash (embedded/external, Future) | Radio (variants) | Interfaces (selection: number, type) |
|------------|--------------------------------------------|---------------|----------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|-----------------------------------|
| ESP32 | Dual Xtensa LX6, 80‑240 MHz, no dedicated LP; ULP co‑proc (FSM‑based, for deep sleep) | 520 KB | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Combos: e.g., U4WDH (2 MB Flash + 0 PSRAM), D0WDR2‑V3 (4 MB flash + 2 MB PSRAM) | 2 MB embedded / 8 MB external | 4 MB embedded / 16 MB external | Wi‑Fi 2.4 GHz (802.11 b/g/n), BT 4.2 (BR/EDR + LE) | 34 GPIOs; 4 SPI; 2 I2S; 2 I2C; 3 UART; Ethernet MAC; TWAI (CAN); ADC (18 ch., 12‑bit); Touch (10); DAC (2, 8‑bit) |
| ESP32‑S2 | Mono Xtensa LX7, 40‑240 MHz, no dedicated LP; ULP co‑procs (RISC‑V + FSM, not simultaneous) | 320 KB + 16 KB RTC | Flash: 0/2/4 MB; PSRAM: 0/2 MB; Combos: e.g. FH2 (2 MB flash + 0 PSRAM), FN4R2 (4 MB flash + 2 MB PSRAM), R2 (0 flash + 2 MB PSRAM) | 2 MB embedded / 1 GB external (typ. 64 MB) | 4 MB embedded / 1 GB external (typ. 128 MB) | Wi‑Fi 2.4 GHz (802.11 b/g/n) | 43 GPIOs; 4 SPI; 1 I2S; 2 I2C; 2 UART; USB OTG (FS); LCD (2: SPI/I2S); Camera (DVP 8/16‑bit); ADC (20 ch., 12‑bit); DAC (2, 8‑bit); Touch (14); RMT (4 ch.); LED PWM (8 ch.) |
| ESP32‑S3 | Dual Xtensa LX7, 40‑240 MHz, no dedicated LP; ULP co‑pros (RISC‑V + FSM, not simultaneous) | 512 KB + 16 KB RTC | Flash: 0/4/8/16 MB; PSRAM: 0/2/4/8/16 MB; Combos: e.g., FN8 (8 MB Flash + 0 PSRAM) , R2 (0 + 2 MB), R8 (0 + 8 MB), R16V (0 + 16 MB), FH4R2 (4 MB Flash + 2 MB PSRAM), FN4R8 (4 MB Flash + 8 MB PSRAM) | 16 MB embedded / 32 MB external (Future: 64 MB) | 16 MB embedded / 32 MB external (Future: 64 MB) | Wi‑Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE) | 45 GPIOs; 4 SPI (2 mem., 2 gen.); 2 I2S; 2 I2C; 3 UART; USB OTG (FS); SD/MMC (2 slots); TWAI; LCD/Camera; ADC (20 ch., 12‑bit); Touch (14); MCPWM; RMT; PCNT; LED PWM |
| ESP32‑C3 | Mono RISC‑V, 40‑160 MHz, no dedicated LP/ULP | 400 KB (16 KB cache) | Flash: 0/4 MB; PSRAM: 0 MB; Combos: e.g. C3 (0 Flash + 0 PSRAM), FH4/C3FH4X (4 MB Flash + 0 PSRAM) – PSRAM external only | 0 MB embedded / 8 MB external (Future: 16 MB) | 4 MB embedded / 16 MB external | Wi‑Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE) | 22/16 GPIOs; 3 SPI; 1 I2S; 1 I2C; 2 UART; USB Serial/JTAG; TWAI; LED PWM (6 ch.); RMT (4 ch.); ADC (6 ch., 12‑bit); Temp sensor |
| ESP32‑C2 | Mono RISC‑V, 20‑120 MHz, no dedicated LP/ULP | 272 KB (16 KB cache) | Flash: 0 MB (external only); PSRAM: 0 MB; Combos: None embedded (e.g., C2FH4: 0 + 0, but modules such as ESP8684 integrate 4 MB Flash external‑style) | 0 MB embedded / 8 MB external (Future: 16 MB) | 0 MB embedded / 16 MB external | Wi‑Fi 2.4 GHz (802.11 b/g/n), BT 5 (LE) | 14 GPIOs; 2 SPI; 1 I2S; 1 I2C; 2 UART; LED PWM; GDMA; SAR ADC (6 ch.); Temp sensor; USB Serial |
| ESP32‑C5 | Dual RISC‑V (HP/LP), HP 40‑240 MHz / LP 20‑48 MHz, dedicated LP yes; no separate ULP | 384 KB HP + 16 KB LP + 320 KB ROM | Flash: 0/4 MB; PSRAM: 0/8 MB; Combos: e.g. B. C5HF4 (4 MB Flash + 0 PSRAM), C5HR8 (0 Flash + 8 MB PSRAM) | 8 MB embedded / 32 MB external (future: 64 MB) | 4 MB embedded / 32 MB external (future: 64 MB) | Wi‑Fi dual‑band 6 (2.4/5 GHz, 802.11 a/b/g/n/ac/ax), BT LE 5 (Core 6.0), 802.15.4 (Zigbee 3.0 / Thread 1.4) | 29 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 CAN FD; SDIO; LED PWM (6 ch.); MCPWM (6 ch.); RMT (4 ch.); PARLIO; PCNT (4); ADC (6 ch., 12‑bit); Temp sensor; Analog Comparator (2 pads) |
| ESP32‑C6 | Dual RISC‑V (HP/LP), HP 40‑160 MHz / LP 20 MHz, dedicated LP yes; no separate ULP | 512 KB HP + 16 KB LP | Flash: 0/4/8 MB; PSRAM: 0 MB; Combos: e.g. C6 (0 + 0), C6FH4 (4 MB flash + 0), C6FH8 (8 MB flash + 0) – PSRAM external only | 0 MB embedded / 16 MB external (Future: 32 MB) | 8 MB embedded / 16 MB external (Future: 32 MB) | Wi‑Fi 6 2.4 GHz (802.11 ax/b/g/n), BT 5.3 (LE + Mesh), 802.15.4 (Zigbee 3.0 / Thread 1.3) | 30/22 GPIOs; 3 SPI; 1 I2S; 2 I2C (+1 LP); 3 UART (+1 LP); USB Serial/JTAG; 2 TWAI; SDIO; LED PWM (6 ch.); MCPWM (3); RMT (4 ch.); PARLIO; PCNT (4); ADC (7 ch., 12‑bit); Temp sensor; GDMA; ETM |
| ESP32‑C61 | Mono RISC‑V, 40‑160 MHz, LP/ULP ja (Power Modes) | 320 KB | Flash: 0/4 MB; PSRAM: 0/2/8 MB; Kombos: z. B. C61HF4 (4 MB Flash + 0 PSRAM), C61HR2 (0 Flash + 2 MB PSRAM), C61HR8 (0 Flash + 8 MB PSRAM) – Quad SPI | 8 MB embedded / 32 MB external (Future) | 4 MB embedded / 32 MB external (Future) | Wi‑Fi 6 2.4 GHz (802.11 ax), BT 5 (LE) | 30 GPIOs; 2 SPI; 1 I2S; 1 I2C; 3 UART; USB Serial/JTAG; SDIO 2.0 Slave; LED PWM; RMT; TWAI; ADC (1 ch., 12‑bit); Temp sensor |
| ESP32‑H2 | Mono RISC‑V, 32 MHz (min typ. low‑power) / 96 MHz, no dedicated LP/ULP; LP components for deep sleep | 320 KB HP + 4 KB LP | Flash: 0/2/4 MB; PSRAM: 0 MB; Combos: e.g. H2FH2S (2 MB Flash + 0 PSRAM), H2FH4S (4 MB Flash + 0 PSRAM) – PSRAM external only | 0 MB embedded / 16 MB external (Future: 32 MB) | 4 MB embedded / 16 MB external (Future: 32 MB) | BT LE 5.3 (1/2 Mbps, Coded PHY, Long Range, Advertising Extensions), 802.15.4 (250 Kbps OQPSK, Thread/Zigbee 3.0/Matter) | 19 GPIOs; 2 SPI (Flash + gen.); 2 UART; 2 I2C; 1 I2S; RMT (2 tx/2 rx ch.); LED PWM (6 ch.); USB Serial/JTAG; TWAI (CAN); GDMA (3 tx/3 rx); PCNT; MCPWM; ADC (5 ch., 12‑bit); Temp sensor; Timers (2 gen. 54‑bit, 52‑bit sys., 3 WDT) |
| ESP32‑H4 | Dual RISC‑V, 96 MHz max, dedizierte LP ja (selective peripherals) | 320 KB | Flash: 0 MB; PSRAM: 0/4 MB; Kombos: z. B. H4 (0 Flash + 0 PSRAM), H4R4 (0 Flash + 4 MB PSRAM) – external Flash support | 0 MB embedded / 4 MB external (Future: 16 MB) | 0 MB embedded / 16 MB external (Future) | BT LE 5.4 (LE), 802.15.4 (Zigbee/Thread/Matter) | 35 GPIOs; I2C; I2S; SPI; UART; LED PWM; ADC; Timers; DMA; TWAI; USB OTG; MCPWM; Touch (14); Event Task Matrix |
| ESP32‑P4 | Dual HP + Mono LP RISC‑V, HP 40‑360 MHz / LP 40 MHz, dedicated LP yes; no separate ULP | 768 KB HP L2MEM + 32 KB LP + 8 KB SPM | Flash: 0 MB; PSRAM: 0/16/32 MB; Combos: e.g. P4NRW16 (0 Flash + 16 MB PSRAM), P4NRW32 (0 + 32 MB PSRAM) | 32 MB embedded / 64 MB external (Future: 128 MB) | 0 MB embedded / 64 MB external (Future: 128 MB) | No integrated radios (MCU‑focused, external possible) | 55 GPIOs (16 LP); 4 SPI (+1 LP); 3 I2S (+1 LP); 3 I2C (+1 Analog +1 I3C); 6 UART (5 HP +1 LP); USB HS/FS OTG + Serial/JTAG; Ethernet (10/100 RMII); 3 TWAI; SD/MMC; LED PWM (8 ch.) ; MCPWM (2); RMT (8 ch.); PARLIO; Touch (14); 2 ADC; VAD; Image: JPEG codec, ISP, H.264 encoder, MIPI CSI/DSI (2‑lane), LCD/Camera |
| **ESP32‑E22** | Dual RISC‑V HP Core @ **500 MHz**, RCP‑Architektur (Radio Co‑Processor) | **1 MB** | Keine embedded (RCP‑Design) | 0 MB embedded / extern über Host‑System | 0 MB embedded / extern über Host‑System | **Tri‑Band Wi‑Fi 6E** (2.4/5/6 GHz), 160 MHz Kanalbandbreite, 2×2 MU‑MIMO, Beamforming, 1024‑QAM, Datenrate bis 2,4 Gbps; **Bluetooth Classic (BR/EDR) + BLE 5.4**; Wi‑Fi CERTIFIED 6E™ (Jun 2026) | **30 GPIOs**; **PCIe 2.1**; **SDIO 3.0**; **USB 2.0**; Linux‑Treiber Open Source (Kernel 5.4+) |
| **ESP32‑H21** | Mono RISC‑V, bis **96 MHz** | 320 KB SRAM + 128 KB ROM | Keine embedded (extern über SPI‑Flash) | 0 MB embedded / extern (über SPI‑Flash) | 0 MB embedded / extern (über SPI‑Flash) | **BT LE 5.0** (BLE 5.3‑zertifiziert) + **802.15.4** (Thread/Zigbee/Matter); **20 dBm Sendeleistung**; **On‑Chip DC‑DC‑Wandler** | **19 GPIOs**; UART, SPI, I²C, I²S, PWM, ADC, Timers, DMA; USB Serial/JTAG |
| **ESP32‑S31** | Dual RISC‑V, **320 MHz**, **128‑Bit SIMD‑Datenpfad** | **512 KB SRAM** | S31 (0 + 0), externe Flash/PSRAM über Octal SPI | extern: bis 64 MB (250 MHz 8‑Bit DDR PSRAM) | extern: bis 64 MB (Octal SPI) | **Wi‑Fi 6** (2,4 GHz, 802.11ax); **BT 5.4** (LE + Classic BR/EDR); **IEEE 802.15.4** (Thread/Zigbee); **1000 Mbps Ethernet MAC** | **60 GPIOs**; DVP‑Camera (8‑16‑Bit); LCD (8‑24‑Bit parallel); 14× Touch; JPEG‑Codec; 2D‑Graphics‑Acceleration (PPA); 2D‑DMA; 2× I2S; USB OTG; SD/MMC; TWAI; SPI; I2C; UART; **Trusted Execution Environment (TEE)** mit APM; **RAM‑based PUF** |

### Notes on the table:

- **Architecture:** Takes into account cores (HP/LP), clock ranges, and low‑power features (ULP/LP).
- **Memory:** Embedded options with variant combos; max values incl. future support (e.g., up to 128 MB for P4).
- **Radios:** All variants, including multi‑protocol (e.g., Wi‑Fi 6 for C5/C6, 802.15.4 for C5/C6/H2 for Matter, Tri‑Band for E22).
- **Interfaces:** Important peripherals with quantities; focused on GPIOs, wireless relevance, and special features (e.g., MIPI for P4, PCIe for E22).
- **Sources:** Directly from Espressif datasheets; no new models beyond the list (as of 2025, e.g., C5 in mass production; C61/H4 new to the portfolio; E22/H21/S31 added in 2026).

### Espressif SoC Product Portfolio

![Espressif SoC Product Portfolio](res/4de262290804bb22f2a6272d7fc53db0.jpg "Espressif SoC Product Portfolio")

> **Note:** The Espressif product portfolio image above (as of September 2025) **does not** include the **ESP32‑E22**, **ESP32‑H21**, and **ESP32‑S31** variants, which have been announced since then. These were added to the table at a later date.

## Deep sleep

[... *Der Deep‑Sleep‑Abschnitt bleibt unverändert – er wurde bereits in früheren Updates vollständig überarbeitet.* ...]

## Thorough evaluation of each model

[... *Die Bewertungen der Modelle bleiben unverändert – sie wurden in früheren Updates bereits vollständig integriert.* ...]

## List of typical applications

[... *Die Liste der 50 Anwendungen und die Bewertungstabelle bleiben unverändert – sie wurden in früheren Updates bereits vollständig integriert.* ...]

## Useful combinations of ESP32 models

[... *Die Kombinationsvorschläge bleiben unverändert – sie wurden in früheren Updates bereits vollständig integriert.* ...]

---

## Cryptographic Security & Post‑Quantum Readiness

This chapter provides a comprehensive analysis of the cryptographic capabilities of the ESP32 family, with a special focus on **quantum‑safe cryptography** and **crypto‑agility** – the ability to replace or upgrade cryptographic algorithms without changing the underlying infrastructure.

### 1. The Quantum Threat – Why RSA and ECC Are Obsolete

The **Q‑Day** (or **Y2Q**) is the point at which a quantum computer becomes powerful enough to break today’s asymmetric encryption (RSA, ECC) in a practical time. This threat is real and imminent:

> **Google has brought forward its Q‑day estimate to 2029.** The reasoning: a quantum computer with one million noisy qubits could break a 2048‑bit RSA key in **under one week**.

This accelerated timeline forces immediate action:

| Entity | PQC Migration Target |
|--------|----------------------|
| **Google** | **2029** (internal) |
| NSA (USA) | 2031 |
| NIST (USA) | 2035 |

The **“Harvest Now, Decrypt Later”** strategy is already in use: attackers collect encrypted data today to decrypt it later with a quantum computer. For security‑critical IoT and industrial applications, **action is required now**.

**Why RSA and ECC have no future:**

| Algorithm | Classical Security | Quantum Attack | Qubits Needed |
|-----------|-------------------|----------------|---------------|
| **RSA‑2048** | ~112 bit | Shor | ~20 million |
| **RSA‑3072** | ~128 bit | Shor | ~10 million |
| **ECC‑256** | ~128 bit | Shor | **2,000 – 10,000** |

The critical insight: **a quantum computer with only 10,000 stable qubits could break ECC‑256**. This requires far fewer qubits than breaking RSA. Therefore, **both RSA and ECC are equally obsolete** – ECC even earlier, due to the lower qubit requirement.

### 2. Quantum‑Resistant Key Exchange – The New Standards

In August 2024, NIST published the first three Post‑Quantum Cryptography (PQC) standards:

| Standard | Algorithm | Type | Purpose |
|----------|-----------|------|---------|
| **FIPS 203** | **ML‑KEM** (formerly CRYSTALS‑Kyber) | Key Encapsulation Mechanism (KEM) | Quantum‑safe key exchange |
| **FIPS 204** | **ML‑DSA** (formerly CRYSTALS‑Dilithium) | Digital Signature | Quantum‑safe signatures |
| **FIPS 205** | **SLH‑DSA** (formerly SPHINCS+) | Stateless Hash‑Based Signature | Fallback for extreme security requirements |

**ML‑KEM (Kyber)** is the primary standard for quantum‑safe key exchange. It is based on the **Module‑Learning‑with‑Errors (MLWE)** problem, which is believed to be resistant to quantum attacks.

**X25519** and **Ed25519** – the widely used ECC curves in TLS 1.3 – are **not quantum‑resistant**. While they offer excellent performance, their security collapses on Q‑Day.

The **long‑term solution** is **hybrid** schemes that combine classical (e.g., X25519) with quantum‑resistant algorithms (e.g., ML‑KEM). TLS 1.3 already supports hybrid groups.

### 3. Cryptographic Hardware Capabilities of the ESP32 Family

Crypto‑agility on ESP32 does **not** mean that a chip can run any algorithm in software – all can do that. The decisive factor is **hardware acceleration** and **ESP‑IDF support** for efficient PQC implementations.

The following table summarises the **hardware‑accelerated cryptographic features** of all relevant ESP32 models, based on official Espressif documentation and the ESP Product Security Feature Matrix.

| Feature | ESP32 | S2 | S3 | C3 | C2 | C5 | C6 | C61 | H2 | H4 | P4 | E22 | H21 | S31 |
|---------|-------|----|----|----|----|----|----|-----|----|----|----|-----|-----|-----|
| **AES** (HW) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **SHA** (HW) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **RSA** (HW) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **ECC** (HW) | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **ECDSA** (HW) | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| **HMAC** (HW) | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Digital Signature (RSA)** | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| **Digital Signature (ECDSA)** | — | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ |
| **APM / TEE** | — | — | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ |
| **Key Manager** | — | — | — | — | — | — | ✓ | — | — | — | ✓ | — | — | — |
| **DPA Protection** | — | — | — | — | — | — | ✓ | — | — | — | ✓ | — | — | — |
| **AES Pseudo‑Round** | — | — | — | — | — | — | ✓ | — | — | — | ✓ | — | — | — |
| **PSA Level 2** | — | — | — | — | — | — | ✓ | — | — | — | — | — | — | — |
| **ECC‑based Secure Boot** | — | — | ✓ | — | — | — | — | — | ✓ | — | — | — | — | ✓ |
| **TRNG** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

*Sources: ESP Product Security Feature Matrix, supplemented by data from the respective chip datasheets.*

### 4. Model‑by‑Model Cryptographic Assessment

#### 4.1 ESP32 (Classic)
- **HW accelerators:** AES, SHA, RSA – **no ECC HW**
- **Missing:** HMAC, Digital Signature Peripheral, TEE
- **Assessment:** Not suitable for PQC (no ECC HW, too slow for software PQC). Adequate for legacy RSA‑2048 applications, but not future‑proof.

#### 4.2 ESP32‑S2
- **HW accelerators:** AES, SHA, RSA
- **ECC:** only for Secure Boot (not general crypto)
- **HMAC, Digital Signature (RSA)** available
- **Assessment:** Limited ECC capabilities. Not recommended for PQC.

#### 4.3 ESP32‑S3
- **HW accelerators:** AES, SHA, RSA, ECC
- **HMAC, Digital Signature (RSA)** available
- **No APM/TEE**
- **Assessment:** Good classical crypto HW, but no TEE. PQC (Kyber/Dilithium) runs in software; benchmarks show Kyber is feasible on the dual‑core, but lacks HW acceleration for PQC‑specific operations.

#### 4.4 ESP32‑C3 (RISC‑V)
- **HW accelerators:** AES‑128/256, SHA‑1/224/256, RSA‑3072
- **ECC, HMAC** available
- **No APM/TEE**
- **PSA Level 1 certified**
- **Assessment:** Good HW support for classical crypto. PQC in software possible (liboqs benchmarks exist for C3), but without HW acceleration.

#### 4.5 ESP32‑C2
- **HW accelerators:** AES, SHA, RSA, ECC (limited scope)
- **No HMAC, no Digital Signature**
- **Assessment:** Minimalistic crypto HW. Unsuitable for PQC (too little performance and memory).

#### 4.6 ESP32‑C5 (Dual‑Band Wi‑Fi 6)
- **HW accelerators:** AES, SHA, RSA, ECC, HMAC, DSA, ECDSA
- **APM (Access Permission Management), PMP (Physical Memory Protection)**
- **External Memory Encryption (XTS‑AES)**
- **TRNG**
- **Assessment:** First RISC‑V platform with **APM/TEE‑like** security. HW ECC for classical crypto, but no PQC‑specific HW. Still, TEE and memory protection make it suitable for security‑critical applications.

#### 4.7 ESP32‑C6 – **The PSA Level 2 Chip**
- **HW accelerators:** AES, SHA, RSA, ECC, HMAC
- **APM/TEE (ESP‑TEE)**
- **Key Manager**
- **DPA Protection** (side‑channel resistant)
- **PSA Level 2 certified** (first RISC‑V MCU with PSA‑L2)
- **Assessment:** **Best ESP32 for security‑critical applications.** PSA‑L2 means the PSA Root of Trust has been laboratory‑tested for resilience against scalable software attacks. **ESP‑TEE** (Trusted Execution Environment) provides hardware‑enforced isolation. PQC in software is possible, but the security architecture is the best in the ESP32 family.

#### 4.8 ESP32‑C61
- **HW accelerators:** AES, SHA, RSA, ECC
- **ECDSA‑based Digital Signature Peripheral** (private keys in eFuse)
- **APM + PMP** (TEE‑like)
- **Assessment:** Affordable Wi‑Fi 6 chip with a solid security package. The **ECDSA‑DS Peripheral** is a real advantage over older models. PQC only in software, but TEE makes it suitable for secure environments.

#### 4.9 ESP32‑H2
- **HW accelerators:** AES‑128/256 (with DPA protection), SHA, RSA, ECC, HMAC
- **Digital Signature (ECDSA)**
- **ECC‑based Secure Boot**
- **No APM/TEE**
- **Assessment:** Ultra‑low‑power with good crypto HW. **ECC‑based Secure Boot** is more modern than RSA‑based on older models. PQC in software possible, but the low compute power (96 MHz) and small SRAM (320 KB) limit complex PQC operations.

#### 4.10 ESP32‑H4
- **HW accelerators:** AES, SHA, RSA, ECC
- **Digital Signature (ECDSA)**
- **TRNG**
- **Assessment:** Like H2, but with dual‑core (96 MHz) and more performance. Better suited for PQC than H2, but still without TEE.

#### 4.11 ESP32‑P4 – **The High‑Performance Flagship**
- **AES** with **DPA resistance** and **Pseudo‑Round protection** (against side‑channel attacks)
- **SHA, RSA, ECC, HMAC** in HW accelerator
- **APM/TEE**
- **Key Manager**
- **Assessment:** **Best performance for PQC in software.** The dual‑core RISC‑V with up to 360 MHz (400 MHz in v3.x) and 768 KB SRAM offers enough “muscle” for computationally intensive PQC algorithms. The DPA‑resistant AES HW is a unique feature. **No integrated radio** – ideal as a central security controller in hybrid systems (e.g., P4 + C6).

#### 4.12 ESP32‑E22 (RCP for Wi‑Fi 6E)
- **Crypto HW** for radio stack security present
- **Focus on RCP architecture** – cryptographic processing is primarily handled by the host system
- **Assessment:** Not to be considered as a standalone crypto engine; security is determined by the host processor.

#### 4.13 ESP32‑H21 (Ultra‑Low‑Power)
- **Crypto HW** similar to H2 (AES, SHA, RSA, ECC, HMAC)
- **No APM/TEE**
- **Assessment:** Like H2, but with optimised power consumption (5 µA deep sleep). Suitable for PQC only in very simple scenarios.

#### 4.14 ESP32‑S31 (Announced)
- **Expected crypto HW:** AES, SHA, RSA, ECC, ECDSA, HMAC
- **TEE + APM** (as expected for RISC‑V platforms)
- **RAM‑based PUF** (Physical Unclonable Function) – unique device identity
- **Assessment:** Potentially the **most secure ESP32** with PUF and TEE. Specifications not final, but promising.

### 5. X25519 / Ed25519 Support – Which ESP32 Can Do It?

**X25519** and **Ed25519** are ECC schemes based on **Curve25519**. They are part of **Elliptic‑Curve Cryptography (ECC)** and are supported by all ESP32 models with an **ECC hardware accelerator** – that is:

- ESP32‑S3
- ESP32‑C3
- ESP32‑C5
- ESP32‑C6
- ESP32‑C61
- ESP32‑H2
- ESP32‑H4
- ESP32‑P4
- ESP32‑E22
- ESP32‑H21
- ESP32‑S31 (announced)

Software support for X25519 and Ed25519 is available in ESP‑IDF via **Mbed TLS** and **wolfSSL**.

**Important:** X25519 and Ed25519 are **not quantum‑resistant**. They offer excellent performance and are suitable for the **transition phase** (hybrid mode with ML‑KEM), but they become obsolete on Q‑Day.

### 6. Recommendations for Quantum‑Safe Architectures on ESP32

| Requirement | Recommended ESP32 | Reason |
|-------------|-------------------|--------|
| **Maximum security (PSA‑L2, TEE, side‑channel protection)** | **ESP32‑C6** | PSA‑L2 certified, ESP‑TEE, DPA protection |
| **Maximum performance for PQC in software** | **ESP32‑P4** | 360–400 MHz, 768 KB SRAM, DPA‑resistant AES |
| **Best compromise (performance + security)** | **ESP32‑S3** | Dual‑core, ECC HW, good for Kyber in SW |
| **Ultra‑low‑power with ECC Secure Boot** | **ESP32‑H2** / **H21** | 7 µA / 5 µA deep sleep, ECC‑based |
| **Low‑cost PQC evaluation** | **ESP32‑C3** | Affordable, RISC‑V, liboqs‑compatible |
| **Future‑proof (PUF + TEE)** | **ESP32‑S31** (announced) | RAM‑based PUF + TEE (specs pending) |

### 7. Practical Implementation – PQC on ESP32 Today

Post‑Quantum Cryptography can already be implemented on ESP32 today:

| Library / Project | Supported ESP32 | Algorithms |
|-------------------|-----------------|------------|
| **wolfSSL** + **wolfCrypt** | C2, C3, C6, S3 | Kyber (ML‑KEM), Dilithium (ML‑DSA) |
| **liboqs** (Open Quantum Safe) | C3, S3, generic | All NIST PQC algorithms |
| **PQCMicro** | All ESP32 (Xtensa/RISC‑V) | ML‑KEM, ML‑DSA, SLH‑DSA |
| **Aethyr Edge Node** | ESP32‑S3 | ML‑KEM‑768, XChaCha20‑Poly1305 |

**Practical example (wolfSSL with Kyber on ESP32)**:

```c
// TLS 1.3 Server with Post-Quantum KEM: KYBER_LEVEL5
// See: https://www.wolfssl.com/post-quantum-key-share-on-the-espressif-esp32/
// The TLS 1.3 handshake uses Kyber for key exchange.
