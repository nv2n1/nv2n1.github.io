---
title: "pcre32_fullinfo(3)"
name: "pcre32_fullinfo"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_fullinfo/"
description: "PCRE – Perl-compatible regular expressions"
---
<p>PCRE &#8211; Perl-compatible regular expressions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;pcre.h&gt;</code> </p>
<pre><code>
 int pcre_fullinfo(const pcre *  code , const pcre_extra * extra ,
      int  what , void * where );
 int pcre16_fullinfo(const pcre16 *  code , const pcre16_extra * extra ,
      int  what , void * where );
 int pcre32_fullinfo(const pcre32 *  code , const pcre32_extra * extra ,
      int  what , void * where );
</code></pre>
<h2>DESCRIPTION</h2>
<p>This function returns information about a compiled pattern. Its arguments are: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled regular expression <br />
&nbsp;<wbr>&nbsp;<i>extra</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Result of&nbsp;<code>pcre[16|32]_study()</code>&nbsp;or NULL <br />
&nbsp;<wbr>&nbsp;<i>what</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;What information is required <br />
&nbsp;<wbr>&nbsp;<i>where</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the information </p>
<p>The following information is available: </p>
<p> <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_BACKREFMAX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of highest back reference <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_CAPTURECOUNT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of capturing subpatterns <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_DEFAULT_TABLES&nbsp;<wbr>&nbsp;Pointer to default tables <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTBYTE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Fixed first data unit for a match, or <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-1 for start of string <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;or after newline, or <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-2 otherwise <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTTABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Table of first data units&nbsp;(after studying) <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_HASCRORLF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return 1 if explicit CR or LF matches exist <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_JCHANGED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return 1 if&nbsp;(?J)&nbsp;or&nbsp;(?-J)&nbsp;was used <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_JIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return 1 after successful JIT compilation <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_JITSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of JIT compiled code <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_LASTLITERAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Literal last data unit required <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MINLENGTH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Lower bound length of matching strings <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MATCHEMPTY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return 1 if the pattern can match an empty string, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 otherwise <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MATCHLIMIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Match limit if set, otherwise PCRE_RROR_UNSET <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MAXLOOKBEHIND&nbsp;<wbr>&nbsp;<wbr>&nbsp;Length&nbsp;(in characters)&nbsp;of the longest lookbehind assertion <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMECOUNT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number of named subpatterns <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMEENTRYSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of name table entry <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to name table <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_OKPARTIAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Return 1 if partial matching can be tried <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(always returns 1 after release 8.00) <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_OPTIONS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits used for compilation <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of compiled pattern <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_STUDYSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size of study data <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTCHARACTER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Fixed first data unit for a match <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTCHARACTERFLAGS Returns <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 if there is a first data character set, which can <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;then be retrieved using PCRE_INFO_FIRSTCHARACTER, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 if the first character is at the start of the data <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string or after a newline, and <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 otherwise <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_RECURSIONLIMIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Recursion limit if set, otherwise PCRE_ERROR_UNSET <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_REQUIREDCHAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Literal last data unit required <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_REQUIREDCHARFLAGS Returns 1 if the last data character is set&nbsp;(which can then <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;be retrieved using PCRE_INFO_REQUIREDCHAR);&nbsp;0 otherwise </p>
<p>The <i>where</i> argument must point to an integer variable, except for the following <i>what</i> values: </p>
<p> <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_DEFAULT_TABLES&nbsp;<wbr>&nbsp;const uint8_t&nbsp;* <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTCHARACTER&nbsp;<wbr>&nbsp;uint32_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTTABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const uint8_t&nbsp;* <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_JITSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MATCHLIMIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_SPTR16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(16-bit library) <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_SPTR32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(32-bit library) <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const unsigned char&nbsp;*&nbsp;(8-bit library) <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_OPTIONS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long int <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_STUDYSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_RECURSIONLIMIT&nbsp;<wbr>&nbsp;uint32_t <br />
&nbsp;<wbr>&nbsp;PCRE_INFO_REQUIREDCHAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t </p>
<p>The yield of the function is zero on success or: </p>
<p> <br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument&nbsp;<i>code</i>&nbsp;was NULL <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument&nbsp;<i>where</i>&nbsp;was NULL <br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;&quot;magic number&quot;&nbsp;was not found <br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_BADOPTION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the value of&nbsp;<i>what</i>&nbsp;was invalid <br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_UNSET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the option was not set </p>
<p>There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd></dl>
