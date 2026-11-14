---
title: "clamav-milter(8)"
name: "clamav-milter"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clamav-milter/"
description: "clamav-milter – milter compatible mail scanner"
---

<p>clamav-milter &#8211; milter compatible mail scanner</p>
<h2>Synopsis</h2>
<p>clamav-milter [options]</p>
<h2>Description</h2>
<p>Clamav-milter is a filter for <code><a href="/docs/linux/man/1-sendmail/">sendmail</a>(1)</code> mail server. It uses a mail scanning engine built into <code><a href="/docs/linux/man/8-clamd/">clamd</a>(8)</code>. </p>
<p> Clamav-milter can use load balancing and fault tolerant techniques to connect to more than one <a href="/docs/linux/man/8-clamd/">clamd</a>(8) server and seamlessly hot-swap to even the load between different machines and to keep scanning for viruses even when a server goes down.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Output help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the version number and exit.</p>
<dt><code>-c FILE, &#8211;config-file=FILE</code></p>
<dd>Read configuration from FILE.</dl>
<h2>Files</h2>
<p>/etc/clamav-milter.conf</p>
<h2>Author</h2>
<p>aCaB &lt;acab [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8), <a href="/docs/linux/man/5-clamav-milter-conf/">clamav-milter.conf</a>(5), <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5) </p>
