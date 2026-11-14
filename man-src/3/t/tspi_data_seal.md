---
title: "tspi_data_seal(3)"
name: "tspi_data_seal"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_data_seal/"
description: "Tspi_Data_Seal – encrypt a data blob in a mannar that is only decryptable by Tspi_Data_Unseal on the same system."
---

<p>Tspi_Data_Seal &#8211; encrypt a data blob in a mannar that is only decryptable by Tspi_Data_Unseal on the same system.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Data_Seal(TSS_HENCDATA </code><i>hEncData</i><code>, TSS_HKEY </code><i>hEncKey</i><code>,</code>
<code> UINT32 </code><i>ulDataLength</i><code>, BYTE* </code><i>rgbDataToSeal</i><code>,</code>
<code> TSS_HPCRS </code><i>hPcrComposite</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Data_Seal</code> encrypts a data blob in a mannar that is only decryptable by Tspi_Data_Unseal on the same system. The data blob is encrypted using a public key operation with the nonmigratable key addressed by the given encryption key object.</p>
<h2>Parameters</h2>
<h3>hEncData</h3>
<p>Handle of the data object which contains the sealed data on successful completion of the command. </p>
<h3>hEncKey</h3>
<p>Handle to the key object addressing the nonmigratable key which is used to encrypt the data. </p>
<h3>ulDataLength</h3>
<p>The Length (in bytes) of the rgbDataToSeal parameter. </p>
<h3>rgbDataToSeal</h3>
<p>Pointer to memory containing the data to be encrypted. </p>
<h3>hPcrComposite</h3>
<p>Handle of the PCR Composite object specifying the PCRs which are part of the sealed data blob. Set to NULL, if the encrypted data should only be bound to the system and PCRs are not of interest.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Data_Seal</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; One of the following parameters <i>hEncData</i>, <i>hEncKey</i>, <i>rgbDataToSeal</i> is invalid.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Data_Seal</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_data_unseal/">Tspi_Data_Unseal</a></code>(3).</p>
