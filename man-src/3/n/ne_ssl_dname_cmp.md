---
title: "ne_ssl_dname_cmp(3)"
name: "ne_ssl_dname_cmp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_dname_cmp/"
description: "ne_ssl_readable_dname, ne_ssl_dname_cmp – SSL distinguished name handling"
---

<p>ne_ssl_readable_dname, ne_ssl_dname_cmp &#8211; SSL distinguished name handling</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_ssl.h&gt;

const char *ne_ssl_readable_dname(const ne_ssl_dname *dname);

int ne_ssl_dname_cmp(const ne_ssl_dname *dn1, const ne_ssl_dname *dn2);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_ssl_readable_dname</code> function creates a single-line, human-readable string out of an <code>ne_ssl_dname</code> object. The returned string is <code>malloc</code>()-allocated, and must be <code>free</code>()d by the caller. </p>
<p> The <code>ne_ssl_dname_cmp</code> function compares two distinguished names, and returns zero if they are equal, or non-zero otherwise.</p>
<h2>Return Value</h2>
<p><code>ne_ssl_readable_dname</code> returns a <code>malloc</code>-allocated string, and never NULL.</p>
<h2>Examples</h2>
<p>See ne_ssl_cert_subject for an example use of <code>ne_ssl_readable_dname</code>.</p>
<h2>See Also</h2>
<p>ne_ssl_cert_subject</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
