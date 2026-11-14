---
title: "tspi_tpm_getstatus(3)"
name: "tspi_tpm_getstatus"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getstatus/"
description: "Tspi_TPM_GetStatus – query the TPM’s status"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_GetStatus &#8211; query the TPM&#8217;s status </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetStatus(TSS_HTPM </code><i>hTPM</i><code>, TSS_FLAG </code><i>statusFlag</i><code>, BOOL* </code><i>pfTpmState</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetStatus</code> queries the status of the TPM, returning a specific status based on the flags specified. <code>This command is not currently implemented</code>. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>statusFlag</h3>
<p>The <i>statusFlag</i> parameter is the status to be retrieved.</p>
<h3>fTpmState</h3>
<p>The <i>pfTpmState</i> parameter is a pointer to the value of the status queried. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetStatus</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetStatus</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_setstatus/">Tspi_TPM_SetStatus</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3).</p>
