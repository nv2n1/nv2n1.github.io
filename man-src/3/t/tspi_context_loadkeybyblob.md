---
title: "tspi_context_loadkeybyblob(3)"
name: "tspi_context_loadkeybyblob"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_loadkeybyblob/"
description: "Tspi_Context_LoadKeyByBlob – load a key into the TPM using the key’s blob."
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Context_LoadKeyByBlob &#8211; load a key into the TPM using the key&#8217;s blob. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_LoadKeyByBlob(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_HKEY </code><i>hUnwrappingKey</i><code>,</code>
<code> UINT32 </code><i>ulBlobLength</i><code>, BYTE* </code><i>rgbBlobData</i><code>,</code>
<code> TSS_HKEY* </code><i>phKey</i><code>); </code></pre>
<h2>Description</h2>
<p><code>Tspi_Context_LoadKeyByBlob</code> creates a key based on the information gotten by the key blob. It then loads the key into the TPM, which unwraps the key blob by using the key associated with <i>hUnwrappingKey</i>. The key blob addressed by hUnwrappingKey must have been already loaded into the TPM. This function returns a handle to the created key object. </p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The <i>hContext</i> parameter is the handle of the context object.</p>
<h3>hUnwrappingKey</h3>
<p>The <i>hUnwrappingKey</i> parameter is the handle of the key object which should be used to unwrap the key information associated with <i>rgbBlobData</i>.</p>
<h3>rgbBlobData</h3>
<p>The <i>rgbBlobData</i> parameter is the wrapped key to load.</p>
<h3>phKey</h3>
<p>The <i>phKey</i> parameter receives the handle of the key object representing the loaded key. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_LoadKeyByBlob</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_LoadKeyByBlob</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3), <code><a href="/docs/linux/man/3-tspi_policy_setsecret/">Tspi_Policy_SetSecret</a></code>(3), <code><a href="/docs/linux/man/3-tspi_getpolicyobject/">Tspi_GetPolicyObject</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_createkey/">Tspi_Key_CreateKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_getattribuint32/">Tspi_GetAttribUint32</a></code>(3).</p>
