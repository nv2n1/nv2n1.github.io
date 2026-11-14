---
title: "tspi_context_getcapability(3)"
name: "tspi_context_getcapability"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_getcapability/"
description: "Tspi_Context_GetCapability – provide the capabilites of a TSS Core Service, TSS Service Provider, or TPM."
---

<p>Tspi_Context_GetCapability &#8211; provide the capabilites of a TSS Core Service, TSS Service Provider, or TPM.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_GetCapability(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>capArea</i><code>,</code>
<code> UINT32 </code><i>ulSubCapLength</i><code>, BYTE* </code><i>rgbSubCap</i><code>,</code>
<code> UINT32* </code><i>pulRespDataLength</i><code>, BYTE** </code><i>prgbRespData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_GetCapability</code> provides the capabilities of the TSS Core Service or TSS Service Provider</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>capArea</h3>
<p>Flag indicating the attribute to query. </p>
<h3>ulSubCapLength</h3>
<p>The length (in bytes) of the rgbSubCap parameter. </p>
<h3>rgbSubCap</h3>
<p>Data indicating the attribute to query. </p>
<h3>pulRespDataLength</h3>
<p>Recieves the length (in bytes) of the prgbRespData parameter. </p>
<h3>prgbRespData</h3>
<p>On successful completion of the command, this parameter points to a buffer containing the actual data of the specified capability.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetCapability</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hContext</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER &#8211; One of the parameters did not match. </font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetCapability</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code>(none)</code>.</p>
