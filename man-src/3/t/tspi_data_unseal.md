---
title: "tspi_data_unseal(3)"
name: "tspi_data_unseal"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_data_unseal/"
description: "Tspi_Data_Unseal – dencrypt data encrypted by Tspi_Data_Seal() only if it was encrypted on the same platform and under the current configuration."
---

<p>Tspi_Data_Unseal &#8211; dencrypt data encrypted by Tspi_Data_Seal() only if it was encrypted on the same platform and under the current configuration.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Data_Unseal(TSS_HENCDATA </code><i>hEncData</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> UINT32 </code><i>pulUnsealedDataLength</i><code>, BYTE** </code><i>prgbUnsealedData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Data_Unseal</code> reveals data encrypted by the Tspi_Data_Seal only if it was encrypted on the same platform and the current configuration. This is internally proofed and guaranteed by the TPM.</p>
<h2>Parameters</h2>
<h3>hEncData</h3>
<p>Handle of the data object which contains the sealed data. </p>
<h3>hKey</h3>
<p>Handle to the key object addressing the nonmigratable key which is used to decrypt the data. </p>
<h3>pulUnsealedDataLength</h3>
<p>The length (in bytes) of the prgbUnsealedData parameter. </p>
<h3>prgbUnsealedData</h3>
<p>On successful completion of the command, this parameter points to a buffer containing the plaintext data. </p>
<h3>hPcrComposite</h3>
<p>Handle of the PCR Composite object specifying the PCRs which are part of the sealed data blob. Set to NULL, if the encrypted data should only be bound to the system and PCRs are not of interest.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Data_Unseal</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <code>hEncData</code> or <code>hKey</code> is not a valid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Data_Unseal</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_data_seal/">Tspi_Data_Seal</a></code>(3).</p>
