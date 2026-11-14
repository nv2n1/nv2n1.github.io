---
title: "tspi_encodeder_tssblob(3)"
name: "tspi_encodeder_tssblob"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_encodeder_tssblob/"
description: "Tspi_EncodeDER_TssBlob – generate a DER encoded TSS blob."
---

<p>Tspi_EncodeDER_TssBlob &#8211; generate a DER encoded TSS blob.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_EncodeDER_TssBlob(UINT32 </code><i>rawBlobSize</i><code>, BYTE* </code><i>rawBlob</i><code>,</code>
<code> UINT32 </code><i>blobType</i><code>, UINT32* </code><i>derBlobSize</i><code>,</code>
<code> BYTE* </code><i>derBlob</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_EncodeDER_TssBlob</code> is used to generate a DER-encoded blob in accordance with the ASN.1 data definitions in the Portable Data section of the Trusted Computing Group Software Stack Specification Version 1.2.</p>
<h2>Parameters</h2>
<h3>rawBlobSize</h3>
<p>Size of the unwrapped blob. </p>
<h3>rawBlob</h3>
<p>Pointer to the unwrapped blob. </p>
<h3>blobType</h3>
<p>Type of blob being wrapped (refer to the TSS_BLOB_TYPE_* constants). </p>
<h3>derBlobSize</h3>
<p>Pointer to the size of the derBlob buffer. On input this parameter contains a pointer to the maximum size of the supplied derBlob buffer. On output this parameter contains a pointer to the actual size of the DER-encoded blob. On input, if this parameter points to a value of 0, then this function will return the size of the buffer required to hold the DER-encoded blob without writing to the derBlob buffer. </p>
<p> <code>Note:</code> If the raw data blob length is less than 2^16 bytes then the DER-encoding may add no more than 20 bytes. </p>
<h3>derBlob</h3>
<p>Pointer to a buffer to hold the DER-encoded blob.</p>
<h2>Return Codes</h2>
<p><code>Tspi_EncodeDER_TssBlob</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_EncodeDER_TssBlob</code> conforms to the Trusted Computing Group Software Specification Version 1.2</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_decodeber_tssblob/">Tspi_DecodeBER_TssBlob</a></code>(3).</p>
