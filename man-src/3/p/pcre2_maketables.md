---
title: "pcre2_maketables(3)"
name: "pcre2_maketables"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_maketables/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
const uint8_t *pcre2_maketables(pcre2_general_context *gcontext);</code></pre>
<h2>Description</h2>
<p>This function builds a set of character tables for character code points that are less than 256. These can be passed to <code>pcre2_compile()</code> in a compile context in order to override the internal, built-in tables (which were either defaulted or made by <code>pcre2_maketables()</code> when PCRE2 was compiled). See the <code>pcre2_set_character_tables()</code> page. You might want to do this if you are using a non-standard locale. If the argument is NULL, <code>malloc()</code> is used to get memory for the tables. Otherwise it must point to a general context, which can supply pointers to a custom memory manager. The function yields a pointer to the tables. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
