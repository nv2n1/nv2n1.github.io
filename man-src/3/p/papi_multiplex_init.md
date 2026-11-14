---
title: "papi_multiplex_init(3)"
name: "papi_multiplex_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_multiplex_init/"
description: "PAPI_multiplex_init –"
---

<p>PAPI_multiplex_init &#8211; </p>
<p> Initialize multiplex support in the PAPI library.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>PAPI_multiplex_init() enables and initializes multiplex support in 
 the PAPI library. 
Multiplexing allows a user to count more events than total physical 
 counters by time sharing the existing counters at some loss in 
 precision. 
Applications that make no use of multiplexing do not need to call 
 this routine. </pre>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_multiplex_init</code>&nbsp;<wbr>(void);</dl>
<p> <code>Examples</code></p>
<dl COMPACT>
<dd>
<pre>* retval = PAPI_multiplex_init();
* </pre>
</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i> This call always returns PAPI_OK</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_multiplex</code> </p>
<p> <code>PAPI_get_multiplex</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
