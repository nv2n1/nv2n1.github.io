---
title: "tspi_hash_verifysignature(3)"
name: "tspi_hash_verifysignature"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_hash_verifysignature/"
description: "Tspi_Hash_VerifySignature – verify the hash value with a given signature"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Hash_VerifySignature &#8211; verify the hash value with a given signature </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Hash_VerifySignature(TSS_HHASH </code><i>hHash</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> UINT32 </code><i>ulSignatureLength</i><code>, BYTE* </code><i>rgbSignature</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Hash_VerifySignature</code> verifies the hash value of a given hash object with a given signature. In order to use this command, one must have a hash and a signature of the hash that one is trying to verify. The public key which corresponds to the private key used to sign the hash is also needed. </p>
<h2>Parameters</h2>
<h3>hHash</h3>
<p>The handle to the hash object instance whose hash value should be signed.</p>
<h3>hKey</h3>
<p>Handle to the key object which should be used for the signature verification.</p>
<h3>ulSignatureLength</h3>
<p>The length of the signature data provided at the parameter <i>rgbSignature</i>.</p>
<h3>rgbSignature</h3>
<p>A pointer to the signature data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Hash_VerifySignature</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
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
<dt><font SIZE="-1">TSS_E_INVALID_SIGSCHEME</font></p>
<dd>Invalid signature scheme. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Hash_VerifySignature</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_hash_updatehash/">Tspi_Hash_UpdateHash</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sethashvalue/">Tspi_Hash_SetHashValue</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sign/">Tspi_Hash_Sign</a></code>(3), <a href="/docs/linux/man/3-tspi_hash_gethashvalue/">Tspi_Hash_GetHashValue</a>(3).</p>
