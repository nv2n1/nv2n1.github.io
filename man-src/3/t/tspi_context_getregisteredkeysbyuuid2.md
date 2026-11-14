---
title: "tspi_context_getregisteredkeysbyuuid2(3)"
name: "tspi_context_getregisteredkeysbyuuid2"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_getregisteredkeysbyuuid2/"
description: "Tspi_Context_GetRegisteredKeysByUUID2 – get an array of TSS_KM_KEYINFO2 structures based on the state of persistent storage."
---

<p>Tspi_Context_GetRegisteredKeysByUUID2 &#8211; get an array of TSS_KM_KEYINFO2 structures based on the state of persistent storage.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_GetRegisteredKeysByUUID2(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>persistentStorageType</i><code>,</code>
<code> TSS_UUID* </code><i>pUuidData</i><code>, UINT32* </code><i>pulKeyHierarchySize</i><code>,</code>
<code> TSS_KM_KEYINFO2** </code><i>ppKeyHierarchy</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_GetRegisteredKeysByUUID2</code> gets an array of TSS_KM_KEYINFO2 structures. This information reflects the state of the registered key hierarchy. The keys stored in the persistent storage are totallly independent from either the context provided in the function call or the context, which was provided while processing the key registration.</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>persistentStorageType</h3>
<p>Flag indicating the persistent storage the key is registered in. </p>
<h3>pUuidData</h3>
<p>The UUID the key was registered in the persistent storage (TSP or connected TCS). If no key UUID is provided, thus KeyUUID is NULL, the returned array of the TSS_KM_KEYINFO2 structure contains data reflecting the whole key hierarchy starting with root key. If a certain key is UUID is provided, the returned array of TSS_KM_KEYINFO2 structures only contains data reflecting the path of the key hierarchy regarding that key. The first array entry is the key addressed by the given UUID followed by its parent key up to the root key. </p>
<h3>pulKeyHierarchySize</h3>
<p>Recieves the length (number of array entries) of the ppKeyHierarchy parameter. </p>
<h3>ppKeyHierarchy</h3>
<p>On successful completion of the command, this parameter points to a buffer containing the actual key hierarchy data.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetRegisteredKeysByUUID2</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hContext</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS.</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetRegisteredKeysByUUID2</code> conforms to the Trusted Computing Group Software Specification version 1.2</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3).</p>
