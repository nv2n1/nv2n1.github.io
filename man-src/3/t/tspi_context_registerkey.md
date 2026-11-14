---
title: "tspi_context_registerkey(3)"
name: "tspi_context_registerkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_registerkey/"
description: "Tspi_Context_RegisterKey – register a key in the TSS Persistent Storage database"
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Context_RegisterKey &#8211; register a key in the TSS Persistent Storage database </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_RegisterKey(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> TSS_FLAG </code><i>persistentStorageType</i><code>, TSS_UUID </code><i>uuidKey</i><code>,</code>
<code> TSS_FLAG </code><i>persistentStorageTypeParent</i><code>, TSS_UUID </code><i>uuidParentKey</i><code>); </code></pre>
<h2>Description</h2>
<p><code>Tspi_Context_RegisterKey</code> is the API that registers a key with the TSS Persistent Storage database so that it can be loaded as necessary. It also includes all information required for loading the key, as well as information about its parent key. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle of the context object.</p>
<h3>hKey</h3>
<p>The <i>hKey</i> parameter is the handle of the key object addressing the key to be registered.</p>
<h3>persistentStorageType</h3>
<p>The <i>persistentStorageType</i> parameter indicates the persistent storage the key is registered in.</p>
<h3>uuidKey</h3>
<p>The <i>uuidKey</i> parameter is the UUID by which the key is registered in persistent storage.</p>
<h3>persistentStorageTypeParent</h3>
<p>The <i>persistentStorageTypeParent</i> parameter indicates the persistent storage that the parent key is registered in.</p>
<h3>uuidParentKey</h3>
<p>The <i>uuidParentKey</i> parameter is the UUID by which the parent key is registered in persistent storage. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_RegisterKey</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_PS_KEY_NOTFOUND</font></p>
<dd>The key cannot be found in the persistent storage database. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Example</h2>
<pre>#include &lt;trousers/tss.h&gt;
int
main(void)
{
 TSS_FLAGS initFlags = ...;
 TSS_HKEY hKey, hSRK;
 TSS_UUID keyUUID = {...};
 // Create a TSP handle
 result = Tspi_Context_Create(&amp;hContext);
 if (result != TSS_SUCCESS)
 Error_Path();
 // Connect to the TCSD
 result = Tspi_Context_Connect(hContext, GLOBALSERVER);
 if (result != TSS_SUCCESS)
 Error_Path();
 // Create the Key Object
 result = Tspi_Context_CreateObject(hContext,
 TSS_OBJECT_TYPE_RSAKEY,
 initFlags, &amp;hKey);
 if (result != TSS_SUCCESS)
 Error_Path();
 // Load parent Key by UUID
 result = Tspi_Context_LoadKeyByUUID(hContext, TSS_PS_TYPE_SYSTEM,
 SRK_UUID, &amp;hSRK);
 if (result != TSS_SUCCESS)
 Error_Path();
 // Do policy/secret handling here
 result = Tspi_Key_CreateKey(hKey, hSRK, 0);
 if (result != TSS_SUCCESS)
 Error_Path();
 // Register the Key in System PS (on the TCSD's platform)
 result = Tspi_Context_RegisterKey(hContext, hKey, TSS_PS_TYPE_SYSTEM,
 keyUUID, TSS_PS_TYPE_SYSTEM,
 SRK_UUID);
 if (result != TSS_SUCCESS)
 Error_Path();
 /* ...
 *
 * Use the key as needed, exiting the program if necessary, reloading
 * the key using Tspi_Context_LoadKeyByUUID() after each restart. Once
 * the key is no longer useful, unregister it from system PS as part
 * of clean up.
 */
 // Unregister the Key
 result = Tspi_Context_UnregisterKey(hContext, TSS_PS_TYPE_SYSTEM,
 migratableSignUUID, &amp;hKey);
 if (result != TSS_SUCCESS)
 Error_Path();
 // exit, discarding hKey
}</pre>
<h2>Conforming To</h2>
<p><code>Tspi_Context_RegisterKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_unregisterkey/">Tspi_Context_UnregisterKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_getregisteredkeybyuuid/">Tspi_Context_GetRegisteredKeyByUUID</a></code>(3).</p>
