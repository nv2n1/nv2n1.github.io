---
title: "pcre2_substring_length_bynumber(3)"
name: "pcre2_substring_length_bynumber"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_length_bynumber/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_length_bynumber(pcre2_match_data *match_data,
                                    uint32_t number, PCRE2_SIZE *length);</code></pre>
<h2>Description</h2>
<p>This function returns the length of a matched substring, identified by number. The arguments are:  The third argument may be NULL if all you want to know is whether or not a substring is set. The yield is zero on success, or a negative error code otherwise. After a partial match, only substring 0 is available. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
