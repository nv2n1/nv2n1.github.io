---
title: "pcre32_maketables(3)"
name: "pcre32_maketables"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_maketables/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
const unsigned char *pcre_maketables(void);
const unsigned char *pcre16_maketables(void);
const unsigned char *pcre32_maketables(void);</code></pre>
<h2>Description</h2>
<p>This function builds a set of character tables for character values less than 256. These can be passed to <code>pcre[16|32]_compile()</code> to override PCRE&#8217;s internal, built-in tables (which were made by <code>pcre[16|32]_maketables()</code> when PCRE was compiled). You might want to do this if you are using a non-standard locale. The function yields a pointer to the tables. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
