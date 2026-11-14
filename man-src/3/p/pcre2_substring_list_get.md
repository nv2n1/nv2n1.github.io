---
title: "pcre2_substring_list_get(3)"
name: "pcre2_substring_list_get"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_list_get/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_list_get(pcre2_match_data *match_data,
                             PCRE2_UCHAR ***listptr, PCRE2_SIZE **lengthsptr);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting all the captured substrings after a pattern match. It builds a list of pointers to the strings, and (optionally) a second list that contains their lengths (in code units), excluding a terminating zero that is added to each of them. All this is done in a single block of memory that is obtained using the same memory allocation function that was used to get the match data block. The convenience function <code>pcre2_substring_list_free()</code> can be used to free it when it is no longer needed. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The match data block<br />
&nbsp;<wbr>&nbsp;<i>listptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put a pointer to the list<br />
&nbsp;<wbr>&nbsp;<i>lengthsptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put a pointer to the lengths, or NULL A pointer to a list of pointers is put in the variable whose address is in <i>listptr</i>. The list is terminated by a NULL pointer. If <i>lengthsptr</i> is not NULL, a matching list of lengths is created, and its address is placed in <i>lengthsptr</i>. The yield of the function is zero on success or PCRE2_ERROR_NOMEMORY if sufficient memory could not be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
