---
title: "gets(3)"
name: "gets"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gets/"
description: "gets – get a string from standard input (DEPRECATED)"
---

<h2 class="name">NAME</h2>
<p> gets &#8211; get a string from standard input (DEPRECATED) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
char *gets(char *s);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Never use this function</i>. </p>
<p> <code>gets</code>() reads a line from <i>stdin</i> into the buffer pointed to by <i>s</i> until either a terminating newline or <code>EOF</code>, which it replaces with a null byte (&#8216;
