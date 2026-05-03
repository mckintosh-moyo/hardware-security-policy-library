# Hardware Security Policy Library — Summary Dashboard Generator
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Description: Generates a color-coded HTML dashboard summarizing
#              all policies in the hardware security policy library

import datetime

# ── Policy data ───────────────────────────────────────────────────────────────
policies = [
    {
        "id": "POL-001",
        "title": "Secure Firmware Development Policy",
        "file": "01-secure-firmware-development-policy.md",
        "purpose": "Establishes minimum security requirements for firmware development, testing, and release.",
        "scope": "All engineering teams involved in firmware development and release.",
        "key_controls": [
            "Firmware must be cryptographically signed using RSA-2048 or ECDSA-256",
            "Debug features must be disabled in all production firmware builds",
            "Critical CVEs must be patched within 30 days of disclosure",
            "SBOM must be maintained for all firmware components",
            "Secure boot must be implemented on all devices"
        ],
        "nist_controls": ["PR.PS-01", "PR.PS-02", "PR.PS-05", "PR.DS-10", "DE.CM-08"],
        "iso_controls": ["A.8.25", "A.8.28", "A.8.20", "A.8.8"],
        "review": "Annual",
        "owner": "Information Security Team",
        "version": "1.0",
        "color": "#1B3A6B"
    },
    {
        "id": "POL-002",
        "title": "Hardware Debug Interface Security Policy",
        "file": "02-debug-interface-security-policy.md",
        "purpose": "Establishes security requirements for JTAG, UART, and hardware debug interface management.",
        "scope": "Hardware engineering, firmware engineering, and manufacturing teams.",
        "key_controls": [
            "JTAG and UART must be completely disabled in production firmware",
            "JTAG disable fuses must be blown during production programming",
            "Field debug access requires authentication and logging",
            "Debug connectors must be inaccessible in final product enclosure",
            "Tamper-evident seals required on enclosures with debug access"
        ],
        "nist_controls": ["PR.PS-01", "PR.PS-05", "PR.AA-01", "PR.AA-02", "PR.AA-03"],
        "iso_controls": ["A.8.9", "A.8.20", "A.7.2", "A.7.4", "A.8.18"],
        "review": "Annual",
        "owner": "Hardware Security Team",
        "version": "1.0",
        "color": "#2E75B6"
    },
    {
        "id": "POL-003",
        "title": "Hardware Supply Chain Security Policy",
        "file": "03-supply-chain-security-policy.md",
        "purpose": "Establishes security requirements for hardware component sourcing and verification.",
        "scope": "Procurement, engineering, and manufacturing teams.",
        "key_controls": [
            "All components must be sourced from an approved vendor list",
            "Security-critical components must be verified for authenticity",
            "Complete Hardware Bill of Materials must be maintained",
            "Counterfeit component detection procedures must be followed",
            "Manufacturing facilities must be assessed for physical security"
        ],
        "nist_controls": ["GV.SC-03", "GV.SC-06", "GV.SC-08", "ID.AM-01", "DE.CM-08"],
        "iso_controls": ["A.5.19", "A.5.20", "A.5.21", "A.5.9"],
        "review": "Annual",
        "owner": "Procurement and Security Teams",
        "version": "1.0",
        "color": "#217A79"
    },
    {
        "id": "POL-004",
        "title": "Vulnerability Disclosure Policy",
        "file": "04-vulnerability-disclosure-policy.md",
        "purpose": "Establishes a formal process for receiving and responding to hardware vulnerability reports.",
        "scope": "All hardware and software components of embedded products.",
        "key_controls": [
            "Vulnerability reports must receive acknowledgment within 2 business days",
            "Critical vulnerabilities must be patched within 30 days",
            "Minimum 90-day coordinated disclosure window for reporters",
            "Safe harbor protection for good faith security researchers",
            "Public security advisories required for Critical and High findings"
        ],
        "nist_controls": ["RS.CO-03", "DE.CM-08", "RS.AN-03", "PR.PS-02", "GV.OC-01"],
        "iso_controls": ["A.6.8", "A.8.8", "A.5.7", "A.5.29"],
        "review": "Annual",
        "owner": "Product Security Team",
        "version": "1.0",
        "color": "#375623"
    },
    {
        "id": "POL-005",
        "title": "Hardware Incident Response Policy",
        "file": "05-hardware-incident-response-policy.md",
        "purpose": "Establishes procedures for detecting, responding to, and recovering from hardware security incidents.",
        "scope": "All security incidents affecting embedded hardware products.",
        "key_controls": [
            "P1 incidents must be acknowledged within 1 hour of detection",
            "Forensic evidence must be preserved before any remediation",
            "Compromised firmware update channels suspended immediately",
            "Post-incident review completed within 14 days of closure",
            "Incident response tested annually through tabletop exercises"
        ],
        "nist_controls": ["RS.MA-01", "RS.AN-03", "RS.MI-01", "RC.RP-01", "DE.CM-01"],
        "iso_controls": ["A.5.24", "A.5.26", "A.5.28", "A.5.29"],
        "review": "Annual + After P1/P2 incidents",
        "owner": "Information Security Team",
        "version": "1.0",
        "color": "#C00000"
    },
]

# ── Date ──────────────────────────────────────────────────────────────────────
date_str = datetime.datetime.now().strftime("%B %d, %Y")

