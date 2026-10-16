Phishing Email Investigation Report

1. Case Information

- Case ID: PHISH-001
- Investigation type: Suspected phishing email
- Environment: Synthetic training environment
- Status: Initial investigation completed
- Classification: Likely phishing
- Severity: Medium — provisional, pending impact assessment

2. Executive Summary

A synthetic email impersonating a Microsoft 365 security notification was analysed using a basic Python indicator-detection script.

The message contained a suspicious sender domain, urgency-based wording and a link requesting account verification. The script identified all three configured indicators.

The available evidence supports a likely phishing classification within this training scenario. No real phishing infrastructure, credential theft or account compromise has been established.

3. Evidence and Findings

Finding 1: Possible Brand Impersonation

The sender address uses the domain "micros0ft-example.invalid", substituting a zero for the letter "o" in the brand name.

Assessment: Suspicious domain construction consistent with an impersonation technique.

Finding 2: Urgency and Pressure

The message warns that the mailbox will be suspended within 24 hours unless the recipient verifies the account.

Assessment: The wording pressures the recipient to act quickly and may discourage independent verification.

Finding 3: Verification Link

The email contains a link to "login.micros0ft-example.invalid/verify".

Assessment: The URL uses the same suspicious domain pattern and requests account verification. It should not be visited during this exercise.

4. Analysis and Validation

The Python script was executed in Google Colab against the synthetic email sample.

- Email sample loaded successfully.
- Analysis script executed successfully.
- Three configured indicators were reported.
- Three automated unit tests executed successfully.
- The tests covered indicator detection, a clean-message scenario and case-insensitive matching.

These results validate the behaviour of the prototype against the tested inputs. They do not establish the accuracy of a production phishing detection system.

5. Impact Assessment

No actual recipient interaction, credential submission, malicious payload execution or account compromise was observed.

The sample uses the reserved ".invalid" domain, confirming that it is a training artefact rather than evidence of a live phishing site.

Actual business impact cannot be established from this sample.

6. Recommended Response

For a comparable real-world alert, an analyst should:

1. Preserve the original email and full message headers.
2. Review SPF, DKIM and DMARC authentication results.
3. Investigate sender and URL indicators using approved security tools.
4. Determine whether the recipient clicked the link or submitted credentials.
5. Search for related messages and affected users.
6. Escalate confirmed malicious activity according to incident response procedures.
 
7. Limitations

- Synthetic email content only.
- No real email headers or authentication results supplied.
- No external URL reputation checks performed.
- No live mail gateway or SIEM integration.
- Detection logic uses simple string matching and may produce false positives or false negatives.

8. Conclusion

The training email exhibits multiple phishing indicators. The Python prototype successfully identified the configured patterns, and its three automated tests passed.

The case is documented as likely phishing within the synthetic scenario. Further evidence would be required to make a definitive determination in a real investigation.

Automated Testing

The Python email analyser was tested against four automated test cases.

Test| Result
Clean message returns no indicators| PASS
Suspicious sender without other indicators| PASS
Detection of three phishing indicators| PASS
Case-insensitive indicator matching| PASS

Total: 4 passed, 0 failed.

Scope limitation: These tests validate the analyser against controlled synthetic inputs. They do not establish that every phishing email will be detected or confirm that a real-world email is malicious.