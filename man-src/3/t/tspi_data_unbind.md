---
title: "tspi_data_unbind(3)"
name: "tspi_data_unbind"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_data_unbind/"
description: "Tspi_Data_Unbind – Decrypts data that has been bound to a key"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Data_Unbind &#8211; Decrypts data that has been bound to a key </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Data_Unbind(TSS_HENCDATA </code><i>hEncData</i><code>, TSS_HKEY </code><i>hEncKey</i><code>,</code>
<code> UINT32* </code><i>pulUnboundDataLength</i><code>, BYTE** </code><i>prgbUnboundData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Data_Unbind</code> decrypts the encrypted data blob exportedfrom the data object used in <code>Tspi_Data_Bind</code>. The encrypted data blob must be imported to the object addressed by <code>Tspi_SetAttribData</code> before calling this method. </p>
<h2>Parameters</h2>
<h3>hEncData</h3>
<p>The handle of the data object which contains the encrypted data.</p>
<h3>hEncKey</h3>
<p>Handle to the key object addressing the private key which is used to decrypt the data.</p>
<h3>pulDataLength</h3>
<p>Receives the length of the data at the parameter <i>prgbUnboundData</i>.</p>
<h3>prgbUnboundData</h3>
<p>Receives a pointer to a buffer containing the plaintext data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Data_Unbind</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hEncData</i> or <i>hEncKey</i> is not a valid handle. </p>
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
<p><code>Tspi_Data_Unbind</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_data_bind/">Tspi_Data_Bind</a></code>(3), <code><a href="/docs/linux/man/3-tspi_data_unseal/">Tspi_Data_Unseal</a></code>(3), <code><a href="/docs/linux/man/3-tspi_data_seal/">Tspi_Data_Seal</a></code>(3).</p>
