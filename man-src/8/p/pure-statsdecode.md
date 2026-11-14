---
title: "pure-statsdecode(8)"
name: "pure-statsdecode"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-statsdecode/"
description: "pure-statsdecode – Show human-readable dates from a \"stats\" logfile"
---

<p>pure-statsdecode &#8211; Show human-readable dates from a &quot;stats&quot; logfile</p>
<h2>Syntax</h2>
<p>pure-statsdecode <i>filename</i><br />
 pure-statsdecode <i>&#8211;</i></p>
<h2>Description</h2>
<p>This program decodes Pure-FTPd&#8217;s &quot;stats&quot; log files and converts timestamps into human-readable dates. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd>means to read the standard input.</p>
<dt><code>filename</code></p>
<dd>is a log file produced with pure-ftpd -O ftpstats:/path/to/logfile</dl>
<h2>Examples</h2>
<p>To run this program the standard way type: pure-statsdecode /var/log/pureftpd.log &gt; /tmp/pureftpd.humanlog Alternativly you can run it as: cat /var/log/pureftpd.log | pure-statsdecode &#8211; | gzip &#8211;best &gt; /tmp/pureftpd.humanlog.gz </p>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2228,</code> <code>RFC 2389</code> and <code>RFC 2428</code>. </p>
