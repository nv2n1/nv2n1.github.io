---
title: "Email Authentication Fundamentals: SPF, DKIM, and DMARC Explained"
date: 2021-10-30 16:17:04 +0000
author: "David Yang"
layout: post
categories: [systems-architecture]
canonical: /setting-up-spf-dkim-and-dmarc-for-domain-to-stop-email-sender-fraud/
---

Email sender fraud remains a persistent problem in email infrastructure. Attackers send messages spoofing legitimate domains, damaging sender reputation and causing rejected mail that creates administrative overhead. SPF, DKIM, and DMARC are DNS-based authentication standards designed to verify email senders and prevent domain spoofing.

## Sender Policy Framework (SPF)

Sender Policy Framework (SPF) is a DNS-based authentication method that lets receiving mail servers verify an email originates from an authorized sender for that domain. An SPF record is a TXT record in your domain’s DNS containing a policy that lists which IP addresses or mail servers are authorized to send email on behalf of your domain.

When a receiving mail server processes an incoming email, it:

1.  Looks up the SPF record for the sender’s domain via DNS query
2.  Extracts the sender’s IP address
3.  Compares that IP against the authorized IPs listed in the SPF record
4.  Accepts, rejects, or flags the email based on the match result

SPF is defined in RFC 7208.

**SPF Record Example:**

    v=spf1 ip4:192.0.2.0 include:_spf.google.com ~all

The `v=spf1` tag denotes the version. Common mechanisms include:

- `ip4:` or `ip6:` — authorizes specific IP addresses
- `include:` — references another domain’s SPF record
- `a:`, `mx:` — authorizes servers listed in A or MX records
- `+all` — accept all (rarely used, insecure)
- `~all` — soft-fail unauthorized senders (default)
- `-all` — hard-fail unauthorized senders (strictest)

Mail hosting providers typically supply SPF records for their customers. Query your domain with:

``` bash
dig -t TXT yourdomain.com +short | grep spf
```

## DomainKeys Identified Mail (DKIM)

DomainKeys Identified Mail (DKIM) uses public-key cryptography to digitally sign emails. The receiving server verifies the signature against the sender’s public key published in DNS, ensuring the message wasn’t forged or modified in transit.

DKIM setup requires:

1.  Domain owner publishes a public cryptographic key as a TXT record in a subdomain
2.  Outbound mail server adds a digital signature (using the private key) to email headers
3.  Receiving server retrieves the public key from DNS and verifies the signature

The DNS record lives in a subdomain using the format `<selector>._domainkey.yourdomain.com`, where the selector is a label identifying the key pair (e.g., `default`, `mail`, `2024`).

DKIM is defined in RFC 6376.

**DKIM Record Example:**

``` bash
dig -t TXT default._domainkey.yourdomain.com +short
```

Returns:

    v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBxxxxxxxxxx

The fields mean:

- `v=DKIM1` — DKIM version
- `k=rsa` — key type (RSA is standard; ed25519 support is growing)
- `p=` — the public key (base64-encoded)
- `t=s` (optional) — test mode flag
- `t=y` (optional) — domain owner’s assertion of DKIM deployment

Mail hosting providers generate and manage DKIM keys. You typically paste the public key into your DNS; the provider keeps the private key on their mail servers.

## Domain-based Message Authentication, Reporting & Conformance (DMARC)

DMARC is a policy framework that combines SPF and DKIM results and instructs receiving servers how to handle authentication failures. It also enables aggregate and forensic reporting on email authentication.

DMARC records are TXT records in the `_dmarc` subdomain of your domain.

DMARC is defined in RFC 7489.

**DMARC Record Example:**

    v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com; ruf=mailto:forensics@yourdomain.com; fo=1; pct=100

**DMARC Record Fields:**

- `v=DMARC1` — DMARC version (required)
- `p=` — policy for failed authentication (required)
  - `none` — monitor only, no action
  - `quarantine` — route to spam folder
  - `reject` — refuse delivery
- `sp=` — subdomain policy (optional; overrides `p=` for subdomains)
- `rua=` — aggregate report recipient email (recommended)
- `ruf=` — forensic report recipient email (optional; verbose, high volume)
- `fo=` — forensic reporting options (0=default, 1=all, d=dkim-only, s=spf-only)
- `pct=100` — percentage of mail to apply the policy to (useful for gradual rollout; start at 10-20%, increase to 100)
- `adkim=r` — DKIM alignment mode (r=relaxed, s=strict; relaxed is default)
- `aspf=r` — SPF alignment mode (relaxed vs. strict)

Query your domain:

``` bash
dig -t TXT _dmarc.yourdomain.com +short
```

## Implementation Best Practices

**Start with SPF and DKIM first.** Both are easier to deploy and have higher adoption. SPF is straightforward if your email provider supplies records. DKIM requires generating keys, but providers handle this.

**Roll out DMARC gradually.** Begin with `p=none` to collect data, then move to `p=quarantine` when confident, then `p=reject`. Use `pct=` to apply policies to a percentage of mail during testing.

**Monitor reports.** Set up aggregate report recipients (`rua=`) to track authentication success rates. Forensic reports (`ruf=`) are more verbose; use them only if needed for debugging.

**Align identifiers.** DMARC checks alignment between the “From” header domain and SPF/DKIM domains. Subdomains may fail alignment; use `sp=` to set different policies.

**Use strict rejection cautiously.** `p=reject` is powerful but risky. Legitimate mail might fail alignment or pass neither SPF nor DKIM. Confirm infrastructure is solid before deploying.

**Validate DNS records:**

``` bash
# Check SPF
dig -t TXT yourdomain.com +short

# Check DKIM (replace 'default' with your selector)
dig -t TXT default._domainkey.yourdomain.com +short

# Check DMARC
dig -t TXT _dmarc.yourdomain.com +short
```

**Tools for testing:**

- Use `nslookup`, `dig`, or online DMARC/SPF validators to confirm records are published
- Send test emails to check headers for authentication results (look for `Authentication-Results:` headers)
- Deploy SPF, DKIM, and DMARC together for maximum protection against spoofing and phishing
