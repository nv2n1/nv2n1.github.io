---
title: "tspi_context_getkeybypublicinfo(3)"
name: "tspi_context_getkeybypublicinfo"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_getkeybypublicinfo/"
description: "Tspi_Context_GetKeyByPublicInfo – search the persistent storage for a registered key using the provided public key information"
---

<p>Tspi_Context_GetKeyByPublicInfo &#8211; search the persistent storage for a registered key using the provided public key information</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_GetKeyByPublicInfo(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>persistentStorageType</i><code>,</code>
<code> TSS_ALGORITHM_ID </code><i>algID</i><code>, UINT32 </code><i>ulPublicInfoLength</i><code>,</code>
<code> BYTE* </code><i>rgbPublicInfo</i><code>, TSS_HKEY* </code><i>phKey</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_GetKeyByPublicInfo</code> searches the persistent storage for a registered key using the provided public key information and creates a key object initalized according to the found data. On successful completion of the method a handle to the created new key object is returned.</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>persistentStorageType</h3>
<p>Flag indicating the persistent storage the key is registered in. </p>
<h3>algId</h3>
<p>This parameter indicates the algorithm of the requested key. </p>
<h3>ulPublicInfoLength</h3>
<p>The length of the public key info provided at the parameter rgbPublicInfo. </p>
<h3>rgbPublicInfo</h3>
<p>The public key info is provided to identify the key to be look for at the persistent storage. In case algID equals to TSS_ALG_RSA this prameter contains the modulus of the public RSA key. </p>
<h3>hKey</h3>
<p>Recieves the handle of the key object representing the key. In case the key hasn&#8217;t been found, this value will be NULL.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_GetKeyByPublicInfo</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hContext</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_GetKeyByPublicInfo</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3).</p>
