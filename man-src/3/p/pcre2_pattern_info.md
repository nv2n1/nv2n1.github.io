---
title: "pcre2_pattern_info(3)"
name: "pcre2_pattern_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_pattern_info/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_pattern_info(const pcre2_code *code, uint32_t what,
                       void *where);</code></pre>
<h2>Description</h2>
<p>This function returns information about a compiled pattern. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to a compiled regular expression pattern<br />
&nbsp;<wbr>&nbsp;<i>what</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;What information is required<br />
&nbsp;<wbr>&nbsp;<i>where</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the information The recognized values for the <i>what</i> argument, and the information they request are as follows:  If <i>where</i> is NULL, the function returns the amount of memory needed for the requested information, in bytes. Otherwise, the <i>where</i> argument must point to an unsigned 32-bit integer (uint32_t variable), except for the following <i>what</i> values, when it must point to a variable of the type shown:<br />
&nbsp;<wbr>&nbsp;PCRE2_INFO_FIRSTBITMAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const uint8_t&nbsp;*<br />
&nbsp;<wbr>&nbsp;PCRE2_INFO_JITSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t<br />
&nbsp;<wbr>&nbsp;PCRE2_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_SPTR<br />
&nbsp;<wbr>&nbsp;PCRE2_INFO_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t The yield of the function is zero on success or:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument&nbsp;<i>code</i>&nbsp;is NULL<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;&quot;magic number&quot;&nbsp;was not found<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADOPTION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the value of&nbsp;<i>what</i>&nbsp;is invalid<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_BADMODE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the pattern was compiled in the wrong mode<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_UNSET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the requested information is not set There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
