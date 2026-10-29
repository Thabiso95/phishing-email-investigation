# Phishing Email Investigation

A cybersecurity portfolio project demonstrating phishing triage, indicator analysis, evidence documentation, MITRE ATT&CK assessment, and automated validation using Python.

## Project Overview

This repository contains two investigations demonstrating defensive Security Operations Center (SOC) workflows.

- **PHISH-001:** Synthetic phishing-email analysis using Python-based indicator detection and automated unit tests.
- **PHISH-002:** Investigation of a suspicious recruitment email, including evidence documentation, a timeline, indicator analysis, findings, and a provisional MITRE ATT&CK assessment.

The project emphasises evidence-based conclusions, transparent limitations, and avoiding unsupported claims about malicious activity.

## Case Study: PHISH-001

**Classification:** Likely phishing within the synthetic training scenario.

### Objectives

- Examine a synthetic email sample.
- Identify configured phishing indicators.
- Implement basic Python detection logic.
- Validate detection behaviour using automated tests.
- Document findings and recommended defensive actions.

### Indicators assessed

1. Possible brand impersonation.
2. Urgency or pressure tactics.
3. A verification link requiring investigation.

### Validation

Previously recorded results: **4 tests passed, 0 failures.**

Tests cover configured indicator detection, clean-message handling, case-insensitive matching, and suspicious sender detection.

These results apply only to the tested synthetic inputs. They do not establish production detection accuracy or a real-world compromise.

## Case Study: PHISH-002

**Classification:** High-risk suspicious recruitment email; suspected recruitment fraud or impersonation remains unconfirmed.

### Objectives

- Assess suspicious recruitment claims and requests.
- Record indicators and supporting evidence.
- Document a chronological investigation timeline.
- Evaluate findings and evidential limitations.
- Assess potentially relevant MITRE ATT&CK techniques.
- Validate investigation documentation with automated tests.

### Investigation highlights

- **Sender and domain assessment:** Records observed details while distinguishing suspicious context from proof of maliciousness.
- **Email authentication:** Assesses reported SPF, DKIM, and DMARC results without treating successful authentication as proof of legitimacy.
- **Financial risk:** Documents a requested third-party compliance fee as a warning sign requiring independent verification.
- **Evidence handling:** Maintains an evidence register, timeline, indicator register, and findings.
- **MITRE ATT&CK:** Evaluates potential techniques without presenting unconfirmed activity as established fact.
- **Defensible conclusion:** Keeps the investigation appropriately qualified rather than declaring fraud or system compromise proven.

### Validation

Previously recorded results: **17 PHISH-002 tests passed, 0 failures.**

The tests validate selected requirements in the incident report, indicator register, and MITRE ATT&CK assessment. They do not independently establish whether the email is fraudulent.

## Repository Structure

```text
phishing-email-investigation/
├── analysis/
│   └── PHISH-002/
│       ├── findings.md
│       ├── indicator-register.md
│       ├── mitre-attack-assessment.md
│       └── timeline.md
├── evidence/
│   ├── PHISH-002/
│   │   └── evidence-register.md
│   ├── phishing-email-001.eml
│   └── README.md
├── reports/
│   ├── PHISH-001-investigation-report.md
│   └── PHISH-002-incident-report.md
├── src/
│   └── analyze_email.py
├── tests/
│   ├── test_analyze_email.py
│   ├── test_phish002_attack.py
│   ├── test_phish002_indicators.py
│   └── test_phish002_report.py
└── README.md
