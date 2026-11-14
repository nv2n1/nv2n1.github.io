---
title: "pcre16_get_stringtable_entries(3)"
name: "pcre16_get_stringtable_entries"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_get_stringtable_entries/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_get_stringtable_entries(const pcre *code,
                                 const char *name, char **first, char **last);

int pcre16_get_stringtable_entries(const pcre16 *code,
                                   PCRE_SPTR16 name, PCRE_UCHAR16 **first, PCRE_UCHAR16 **last);

int pcre32_get_stringtable_entries(const pcre32 *code,
                                   PCRE_SPTR32 name, PCRE_UCHAR32 **first, PCRE_UCHAR32 **last);</code></pre>
<h2>Description</h2>
<p>This convenience function finds, for a compiled pattern, the first and last entries for a given name in the table that translates capturing parenthesis names into numbers. When names are required to be unique (PCRE_DUPNAMES is <i>not</i> set), it is usually easier to use <code>pcre[16|32]_get_stringnumber()</code> instead.  The yield of the function is the length of each entry, or PCRE_ERROR_NOSUBSTRING if none are found. There is a complete description of the PCRE native API, including the format of the table entries, in the <code>pcreapi</code> page, and a description of the POSIX API in the <code>pcreposix</code> page. </p>
