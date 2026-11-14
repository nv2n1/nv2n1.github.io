---
title: "tspi_context_loadkeybyuuid(3)"
name: "tspi_context_loadkeybyuuid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_loadkeybyuuid/"
description: "Tspi_Context_LoadKeyByUUID – load a key that’s been registered in persistent storage."
---

<p>Tspi_Context_LoadKeyByUUID &#8211; load a key that&#8217;s been registered in persistent storage.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_LoadKeyByUUID(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>persistentStorageType</i><code>, </code>
<code> TSS_UUID </code><i>uuidData</i><code>, TSS_HKEY* </code><i>phKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_LoadKeyByUUID</code> creates a key object based on the information got from the manager using the UUID and loads the key into the TPM. The persistent storage provides all information to load the parent keys required to load the key associated with the given UUID.</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>persistentStorageType</h3>
<p>Flag indicating the persistent storage the key is registered in. Should be either TSS_PS_TYPE_USER ot TSS_PS_TYPE_SYSTEM. </p>
<h3>uuidData</h3>
<p>The UUID of the key by which the key was registered in the persistent storage (TSP or connected TCS). </p>
<h3>phKey</h3>
<p>Receives the handle of the key object representing the loaded key.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_LoadKeyByUUID</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hContext</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER &#8211; <i>persistentStorageType</i> is not valid.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS.</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_LoadKeyByUUID</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_loadkeybyblob/">Tspi_Context_LoadKeyByBlob</a>(3)</code>, <code><a href="/docs/linux/man/3-tspi_key_loadkey/">Tspi_Key_LoadKey</a>(3)</code>.</p>
