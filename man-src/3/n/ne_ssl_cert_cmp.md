---
title: "ne_ssl_cert_cmp(3)"
name: "ne_ssl_cert_cmp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_cert_cmp/"
description: "ne_ssl_cert_cmp, ne_ssl_cert_free – functions to operate on certificate objects"
---

<p>ne_ssl_cert_cmp, ne_ssl_cert_free &#8211; functions to operate on certificate objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_header.h&gt;

int ne_ssl_cert_cmp(const ne_ssl_certificate *c1, const ne_ssl_certificate *c2);

void ne_ssl_cert_free(ne_ssl_certificate *cert);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_ssl_cert_cmp</code> function can be used to compare two certificate objects; it returns zero if they refer to the same certificate, and non-zero otherwise. </p>
<p> The <code>ne_ssl_cert_free</code> function can be used to destroy a certificate object when it is no longer needed.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
