---
title: "perror(3)"
name: "perror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-perror/"
description: "perror – print a system error message"
---

<p>perror &#8211; print a system error message</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
void perror(const char *s);
#include &lt;errno.h&gt;</code></pre>
<p> <code>const char * const </code><i>sys_errlist</i><code>[];</code><br />
 <code>int </code><i>sys_nerr</i><code>;</code><br />
 <code>int </code><i>errno</i><code>; </code>/* Not really declared this way; see <a href="/docs/linux/man/3-errno/">errno</a>(3) */ Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <i>sys_errlist</i>, <i>sys_nerr</i>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;From glibc 2.19 to 2.31:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The <code>perror</code>() function produces a message on standard error describing the last error encountered during a call to a system or library function. </p>
<p> First (if <i>s</i> is not NULL and <i>*s</i> is not a null byte (&#8216;
