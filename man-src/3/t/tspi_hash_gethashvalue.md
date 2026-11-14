---
title: "tspi_hash_gethashvalue(3)"
name: "tspi_hash_gethashvalue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_hash_gethashvalue/"
description: "Tspi_Hash_GetHashValue – get the current hash value of a hash object"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Hash_GetHashValue &#8211; get the current hash value of a hash object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Hash_GetHashValue(TSS_HHASH </code><i>hHash</i><code>, UINT32* </code><i>pulHashValueLength</i><code>, BYTE** </code><i>prgbHashValue</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Hash_GetHashValue</code> gets the hash value of a hash object. <code>Tspi_Context_FreeMemory</code> must be used to clean up after this function, as memory is allocated for the <i>prgbHashValue</i> data. </p>
<h2>Parameters</h2>
<h3>hHash</h3>
<p>The handle to the hash object instance whose hash value should be signed.</p>
<h3>pulHashValueLength</h3>
<p>Receives the length of the hash value data returned at the parameter <i>prgbHashValue</i>.</p>
<h3>prgbHashValue</h3>
<p>Receives a pointer to the hash value data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Hash_GetHashValue</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hHash</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
<dt><font SIZE="-1">TSS_E_HASH_INVALID_LENGTH</font></p>
<dd>Hash length is inconsistent with hash algorithm. </p>
<dt><font SIZE="-1">TSS_E_HASH_NO_DATA</font></p>
<dd>Hash object has no internal hash value. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Hash_GetHashValue</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_hash_updatehash/">Tspi_Hash_UpdateHash</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sign/">Tspi_Hash_Sign</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_verifysignature/">Tspi_Hash_VerifySignature</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sethashvalue/">Tspi_Hash_SetHashValue</a></code>(3).</p>
