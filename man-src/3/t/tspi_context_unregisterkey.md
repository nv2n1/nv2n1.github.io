---
title: "tspi_context_unregisterkey(3)"
name: "tspi_context_unregisterkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_unregisterkey/"
description: "Tspi_Context_UnregisterKey – unregister a key from the persistent storage device."
---

<p>Tspi_Context_UnregisterKey &#8211; unregister a key from the persistent storage device.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_UnregisterKey(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>persistentStorageType</i><code>,</code>
<code> TSS_UUID </code><i>uuidKey</i><code>, TSS_HKEY* </code><i>phKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_UnregisterKey</code> provides the capabilities of the TSS Core Service or TSS Service Provider</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>persistentStorageType</h3>
<p>Flag indicating the persistent storage. </p>
<h3>uuidKey</h3>
<p>The UUID of the key to be removed from the persistent storage. </p>
<h3>phKey</h3>
<p>Recieves the handle of a key object containing the information from the archive. </p>
<h3>pulRespDataLength</h3>
<p>Recieves the length (in bytes) of the prgbRespData parameter. </p>
<h3>prgbRespData</h3>
<p>On successful completion of the command, this parameter points to the buffer containing the actual data of the specified capability. The handle of the object to be destroyed </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_UnregisterKey</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; the parameter <i>hContext</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_PS_KEY_NOTFOUND &#8211; the parameter <i>uuidKey</i> is an invalid UUID.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
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
<p><code>Tspi_Context_UnregisterKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_createkey/">Tspi_Key_CreateKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_registerkey/">Tspi_Context_RegisterKey</a></code>(3).</p>
