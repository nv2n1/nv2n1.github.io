---
title: "tspi_context_getdefaultpolicy(3)"
name: "tspi_context_getdefaultpolicy"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_getdefaultpolicy/"
description: "Tspi_Context_GetDefaultPolicy – Get a handle to the default policy object of a given context."
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Context_GetDefaultPolicy &#8211; Get a handle to the default policy object of a given context. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<dl COMPACT><dt><code>TSS_RESULT Tspi_Context_GetDefaultPolicy(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_HPOLICY </code><i>*phPolicy</i><code>); </code></pre>
</dl>
<h2>Description</h2>
<p><code>Tspi_Context_GetDefaultPolicy</code></p>
<dd>determines what policy is used by all of the keys in a given context. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle of the context object.</p>
<h3>phPolicy</h3>
<p>The <i>phPolicy</i> parameter receives the handle of the default policy object bound to the context. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetDefaultPolicy</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetDefaultPolicy</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_create/">Tspi_Context_Create</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_connect/">Tspi_Context_Connect</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_freememory/">Tspi_Context_FreeMemory</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_close/">Tspi_Context_Close</a></code>(3).</p>
