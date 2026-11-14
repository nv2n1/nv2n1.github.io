---
title: "pcre32_config(3)"
name: "pcre32_config"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre32_config/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_config(int what, void *where);
int pcre16_config(int what, void *where);
int pcre32_config(int what, void *where);</code></pre>
<h2>Description</h2>
<p>This function makes it possible for a client program to find out which optional features are available in the version of the PCRE library it is using. The arguments are as follows:<br />
&nbsp;<wbr>&nbsp;<i>what</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A code specifying what information is required<br />
&nbsp;<wbr>&nbsp;<i>where</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to where to put the data The <i>where</i> argument must point to an integer variable, except for PCRE_CONFIG_MATCH_LIMIT, PCRE_CONFIG_MATCH_LIMIT_RECURSION, and PCRE_CONFIG_PARENS_LIMIT, when it must point to an unsigned long integer, and for PCRE_CONFIG_JITTARGET, when it must point to a const char*. The available codes are:  The function yields 0 on success or PCRE_ERROR_BADOPTION otherwise. That error is also given if PCRE_CONFIG_UTF16 or PCRE_CONFIG_UTF32 is passed to <code>pcre_config()</code>, if PCRE_CONFIG_UTF8 or PCRE_CONFIG_UTF32 is passed to <code>pcre16_config()</code>, or if PCRE_CONFIG_UTF8 or PCRE_CONFIG_UTF16 is passed to <code>pcre32_config()</code>. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
