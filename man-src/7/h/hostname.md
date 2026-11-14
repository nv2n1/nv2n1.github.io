---
title: "hostname(7)"
name: "hostname"
section: "7"
letter: "h"
url: "/docs/linux/man/7-hostname/"
description: "hostname – hostname resolution description"
---

<p>hostname &#8211; hostname resolution description</p>
<h2>Description</h2>
<p>Hostnames are domains, where a domain is a hierarchical, dot-separated list of subdomains; for example, the machine &quot;monet&quot;, in the &quot;example&quot; subdomain of the &quot;com&quot; domain would be represented as &quot;monet.example.com&quot;. </p>
<p> Each element of the hostname must be from 1 to 63 characters long and the entire hostname, including the dots, can be at most 253 characters long. Valid characters for hostnames are <code><a href="/docs/linux/man/7-ascii/">ASCII</a></code>(7) letters from <i>a</i> to <i>z</i>, the digits from <i>0</i> to <i>9</i>, and the hyphen (-). A hostname may not start with a hyphen. </p>
<p> Hostnames are often used with network client and server programs, which must generally translate the name to an address for use. (This task is generally performed by either <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) or the obsolete <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3).) </p>
<p> Hostnames are resolved by the NSS framework in glibc according to the <code>hosts</code> configuration in <code>nsswitch.conf</code>. The DNS-based name resolver (in the <code>dns</code> NSS service module) resolves them in the following fashion. </p>
<p> If the name consists of a single component, that is, contains no dot, and if the environment variable <code>HOSTALIASES</code> is set to the name of a file, that file is searched for any string matching the input hostname. The file should consist of lines made up of two white-space separated strings, the first of which is the hostname alias, and the second of which is the complete hostname to be substituted for that alias. If a case-insensitive match is found between the hostname to be resolved and the first field of a line in the file, the substituted name is looked up with no further processing. </p>
<p> If the input name ends with a trailing dot, the trailing dot is removed, and the remaining name is looked up with no further processing. </p>
<p> If the input name does not end with a trailing dot, it is looked up by searching through a list of domains until a match is found. The default search list includes first the local domain, then its parent domains with at least 2 name components (longest first). For example, in the domain cs.example.com, the name lithium.cchem will be checked first as lithium.cchem.cs.example and then as lithium.cchem.example.com. lithium.cchem.com will not be tried, as there is only one component remaining from the local domain. The search path can be changed from the default by a system-wide configuration file (see <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5)).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5), <code><a href="/docs/linux/man/7-mailaddr/">mailaddr</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8) </p>
<p> IETF RFC 1123 </p>
<p> IETF RFC 1178</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
