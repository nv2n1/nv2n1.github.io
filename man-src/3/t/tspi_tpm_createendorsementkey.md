---
title: "tspi_tpm_createendorsementkey(3)"
name: "tspi_tpm_createendorsementkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_createendorsementkey/"
description: "Tspi_TPM_CreateEndorsementKey – create the endorsement key"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_CreateEndorsementKey &#8211; create the endorsement key </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_CreateEndorsementKey(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_CreateEndorsementKey</code> creates an endorsement key. <code>This function is currently not implemented</code>. Before this method is called, the key information for creating the key must be set in the key object by <i>Tspi_SetAttribData</i>. On return, the public endorsement key can be retrieved by <i>Tspi_GetAttribData</i> from the key object. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>hKey</h3>
<p>The <i>hKey</i> parameter is the handle of the key specifying the attributes of the endorsement key to create.</p>
<h3>pValidationData</h3>
<p>The <i>pValidationData</i> parameter is a validation data structure. It provides external information required to compute the signature. Once the command is completed, the structure provides a buffer containing the validation data and a buffer containing the data the validation data was computed from. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CreateEndorsementKey</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> or <i>hKey</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CreateEndorsementKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getpubendorsementkey/">Tspi_TPM_GetPubEndorsementKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_getpubkey/">Tspi_Key_GetPubKey</a></code>(3).</p>
