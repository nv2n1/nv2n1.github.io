---
title: "tspi_tpm_checkmaintenancepubkey(3)"
name: "tspi_tpm_checkmaintenancepubkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_checkmaintenancepubkey/"
description: "Tspi_TPM_CheckMaintenancePubKey- check the public maintenance key"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_CheckMaintenancePubKey- check the public maintenance key </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_CheckMaintenancePubKey(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hMaintenanceKey</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_CheckMaintenancePubKey</code> checks the public maintenance key. If <i>hMaintenanceKey</i> is NULL, then <i>pValidationData</i> must not be NULL; the caller has to proof the digest on its own. If <i>hMaintenanceKey</i> is not NULL, then <i>pValidationData</i> must be NULL; the TSS service provider proofs the digest got internally from the TPM. The key information required for proofing the public maintenance key must be set in the key object by Tspi_SetAttribData before this method is called. <code>This function is not yet implemented</code>.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object </p>
<h3>hMaintenanceKey</h3>
<p>Handle of the maintenance key object </p>
<h3>pValidationData</h3>
<p>Validation data structure. [IN] Provide externalData information required to compute the signature. [OUT] On successful completion of the ocmmand, the structure provides a buffer containing the validation data and a buffer containing the data the validation data was computed from. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CheckMaintenancePubKey</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected.</p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more of the parameters is incorrect.</p>
<dt><font SIZE="-1">TSS_E_NOTIMPL</font></p>
<dd>The command is not implemented. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CheckMaintenancePubKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_loadmaintenancepubkey/">Tspi_TPM_LoadMaintenancePubKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_createmaintenancearchive/">Tspi_TPM_CreateMaintenanceArchive</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_killmaintenancefeature/">Tspi_TPM_KillMaintenanceFeature</a></code>(3).</p>
