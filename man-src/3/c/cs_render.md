---
title: "cs_render(3)"
name: "cs_render"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_render/"
description: "cs_render – render a CS parse tree"
---

<h2 class="name">NAME</h2>
<p> cs_render &#8211; render a CS parse tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
NEOERR *cs_render(CSPARSE *parse, void *ctx, CSOUTFUNC cb);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; the CSPARSE structure containing the CS parse tree<br />
 that will be evaluated<br />
 ctx &#8211; user data that will be passed as the first variable to<br />
 the CSOUTFUNC.<br />
 cb &#8211; a CSOUTFUNC called to render the output. A CSOUTFUNC is<br />
 defined as:<br />
 typedef NEOERR* (*CSOUTFUNC)(void *, char *); </p>
<h2>DESCRIPTION</h2>
<p> cs_render will evaluate a CS parse tree, calling the CSOUTFUNC passed to it for output. Note that calling cs_render multiple times on the same parse tree may or may not render the same output as the set statement has side-effects, it updates the HDF data used by the render. Typically, you will call one of the cs_parse functions before calling this function. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
