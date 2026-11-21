---

title: "axfrdns(8)"
name: "axfrdns"
section: "8"
letter: "a"
url: "/docs/linux/man/8-axfrdns/"
---

<dl>
<dt><code>axfrdns</code> [OPTIONS]</dt>
<dd>
<h2>Description</h2>
<p><code>axfrdns</code> is a zone transfer server. It reads a zone transfer request in DNS-over-TCP format from its standard input and responds with a locally configured information. <code>axfrdns</code> looks up zone-transfer results in data.cdb, a binary file created by <a href="/docs/linux/man/1-tinydns-data/">tinydns-data</a>(1). It also responds to normal client queries such as SOA queries, which usually precede zone transfer requests. <code>axfrdns</code> allows zone transfer for any zone listed in the $AXFR variable. AXFR is a slash separated list of domain names. If AXFR is not set, <code>axfrdns</code> allows zone transfer for all zone available in data.cdb. </p>
<h2>Options</h2>
</dd><dl>
<dt><code>-d &lt;value&gt;</code></dt>
<dd>&nbsp;<wbr>print debug messages</dd>
<dt><code>-D</code></dt>
<dd>&nbsp;<wbr>run as daemon</dd>
<dt><code>-h &#8211;help</code></dt>
<dd>&nbsp;<wbr>print this help</dd>
<dt><code>-v &#8211;version</code></dt>
<dd>&nbsp;<wbr>print version information </dd>
</dl>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/axfrdns.conf</p>
<h2>See</h2>
<p><a rel="nofollow" href="http://cr.yp.to/djbdns/axfrdns.html">http://cr.yp.to/djbdns/axfrdns.html</a></p>
<h2>Bugs</h2>
<p>Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Manual Author</h2>
<p>Prasad J Pandit</p>
</dl>