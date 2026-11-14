---
title: "pcre2_serialize_free(3)"
name: "pcre2_serialize_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_serialize_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_serialize_free(uint8_t *bytes);</code></pre>
<h2>Description</h2>
<p>This function frees the memory that was obtained by <code>pcre2_serialize_encode()</code> to hold a serialized byte stream. The argument must point to such a byte stream or be NULL, in which case the function returns without doing anything. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the serialization functions in the <code>pcre2serialize</code> page. </p>
