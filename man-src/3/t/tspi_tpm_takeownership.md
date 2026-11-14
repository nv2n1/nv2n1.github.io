---
title: "tspi_tpm_takeownership(3)"
name: "tspi_tpm_takeownership"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_takeownership/"
description: "Tspi_TPM_TakeOwnership – take ownership of a TPM"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_TakeOwnership &#8211; take ownership of a TPM </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_TakeOwnership(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hKeySRK</i><code>,</code>
<code> TSS_HKEY </code><i>hEndorsementPubKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_TakeOwnership</code> takes ownership of a TPM. Taking ownership is the process of inserting a shared secret into the TPM. The owner of the TPM (anyone who knows the shared secret) has the right to perform special operations. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>hKeySRK</h3>
<p>The <i>hKeySRK</i> parameter is the handle to the object representing the TPM&#8217;s Storage Root Key.</p>
<h3>hEndorsementPubKey</h3>
<p>The <i>hEndorsementPubKey</i> parameter is the handle to the object representing the TPM&#8217;s endorsement public key. This key is required for encrypting the secret of the SRK and the TPM owner secret. If NULL, the TSP internally queries the TPM for that endorsement public key. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_TakeOwnership</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd>Either the TPM or one of the key handles is not valid. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_TakeOwnership</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_clearowner/">Tspi_TPM_ClearOwner</a></code>(3)</p>
