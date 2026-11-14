---
title: "tspi_context_gettpmobject(3)"
name: "tspi_context_gettpmobject"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_gettpmobject/"
description: "Context_GetTpmObject – get the handle of the TPM object associated with a context."
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Context_GetTpmObject &#8211; get the handle of the TPM object associated with a context. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<br>
<dl COMPACT><dt><code>TSS_RESULT Tspi_Context_GetTpmObject(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_HTPM* </code><i>phTPM</i><code>); </code></pre>
</dl>
<h2>Description</h2>
<p><code>Tspi_Context_GetTpmObject</code> retrieves the TPM object of a context. Only one instance of this</p>
<dd>object exists for a given context and implicitly represents a TPM owner. This function is normally called at the beginning of a program, right after the context is established. You must have a context established prior to calling this function. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle of the context object (already existing).</p>
<h3>phTPM</h3>
<p>The <i>phTPM</i> parameter is a pointer to where the handle of the TPM will be placed. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetTpmObject</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more of the parameters is incorrect. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetTpmObject</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_create/">Tspi_Context_Create</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_connect/">Tspi_Context_Connect</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_freememory/">Tspi_Context_FreeMemory</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_close/">Tspi_Context_Close</a></code>(3).</p>
