---
title: "tspi_context_getkeybyuuid(3)"
name: "tspi_context_getkeybyuuid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_getkeybyuuid/"
description: "Tspi_Context_GetKeyByUUID – get a handle to a key registered in persistent storage."
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Context_GetKeyByUUID &#8211; get a handle to a key registered in persistent storage. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_GetKeyByUUID(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>persistentStorageType</i><code>,</code>
<code> TSS_UUID </code><i>uuidData</i><code>, TSS_HKEY* </code><i>phKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Context_GetKeyByUUID</code> searches the Persistent Storage database for a registered key using the given UUID. It then creates a key object initialized to the found data and returns a handle to the key object. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle of the context object.</p>
<h3>persistentStorageType</h3>
<p>The <i>persistentStorageType</i> parameter indicates the persistent storage the key is registered in.</p>
<h3>uuidData</h3>
<p>The <i>uuidData</i> parameter is the UUID by which the key is registered in persistent storage.</p>
<h3>phKey</h3>
<p>The <i>phKey</i> parameter receives the handle of the key object representing the key. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetKeyByUUID</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is an invalid handle. </p>
<dt><font SIZE="-1">TSS_E_PS_KEY_NOTFOUND</font></p>
<dd>The key cannot be found in the persistent storage database. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetKeyByUUID</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_gettpmobject/">Tspi_Context_GetTpmObject</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_getregisteredkeysbyuuid/">Tspi_Context_GetRegisteredKeysByUUID</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_getkeybypublicinfo/">Tspi_Context_GetKeyByPublicInfo</a></code>(3).</p>
