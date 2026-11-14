---
title: "pcre2_compile(3)"
name: "pcre2_compile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_compile/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_code *pcre2_compile(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, int *<i>errorcode</i>, PCRE2_SIZE *<i>erroroffset,</i>
<code> pcre2_compile_context *</code><i>ccontext</i>);</pre>
<h2>Description</h2>
<p>This function compiles a regular expression pattern into an internal form. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>pattern</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A string containing expression to be compiled<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The length of the string or PCRE2_ZERO_TERMINATED<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>errorcode</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put an error code<br />
&nbsp;<wbr>&nbsp;<i>erroffset</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put an error offset<br />
&nbsp;<wbr>&nbsp;<i>ccontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to a compile context or NULL The length of the pattern and any error offset that is returned are in code units, not characters. A compile context is needed only if you want to provide custom memory allocation functions, or to provide an external function for system stack size checking, or to change one or more of these parameters:<br />
&nbsp;<wbr>&nbsp;What&nbsp;\R matches&nbsp;(Unicode newlines, or CR, LF, CRLF only);<br />
&nbsp;<wbr>&nbsp;PCRE2&#8217;s character tables;<br />
&nbsp;<wbr>&nbsp;The newline character sequence;<br />
&nbsp;<wbr>&nbsp;The compile time nested parentheses limit;<br />
&nbsp;<wbr>&nbsp;The maximum pattern length&nbsp;(in code units)&nbsp;that is allowed.<br />
&nbsp;<wbr>&nbsp;The additional options bits&nbsp;(see pcre2_set_compile_extra_options()) The option bits are:<br />
&nbsp;<wbr>&nbsp;PCRE2_ANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Force pattern anchoring<br />
&nbsp;<wbr>&nbsp;PCRE2_ALLOW_EMPTY_CLASS&nbsp;<wbr>&nbsp;Allow empty classes<br />
&nbsp;<wbr>&nbsp;PCRE2_ALT_BSUX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alternative handling of&nbsp;
