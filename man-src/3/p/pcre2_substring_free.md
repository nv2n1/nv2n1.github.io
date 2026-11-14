---
title: "pcre2_substring_free(3)"
name: "pcre2_substring_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_substring_free(PCRE2_UCHAR *buffer);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for freeing the memory obtained by a previous call to <code>pcre2_substring_get_byname()</code> or <code>pcre2_substring_get_bynumber()</code>. Its only argument is a pointer to the string. If the argument is NULL, the function does nothing. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
