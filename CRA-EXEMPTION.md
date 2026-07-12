# CRA Exemption & Non‑Liability Statement

**Version:** 2.0  
**Date:** July 2026  
**Applicable Regulation:** Regulation (EU) 2024/2847 (Cyber Resilience Act – CRA)

---

## 1. Project Status – Explicit Exclusion

This repository and its contents (the “Project”) are provided by a **private individual** outside the course of any commercial activity.

The Project is:
- Fully open-source (licensed under CC BY 4.0).
- Provided free of charge, without any commercial offering, paid services, or monetization.
- Not “placed on the market” or “put into service” within the meaning of the CRA.

**Therefore, pursuant to Article 2(5) of the CRA, this Project is explicitly excluded from the scope of the Regulation.**

---

## 2. Nature of the Content – Documentation, Not Executable Software

This is the **most critical argument** that many legal departments overlook:

The Project consists **exclusively** of:
- Informational text content (Markdown, tables, analysis, descriptions)
- Static reference data and technical overviews
- No executable code, binaries, libraries, drivers, or firmware
- No digital instructions that could be integrated into a “product with digital elements”

**Legal Consequence:**
The CRA defines a “product with digital elements” (Art. 3(1)) as software or hardware that performs a **function** (e.g., controlling, processing, storing, or transmitting data).  
Static documentation – even if it describes technical products – **does not perform any such function**. It is not software in the sense of the CRA.

The European Commission’s own guidance on the CRA explicitly clarifies that **standalone documentation is not a “product with digital elements”** unless it is bundled as the user manual for a specific regulated product (which is not the case here).

**Therefore, the CRA does not apply to this Project from the very outset – regardless of the commercial/non-commercial question.**

---

## 3. Legal Basis – The “Non-Commercial” Exclusion (Secondary Argument)

Even if one were to (incorrectly) interpret this documentation as “software,” the CRA explicitly excludes non-commercial open-source projects.

The CRA applies **only** to products with digital elements that are made available on the market **in the course of a commercial activity**.

**Recital 10** (extract):
> *“Free and open-source software developed or supplied outside the course of a commercial activity should not be covered by this Regulation.”*

**Recital 18** (extract, addressing the liability myth):
> *“[…] the natural or legal person who makes the product available, whether for payment or free of charge, should not be considered a manufacturer if the product is not made available in the course of a commercial activity. **Developers contributing unpaid to open source are not subject to obligations under this Regulation, even if the software ends up in critical infrastructure.**”*

---

## 4. Clarification on Liability – “Downstream Responsibility”

**Addressed to Legal Departments (the “walls” you are speaking to):**

We are aware that many legal departments currently interpret the CRA as imposing compliance obligations (e.g., full conformity assessment, SBOM submission, vulnerability reporting, CE marking) on *all* software contributors. **This interpretation is legally incorrect.**

### 4.1 No “Liability by Association”
The CRA does **not** establish a cascade of liability that flows upstream to individual open-source developers or document authors.  
If a commercial entity integrates information from this Project into a product placed on the EU market, the **sole liability** (including product liability under Art. 32) rests with that **commercial manufacturer, importer, or distributor** – not with the original author.

### 4.2 The “Manufacturer” Definition
According to Article 3(1), a “manufacturer” is a natural or legal person who develops or manufactures a product **and places it on the market under their own name or trademark**.  
As this Project is distributed without a commercial brand, under a generic open-source license, and without any associated commercial distribution channel, the author is **not** a manufacturer under the CRA.

### 4.3 CE Marking
Pursuant to Art. 30 of the CRA, the CE marking indicates conformity **for the finished commercial product**.  
An open-source repository **must not** and **cannot** carry a CE marking. Imposing such a requirement on an upstream library or documentation project is a violation of the Regulation itself.

---

## 5. Clarification on “Open Source Stewards”

We acknowledge that the CRA has special rules for so-called “Open Source Stewards” (Art. 3(14)). However, these rules apply only to entities that:
- Regularly supply open-source software,
- Have a **legal personality** (e.g., a foundation, company, or association),
- And **engage in commercial activities** or act as a commercial intermediary.

A private individual maintaining a single documentation repository **does not** fall under this definition.

---

## 6. What Legal Departments Should Actually Do

If your company uses information from this Project in a commercial product, your **internal compliance obligations** are:

1. **Assess the risk** of the *finished* product you place on the market.
2. **Perform the conformity assessment** for your *own* product (not for this documentation).
3. **Create a Software Bill of Materials (SBOM)** for your *own* product.
4. **Report exploited vulnerabilities** of your *own* product to ENISA within 24 hours (Art. 14).

**You are not required to:**
- Demand a CE marking from this Project.
- Demand a full third-party audit of this Project.
- Force this Project to implement organisational security processes.
- Treat this documentation as if it were executable software.

---

## 7. Ready‑to‑Use Statement for Legal Departments (Copy & Paste)

If you are facing a legal department that insists on a formal declaration, you may forward the following text:

---

**Subject: CRA Applicability – Official Statement**

> *“Pursuant to Article 2(5) of the CRA and Recital 10, it is hereby confirmed that this repository is not operated commercially and does not contain any executable software. The content consists exclusively of static text documents (analyses, tables, descriptions). Legally, it is not a ‘product with digital elements’ within the meaning of the CRA. A conformity assessment, CE marking, or reporting obligations on your part are neither required for this repository nor will we initiate them. Sole responsibility for CRA compliance lies with the party that integrates this information into a commercial product and places it on the market.”*

---

## 8. Recommendations for Downstream Users

For absolute clarity and to simplify your internal compliance, we recommend:

- If you deploy this information in an industrial, medical, or critical environment, you must perform your own **risk assessment** for the *combined* system.
- If you modify or re-publish this content as part of a commercial offering, you become the manufacturer of the *derived* product and are responsible for its compliance.

---

## 9. References

- [Regulation (EU) 2024/2847 (Full Text)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847)
- [EU Cyber Resilience Act – Open Source Guidance (European Commission)](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source)

---

*This statement is provided for informational and compliance transparency purposes. It does not constitute legal advice. Downstream users are encouraged to consult with legal counsel regarding their specific implementation and commercial context.*
