---
title: "axfr-get(1)"
name: "axfr-get"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axfr-get/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>axfr-get</code> [OPTIONS] &lt;DOMAIN-NAME&gt; &lt;OUTFILE&gt; &lt;OUTFILE.TMP&gt;</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>axfr-get</code> is a DNS zone transfer client. It sends a zone transfer request in DNS-over-TCP format to descriptor 7, reads the result from descriptor 6 and saves the result in a file. </p>
<p> <code>axfr-get</code> performs the zone transfer for the given domain, and writes the result to file &#8211; OUTFILE.TMP in a format that can be used as input to <a href="/docs/linux/man/1-tinydns-data/">tinydns-data</a>(1). If the zone transfer completes successfully, axfr-get renames OUTFILE.TMP to OUTFILE. </p>
<h2>SEE</h2>
<p> <a rel="nofollow" href="http://cr.yp.to/djbdns/axfr-get.html">http://cr.yp.to/djbdns/axfr-get.html</a> </p>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Manual Author</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
