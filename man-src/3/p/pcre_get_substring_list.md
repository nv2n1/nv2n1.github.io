---
title: "pcre_get_substring_list(3)"
name: "pcre_get_substring_list"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre_get_substring_list/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_get_substring_list(const char *subject,
                            int *ovector, int stringcount, const char ***listptr);

int pcre16_get_substring_list(PCRE_SPTR16 subject,
                              int *ovector, int stringcount, PCRE_SPTR16 **listptr);

int pcre32_get_substring_list(PCRE_SPTR32 subject,
                              int *ovector, int stringcount, PCRE_SPTR32 **listptr);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a list of all the captured substrings. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>subject</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Subject that has been successfully matched<br />
&nbsp;<wbr>&nbsp;<i>ovector</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Offset vector that&nbsp;<code>pcre[16|32]_exec</code>&nbsp;used<br />
&nbsp;<wbr>&nbsp;<i>stringcount</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Value returned by&nbsp;<code>pcre[16|32]_exec</code><br />
&nbsp;<wbr>&nbsp;<i>listptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put a pointer to the list The memory in which the substrings and the list are placed is obtained by calling <code>pcre[16|32]_malloc()</code>. The convenience function <code>pcre[16|32]_free_substring_list()</code> can be used to free it when it is no longer needed. A pointer to a list of pointers is put in the variable whose address is in <i>listptr</i>. The list is terminated by a NULL pointer. The yield of the function is zero on success or PCRE_ERROR_NOMEMORY if sufficient memory could not be obtained. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
