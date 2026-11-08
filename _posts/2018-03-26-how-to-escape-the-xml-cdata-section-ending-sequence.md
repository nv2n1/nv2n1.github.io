---
title: "Handling `]]>` in XML CDATA Sections"
date: 2018-03-26 15:40:07 +0000
modified: 2026-04-12 16:52:44 +0000
author: "Q A"
layout: post
categories: [testing-devops]
canonical: /how-to-escape-the-xml-cdata-section-ending-sequence/
---

In XML, CDATA (Character Data) sections let you include text without worrying about XML special characters. Everything inside `<![CDATA[` and `]]>` is treated as literal text — no parsing, no entity references. This is useful for embedding code snippets, scripts, or any content with lots of `<`, `>`, or `&` characters.

The catch: you can’t include the sequence `]]>` inside a CDATA section because that’s what closes it. If your data contains `]]>`, the parser will terminate the CDATA early, breaking your XML.

## Splitting CDATA Sections

The standard workaround is to split the CDATA at the problem point:

``` xml
<![CDATA[some data ]]]]><![CDATA[> more data]]>
```

How this works:

1.  Close the first CDATA with `]]>`
2.  Add the problematic `>` character as a literal character outside CDATA
3.  Open a new CDATA section for the remaining content

The parser sees this as two consecutive CDATA sections with a single `>` between them, which concatenates to your original `]]>` sequence.

## Practical Example

If you’re storing JavaScript or code that contains `]]>`:

``` xml
<script>
<![CDATA[
function test() {
  var arr = [1, 2, 3];
  console.log(arr);
  // Comment with ]]
]]><![CDATA[> in it
}
]]>
</script>
```

## Better Approaches for 2026

**Use a library, not manual XML generation.** This is the real 2026 best practice. Manually constructing XML is error-prone and creates injection vulnerabilities.

**Python with lxml:**

``` python
from lxml import etree

root = etree.Element("data")
element = etree.SubElement(root, "content")
element.text = "some data ]]> more data"  # Library handles escaping

xml_string = etree.tostring(root, pretty_print=True, encoding='unicode')
print(xml_string)
```

The library automatically escapes or encodes the problematic sequence for you.

**Java with JAXB:**

``` java
import javax.xml.bind.JAXBContext;
import javax.xml.bind.Marshaller;

@XmlRootElement
public class Data {
    @XmlElement
    public String content = "some data ]]> more data";
}

JAXBContext context = JAXBContext.newInstance(Data.class);
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(new Data(), System.out);
```

Again, the marshaller handles the encoding transparently.

**Go with encoding/xml:**

``` go
package main

import (
    "encoding/xml"
    "fmt"
)

type Data struct {
    Content string `xml:"content"`
}

d := Data{Content: "some data ]]> more data"}
b, _ := xml.MarshalIndent(d, "", "  ")
fmt.Println(string(b))
```

## When Manual Splitting Is Still Needed

If you absolutely must hand-craft XML (legacy systems, template generation), the CDATA splitting technique works, but be extra careful:

- Validate your XML with `xmllint` or similar tools
- Test edge cases like multiple `]]>` sequences in the same data
- Consider whether escaping instead of CDATA is simpler

``` bash
xmllint --format --noout your_file.xml
```

## Context: Why This Matters Less Now

XML remains entrenched in enterprise environments (SOAP APIs, SVG, Office Open XML), but for new projects, JSON dominates. If you’re designing a new API or configuration format, JSON’s simplicity avoids these escaping headaches entirely.

That said, when you do encounter XML, using a parser library is non-negotiable. Hand-rolled XML parsing and generation is a security risk and rarely necessary with modern tools.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Handling \`\]\]\>\` in XML CDATA Sections with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Handling \`\]\]\>\` in XML CDATA Sections. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
