---
title: "pcre32_get_stringnumber(3)"
name: "pcre32_get_stringnumber"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_get_stringnumber/"
---

PCRE - Perl-compatible regular expressions

<h2>Synopsis</h2>

<pre><code>#include &lt;pcre.h&gt;
int pcre_get_stringnumber(const pcre *code,
                          const char *name);

int pcre16_get_stringnumber(const pcre16 *code,
                            PCRE_SPTR16 name);

int pcre32_get_stringnumber(const pcre32 *code,
                            PCRE_SPTR32 name);</code></pre>

<h2>Description</h2>

This convenience function finds the number of a named substring capturing parenthesis in a compiled pattern. Its arguments are: 
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compiled regular expression 
&nbsp;<wbr>&nbsp;<i>name</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Name whose number is required The yield of the function is the number of the parenthesis if the name is found, or PCRE_ERROR_NOSUBSTRING otherwise. When duplicate names are allowed (PCRE_DUPNAMES is set), it is not defined which of the numbers is returned by <b>pcre[16|32]_get_stringnumber()</b>. You can obtain the complete list by calling <b>pcre[16|32]_get_stringtable_entries()</b>. There is a complete description of the PCRE native API in the <b>pcreapi</b> page and a description of the POSIX API in the <b>pcreposix</b> page. 
