---
title: "pcre2_substring_nametable_scan(3)"
name: "pcre2_substring_nametable_scan"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_nametable_scan/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_nametable_scan(const pcre2_code *code,
                                   PCRE2_SPTR name, PCRE2_SPTR *first, PCRE2_SPTR *last);</code></pre>
<h2>Description</h2>
<p>This convenience function finds, for a compiled pattern, the first and last entries for a given name in the table that translates capture group names into numbers.  When the name is found in the table, if <i>first</i> is NULL, the function returns a group number, but if there is more than one matching entry, it is not defined which one. Otherwise, when both pointers have been set, the yield of the function is the length of each entry in code units. If the name is not found, PCRE2_ERROR_NOSUBSTRING is returned. There is a complete description of the PCRE2 native API, including the format of the table entries, in the <code>pcre2api</code> page, and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
