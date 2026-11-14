---
title: "pcre32_get_named_substring(3)"
name: "pcre32_get_named_substring"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_get_named_substring/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_get_named_substring(const pcre *code,
                             const char *subject, int *ovector,
                             int stringcount, const char *stringname,
                             const char **stringptr);

int pcre16_get_named_substring(const pcre16 *code,
                               PCRE_SPTR16 subject, int *ovector,
                               int stringcount, PCRE_SPTR16 stringname,
                               PCRE_SPTR16 *stringptr);

int pcre32_get_named_substring(const pcre32 *code,
                               PCRE_SPTR32 subject, int *ovector,
                               int stringcount, PCRE_SPTR32 stringname,
                               PCRE_SPTR32 *stringptr);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a captured substring by name. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled pattern<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject that has been successfully matched<br />
&nbsp;<wbr>&nbsp;<i>ovector</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset vector that&nbsp;<code>pcre[16|32]_exec()</code>&nbsp;used<br />
&nbsp;<wbr>&nbsp;<i>stringcount</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Value returned by&nbsp;<code>pcre[16|32]_exec()</code><br />
&nbsp;<wbr>&nbsp;<i>stringname</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name of the required substring<br />
&nbsp;<wbr>&nbsp;<i>stringptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the string pointer The memory in which the substring is placed is obtained by calling <code>pcre[16|32]_malloc()</code>. The convenience function <code>pcre[16|32]_free_substring()</code> can be used to free it when it is no longer needed. The yield of the function is the length of the extracted substring, PCRE_ERROR_NOMEMORY if sufficient memory could not be obtained, or PCRE_ERROR_NOSUBSTRING if the string name is invalid. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
