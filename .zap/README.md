# ZAP DAST Scan Configuration

This directory contains configuration for the OWASP ZAP Dynamic Application Security Testing (DAST) scan that runs as part of our CI/CD pipeline.

## Overview

The `rules.tsv` file customizes how the ZAP scanner behaves during security testing. It determines which security findings should:
- Fail the build (critical security issues)
- Generate warnings (moderate issues)
- Be ignored (low risk or false positives)

## How It Works

### File Format

The `rules.tsv` file uses a tab-separated format with three columns:
```
[Rule ID]    [Action]    [Description]
```

### Actions

- `FAIL`: Critical security issues that will cause the build to fail
- `WARN`: Moderate issues that generate warnings but don't fail the build
- `IGNORE`: Issues that will be suppressed in the scan results

### When Does It Run?

The ZAP scan runs automatically:
1. On every push to the main branch
2. The scan is executed as part of the GitHub Actions workflow (`.github/workflows/zap-scan.yml`)
3. The application is built and run in a Docker container
4. ZAP performs a full scan against the running application
5. Results are processed according to the rules in `rules.tsv`

## Current Rule Configuration

### Critical Issues (FAIL)
These vulnerabilities will cause the build to fail:
- Cross-Site Scripting (XSS) - both reflected and persistent
- SQL Injection vulnerabilities (Multiple database types)
- Cross-Site Request Forgery (CSRF)
- Padding Oracle attacks

### Warning Issues (WARN)
These generate warnings but don't fail the build:
- Application error disclosures
- Loosely scoped cookies

### Ignored Issues (IGNORE)
Low-risk or commonly false positive findings:
- Cookie flags (HttpOnly, Secure, SameSite)
- Security headers (X-Frame-Options, CSP, etc.)
- Cache control headers
- Debug error messages
- Version information disclosure
- Timestamp disclosures

## Customizing the Rules

To modify the scan behavior:
1. Edit the `rules.tsv` file
2. Change the action (FAIL/WARN/IGNORE) for existing rules
3. Add new rules following the same format
4. Remove rules you don't want to check

## Best Practices

1. **Review Failed Builds**: Always investigate failed security scans - they indicate potential vulnerabilities
2. **Warning Analysis**: Periodically review warnings to identify security improvements
3. **Rule Updates**: Update rules as your security requirements evolve
4. **False Positives**: Move rules to IGNORE only if you're confident they're false positives

## Troubleshooting

Common issues and solutions:
1. **Scan Timeouts**: The scan may timeout on large applications. Adjust the timeout in the GitHub Actions workflow if needed.
2. **False Positives**: If you consistently get false positives, consider moving the rule to IGNORE.
3. **Build Failures**: Check the ZAP scan logs in GitHub Actions for detailed information about failed security checks.

## Additional Resources

- [OWASP ZAP Documentation](https://www.zaproxy.org/docs/)
- [ZAP Rules Documentation](https://www.zaproxy.org/docs/alerts/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) 