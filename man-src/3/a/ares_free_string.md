---
title: "ares_free_string(3)"
name: "ares_free_string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_free_string/"
description: "ares_free_string – Free strings allocated by ares functions"
---

<h2>NAME</h2>
<p> ares_free_string &#8211; Free strings allocated by ares functions</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_free_string(void *str)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>ares_free_string</i> function frees a string allocated by an ares function.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_mkquery/">ares_mkquery</a></code>(3) <code><a href="/docs/linux/man/3-ares_expand_string/">ares_expand_string</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 2000 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
