---
title: "pcre2_match_data_create_from_pattern(3)"
name: "pcre2_match_data_create_from_pattern"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_match_data_create_from_pattern/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_match_data *pcre2_match_data_create_from_pattern(</code>
<code> const pcre2_code *</code><i>code</i>, pcre2_general_context *<i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function creates a new match data block, which is used for holding the result of a match. The first argument points to a compiled pattern. The number of capturing parentheses within the pattern is used to compute the number of pairs of offsets that are required in the match data block. These form the &quot;output vector&quot; (ovector) within the match data block, and are used to identify the matched string and any captured substrings. The second argument points to a general context, for custom memory management, or is NULL to use the same memory allocator as was used for the compiled pattern. The result of the function is NULL if the memory for the block could not be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
