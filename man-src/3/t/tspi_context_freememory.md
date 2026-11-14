---
title: "tspi_context_freememory(3)"
name: "tspi_context_freememory"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_freememory/"
description: "Tspi_Context_FreeMemory – Free allocated memory for a given context."
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Context_FreeMemory &#8211; Free allocated memory for a given context. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<br>
<dl COMPACT><dt><code>TSS_RESULT Tspi_Context_FreeMemory(TSS_HCONTEXT </code><i>hContext</i><code>, BYTE* </code><i>rgbMemory</i><code>);</code></pre>
</dl>
<h2>Description</h2>
<p><code>Tspi_Context_FreeMemory</code> frees memory allocated by the TSS Service Provider on a per-context basis.</p>
<dd>This should be used before Tspi_Context_Close is called, to avoid memory leaks. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle to the local context.</p>
<h3>rgbMemory</h3>
<p>The <i>rgbMemory</i> parameter is a pointer to the memory block to be freed. If this is NULL, all memory blocks bound to the context are freed. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_FreeMemory</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_FreeMemory</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_create/">Tspi_Context_Create</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_close/">Tspi_Context_Close</a></code>(3).</p>
