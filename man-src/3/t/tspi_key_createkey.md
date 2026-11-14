---
title: "tspi_key_createkey(3)"
name: "tspi_key_createkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_createkey/"
description: "Tspi_Key_CreateKey – create a key pair within the TPM, wrapping it with the key addressed by hWrappingKey."
---

<p>Tspi_Key_CreateKey &#8211; create a key pair within the TPM, wrapping it with the key addressed by hWrappingKey.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_CreateKey(TSS_HKEY </code><i>hKey</i><code>, TSS_HKEY </code><i>hWrappingKey</i><code>, TSS_HPCRS </code><i>hPcrComposite</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Key_CreateKey</code> calls the TPM command TPM_CreateWrapKey. If hPcrComposite is not set to NULL, the created key blob is bound to this PCR values. The key object addressed by hKey must contain the key information needed for the creation.</p>
<h2>Parameters</h2>
<h3>hKey</h3>
<p>The handle of the key object to create. </p>
<h3>hWrappingKey</h3>
<p>The handle to the key used to wrap the newly created key. </p>
<h3>hPcrComposite</h3>
<p>The handle to an object, if the value of the handle doesn&#8217;t equal NULL, the newly create key will be bound ot the PCR values described with this object. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_CreateKey</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hKey</i>, <i>hWrappingKey</i> or <i>hPcrComposite</i> are invalid parameters.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_CreateKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_wrapkey/">Tspi_Key_WrapKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_certifykey/">Tspi_Key_CertifyKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_registerkey/">Tspi_Key_RegisterKey</a></code>(3).</p>
