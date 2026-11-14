---
title: "cs_register_esc_strfunc(3)"
name: "cs_register_esc_strfunc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_register_esc_strfunc/"
description: "cs_register_esc_strfunc – cs_register_strfunc with escaping context"
---

<h2 class="name">NAME</h2>
<p> cs_register_esc_strfunc &#8211; cs_register_strfunc with escaping context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre>
NEOERR *cs_register_esc_strfunc(CSPARSE *parse, char *funcname,
                                CSSTRFUNC str_func);
</pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a pointer to a CSPARSE structure initialized with cs_init()<br />
 funcname &#8211; the name for the CS function call<br />
 Note that registering a duplicate funcname will<br />
 raise a NERR_DUPLICATE error<br />
 str_func &#8211; a CSSTRFUNC not-callback </p>
<h2>DESCRIPTION</h2>
<p> cs_register_esc_strfunc functions exactly as cs_register_strfunc except that it changes the evaluation escaping context to disable default escaping. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
