PHISH-002 — Investigation Findings

1. Objective

Assess whether a recruitment email claiming to represent Willemse Advisory Group is consistent with a legitimate hiring process or presents indicators of possible recruitment fraud or business impersonation.

2. Key Findings

F-001: Newly Registered Sending Domain

Observation: The supplied RDAP record shows that "wagjobs.online" was created on 27 October 2026 at 13:24:04 UTC. The email's Date header is 29 October 2026 at 07:56:22 UTC.

Assessment: The domain was approximately 42 hours and 32 minutes old when the email was sent.

Confidence: High for the reported timestamps; moderate as a risk indicator.

Limitation: A new domain is not inherently malicious.

F-002: Email Authentication Passed

Observation: Gmail's original authentication results report SPF, DKIM and DMARC as PASS. A DKIM public key is published for selector "s1".

Assessment: The message passed the configured authentication checks for its sending domain.

Confidence: High for the recorded Gmail results.

Limitation: Authentication does not prove that the sender represents the advertised employer.

F-003: SPF Diagnostic Discrepancy

Observation: MXToolbox displayed a failure diagnostic during the SPF lookup, while Gmail's original headers report SPF PASS for the received email.

Assessment: The discrepancy has not been reconciled.

Confidence: High that both outputs were observed; low for any explanation of the discrepancy.

Required action: Preserve the full diagnostic output and investigate the exact evaluation context before drawing a conclusion.

F-004: Vacancy and Business Identity Unverified

Observation: The analyst did not find a careers page listing the IT Helpdesk Support vacancy. A CIPC search under the advertised business name returned no matching result.

Assessment: The vacancy and legal identity remain unverified.

Confidence: High that these searches produced no match in the locations checked.

Limitation: The vacancy could be advertised elsewhere, and the business may use a different registered legal name.

F-005: Potential Identity and Financial Exposure

Observation: The email requests a certified identity document, qualifications and an updated CV. It also mentions an optional R310 screening service.

Assessment: If the sender is deceptive, complying could expose personal information or result in financial loss.

Confidence: High that the requests appeared in the email; the sender's intent remains unproven.

F-006: No Engagement Reported

Observation: The recipient reports no reply, document submission or payment.

Assessment: No engagement or resulting compromise was reported at the time of investigation.

Confidence: Based on the recipient's statement.

3. Alternative Explanations

- A legitimate organisation may use a newly registered recruitment domain.
- The organisation may operate under a trading name different from its registered legal name.
- The vacancy may have been distributed directly or through a job platform rather than a careers page.
- The SPF diagnostic discrepancy may result from differences in lookup or evaluation context.

These alternatives have not been verified and do not remove the need for caution.

4. Overall Assessment

Classification: Suspicious recruitment email; suspected recruitment fraud or business impersonation.

Disposition: Open — further verification required.

The combination of a very recently registered domain, an unverified vacancy and business identity, and requests for sensitive documents and a paid screening service warrants heightened caution.

The available evidence does not conclusively establish malicious intent or prove that the sender is impersonating a legitimate organisation.

5. Recommended Response

- Do not pay the proposed screening fee while the provider and hiring process remain unverified.
- Do not send sensitive identity documents to the unverified sender.
- Preserve the original email and full headers privately.
- Seek confirmation through independently obtained business contact details.
- Update the case if reliable evidence confirms or refutes the recruiter's affiliation.

6. Analyst Learning Points

1. Email authentication and organisational legitimacy are separate questions.
2. Domain age is a risk indicator, not a verdict.
3. Negative search results must be documented with their scope and limitations.
4. Findings should distinguish observed facts, analytical interpretations and unresolved hypotheses.
5. A defensible case report should remain open when evidence is insufficient for a final conclusion.