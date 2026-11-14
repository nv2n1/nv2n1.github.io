---
title: "pcre16_fullinfo(3)"
name: "pcre16_fullinfo"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_fullinfo/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_fullinfo(const pcre *code, const pcre_extra *extra,
                  int what, void *where);

int pcre16_fullinfo(const pcre16 *code, const pcre16_extra *extra,
                    int what, void *where);

int pcre32_fullinfo(const pcre32 *code, const pcre32_extra *extra,
                    int what, void *where);</code></pre>
<h2>Description</h2>
<p>This function returns information about a compiled pattern. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled regular expression<br />
&nbsp;<wbr>&nbsp;<i>extra</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Result of&nbsp;<code>pcre[16|32]_study()</code>&nbsp;or NULL<br />
&nbsp;<wbr>&nbsp;<i>what</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;What information is required<br />
&nbsp;<wbr>&nbsp;<i>where</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put the information The following information is available:  The <i>where</i> argument must point to an integer variable, except for the following <i>what</i> values:<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_DEFAULT_TABLES&nbsp;<wbr>&nbsp;const uint8_t&nbsp;*<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTCHARACTER&nbsp;<wbr>&nbsp;uint32_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_FIRSTTABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const uint8_t&nbsp;*<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_JITSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_MATCHLIMIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_SPTR16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(16-bit library)<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_SPTR32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(32-bit library)<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_NAMETABLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const unsigned char&nbsp;*&nbsp;(8-bit library)<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_OPTIONS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long int<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_SIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_STUDYSIZE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_RECURSIONLIMIT&nbsp;<wbr>&nbsp;uint32_t<br />
&nbsp;<wbr>&nbsp;PCRE_INFO_REQUIREDCHAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t The yield of the function is zero on success or:<br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument&nbsp;<i>code</i>&nbsp;was NULL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the argument&nbsp;<i>where</i>&nbsp;was NULL<br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_BADMAGIC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;&quot;magic number&quot;&nbsp;was not found<br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_BADOPTION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the value of&nbsp;<i>what</i>&nbsp;was invalid<br />
&nbsp;<wbr>&nbsp;PCRE_ERROR_UNSET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the option was not set There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
