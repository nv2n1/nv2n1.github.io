---
title: "tspi_tpm_setstatus(3)"
name: "tspi_tpm_setstatus"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_setstatus/"
description: "Tspi_TPM_SetStatus – modify the TPM’s status"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_SetStatus &#8211; modify the TPM&#8217;s status </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_SetStatus(TSS_HTPM </code><i>hTPM</i><code>, TSS_FLAG </code><i>statusFlag</i><code>,</code>
<code> TSS_BOOL </code><i>fTpmState</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_SetStatus</code> alters the status of the TPM. Depending on the chosen <i>statusFlag</i>, <i>fTpmState</i> may or may not be ignored. This command requires that the TPM be on and the handle to the TPM available. <code>This command is not currently implemented</code>. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>statusFlag</h3>
<p>The <i>statusFlag</i> parameter is what the TPM status should be set to.</p>
<h3>fTpmState</h3>
<p>The <i>fTpmState</i> parameter is the status value to set. For some states, this flag is ignored. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_SetStatus</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_SetStatus</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getstatus/">Tspi_TPM_GetStatus</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3).</p>
