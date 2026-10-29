# PHISH-002 — MITRE ATT&CK Assessment

## Case context

- **Case ID:** PHISH-002
- **Assessment status:** Provisional
- **Case classification:** High-risk recruitment email; suspected recruitment fraud or impersonation
- **Purpose:** Assess whether observed evidence supports mapping the case to MITRE ATT&CK.

## Technique assessment

| ATT&CK technique | Name | Assessment | Evidence and limitation |
|---|---|---|---|
| T1566 | Phishing | Not confirmed | A suspicious recruitment email was received, but the evidence does not establish that it was used to gain access to a system or deliver a malicious payload. |
| T1566.002 | Spearphishing Link | Not confirmed | No malicious link or link-based compromise has been established. The email proposed sending a meeting link after confirmation. |
| T1566.001 | Spearphishing Attachment | Not confirmed | The email requested documents from the recipient; that is not evidence of a malicious attachment. No malicious attachment has been established. |
| T1598 | Phishing for Information | Possible investigative hypothesis only | The email requested a CV, certified identity document, and qualifications. This could expose personal information, but the sender's intent and any connection to an intrusion operation remain unverified. |

## Findings

1. The observed behaviour raises concerns about recruitment legitimacy and possible personal-data or financial exposure.
2. The evidence does not establish malware delivery, credential theft, account compromise, or initial access to an organisation.
3. ATT&CK is designed to describe adversary tactics and techniques. A suspected recruitment scam should not automatically be treated as a confirmed ATT&CK event.
4. T1598 is included only as a hypothesis for review, not as a confirmed technique used by the sender.

## Detection opportunities

- Review mail gateway or mailbox audit logs for similar messages using the same sender domain, subject, or message identifiers.
- If an organisation received similar messages, search for messages sent from `wagjobs.online` and identify recipients.
- Review URL, attachment, and click telemetry only if those artefacts exist; none should be assumed from the current evidence.
- Follow the organisation's approved process for handling suspicious recruitment messages and protecting personal information.

## Conclusion

**No MITRE ATT&CK technique is confirmed by the evidence currently available.** The email warrants further verification and cautious handling, but technical attribution or claims of system compromise would be unsupported.

## References

- MITRE ATT&CK Enterprise: https://attack.mitre.org/
- T1566 — Phishing: https://attack.mitre.org/techniques/T1566/
- T1598 — Phishing for Information: https://attack.mitre.org/techniques/T1598/
