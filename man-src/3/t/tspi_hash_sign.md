---
title: "tspi_hash_sign(3)"
name: "tspi_hash_sign"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_hash_sign/"
description: "Tspi_Hash_Sign – sign the hash data of an object with a signing key"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Hash_Sign &#8211; sign the hash data of an object with a signing key </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Hash_Sign(TSS_HHASH </code><i>hHash</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> UINT32 </code><i>pulSignatureLength</i><code>, BYTE** </code><i>prgbSignature</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Hash_Sign</code> signs the hash data of an object with a given signing key. The data must be set at the hash instance associated with <i>hHash</i> by calling <code>Tspi_Hash_SetHashValue</code> or <code>Tspi_Hash_UpdateHash</code>. The <code>Tspi_Hash_Sign</code> method allocates a memory block for the <i>prgbSignature</i> data. This memory must be released using <code>Tspi_Context_FreeMemory</code>. </p>
<h2>Parameters</h2>
<h3>hHash</h3>
<p>The handle to the hash object instance whose hash value should be signed.</p>
<h3>hKey</h3>
<p>Handle to the key object which should be used for the signature.</p>
<h3>pulSignatureLength</h3>
<p>Receives the length of the signature data returned at the parameter <i>prgbSignature</i> on successful completion.</p>
<h3>prgbSignature</h3>
<p>Receives a pointer to the signature data on successful completion. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Hash_Sign</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hKey</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
<dt><font SIZE="-1">TSS_E_HASH_INVALID_LENGTH</font></p>
<dd>Hash length is inconsistent with hash algorithm. </p>
<dt><font SIZE="-1">TSS_E_HASH_NO_DATA</font></p>
<dd>Hash object has no internal hash value. </p>
<dt><font SIZE="-1">TSS_E_HASH_NO_IDENTIFIER</font></p>
<dd>The hash algorithm identifier is not set. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Hash_Sign</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_hash_updatehash/">Tspi_Hash_UpdateHash</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sethashvalue/">Tspi_Hash_SetHashValue</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_verifysignature/">Tspi_Hash_VerifySignature</a></code>(3).</p>
