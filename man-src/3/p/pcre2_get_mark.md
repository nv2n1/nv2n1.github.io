---
title: "pcre2_get_mark(3)"
name: "pcre2_get_mark"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_get_mark/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>PCRE2_SPTR pcre2_get_mark(pcre2_match_data *</code><i>match_data</i>);</pre>
<h2>Description</h2>
<p>After a call of <code>pcre2_match()</code> that was passed the match block that is this function&#8217;s argument, this function returns a pointer to the last (*MARK), (*PRUNE), or (*THEN) name that was encountered during the matching process. The name is zero-terminated, and is within the compiled pattern. The length of the name is in the preceding code unit. If no name is available, NULL is returned. After a successful match, the name that is returned is the last one on the matching path. After a failed match or a partial match, the last encountered name is returned. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
