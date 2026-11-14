---
title: "pcre2_set_character_tables(3)"
name: "pcre2_set_character_tables"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_set_character_tables/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_set_character_tables(pcre2_compile_context *ccontext,
                               const uint8_t *tables);</code></pre>
<h2>Description</h2>
<p>This function sets a pointer to custom character tables within a compile context. The second argument must be the result of a call to <code>pcre2_maketables()</code> or NULL to request the default tables. The result is always zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
