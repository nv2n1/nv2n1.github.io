---
title: "pcre2_substring_copy_bynumber(3)"
name: "pcre2_substring_copy_bynumber"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_copy_bynumber/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_copy_bynumber(pcre2_match_data *match_data,
                                  uint32_t number, PCRE2_UCHAR *buffer,
                                  PCRE2_SIZE *bufflen);</code></pre>
<h2>Description</h2>
<p>This is a convenience function for extracting a captured substring into a given buffer. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The match data block for the match<br />
&nbsp;<wbr>&nbsp;<i>number</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of the required substring<br />
&nbsp;<wbr>&nbsp;<i>buffer</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Buffer to receive the string<br />
&nbsp;<wbr>&nbsp;<i>bufflen</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length of buffer The <i>bufflen</i> variable is updated with the length of the extracted string, excluding the terminating zero. The yield of the function is zero for success or one of the following error numbers:<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NOSUBSTRING&nbsp;<wbr>&nbsp;<wbr>&nbsp;there are no groups of that number<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_UNAVAILBLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the ovector was too small for that group<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_UNSET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the group did not participate in the match<br />
&nbsp;<wbr>&nbsp;PCRE2_ERROR_NOMEMORY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the buffer is too small There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
