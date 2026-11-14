---
title: "pcre2_match_data_free(3)"
name: "pcre2_match_data_free"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_match_data_free/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
void pcre2_match_data_free(pcre2_match_data *match_data);</code></pre>
<h2>Description</h2>
<p>If <i>match_data</i> is NULL, this function does nothing. Otherwise, <i>match_data</i> must point to a match data block, which this function frees, using the memory freeing function from the general context or compiled pattern with which it was created, or <code>free()</code> if that was not set. If the PCRE2_COPY_MATCHED_SUBJECT was used for a successful match using this match data block, the copy of the subject that was remembered with the block is also freed. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
