PHISH-002 — Evidence Register

Purpose

Record the evidence collected during the investigation of a suspicious recruitment email received on 29 October 2026. Distinguish direct observations from interpretations and unresolved questions.

Evidence Inventory

ID| Evidence| Source| Finding| Limitation
E-001| Original email and headers| Gmail — Show original| SPF, DKIM and DMARC reported PASS| Authentication does not establish employer legitimacy
E-002| Email body| Original received email| Requests CV, certified ID and qualifications; mentions R310 screening service| No payment request outcome or provider verification established
E-003| Domain registration record| User-collected RDAP result| Domain created 27 October 2026 at 13:24:04 UTC| Registrant identity was redacted
E-004| MX lookup| MXToolbox| MX points to mx.stackmail.com| Hosting configuration does not establish legitimacy
E-005| SPF lookup| MXToolbox| Published SPF record includes Stackmail, A and MX mechanisms| Tool displayed a failure diagnostic; discrepancy with Gmail PASS unresolved
E-006| DKIM lookup| MXToolbox| Public key exists for selector s1| Key presence does not identify the operator
E-007| DMARC lookup| MXToolbox| Policy is p=none| Monitoring-only policy
E-008| Careers-page check| Company website checked by analyst| No careers page listing the vacancy found| Vacancy could be advertised elsewhere
E-009| Business-name search| CIPC search performed by analyst| No matching result under advertised name| Alternate registered name not ruled out
E-010| Address comparison| Email and source checked by analyst| Address reportedly matches| Address match does not verify recruiter affiliation
E-011| Recipient engagement| Recipient statement| No reply, document submission or payment reported| Based on recipient's account

Evidence Handling

- Preserve the original email and full headers in private storage.
- Do not publish raw headers if they expose personal information or account identifiers.
- Do not commit identity documents, private email files, phone numbers or other sensitive personal data.
- Retain source URLs, collection dates and screenshots where available.
- Redact personal information from public evidence.
- Do not alter the original evidence; perform analysis on copies.

Current Assessment

The available evidence supports a high-caution classification for suspected recruitment fraud or impersonation. The sender's identity, the legal entity behind the advertised business, and the vacancy remain unverified.

This assessment is provisional and must be updated if new evidence becomes available.