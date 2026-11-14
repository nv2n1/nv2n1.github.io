---
title: "tspi_hash_updatehashvalue(3)"
name: "tspi_hash_updatehashvalue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_hash_updatehashvalue/"
description: "Tspi_Hash_UpdateHashValue – update the hash value of a hash object"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Hash_UpdateHashValue &#8211; update the hash value of a hash object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Hash_UpdateHashValue(TSS_HHASH </code><i>hHash</i><code>, UINT32 </code><i>ulDataLength</i><code>, BYTE* </code><i>rgbData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Hash_UpdateHashValue</code> updates the hash value of a hash object with new information. If the object was created with the flag TSS_HASH_OTHER, then this method will return an error. <code>The object can&#8217;t be modified after Tspi_Hash_SetHashValue, Tspi_Hash_GetHashValue, Tspi_Hash_Sign, or Tspi_Hash_VerifySignature have been called on it.</code> </p>
<h2>Parameters</h2>
<h3>hHash</h3>
<p>The handle to the hash object instance whose hash value should be signed.</p>
<h3>ulDataLength</h3>
<p>Indicates the length of the data provided at the parameter <i>rgbData</i>.</p>
<h3>rgbData</h3>
<p>A pointer to the data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Hash_UpdateHashValue</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
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
<p><code>Tspi_Hash_UpdateHashValue</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_hash_gethashvalue/">Tspi_Hash_GetHashValue</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sign/">Tspi_Hash_Sign</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sethashvalue/">Tspi_Hash_SetHashValue</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_verifysignature/">Tspi_Hash_VerifySignature</a></code>(3).</p>
