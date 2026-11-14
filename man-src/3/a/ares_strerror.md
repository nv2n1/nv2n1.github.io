---
title: "ares_strerror(3)"
name: "ares_strerror"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_strerror/"
description: "ares_strerror – Get the description of an ares library error code"
---

<h2>NAME</h2>
<p> ares_strerror &#8211; Get the description of an ares library error code</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
const char *ares_strerror(int code)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_strerror</code> function gets the description of the ares library error code <i>code</i>, returning the result as a NUL-terminated C string.</p>
<h2>NOTES</h2>
<p> This function is not compatible with ares, it takes a different set of arguments.</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
