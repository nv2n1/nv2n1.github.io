---
title: "pcre2_maketables_free(3)"
name: "pcre2_maketables_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_maketables_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_maketables_free(pcre2_general_context *gcontext,
                           const uint8_t *tables);</code></pre>
<h2>Description</h2>
<p>This function discards a set of character tables that were created by a call to <code>pcre2_maketables()</code>. The <i>gcontext</i> parameter should match what was used in that call to account for any custom allocators that might be in use; if it is NULL the system <code>free()</code> is used. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page. </p>
