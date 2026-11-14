---
title: "ods-signer(8)"
name: "ods-signer"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ods-signer/"
description: "ods-signer – OpenDNSSEC Signer Engine client"
---

<p><code>ods-signer </code> &#8211; OpenDNSSEC Signer Engine client </p>
<h2>Synopsis</h2>
<p><code>ods-signer</code> [<code>-h</code>] <i>clear </i> <i>&lt;zone&gt;</i> | <i>flush</i> | <i>queue</i> | <i>reload</i> | <i>running</i> | <i>sign </i> <i>&lt;zone&gt;</i>[<i>&#8211;serial</i>&lt;number&gt;<i>]</i> | <i>sign &#8211;all </i> | <i>start</i> | <i>stop</i> | <i>update</i> [<code>&#8211;all</code>] | <i>update</i> <i>&lt;zone&gt;</i> | <i>retransfer</i> <i>&lt;zone&gt;</i> | <i>verbosity</i> <i>&lt;number&gt;</i> | <i>zones</i> </p>
<h2>Description</h2>
<p>ods-signer is part of the OpenDNSSEC software. With this tool, you can send commands to the signer engine daemon. For more information, go to <code><a rel="nofollow" href="http://www.opendnssec.org">http://www.opendnssec.org</a></code> and visit the Documentation page. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show this help.</dl>
<h2>Diagnostics</h2>
<p>will log all the problems via stderr.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/1-ods-ksmutil/">ods-ksmutil</a>(1), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>Authors</h2>
<p><code>ods-signer</code> was written by NLnet Labs as part of the OpenDNSSEC project.</p>
