---
title: "tspi_data_bind(3)"
name: "tspi_data_bind"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_data_bind/"
description: "Tspi_Data_Bind – Encrypts a data blob"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Data_Bind &#8211; Encrypts a data blob </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Data_Bind(TSS_HENCDATA </code><i>hEncData</i><code>, TSS_HKEY </code><i>hEncKey</i><code>,</code>
<code> UINT32 </code><i>ulDataLength</i><code>, BYTE* </code><i>rgbDataToBind</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Data_Bind</code> encrypts a data blob in a manner that is decryptable by <code>Tspi_Data_Unbind</code>. The data blob is encrypted using a public key operation with the key addressed by the given encryption key object. To bind data that is larger than the RSA public key modulus is the responsibility of the caller to perform the blocking and subsequent combination of data. The bound data blob is stored in the data object addressed by <i>hEncData</i> and can be exported from the object by <code>Tspi_GetAttribData</code>. The caller of this function should perform validations that the public key presented to it is from a valid TPM. </p>
<h2>Parameters</h2>
<h3>hEncData</h3>
<p>The handle of the data object which contains the encrypted data on successful completion of the command.</p>
<h3>hEncKey</h3>
<p>Handle to the key object addressing the public key which is used to encrypt the data.</p>
<h3>ulDataLength</h3>
<p>Indicates the length of the data provided at the parameter <i>rgbDataToBind</i>.</p>
<h3>rgbDataToBind</h3>
<p>A pointer to the data to be encrypted. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Data_Bind</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hHash</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
<dt><font SIZE="-1">TSS_E_INVALID_ENCSCHEME</font></p>
<dd>Invalid encryption scheme. </p>
<dt><font SIZE="-1">TSS_E_ENC_INVALID_LENGTH</font></p>
<dd>Invalid length of data to be encypted. </p>
<dt><font SIZE="-1">TSS_E_ENC_NO_DATA</font></p>
<dd>No data to encrypt. </p>
<dt><font SIZE="-1">TSS_E_ENC_INVALID_TYPE</font></p>
<dd>Invalid encryption type. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Data_Bind</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_data_unbind/">Tspi_Data_Unbind</a></code>(3), <code><a href="/docs/linux/man/3-tspi_data_unseal/">Tspi_Data_Unseal</a></code>(3), <code><a href="/docs/linux/man/3-tspi_data_seal/">Tspi_Data_Seal</a></code>(3).</p>
