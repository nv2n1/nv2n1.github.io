---
title: "cs_parse_string(3)"
name: "cs_parse_string"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_parse_string/"
description: "cs_parse_string – parse a CS template string"
---

<h2 class="name">NAME</h2>
<p> cs_parse_string &#8211; parse a CS template string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
NEOERR *cs_parse_string(CSPARSE *parse, char *buf, size_t blen);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a CSPARSE structure created with cs_init<br />
 buf &#8211; the string to parse. Embedded NULLs are not currently<br />
 supported<br />
 blen &#8211; the length of the string </p>
<h2>DESCRIPTION</h2>
<p> cs_parse_string parses a string. The string is modified, and internal references are kept by the parse tree. For this reason, ownership of the string is transfered to the CS system, and the string will be free&#8217;d when cs_destroy() is called. The parse information will be appended to the current parse tree. During parse, the only HDF variables which are evaluated are those used in evar or include statements. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
