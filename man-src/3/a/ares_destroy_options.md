---
title: "ares_destroy_options(3)"
name: "ares_destroy_options"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_destroy_options/"
description: "ares_destroy_options – Destroy options initialized with ares_save_options"
---

<h2>NAME</h2>
<p> ares_destroy_options &#8211; Destroy options initialized with ares_save_options</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_destroy_options(struct ares_options *options)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_destroy_options</code> function destroys the options struct identified by <i>options</i>, freeing all memory allocated by ares_save_options. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a></code>(3), <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Brad House<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
