# Shopping List

## USB Interface Speed Note

When choosing a board for USB-heavy applications (mass storage, high-throughput data transfer, video capture), 
note that not all "USB OTG" is equal:

- **Full Speed only (12 Mbit/s):** ESP32-S2, ESP32-S3
- **High Speed (480 Mbit/s):** ESP32-P4 (dedicated High-Speed OTG controller, separate from its Full-Speed controller)
- **Expected High Speed (unconfirmed):** ESP32-S31 — not yet stated in a public datasheet; positioning as S3 successor suggests it, but treat as unverified until Espressif publishes final specs.

For applications needing fast USB throughput (e.g. UVC video capture, mass storage emulation), P4 is currently 
the only *confirmed* High-Speed option in the family.

*(h/t [ukezi](https://www.reddit.com/user/ukezi/) on [r/embedded](https://www.reddit.com/r/embedded/comments/1vdgc5l/comment/p19jubw/) for flagging this)*
