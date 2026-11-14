---
title: "cs_init(3)"
name: "cs_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_init/"
description: "cs_init – create and initialize a CS context"
---

<h2 class="name">NAME</h2>
<p> cs_init &#8211; create and initialize a CS context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre>
NEOERR *cs_init (CSPARSE **parse, HDF *hdf);
</pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a pointer to a pointer to a CSPARSE structure that<br />
 will be created<br />
 hdf &#8211; the HDF dataset to be used during parsing and rendering </p>
<h2>DESCRIPTION</h2>
<p> cs_init will create a CSPARSE structure and initialize it. This structure maintains the state and information necessary for parsing and rendering a CS template. </p>
<p> MT-Level: cs routines perform no locking, and neither do hdf routines. They should be safe in an MT environment as long as they are confined to a single thread. </p>
<h2>RETURN VALUE</h2>
<p> parse will contain a pointer to the allocated CSPARSE<br />
 structure. This structure will be deallocated with<br />
 cs_destroy() </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
