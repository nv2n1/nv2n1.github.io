---
title: "ods-signerd(8)"
name: "ods-signerd"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ods-signerd/"
description: "ods-signerd – OpenDNSSEC Signer Engine daemon"
---

<p><code>ods-signerd</code> &#8211; OpenDNSSEC Signer Engine daemon</p>
<h2>Synopsis</h2>
<p><code>ods-signerd</code> [<code>-1</code>] [<code>-c</code> <i>FILE</i>] [<code>-d</code>] [<code>-h</code>] [<code>-i</code>] [<code>-v</code>] [<code>-V</code>] </p>
<h2>Description</h2>
<p>ods-signerd is part of the OpenDNSSEC software. It will keep your DNS zones continuous signed. For more information, go to <code><a rel="nofollow" href="http://www.opendnssec.org">http://www.opendnssec.org</a></code> and visit the Documentation page. </p>
<h2>Options</h2>
<dl>
<dt><code>-1</code></p>
<dd>Run signer engine once, then exit (for debugging purposes).</p>
<dt><code>-c</code><i> FILE</i></p>
<dd>Read configuration from file, instead of using the default.</p>
<dt><code>-d</code></p>
<dd>Run daemon in foreground.</p>
<dt><code>-h</code></p>
<dd>Show this help.</p>
<dt><code>-i</code></p>
<dd>Print configuration and exit (for debugging purposes).</p>
<dt><code>-v</code></p>
<dd>Increase verbosity.</p>
<dt><code>-V</code></p>
<dd>Show version and exit.</dl>
<h2>Diagnostics</h2>
<p>will log all the problems via standard <a href="/docs/linux/man/8-syslog/">syslog</a>(8).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>ods-signerd</code> was written by NLnet Labs as part of the OpenDNSSEC project.</p>
