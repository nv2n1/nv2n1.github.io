---
title: "pcre2_get_startchar(3)"
name: "pcre2_get_startchar"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_get_startchar/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>PCRE2_SIZE pcre2_get_startchar(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Description</h2>
<p>After a successful call of <code>pcre2_match()</code> that was passed the match block that is this function&#8217;s argument, this function returns the code unit offset of the character at which the successful match started. For a non-partial match, this can be different to the value of <i>ovector[0]</i> if the pattern contains the \K escape sequence. After a partial match, however, this value is always the same as <i>ovector[0]</i> because \K does not affect the result of a partial match. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
