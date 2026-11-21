---

title: "pcre2_substring_nametable_scan(3)"
name: "pcre2_substring_nametable_scan"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_substring_nametable_scan/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>

<p> <code>#include &lt;pcre2.h&gt;</code> </p>
<pre><code>
 int pcre2_substring_nametable_scan(const pcre2_code *  code ,
   PCRE2_SPTR  name , PCRE2_SPTR * first , PCRE2_SPTR * last );
</code></pre>
<h2>DESCRIPTION</h2>
<p>This convenience function finds, for a compiled pattern, the first and last entries for a given name in the table that translates capture group names into numbers. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled regular expression <br />
&nbsp;<wbr>&nbsp;<i>name</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name whose entries required <br />
&nbsp;<wbr>&nbsp;<i>first</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to return a pointer to the first entry <br />
&nbsp;<wbr>&nbsp;<i>last</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to return a pointer to the last entry </p>
<p>When the name is found in the table, if <i>first</i> is NULL, the function returns a group number, but if there is more than one matching entry, it is not defined which one. Otherwise, when both pointers have been set, the yield of the function is the length of each entry in code units. If the name is not found, PCRE2_ERROR_NOSUBSTRING is returned. </p>
<p>There is a complete description of the PCRE2 native API, including the format of the table entries, in the <code>pcre2api</code> page, and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
