PHISH-002 — Recruitment Email Investigation

1. Case Overview

- Case ID: PHISH-002
- Case type: Suspected phishing / recruitment fraud
- Date received: 29 October 2026
- Severity: Provisional — High Caution
- Status: Open — further verification required
- Analyst: SOC Portfolio Analyst
- Evidence source: Email received directly by the analyst

2. Executive Summary

An unsolicited recruitment email invited the recipient to an introductory interview for an IT Helpdesk Support position associated with Willemse Advisory Group.

The message requested an updated CV, a certified identity document and academic qualifications. It also described a criminal-record and credit evaluation process, including an optional third-party screening service costing R310.

The investigation identified several warning signs:

- The sending domain was registered approximately 42.5 hours before the email was received.
- The advertised vacancy could not be independently verified through a careers page.
- A CIPC search under the advertised business name returned no matching result.
- The email used a recruitment domain different from the company website checked.
- The screening-fee arrangement and request for identity documents create potential financial-fraud and identity-exposure risks.

Email authentication results showed SPF, DKIM and DMARC passing in the original Gmail headers. These results establish authentication against the sending domain but do not establish the sender's affiliation with a legitimate employer.

Initial conclusion: The email is suspicious and may represent recruitment fraud or business impersonation. Fraud has not been conclusively established. Further verification is required.

3. Incident Details

The email subject was:

"IT Helpdesk Support Introductory Interview | Willemse Advisory Group"

The message proposed an online interview on 2 November 2026 at 10:00 SAST. It stated that a meeting link would be provided after confirmation.

The sender requested:

- An updated CV
- A certified copy of the recipient's identity document
- Academic qualifications and certificates

The message also referred to criminal-record and ITC credit checks and offered an optional third-party screening service for R310.

The recipient reported no reply, document submission or payment.

4. Technical Evidence

4.1 Email authentication

The original Gmail headers reported:

- SPF: PASS
- DKIM: PASS
- DMARC: PASS

The message's Return-Path and From domain were aligned with "wagjobs.online". A DKIM signature used selector "s1".

These results are consistent with the message being sent through infrastructure authorised to send for the domain. They do not verify the recruiter's identity or the legitimacy of the vacancy.

4.2 DNS findings

- MX: "mx.stackmail.com"
- SPF: "v=spf1 include:spf.stackmail.com a mx -all"
- DKIM selector: "s1"
- DMARC policy: "p=none"
- DNS hosting: StackDNS nameservers

The DMARC policy is monitoring-only. The SPF diagnostic tool also displayed a failure result, which was not reconciled with Gmail's original SPF PASS result. The discrepancy remains unresolved and must not be reported as a confirmed SPF failure.

4.3 Domain registration

The supplied RDAP lookup reported that "wagjobs.online" was created on 27 October 2026 at 13:24:04 UTC. The email was sent on 29 October 2026 at 07:56:22 UTC.

The interval is approximately 42 hours and 32 minutes.

A recently registered domain is a contextual risk indicator, not proof of malicious activity.

5. OSINT and Business Verification

The analyst checked the company's website and publicly available business information.

Findings:

- No careers page listing the specific IT Helpdesk Support vacancy was found.
- The recruitment email used a different domain from the company website checked.
- A CIPC search under the advertised business name returned no matching result.
- The address appeared to match a source checked by the analyst; business identity and recruiter affiliation remain unverified.

A failed company-name search does not establish that no legal entity exists. The business may use a different registered name.

6. Indicators and Risk Factors

Indicator| Assessment
Domain registered shortly before delivery| High concern
Vacancy not independently verified| High concern
Legal entity not verified under advertised name| Unresolved
Request for identity documents| Potential identity-exposure risk
Optional R310 screening service| Potential financial risk
SPF, DKIM and DMARC passed| Authentication evidence, not proof of legitimacy
Matching address reported by analyst| Partial consistency; insufficient verification

7. Impact Assessment

No direct compromise or financial loss was reported at the time of investigation.

Potential impacts if the recipient had engaged include:

- Identity-document exposure
- Payment to an unverified screening provider
- Further social engineering
- Collection of personal and employment information

These are potential impacts, not confirmed outcomes.

8. Recommended Actions

1. Do not pay the screening fee while the employer and provider remain unverified.
2. Do not send identity documents or additional sensitive information.
3. Preserve the original email and complete headers securely.
4. Verify the vacancy and recruiter through independently sourced business contact details.
5. Report the email through the email provider if it is believed to be deceptive.
6. Reassess the case if new evidence establishes the business identity, recruiter affiliation or screening provider.

9. Limitations

This investigation did not establish who controls the sending domain, whether the advertised company is connected to that domain, or whether the vacancy is genuine.

The SPF diagnostic discrepancy remains unresolved. No malicious attachment or interview link was available for analysis at the time of investigation.

The case is therefore classified as suspected recruitment fraud or impersonation, not confirmed phishing.

10. Final Disposition

Status: Open — further verification required.

Assessment: Suspicious recruitment email with multiple risk indicators. No recipient engagement or resulting compromise reported.

Evidence standard: Conclusions are limited to observed email metadata, supplied DNS/RDAP results and the checks performed by the analyst.