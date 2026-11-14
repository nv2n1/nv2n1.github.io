---
title: "papi_shutdown(3)"
name: "papi_shutdown"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_shutdown/"
description: "PAPI_shutdown –"
---

<p>PAPI_shutdown &#8211; </p>
<p> Finish using PAPI and free all related resources.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Prototype:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>void&nbsp;<wbr><code>PAPI_shutdown(&nbsp;<wbr>void&nbsp;<wbr>)</code>;</dl>
<p> <code>PAPI_shutdown()</code> is an exit function used by the PAPI Library to free resources and shut down when certain error conditions arise. It is not necessary for the user to call this function, but doing so allows the user to have the capability to free memory and resources used by the PAPI Library. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>PAPI_init_library</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
