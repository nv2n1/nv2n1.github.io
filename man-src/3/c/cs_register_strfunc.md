---
title: "cs_register_strfunc(3)"
name: "cs_register_strfunc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cs_register_strfunc/"
description: "cs_register_strfunc – register a string handling function"
---

<h2 class="name">NAME</h2>
<p> cs_register_strfunc &#8211; register a string handling function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cs/cs.h&gt;
</code></pre>
<pre><code>
NEOERR *cs_register_strfunc(CSPARSE *parse, char *funcname, CSSTRFUNC str_func);
</code></pre>
<h2>ARGUMENTS</h2>
<p> parse &#8211; a pointer to a CSPARSE structure initialized with cs_init()<br />
 funcname &#8211; the name for the CS function call<br />
 Note that registering a duplicate funcname will<br />
 raise a NERR_DUPLICATE error<br />
 str_func &#8211; a CSSTRFUNC not-callback </p>
<h2>DESCRIPTION</h2>
<p> cs_register_strfunc will register a string function that can be called during CS render. This not-callback is designed to allow for string formating/escaping functions that are not built-in to CS (since CS is not HTML specific, for instance, but it is very useful to have CS have functions for javascript/html/url escaping). Note that we explicitly don&#8217;t provide any associated data or anything to attempt to keep you from using this as a generic callback&#8230; The format of a CSSTRFUNC is: NEOERR * str_func(char *in, char **out); This function should not modify the input string, and should allocate the output string with a libc function. (as we will call free on it) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cs_dump/">cs_dump</a></code>(3), <a href="/docs/linux/man/3-cs_destroy/">cs_destroy</a><code>(3), <a href="/docs/linux/man/3-cs_render/">cs_render</a></code>(3), <a href="/docs/linux/man/3-cs_register_esc_strfunc/">cs_register_esc_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parsev/">cs_arg_parsev</a></code>(3), <a href="/docs/linux/man/3-cs_register_fileload/">cs_register_fileload</a><code>(3), <a href="/docs/linux/man/3-cs_init/">cs_init</a></code>(3), <a href="/docs/linux/man/3-cs_register_strfunc/">cs_register_strfunc</a><code>(3), <a href="/docs/linux/man/3-cs_arg_parse/">cs_arg_parse</a></code>(3), <a href="/docs/linux/man/3-cs_parse_string/">cs_parse_string</a><code>(3), <a href="/docs/linux/man/3-cs_parse_file/">cs_parse_file</a></code>(3), =<code>(3), cs_register_function</code> </p>
<h2>Index</h2>
