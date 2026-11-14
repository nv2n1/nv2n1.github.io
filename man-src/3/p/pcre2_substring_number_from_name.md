---
title: "pcre2_substring_number_from_name(3)"
name: "pcre2_substring_number_from_name"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_number_from_name/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_substring_number_from_name(const pcre2_code *code,
                                     PCRE2_SPTR name);</code></pre>
<h2>Description</h2>
<p>This convenience function finds the number of a named substring capturing parenthesis in a compiled pattern, provided that it is a unique name. The function arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled regular expression<br />
&nbsp;<wbr>&nbsp;<i>name</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name whose number is required The yield of the function is the number of the parenthesis if the name is found, or PCRE2_ERROR_NOSUBSTRING if it is not found. When duplicate names are allowed (PCRE2_DUPNAMES is set), if the name is not unique, PCRE2_ERROR_NOUNIQUESUBSTRING is returned. You can obtain the list of numbers with the same name by calling <code>pcre2_substring_nametable_scan()</code>. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
