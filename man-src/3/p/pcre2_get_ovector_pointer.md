---
title: "pcre2_get_ovector_pointer(3)"
name: "pcre2_get_ovector_pointer"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_get_ovector_pointer/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>PCRE2_SIZE *pcre2_get_ovector_pointer(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Description</h2>
<p>This function returns a pointer to the vector of offsets that forms part of the given match data block. The number of pairs can be found by calling <code>pcre2_get_ovector_count()</code>. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
