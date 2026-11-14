---
title: "pcre2_substring_get_byname(3)"
name: "pcre2_substring_get_byname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_get_byname/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_get_byname(pcre2_match_data *match_data,
                               PCRE2_SPTR name, PCRE2_UCHAR **bufferptr, PCRE2_SIZE *bufflen);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a captured substring by name into newly acquired memory. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The match data for the match<br />
&nbsp;<wbr>&nbsp;<i>name</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name of the required substring<br />
&nbsp;<wbr>&nbsp;<i>bufferptr</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the string pointer<br />
&nbsp;<wbr>&nbsp;<i>bufflen</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the string length The memory in which the substring is placed is obtained by calling the same memory allocation function that was used for the match data block. The convenience function <code>pcre2_substring_free()</code> can be used to free it when it is no longer needed. The yield of the function is zero for success or one of the following error numbers:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NOSUBSTRING&nbsp;<wbr>&nbsp;<wbr>&nbsp;there are no groups of that name<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_UNAVAILBLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the ovector was too small for that group<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_UNSET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the group did not participate in the match<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NOMEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory could not be obtained If there is more than one group with the given name, the first one that is set is returned. In this situation PCRE2_ERROR_UNSET means that no group with the given name was set. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
