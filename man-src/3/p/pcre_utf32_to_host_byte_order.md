---
title: "pcre_utf32_to_host_byte_order(3)"
name: "pcre_utf32_to_host_byte_order"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre_utf32_to_host_byte_order/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre32_utf32_to_host_byte_order(PCRE_UCHAR32 *output,
                                    PCRE_SPTR32 input, int length, int *host_byte_order,
                                    int keep_boms);</code></pre>
<h2>Description</h2>
<p>This function, which exists only in the 32-bit library, converts a UTF-32 string to the correct order for the current host, taking account of any byte order marks (BOMs) within the string. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>output</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to output buffer, may be the same as&nbsp;<i>input</i><br />
&nbsp;<wbr>&nbsp;<i>input</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to input buffer<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;number of 32-bit units in the input, or negative for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a zero-terminated string<br />
&nbsp;<wbr>&nbsp;<i>host_byte_order</i>&nbsp;<wbr>&nbsp;a NULL value or a non-zero value pointed to means<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start in host byte order<br />
&nbsp;<wbr>&nbsp;<i>keep_boms</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if non-zero, BOMs are copied to the output string The result of the function is the number of 32-bit units placed into the output buffer, including the zero terminator if the string was zero-terminated. If <i>host_byte_order</i> is not NULL, it is set to indicate the byte order that is current at the end of the string. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