# ── Generate HTML ─────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hardware Security Policy Library</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f5f5f5;
            color: #333;
        }}
        h1 {{ color: #1B3A6B; border-bottom: 3px solid #1B3A6B; padding-bottom: 10px; }}
        h2 {{ color: #2E75B6; margin-top: 30px; }}
        .meta {{
            background: #1B3A6B; color: white;
            padding: 15px 20px; border-radius: 6px; margin-bottom: 25px;
        }}
        .meta p {{ margin: 4px 0; }}
        .grid {{
            display: grid; grid-template-columns: repeat(5, 1fr);
            gap: 15px; margin-bottom: 30px;
        }}
        .card {{
            padding: 15px; border-radius: 8px;
            text-align: center; color: white;
            font-weight: bold; font-size: 0.85em;
        }}
        .policy-card {{
            background: white; border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 25px; overflow: hidden;
        }}
        .policy-header {{
            padding: 15px 20px; color: white;
            display: flex; justify-content: space-between;
            align-items: center;
        }}
        .policy-header h3 {{ margin: 0; font-size: 1em; }}
        .policy-body {{ padding: 20px; }}
        .policy-body p {{ margin: 0 0 10px 0; font-size: 0.9em; }}
        .controls-grid {{
            display: grid; grid-template-columns: 1fr 1fr;
            gap: 15px; margin-top: 15px;
        }}
        .control-box {{
            background: #f9f9f9; border-radius: 6px;
            padding: 12px; font-size: 0.85em;
        }}
        .control-box h4 {{
            margin: 0 0 8px 0; color: #1B3A6B;
            font-size: 0.9em;
        }}
        .badge {{
            display: inline-block; padding: 2px 8px;
            border-radius: 10px; color: white;
            font-size: 0.78em; font-weight: bold;
            margin: 2px;
        }}
        ul {{ margin: 0; padding-left: 18px; }}
        li {{ margin-bottom: 4px; }}
        .meta-row {{
            display: flex; gap: 20px;
            font-size: 0.85em; color: #666;
            margin-top: 10px;
        }}
        .footer {{
            margin-top: 40px; text-align: center;
            color: #888; font-size: 0.85em;
            border-top: 1px solid #ddd; padding-top: 15px;
        }}
    </style>
</head>
<body>
    <h1>Hardware Security Policy Library</h1>
    <div class="meta">
        <p><strong>Author:</strong> Mckintosh Mpumelelo Moyo</p>
        <p><strong>Program:</strong> MS Cybersecurity — Yeshiva University, Katz School</p>
        <p><strong>Frameworks:</strong> NIST CSF 2.0 | ISO/IEC 27001:2022</p>
        <p><strong>Generated:</strong> {date_str}</p>
    </div>

    <h2>Policy Overview</h2>
    <div class="grid">
"""

for pol in policies:
    html += f"""
        <div class="card" style="background:{pol['color']}">
            {pol['id']}<br>{pol['title'].replace(' Policy','').replace(' Security','').replace('Hardware ','')}
        </div>
"""

html += """
    </div>

    <h2>Policy Details</h2>
"""

for pol in policies:
    nist_badges = "".join([f'<span class="badge" style="background:#1B3A6B">{c}</span>' for c in pol['nist_controls']])
    iso_badges = "".join([f'<span class="badge" style="background:#217A79">{c}</span>' for c in pol['iso_controls']])
    key_controls_html = "".join([f"<li>{c}</li>" for c in pol['key_controls']])

    html += f"""
    <div class="policy-card">
        <div class="policy-header" style="background:{pol['color']}">
            <h3>{pol['id']} — {pol['title']}</h3>
            <span style="font-size:0.85em">v{pol['version']}</span>
        </div>
        <div class="policy-body">
            <p><strong>Purpose:</strong> {pol['purpose']}</p>
            <p><strong>Scope:</strong> {pol['scope']}</p>
            <div class="controls-grid">
                <div class="control-box">
                    <h4>Key Controls</h4>
                    <ul>{key_controls_html}</ul>
                </div>
                <div class="control-box">
                    <h4>NIST CSF 2.0 Controls</h4>
                    {nist_badges}
                    <h4 style="margin-top:12px">ISO 27001:2022 Controls</h4>
                    {iso_badges}
                </div>
            </div>
            <div class="meta-row">
                <span><strong>Review:</strong> {pol['review']}</span>
                <span><strong>Owner:</strong> {pol['owner']}</span>
                <span><strong>File:</strong> {pol['file']}</span>
            </div>
        </div>
    </div>
"""

html += f"""
    <div class="footer">
        <p>Hardware Security Policy Library — {len(policies)} Policies</p>
        <p>Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University</p>
        <p>Frameworks: NIST CSF 2.0 | ISO/IEC 27001:2022</p>
    </div>
</body>
</html>
"""

# ── Save report ───────────────────────────────────────────────────────────────
output_file = "summary/policy-dashboard.html"
with open(output_file, "w") as f:
    f.write(html)

print("=" * 55)
print("  Hardware Security Policy Dashboard — Generated!")
print("=" * 55)
print(f"  Date:            {date_str}")
print(f"  Total Policies:  {len(policies)}")
for pol in policies:
    print(f"  {pol['id']}:        {pol['title']}")
print("=" * 55)
print(f"  Dashboard saved to: {output_file}")
print("=" * 55)