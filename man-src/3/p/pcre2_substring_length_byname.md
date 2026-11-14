---
title: "pcre2_substring_length_byname(3)"
name: "pcre2_substring_length_byname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_length_byname/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_length_byname(pcre2_match_data *match_data,
                                  PCRE2_SPTR name, PCRE2_SIZE *length);</code></pre>
<h2>Description</h2>
<p>This function returns the length of a matched substring, identified by name. The arguments are:  The yield is zero on success, or an error code if the substring is not found. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
