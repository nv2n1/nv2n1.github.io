---
title: "pcre16_version(3)"
name: "pcre16_version"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_version/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
const char *pcre_version(void);
const char *pcre16_version(void);
const char *pcre32_version(void);</code></pre>
<h2>Description</h2>
<p>This function (even in the 16-bit and 32-bit libraries) returns a zero-terminated, 8-bit character string that gives the version number of the PCRE library and the date of its release. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
