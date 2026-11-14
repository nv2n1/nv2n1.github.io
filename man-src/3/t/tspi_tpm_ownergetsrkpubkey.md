---
title: "tspi_tpm_ownergetsrkpubkey(3)"
name: "tspi_tpm_ownergetsrkpubkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_ownergetsrkpubkey/"
description: "Tspi_TPM_OwnerGetSRKPubKey – get public key of the SRK"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_OwnerGetSRKPubKey &#8211; get public key of the SRK </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_OwnerGetSRKPubKey(TSS_HTPM </code><i>hTPM</i><code>,</code>
<code> UINT32* </code><i>pulPubKeyLength</i><code>,</code>
<code> BYTE** </code><i>prgbPubKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_OwnerGetSRKPubKey</code> returns the public key of the key object using owner authorization. This can only be used on 1.2 TPMs, and only to return the public key of the SRK. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>pulPubKeyLength</h3>
<p>The <i>pulPubKeyLength</i> parameter is the length (in bytes) of the prgbPubKey parameter.</p>
<h3>prgbPubKey</h3>
<p>The <i>prgbPubKey</i> parameter is the pointer to the memory block containing the public key blob retrieved for the key object referenced by hKey. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_OwnerGetSRKPubKey</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_TPM_UNSUPPORTED</font></p>
<dd>The TPM is not version 1.2 or later &#8211; (Note: still unimplemented) </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_OwnerGetSRKPubKey</code> conforms to the Trusted Computing Group Software Specification version 1.2 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_freememory/">Tspi_Context_FreeMemory</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_getpubkey/">Tspi_Key_GetPubKey</a></code>(3).</p>
