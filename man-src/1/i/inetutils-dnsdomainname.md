---

title: "inetutils-dnsdomainname(1)"
name: "inetutils-dnsdomainname"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inetutils-dnsdomainname/"
description: "dnsdomainname – show DNS domain name"
---

<p>GNU Network Utilities</p>

<p> <code>dnsdomainname</code> &#8211; show DNS domain name </p>
<h2>SYNOPSIS</h2>
<p> <code>dnsdomainname</code> [<i>option &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Show the domain part of the system&#8217;s fully qualified host name. </p>
<p> The tool uses <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) to get the host name of the system and getaddrinfo(2) to resolve it into a canonical name. The part after the first period (`.&#8217; ) of the canonical name is shown.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-? , -help</code></dt>
<dd> Give this help list.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give a short usage message.</dd>
<dt><code>-V , -version</code></dt>
<dd> Print program version.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2), <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3) </p>
