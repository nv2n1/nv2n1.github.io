---
title: "cs_register_fileload(3)"
name: "cs_register_fileload"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_register_fileload/"
description: "cs_register_fileload – register a fileload function"
---

<h2 class="name">NAME</h2>
<p> cs_register_fileload &#8211; register a fileload function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
void cs_register_fileload(CSPARSE *parse, void *ctx, CSFILELOAD fileload);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a pointer to an initialized CSPARSE structure<br />
 ctx &#8211; pointer that is passed to the CSFILELOAD function when called<br />
 fileload &#8211; a CSFILELOAD function </p>
<h2>DESCRIPTION</h2>
<p> cs_register_fileload registers a fileload function that overrides the built-in function. The built-in function uses hdf_search_path and ne_file_load (based on stat/open/read) to find and load the file on every template render. You can override this function if you wish to provide other template search functions, or load the template from an in-memory cache, etc. This fileload function will be used by cs_parse, including </p>
<p> include: commands in the template. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
