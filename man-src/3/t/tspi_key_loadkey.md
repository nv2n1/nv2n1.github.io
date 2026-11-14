---
title: "tspi_key_loadkey(3)"
name: "tspi_key_loadkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_loadkey/"
description: "Tspi_Key_LoadKey – load a key into the TPM"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Key_LoadKey &#8211; load a key into the TPM </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_LoadKey(TSS_HKEY </code><i>hKey</i><code>, TSS_HKEY </code><i>hUnwrappingKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Key_LoadKey</code> loads the key referenced by <i>hKey</i> into the TPM. </p>
<h2>Parameters</h2>
<h3>hKey</h3>
<p>The <i>hKey</i> parameter is the handle of the key object to load.</p>
<h3>hUnwrappingKey</h3>
<p>The <i>hUnwrappingKey</i> parameter is the handle of the key which should be used to unwrap the key addressed by <i>hKey</i>. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_LoadKey</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd>Either <i>hKey</i> or <i>hUnwrappingKey</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_LoadKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_unloadkey/">Tspi_Key_UnloadKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_getpubkey/">Tspi_Key_GetPubKey</a></code>(3).</p>
