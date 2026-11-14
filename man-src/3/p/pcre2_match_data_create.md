---
title: "pcre2_match_data_create(3)"
name: "pcre2_match_data_create"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_match_data_create/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_match_data *pcre2_match_data_create(uint32_t </code><i>ovecsize</i>,
<code> pcre2_general_context *</code><i>gcontext</i>);</pre>
<h2>Description</h2>
<p>This function creates a new match data block, which is used for holding the result of a match. The first argument specifies the number of pairs of offsets that are required. These form the &quot;output vector&quot; (ovector) within the match data block, and are used to identify the matched string and any captured substrings. There is always one pair of offsets; if <code>ovecsize</code> is zero, it is treated as one. The second argument points to a general context, for custom memory management, or is NULL for system memory management. The result of the function is NULL if the memory for the block could not be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
