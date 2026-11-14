---
title: "tspi_decodeber_tssblob(3)"
name: "tspi_decodeber_tssblob"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_decodeber_tssblob/"
description: "Tspi_DecodeBER_TssBlob – unwraps a BER-encoded TSS blob."
---

<p>Tspi_DecodeBER_TssBlob &#8211; unwraps a BER-encoded TSS blob.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_DecodeBER_TssBlob(UINT32 </code><i>berBlobSize</i><code>, BYTE* </code><i>berBlob</i><code>,</code>
<code> UINT32* </code><i>blobType</i><code>, UINT32* </code><i>rawBlobSize</i><code>,</code>
<code> BYTE* </code><i>rawBlob</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_DecodeBER_TssBlob</code> is used to unwrap a BER-encoded blob in accordance with the ASN.1 data definitions in the Portable Data section of the Trusted Computing Group Software Stack Specification Version 1.2.</p>
<h2>Parameters</h2>
<h3>berBlobSize</h3>
<p>Size of the BER-encoded blob. </p>
<h3>berBlob</h3>
<p>Pointer to the BER-encoded blob. </p>
<h3>blobType</h3>
<p>Pointer to the type of blob being unwrapped (refer to the TSS_BLOB_TYPE_* constants). </p>
<h3>rawBlobSize</h3>
<p>Pointer to the size of the rawBlob buffer. On input this parameter contains a pointer to the maximum size of the supplied rawBlob buffer. On output this parameter contains a pointer to the actual size of the unwrapped blob. On input, if this parameter points to a value of 0, then this function will return the size of the buffer required to hold the unwrapped blob without writing to the rawBlob buffer. </p>
<p> <code>Note:</code> The output data must be shorter than the BER-encoding, so berBlobSize is a useful upper limit on rawBlob buffer size. </p>
<h3>rawBlob</h3>
<p>Pointer to a buffer to hold the unwrapped blob.</p>
<h2>Return Codes</h2>
<p><code>Tspi_EncodeDER_TssBlob</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_DecodeBER_TssBlob</code> conforms to the Trusted Computing Group Software Specification Version 1.2</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_decodeber_tssblob/">Tspi_DecodeBER_TssBlob</a></code>(3).</p>
