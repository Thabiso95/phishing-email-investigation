# PHISH-002 — Indicator Register

## Case information

- **Case ID:** PHISH-002
- **Classification:** High-risk recruitment email; suspected recruitment fraud or impersonation
- **Status:** Open — affiliation unverified
- **Purpose:** Record observable indicators without incorrectly labelling unverified infrastructure as malicious.

## Indicator table

| ID | Indicator type | Value | Observation | Assessment | Confidence |
|---|---|---|---|---|---|
| IND-001 | Domain | `wagjobs.online` | Domain registration was recorded approximately 42 hours before the email was received. | Suspicious context; domain age alone does not prove maliciousness. | High confidence in the recorded age; low confidence as a standalone malicious indicator |
| IND-002 | Email address | `recruitment@wagjobs.online` | Address used as the sender of the recruitment email. | Sender identity and affiliation with the named organisation remain unverified. | High confidence that the address appeared in the email |
| IND-003 | Email address | `hr@wagjobs.online` | Address listed in the email signature. | Association with a legitimate employer has not been independently established. | High confidence that the address appeared in the email |
| IND-004 | Sending IP address | `185.151.28.79` | IP address reported in the email's SPF authentication result. | Observed sending infrastructure only; no evidence here establishes that the IP is malicious. | High confidence in the recorded header value |
| IND-005 | Authentication result | SPF, DKIM and DMARC passed | Gmail reported all three checks passing for the message. | Supports domain-level authentication, not the legitimacy of the recruiter or job offer. | High confidence based on the received headers |
| IND-006 | Payment request | R310 third-party compliance fee | The email described an optional fee associated with a compliance process. | Potential financial-risk indicator requiring independent verification. | High confidence that the request appeared in the email |

## Handling guidance

1. Do not automatically block or label these indicators as malicious based on this case alone.
2. Do not submit the sender IP or domain to public blocklists as confirmed malicious without additional evidence.
3. Do not visit links, contact numbers, or payment providers supplied in the suspicious email to verify the sender.
4. Verify the vacancy and recruitment relationship through independently sourced official contact details.
5. Preserve the original email and full headers privately. Redact personal information before sharing evidence publicly.

## Limitations

- Authentication results show that the message passed the reported domain authentication checks; they do not establish that the named organisation authorised the recruitment activity.
- A recently registered domain is a risk signal, not proof of fraud.
- The sender's identity, the vacancy, and the stated compliance process remain unverified.
- This register records observations and assessments, not confirmed malicious indicators.

## Current disposition

**High risk — further verification required.** No response, document submission, or payment had been made at the time of investigation.
