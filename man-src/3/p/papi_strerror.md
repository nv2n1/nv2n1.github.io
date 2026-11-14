---
title: "papi_strerror(3)"
name: "papi_strerror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_strerror/"
description: "PAPI_strerror –"
---

<p>PAPI_strerror &#8211; </p>
<p> Returns a string describing the PAPI error code.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>char&nbsp;<wbr>*&nbsp;<wbr><code>PAPI_strerror(&nbsp;<wbr>int errorCode&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>code</i> &#8212; the error code to interpret</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>*error</i> &#8212; a pointer to the error string.<br />
 <i>NULL</i> &#8212; the input error code to <code>PAPI_strerror()</code> is invalid.</dl>
<p> <code>PAPI_strerror()</code> returns a pointer to the error message corresponding to the error code code. If the call fails the function returns the NULL pointer. This function is not implemented in Fortran. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int ret;
* int EventSet = PAPI_NULL;
* int native = 0x0;
* char error_str[PAPI_MAX_STR_LEN];
*
* ret = PAPI_create_eventset(&amp;EventSet);
* if (ret != PAPI_OK)
* {
* fprintf(stderr, &quot;PAPI error %d: %s, ret, PAPI_strerror(retval));
* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* }
* // Add Total Instructions Executed to our EventSet
* ret = PAPI_add_event(EventSet, PAPI_TOT_INS);
* if (ret != PAPI_OK)
* {
* PAPI_perror( &quot;PAPI_add_event&quot;);
* fprintf(stderr,&quot;PAPI_error %d: %s, ret, error_str);
* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* }
* // Start counting
* ret = PAPI_start(EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_perror</code> <code>PAPI_set_opt</code> <code>PAPI_get_opt</code> <code>PAPI_shutdown</code> <code>PAPI_set_debug</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
