---
title: "cs_parse_file(3)"
name: "cs_parse_file"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_parse_file/"
description: "cs_parse_file – parse a CS template file"
---

<h2 class="name">NAME</h2>
<p> cs_parse_file &#8211; parse a CS template file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
NEOERR *cs_parse_file(CSPARSE *parse, const char *path);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a CSPARSE structure created with cs_init<br />
 path &#8211; the path to the file to parse </p>
<h2>DESCRIPTION</h2>
<p> cs_parse_file will parse the CS template located at path. It will use hdf_search_path() if path does not begin with a &#8216;/&#8217;. The parsed CS template will be appended to the current parse tree stored in the CSPARSE structure. The entire file is loaded into memory and parsed in place. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
