---
title: "cs_destroy(3)"
name: "cs_destroy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_destroy/"
description: "cs_destroy – clean up and dealloc a parse tree"
---

<h2 class="name">NAME</h2>
<p> cs_destroy &#8211; clean up and dealloc a parse tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
void cs_destroy(CSPARSE **parse);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a pointer to a parse structure. </p>
<h2>DESCRIPTION</h2>
<p> cs_destroy will clean up all the memory associated with a CSPARSE structure, including strings passed to cs_parse_string. This does not clean up any memory allocated by your own CSOUTFUNC or the HDF data structure passed to cs_init. It is safe to call this with a NULL pointer, and it will leave parse NULL as well (ie, it can be called more than once on the same var) </p>
<h2>RETURN VALUE</h2>
<p> parse &#8211; will be NULL </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
