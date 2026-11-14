---
title: "papi_perror(3)"
name: "papi_perror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_perror/"
description: "PAPI_perror –"
---

<p>PAPI_perror &#8211; </p>
<p> Produces a string on standard error, describing the last library error.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>void&nbsp;<wbr><code>PAPI_perror(&nbsp;<wbr>char&nbsp;<wbr>*s&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>s</i> &#8212; Optional message to print before the string describing the last error message.</dl>
<p> The routine <code>PAPI_perror()</code> produces a message on the standard error output, describing the last error encountered during a call to PAPI. If s is not NULL, s is printed, followed by a colon and a space. Then the error message and a new-line are printed. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int ret;
* int EventSet = PAPI_NULL;
* int native = 0x0;
*
* ret = PAPI_create_eventset(&amp;EventSet);
* if (ret != PAPI_OK)
* {
* fprintf(stderr, * <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* }
* // Add Total Instructions Executed to our EventSet
* ret = PAPI_add_event(EventSet, PAPI_TOT_INS);
* if (ret != PAPI_OK)
* {
* PAPI_perror( &quot;PAPI_add_event&quot; );
* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* }
* // Start counting
* ret = PAPI_start(EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_strerror</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
