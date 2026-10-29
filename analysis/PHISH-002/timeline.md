PHISH-002 — Investigation Timeline

Case Information

- Case ID: PHISH-002
- Incident type: Suspected recruitment fraud / impersonation
- Email received: 29 October 2026 at 07:56:22 UTC
- Investigation status: Open — further verification required
- All times: UTC unless otherwise specified

Timeline

Timestamp| Event| Evidence / Source| Analyst Interpretation
27 Oct 2026 13:24:04| "wagjobs.online" registered| RDAP result supplied during investigation| Domain age is a significant contextual risk indicator; not proof of fraud
29 Oct 2026 07:56:22| Recruitment email sent| Original email headers| Message proposes an IT Helpdesk Support interview and requests personal documents
29 Oct 2026 07:56:25–07:56:26| Email received and processed by Gmail| Received and X-Received headers| Message reached Gmail; authentication results reported PASS
29 Oct 2026| MX and DMARC lookups performed| MXToolbox results| MX exists; DMARC policy is "p=none"
29 Oct 2026| SPF lookup performed| MXToolbox result| SPF record identified; diagnostic failure requires reconciliation with Gmail's SPF PASS
29 Oct 2026| DKIM lookup performed| MXToolbox result| Public key exists for selector "s1"
29 Oct 2026| Company website and vacancy checked| Analyst's website review| No careers page listing the specific vacancy found
29 Oct 2026| CIPC search performed| Analyst's CIPC search| No match found under the advertised business name; alternate legal name remains possible
29 Oct 2026| Recipient engagement assessed| Recipient statement| No reply, document submission or payment reported

Timeline Assessment

The sending domain was registered approximately 42 hours and 32 minutes before the email was sent.

The timing, unverified vacancy, unverified business identity and requests for sensitive documents justify further investigation. Successful email authentication does not establish that the sender is affiliated with the advertised employer.

Outstanding Actions

1. Verify the legal entity behind the advertised business name.
2. Verify the recruiter's affiliation using independently sourced contact information.
3. Investigate the third-party screening provider and its payment arrangement, if identifiable without contacting the sender.
4. Reconcile the SPF diagnostic output with the original Gmail authentication result.
5. Update the case disposition if new evidence confirms or refutes the suspected fraud.

Limitations

Some investigative actions are recorded by date only because exact collection times were not captured. These dates reflect the analyst's account and should not be interpreted as independently timestamped forensic records.