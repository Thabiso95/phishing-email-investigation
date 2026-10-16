Phishing Email Investigation

Project Overview

This project demonstrates a basic Security Operations Center (SOC) workflow for investigating a suspected phishing email using synthetic evidence, Python-based indicator analysis and automated unit tests.

The investigation focuses on identifying suspicious sender-domain patterns, urgency-based social engineering and account-verification links.

Objectives

- Examine a synthetic phishing email.
- Identify suspicious indicators.
- Implement basic Python detection logic.
- Validate expected behaviour using automated tests.
- Document findings, limitations and recommended incident response actions.

Case Study: PHISH-001

Classification: Likely phishing within the synthetic training scenario.

The sample contains three configured indicators:

1. Possible brand impersonation.
2. Urgency or pressure tactics.
3. A verification link requiring investigation.

No live phishing infrastructure or account compromise was established.

Repository Structure

phishing-email-investigation/
├── evidence/
│   ├── README.md
│   └── phishing-email-001.eml
├── src/
│   └── analyze_email.py
├── tests/
│   └── test_analyze_email.py
├── reports/
│   └── PHISH-001-investigation-report.md
└── README.md

Validation Results

The Python analysis script was executed in Google Colab against the synthetic email evidence.

Automated test results: 4 passed, 0 failed.

The tests cover:

- Detection of three configured phishing indicators.
- Handling of a clean-message example.
- Case-insensitive matching for the verification-link rule.
- Detection of a suspicious sender without other indicators.

These results apply only to the tested synthetic inputs. They do not establish production detection accuracy or confirm a real-world phishing incident.

Tools and Technologies

- Python
- Google Colab
- Git and GitHub
- Python "unittest"
- Email and phishing investigation concepts

Limitations

- Synthetic email evidence only.
- No live email gateway or SIEM integration.
- No real email authentication headers.
- No external threat-intelligence checks.
- Basic string matching may produce false positives and false negatives.

Future Improvements

- Parse real-format email headers from sanitised test samples.
- Add SPF, DKIM and DMARC result analysis.
- Improve URL and domain parsing.
- Expand tests for edge cases and false positives.
- Integrate the investigation workflow with a SIEM in a suitable lab.

Disclaimer

This repository is for defensive security education and portfolio development. All email samples are synthetic and intended for safe analysis.