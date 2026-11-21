---
title: "pcre2_substring_length_byname(3)"
name: "pcre2_substring_length_byname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_length_byname/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---
<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;pcre2.h&gt;</code> </p>
<pre><code>
 int pcre2_substring_length_byname(pcre2_match_data *  match_data ,
   PCRE2_SPTR  name , PCRE2_SIZE * length );
</code></pre>
<h2>DESCRIPTION</h2>
<p>This function returns the length of a matched substring, identified by name. The arguments are: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<i>match_data</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The match data block for the match <br />
&nbsp;<wbr>&nbsp;<i>name</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The substring name <br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to return the length </p>
<p>The yield is zero on success, or an error code if the substring is not found. </p>
<p>There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
