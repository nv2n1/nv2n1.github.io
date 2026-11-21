---
title: "pcre2_substring_length_bynumber(3)"
name: "pcre2_substring_length_bynumber"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_length_bynumber/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---
<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;pcre2.h&gt;</code> </p>
<pre><code>
 int pcre2_substring_length_bynumber(pcre2_match_data *  match_data ,
   uint32_t  number , PCRE2_SIZE * length );
</code></pre>
<h2>DESCRIPTION</h2>
<p>This function returns the length of a matched substring, identified by number. The arguments are: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The match data block for the match <br />
&nbsp;<wbr>&nbsp;<i>number</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The substring number <br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to return the length, or NULL </p>
<p>The third argument may be NULL if all you want to know is whether or not a substring is set. The yield is zero on success, or a negative error code otherwise. After a partial match, only substring 0 is available. </p>
<p>There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
