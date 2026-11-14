---
title: "pcre2_pattern_convert(3)"
name: "pcre2_pattern_convert"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_pattern_convert/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_pattern_convert(PCRE2_SPTR pattern, PCRE2_SIZE length,
                          uint32_t options, PCRE2_UCHAR **buffer,
                          PCRE2_SIZE *blength, pcre2_convert_context *cvcontext);</code></pre>
<h2>Description</h2>
<p>This function is part of an experimental set of pattern conversion functions. It converts a foreign pattern (for example, a glob) into a PCRE2 regular expression pattern. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>pattern</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The foreign pattern<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The length of the input pattern or PCRE2_ZERO_TERMINATED<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>buffer</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to pointer to output buffer, or NULL<br />
&nbsp;<wbr>&nbsp;<i>blength</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to output length field<br />
&nbsp;<wbr>&nbsp;<i>cvcontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to a convert context or NULL The length of the converted pattern (excluding the terminating zero) is returned via <i>blength</i>. If <i>buffer</i> is NULL, the function just returns the output length. If <i>buffer</i> points to a NULL pointer, heap memory is obtained for the converted pattern, using the allocator in the context if present (or else <code>malloc()</code>), and the field pointed to by <i>buffer</i> is updated. If <i>buffer</i> points to a non-NULL field, that must point to a buffer whose size is in the variable pointed to by <i>blength</i>. This value is updated. The option bits are:<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_UTF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Input is UTF<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_NO_UTF_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check UTF validity<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_POSIX_BASIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Convert POSIX basic pattern<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_POSIX_EXTENDED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Convert POSIX extended pattern<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;Convert<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB_NO_WILD_SEPARATOR&nbsp;<wbr>&nbsp;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;various types<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB_NO_STARSTAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of glob The return value from <code>pcre2_pattern_convert()</code> is zero on success or a non-zero PCRE2 error code. The pattern conversion functions are described in the <code>pcre2convert</code> documentation. </p>
