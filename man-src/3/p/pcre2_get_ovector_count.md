---
title: "pcre2_get_ovector_count(3)"
name: "pcre2_get_ovector_count"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_get_ovector_count/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>uint32_t pcre2_get_ovector_count(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Description</h2>
<p>This function returns the number of pairs of offsets in the ovector that forms part of the given match data block. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
