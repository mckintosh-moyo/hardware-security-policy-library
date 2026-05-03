# Policy: Hardware Supply Chain Security
# Version: 1.0
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Framework Alignment: NIST CSF 2.0 | ISO/IEC 27001:2022
# Review Cadence: Annual or after any supply chain security incident

---

## 1. Purpose

This policy establishes security requirements for the sourcing,
verification, and management of hardware components used in
embedded products. It addresses the risk of counterfeit components,
tampered hardware, and compromised supply chain partners that could
introduce vulnerabilities into products before they reach customers.

---

## 2. Scope

This policy applies to all procurement, engineering, and manufacturing
teams responsible for sourcing and integrating hardware components
into embedded products.

---

## 3. Policy Statements

### 3.1 Approved Vendor Requirements
- All hardware components must be sourced from an approved vendor
  list maintained by the procurement and security teams
- New vendors must undergo a security assessment before approval
- Vendor security assessments must be renewed every two years
- Direct sourcing from unauthorized third-party marketplaces is
  prohibited for security-critical components

### 3.2 Component Verification Requirements
- All incoming security-critical components must be verified for
  authenticity before use in production
- Verification methods must include at minimum visual inspection
  and electrical characteristic testing
- A sample of each component batch must undergo detailed
  authenticity testing
- Any component that fails verification must be quarantined and
  reported to the security team immediately

### 3.3 Bill of Materials Requirements
- A complete Hardware Bill of Materials must be maintained for
  every product
- The BOM must include manufacturer name, part number, version,
  and supplier for every component
- The BOM must be updated whenever components are changed or
  substituted
- BOMs must be stored securely and made available for security
  audits upon request

### 3.4 Counterfeit Component Prevention
- Engineering teams must use counterfeit detection procedures
  for all integrated circuits and security-critical components
- Suspected counterfeit components must be reported to the
  procurement team and security team immediately
- Confirmed counterfeit components must be reported to the
  original component manufacturer
- A record of all counterfeit incidents must be maintained

### 3.5 Secure Manufacturing Requirements
- Manufacturing facilities must be assessed for physical security
  controls before use
- Access to production lines must be restricted to authorized
  personnel only
- Manufacturing processes must include tamper-evident packaging
  before shipment
- A chain of custody must be maintained from manufacturing to
  customer delivery

### 3.6 Third Party Software and Firmware Components
- All third-party firmware libraries and software components
  must be reviewed for known CVEs before integration
- Open source components must be tracked in the SBOM
- License compliance must be verified for all third-party
  components
- Third-party components must be updated when security patches
  are released

---

## 4. Control Mapping

| Policy Statement | NIST CSF 2.0 | ISO 27001:2022 |
|---|---|---|
| Approved vendor requirements | GV.SC-03, GV.SC-06 | A.5.19, A.5.20 |
| Component verification | GV.SC-06, GV.SC-08 | A.5.20, A.5.21 |
| Bill of materials | ID.AM-01, GV.SC-06 | A.5.9, A.5.21 |
| Counterfeit prevention | GV.SC-06, DE.CM-08 | A.5.20, A.8.8 |
| Secure manufacturing | PR.AA-02, GV.SC-08 | A.7.2, A.5.21 |
| Third party components | GV.SC-03, PR.PS-02 | A.5.19, A.8.8 |

---

## 5. Compliance and Exceptions

- Compliance will be assessed during annual supply chain audits
- Exceptions require CISO and procurement director approval
- Supply chain security incidents must be reported to the
  security team within 24 hours of discovery

---

## 6. Review and Maintenance

- This policy will be reviewed annually
- Reviews triggered by supply chain incidents or new regulatory
  requirements
- Policy owner: Procurement and Security Teams

---

## 7. References

- NIST CSF 2.0 — nvlpubs.nist.gov
- NIST SP 800-161 — Supply Chain Risk Management
- ISO/IEC 27001:2022
- ISO 28000 — Supply Chain Security Management