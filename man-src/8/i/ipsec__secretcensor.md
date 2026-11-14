---
title: "ipsec__secretcensor(8)"
name: "ipsec__secretcensor"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec__secretcensor/"
description: "ipsec__secretcensor – internal routing to sanitize files"
---

<p>ipsec__secretcensor &#8211; internal routing to sanitize files</p>
<h2>Description</h2>
<p><i>_secretcensor</i> is called by <code>ipsec barf</code> to process the /etc/ipsec.secrets file to remove the private key components from the file prior to revealing the contents.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_barf/">ipsec_barf</a></code>(8).</p>
<h2>History</h2>
<p>Man page written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael Richardson. Original program by Henry Spencer.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
