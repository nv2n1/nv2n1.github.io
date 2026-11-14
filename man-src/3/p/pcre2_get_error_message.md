---
title: "pcre2_get_error_message(3)"
name: "pcre2_get_error_message"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_get_error_message/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_get_error_message(int errorcode, PCRE2_UCHAR *buffer,
                            PCRE2_SIZE bufflen);</code></pre>
<h2>Description</h2>
<p>This function provides a textual error message for each PCRE2 error code. Compilation errors are positive numbers; UTF formatting errors and matching errors are negative numbers. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>errorcode</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;an error code&nbsp;(positive or negative)<br />
&nbsp;<wbr>&nbsp;<i>buffer</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;where to put the message<br />
&nbsp;<wbr>&nbsp;<i>bufflen</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the length of the buffer&nbsp;(code units) The function returns the length of the message in code units, excluding the trailing zero, or the negative error code PCRE2_ERROR_NOMEMORY if the buffer is too small. In this case, the returned message is truncated (but still with a trailing zero). If <i>errorcode</i> does not contain a recognized error code number, the negative value PCRE2_ERROR_BADDATA is returned. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
