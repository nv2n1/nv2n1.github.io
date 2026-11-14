---
title: "pcre_copy_substring(3)"
name: "pcre_copy_substring"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre_copy_substring/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_copy_substring(const char *subject, int *ovector,
                        int stringcount, int stringnumber, char *buffer,
                        int buffersize);

int pcre16_copy_substring(PCRE_SPTR16 subject, int *ovector,
                          int stringcount, int stringnumber, PCRE_UCHAR16 *buffer,
                          int buffersize);

int pcre32_copy_substring(PCRE_SPTR32 subject, int *ovector,
                          int stringcount, int stringnumber, PCRE_UCHAR32 *buffer,
                          int buffersize);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a captured substring into a given buffer. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject that has been successfully matched<br />
&nbsp;<wbr>&nbsp;<i>ovector</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset vector that&nbsp;<code>pcre[16|32]_exec()</code>&nbsp;used<br />
&nbsp;<wbr>&nbsp;<i>stringcount</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Value returned by&nbsp;<code>pcre[16|32]_exec()</code><br />
&nbsp;<wbr>&nbsp;<i>stringnumber</i>&nbsp;<wbr>&nbsp;Number of the required substring<br />
&nbsp;<wbr>&nbsp;<i>buffer</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Buffer to receive the string<br />
&nbsp;<wbr>&nbsp;<i>buffersize</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of buffer The yield is the length of the string, PCRE_ERROR_NOMEMORY if the buffer was too small, or PCRE_ERROR_NOSUBSTRING if the string number is invalid. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
