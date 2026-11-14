---
title: "pcre2_config(3)"
name: "pcre2_config"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_config/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;
int pcre2_config(uint32_t what, void *where);</code></pre>
<h2>Description</h2>
<p>This function makes it possible for a client program to find out which optional features are available in the version of the PCRE2 library it is using. The arguments are as follows:<br />
&nbsp;<wbr>&nbsp;<i>what</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A code specifying what information is required<br />
&nbsp;<wbr>&nbsp;<i>where</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to where to put the information If <i>where</i> is NULL, the function returns the amount of memory needed for the requested information. When the information is a string, the value is in code units; for other types of data it is in bytes. If <code>where</code> is not NULL, for PCRE2_CONFIG_JITTARGET, PCRE2_CONFIG_UNICODE_VERSION, and PCRE2_CONFIG_VERSION it must point to a buffer that is large enough to hold the string. For all other codes it must point to a uint32_t integer variable. The available codes are:  The function yields a non-negative value on success or the negative value PCRE2_ERROR_BADOPTION otherwise. This is also the result for the PCRE2_CONFIG_JITTARGET code if JIT support is not available. When a string is requested, the function returns the number of code units used, including the terminating zero. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
