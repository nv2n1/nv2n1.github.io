---
title: "tspi_tpm_getpubendorsementkey(3)"
name: "tspi_tpm_getpubendorsementkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getpubendorsementkey/"
description: "Tspi_TPM_GetPubEndorsementKey – create a TSS key object from the TPM’s public endorsement key"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_GetPubEndorsementKey &#8211; create a TSS key object from the TPM&#8217;s public endorsement key </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetPubEndorsementKey(TSS_HTPM </code><i>hTPM</i><code>, TSS_BOOL </code><i>fOwnerAuthorized</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code>, TSS_HKEY* </code><i>phEndorsementPubKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetPubEndorsementKey</code> This function retrieves the public endorsement key (PubEK) from the TPM and creates a TSS key object for it, whose handle is returned in <i>phEndorsementPubKey</i>. Due to the fact that different TPM chips validate the PubEK in different ways, application verification of the PubEK (using a non-NULL <i>pValidationData</i> is <code>broken</code>. Tspi_TPM_GetPubEndorsementKey should be called with a NULL <i>pValidationData</i> parameter to allow the TSS to verify the PubEK itself. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>fOwnerAuthorized</h3>
<p>If TRUE, the TPM owner secret must be provided to get the public endorsement key. If FALSE, no TPM owner secret must be provided to get the public endorsement key.</p>
<h3>pValidationData</h3>
<p>If non-NULL, the application should set the pValidationData-&gt;rgbExternalData parameter to 20 bytes of random data before calling Tspi_TPM_GetPubEndorsementKey. On successful completion of the command, the structure will provide buffers containing the validation data and the buffer the validation data was computed from.</p>
<h3>phEndorsementPubKey</h3>
<p>Receives a handle to a key object representing the TPM&#8217;s public endorsement key. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetPubEndorsementKey</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
<dt><font SIZE="-1">TPM_E_DISABLED_CMD</font></p>
<dd>Reading of PubEK from TPM has been disabled. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetPubEndorsementKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_getpubkey/">Tspi_Key_GetPubKey</a></code>(3).</p>
