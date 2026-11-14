---
title: "pcre32_copy_named_substring(3)"
name: "pcre32_copy_named_substring"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_copy_named_substring/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_copy_named_substring(const pcre *code,
                              const char *subject, int *ovector,
                              int stringcount, const char *stringname,
                              char *buffer, int buffersize);

int pcre16_copy_named_substring(const pcre16 *code,
                                PCRE_SPTR16 subject, int *ovector,
                                int stringcount, PCRE_SPTR16 stringname,
                                PCRE_UCHAR16 *buffer, int buffersize);

int pcre32_copy_named_substring(const pcre32 *code,
                                PCRE_SPTR32 subject, int *ovector,
                                int stringcount, PCRE_SPTR32 stringname,
                                PCRE_UCHAR32 *buffer, int buffersize);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a captured substring, identified by name, into a given buffer. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pattern that was successfully matched<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject that has been successfully matched<br />
&nbsp;<wbr>&nbsp;<i>ovector</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset vector that&nbsp;<code>pcre[16|32]_exec()</code>&nbsp;used<br />
&nbsp;<wbr>&nbsp;<i>stringcount</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Value returned by&nbsp;<code>pcre[16|32]_exec()</code><br />
&nbsp;<wbr>&nbsp;<i>stringname</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name of the required substring<br />
&nbsp;<wbr>&nbsp;<i>buffer</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Buffer to receive the string<br />
&nbsp;<wbr>&nbsp;<i>buffersize</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of buffer The yield is the length of the substring, PCRE_ERROR_NOMEMORY if the buffer was too small, or PCRE_ERROR_NOSUBSTRING if the string name is invalid. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
