---
title: "tspi_tpm_collateidentityrequest(3)"
name: "tspi_tpm_collateidentityrequest"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_collateidentityrequest/"
description: "Tspi_TPM_CollateIdentityRequest – Gets all the informatin necessary to send to a trusted third party (TTP), repartory to asking the TTP to create a certificate for identity."
---

<p>Tspi_TPM_CollateIdentityRequest &#8211; Gets all the informatin necessary to send to a trusted third party (TTP), repartory to asking the TTP to create a certificate for identity.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_CollateIdentityRequest(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hKeySRK</i><code>,</code>
<code> TSS_HKEY </code><i>hCAPPubKey</i><code>,</code>
<code> UINT32 </code><i>ulIdentityLabelData</i><code>, BYTE* </code><i>rgbIdentityLabelData</i><code>,</code>
<code> TSS_HKEY </code><i>hIdentityKey</i><code>, TSS_ALGORITHM_ID </code><i>algid</i><code>,</code>
<code> UINT32* </code><i>pulTCPAIdentityReqLength</i><code>, BYTE** </code><i>prgbTCPAIdentityReq</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_TPM_CollateIdentityRequest</code> creates an identity key, binds it to the label and returns a certificate request package. The privacty CA requires this certificate request to attest the identity key. </p>
<p> Only the Owner of the TPM has the privledge of creating a TPM identity key. </p>
<p> The symmetric session key is required to provide confidentiality of the &quot;TCPA_IDENTITY_REQ&quot; data structure, which should be sent to the Privacy CA chosen by the owner.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object. </p>
<h3>hKeySRK</h3>
<p>Handle to the key object representing the Storage Root Key </p>
<h3>hCAPubKey</h3>
<p>Handle to the key object representing the public key of the CA which signs the certificate of the created identity key. </p>
<h3>ulIdentityLabelLength</h3>
<p>Supplies the length (in bytes) of the rgbIdentityLabelData parameter </p>
<h3>rgbLabelData</h3>
<p>Pointer to a memory block containing the identity label, which should be a UNICODE string </p>
<h3>hIdentityKey</h3>
<p>Handle to the identity key object </p>
<h3>algid</h3>
<p>The type of symmetric algorithm touse as requred by the Enhanced CA. </p>
<h3>pulTCPAIdentityReqLength</h3>
<p>Recieves the length (in bytes) of the prgbTCPAIdentityReq parameter </p>
<h3>prgbTCPAIdentyReq</h3>
<p>Pointer to the memory block containing the certicficate request structure.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CollateIdentityRequest</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd>Either <code>hTPM</code> or <code>hKeySRK</code> or <code>hCAPubKey</code> is not a valid handle.</p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS.</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CollateIdentityRequest</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3).</p>
