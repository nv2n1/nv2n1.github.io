---
title: "ipv6logconv(8)"
name: "ipv6logconv"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipv6logconv/"
description: "ipv6logconv – HTTP server log file converter for statistics"
---

<p>ipv6logconv &#8211; HTTP server log file converter for statistics</p>
<h2>Synopsis</h2>
<p>cat /var/log/httpd/access_log | <code>ipv6logconv</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>This program converts IPv4/IPv6 addresses in HTTP server log files </p>
<p> The converted output can be used to create statistics with analog </p>
<p> Takes data from stdin, proceed it to stdout</p>
<h2>Options</h2>
<p>General options:</p>
<dl>
<dt><code>[-d|&#8211;debug </code><i>DEBUGVALUE</i><code>]</code></dt>
<dd>debug value (bitwise like) can also be set by IPV6CALC_DEBUG environment value</dd>
<dt><code>[-v|&#8211;version [-v [-v]]]</code></dt>
<dd>version information (2 optional detail levels)</dd>
<dt><code>[-v|&#8211;version -h]</code></dt>
<dd>explanation of feature tokens</dd>
<dt><code>[-V|&#8211;verbose]</code></dt>
<dd>be more verbose</dd>
<dt><code>[-h|&#8211;help|-?]</code></dt>
<dd>this online help</dd></dl>
<p> Performance options:</p>
<dl>
<dt><code>[-n|&#8211;nocache]</code></dt>
<dd>disable caching</dd>
<dt><code>[-c|&#8211;cachelimit </code><i>VALUE</i><code>]</code></dt>
<dd>set cache limit; default: <code>20</code>, maximum: <code>200</code>.</dd></dl>
<p> Output options:</p>
<dl>
<dt><code>[&#8211;out </code><i>OUTPUTTYPE</i><code>]</code></dt>
<dd>Specify output type:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>addrtype</code></dt>
<dd>Address type</dd>
<dt><code>ouitype</code></dt>
<dd>OUI (IEEE) type</dd>
<dt><code>ipv6addrtype</code></dt>
<dd>IPv6 address type</dd>
<dt><code>any</code></dt>
<dd>any type</dd></dl>
</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipv6calc/">ipv6calc</a>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;ipv6calc [at] lists.deepspace6.net&gt; or to the authors. </p>
<p> Homepage: <a rel="nofollow" href="http://www.deepspace6.net/projects/ipv6calc.html">http://www.deepspace6.net/projects/ipv6calc.html</a></p>
<h2>License</h2>
<p>GPLv2</p>
<h2>Authors</h2>
<p>Peter Bieringer &lt;pb [at] bieringer.de&gt;</p>
