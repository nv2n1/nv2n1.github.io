---
title: "When should the authors anonymize themselves in a paper submitted to a conference for review?"
date: 2018-03-24 11:45:09 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/when-should-the-authors-anonymize-themselves-in-a-paper-submitted-to-a-conference-for-review/
---

<div class="qa-question">

</div>

When should the authors anonymize themselves in a paper submitted to a conference for review?

<div class="qa-answer">

</div>

**Several general concepts**:

- **Peer review** is the evaluation of work by one or more people of similar competence to the producers of the work (peers). — <a href="https://en.wikipedia.org/wiki/Peer_review" rel="nofollow noopener" target="_blank">Wikipedia</a>

- **Single-blind** describes experiments where information that could introduce bias or otherwise skew the result is withheld from the participants, but the experimenter will be in full possession of the facts.

- **Double-blind** describes an especially stringent way of conducting an experiment which attempts to eliminate subjective, unrecognized biases carried by an experiment’s subjects (usually human) and conductors. — <a href="https://en.wikipedia.org/wiki/Blind_experiment" rel="nofollow noopener" target="_blank">Wikipedia</a>

**In summary**, “peer reviewed” means that your paper will be reviewed by one ore more reviewers before being accepted/published. If the peer review process is single-blind or double-blind, you should anonymize yourselves.

How and what to anonymize for papers depends on the conference/journal’s requirement. For a general reference, you may take a look at the Section “Anonymizing rules” of SOSP 2013’s <a href="https://web.archive.org/web/20180122124058/http://sigops.org:80/sosp/sosp13/submission.html" rel="nofollow noopener" target="_blank">“Submission Guidelines”</a>:

> As an author, you should not identify yourself in the paper either explicitly or by implication (e.g., through the references or acknowledgments). However, only non-destructive anonymization is required. For example, system names may be left un-anonymized, if the system name is important for a reviewer to be able to evaluate the work.\
> …\
> Additionally, please take the following steps when preparing your submission:
>
> - Remove authors’ names and affiliations from the title page.
>
> - Remove acknowledgement of identifying names and funding sources.
>
> - Use care in naming your files. Source file names, e.g., Joe.Smith.dvi,\
>   are often embedded in the final output as readily accessible comments.
>
> - Use care in referring to related work, particularly your own. Do not\
>   omit references to provide anonymity, as this leaves the reviewer\
>   unable to grasp the context. Instead, a good solution is to reference\
>   your past work in the third person, just as you would any other piece\
>   of related work.
>
> - If you have a concurrent submission, reference it as follows: “Closely\
>   related work describes a microkernel implementation \[Anonymous 2013\].”\
>   with the corresponding citation: “\[Anonymous 2013\] Under submission.\
>   Details omitted for double-blind reviewing.”
>
> - Work that extends an author’s previous workshop paper is welcome, but\
>   authors should (a) acknowledge their own previous workshop\
>   publications with an anonymous citation and (b) explain the\
>   differences between the SOSP submission and the prior workshop paper.
>
> - If you cite anonymous work, you must also send the deanonymized\
>   reference(s) to the PC chair in a separate email.
>
> We recognize that, even following these guidelines, closely building\
> on your own prior work may indirectly reveal your identity. Even\
> though a reviewer might think they can guess which group you are from,\
> s/he should have some doubts.

## 2026 Best Practices and Advanced Techniques

For When should the authors anonymize themselves in a paper submitted to a conference for review?, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
