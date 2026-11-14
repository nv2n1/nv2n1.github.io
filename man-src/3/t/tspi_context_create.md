---
title: "tspi_context_create(3)"
name: "tspi_context_create"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_create/"
description: "Tspi_Context_Create – create a TSP context handle."
---

<p>Tspi_Context_Create &#8211; create a TSP context handle.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_Create(TSS_HCONTEXT* </code><i>phContext</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Context_Create</code> creates a handle to a new context object. The context is then used by other API functions to track resources related to it.</p>
<h2>Parameters</h2>
<h3>phContext</h3>
<p>Receives the handle to the created context object. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_Create</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An internal error occurred in the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_Create</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_close/">Tspi_Context_Close</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_connect/">Tspi_Context_Connect</a></code>(3).</p>
