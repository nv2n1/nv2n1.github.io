---
title: "strsep(3)"
name: "strsep"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strsep/"
description: "strsep – extract token from string"
---

<p>strsep &#8211; extract token from string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strsep(char **stringp, const char *delim);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strsep</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>If <i>*stringp</i> is NULL, the <code>strsep</code>() function returns NULL and does nothing else. Otherwise, this function finds the first token in the string <i>*stringp</i>, that is delimited by one of the bytes in the string <i>delim</i>. This token is terminated by overwriting the delimiter with a null byte (&#8216;
