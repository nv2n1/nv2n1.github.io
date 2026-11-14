---
title: "tspi_hash_sethashvalue(3)"
name: "tspi_hash_sethashvalue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_hash_sethashvalue/"
description: "Tspi_Hash_SetHashValue – Sets the hash value of a hash object for non-SHA1 hash objects."
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Hash_SetHashValue &#8211; Sets the hash value of a hash object for non-SHA1 hash objects. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Hash_SetHashValue(TSS_HHASH </code><i>hHash</i><code>, UINT32 </code><i>ulHashValueLength</i><code>, BYTE* </code><i>rgbHashValue</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Hash_SetHashValue</code> sets the hash value of a hash object. If the object was created with the flag TSS_HASH_OTHER, then the hash identifier has to be set by calling <code>Tspi_SetAttribData</code> to perform the sign operation. </p>
<h2>Parameters</h2>
<h3>hHash</h3>
<p>The handle to the hash object instance whose hash value should be signed.</p>
<h3>ulHashValueLength</h3>
<p>Indicates the length of the hash value data provided at the parameter <i>rgbHashValue</i>.</p>
<h3>rgbHashValue</h3>
<p>A pointer to the hash value data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Hash_SetHashValue</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
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
<p><code>Tspi_Hash_SetHashValue</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_hash_updatehash/">Tspi_Hash_UpdateHash</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_sign/">Tspi_Hash_Sign</a></code>(3), <code><a href="/docs/linux/man/3-tspi_hash_gethashvalue/">Tspi_Hash_GetHashValue</a></code>(3).</p>
