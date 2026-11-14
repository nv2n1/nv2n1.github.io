---
title: "cs_dump(3)"
name: "cs_dump"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_dump/"
description: "cs_dump – dump the cs parse tree"
---

<h2 class="name">NAME</h2>
<p> cs_dump &#8211; dump the cs parse tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
NEOERR *cs_dump(CSPARSE *parse, void *ctx, CSOUTFUNC cb);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; the CSPARSE structure created with cs_init<br />
 ctx &#8211; user data to be passed to the CSOUTFUNC<br />
 cb &#8211; a CSOUTFUNC callback </p>
<h2>DESCRIPTION</h2>
<p> cs_dump will dump the CS parse tree in the parse struct. This can be useful for debugging your templates. This function also uses the CSOUTFUNC callback to display the parse tree. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
