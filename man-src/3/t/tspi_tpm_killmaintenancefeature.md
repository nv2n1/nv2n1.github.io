---
title: "tspi_tpm_killmaintenancefeature(3)"
name: "tspi_tpm_killmaintenancefeature"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_killmaintenancefeature/"
description: "Tspi_TPM_KillMaintenanceFeature – Disables the ability to create a maintenance archive"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_KillMaintenanceFeature &#8211; Disables the ability to create a maintenance archive </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_KillMaintenanceFeature(TSS_HTPM </code><i>hTPM</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_KillMaintenanceFeature</code> disables the functionality of creating a maintenance archive. <code>This feature is not yet implemented</code>. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_KillMaintenanceFeature</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_NOTIMPL</font></p>
<dd>The function is not implemented. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_KillMaintenanceFeature</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_createmaintenancearchive/">Tspi_TPM_CreateMaintenanceArchive</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_loadmaintenancepubkey/">Tspi_TPM_LoadMaintenancePubKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_checkmaintenancepubkey/">Tspi_TPM_CheckMaintenancePubKey</a></code>(3).</p>
