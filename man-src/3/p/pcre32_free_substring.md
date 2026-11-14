---
title: "pcre32_free_substring(3)"
name: "pcre32_free_substring"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_free_substring/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
void pcre_free_substring(const char *stringptr);
void pcre16_free_substring(PCRE_SPTR16 stringptr);
void pcre32_free_substring(PCRE_SPTR32 stringptr);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for freeing the store obtained by a previous call to <code>pcre[16|32]_get_substring()</code> or <code>pcre[16|32]_get_named_substring()</code>. Its only argument is a pointer to the string. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
