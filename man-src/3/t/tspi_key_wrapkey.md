---
title: "tspi_key_wrapkey(3)"
name: "tspi_key_wrapkey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_wrapkey/"
description: "Tspi_Key_WrapKey – wrap a key with the key addressed by hWrappingKey."
---

<p>Tspi_Key_WrapKey &#8211; wrap a key with the key addressed by hWrappingKey.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_WrapKey(TSS_HKEY </code><i>hKey</i><code>, TSS_HKEY </code><i>hWrappingKey</i><code>,</code>
<code> TSS_HPCRS </code><i>hPcrComposite</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Key_WrapKey</code> wraps the private key <i>hKey</i> using the public key addressed by <i>hWrappingKey</i>. If hPcrComposite is not set to NULL (0), the created key blob is bound to its PCR values. The key object addressed by <i>hKey</i> must contain the key information needed for the creation. On successful return from this call, <i>hKey</i> can be loaded into a TPM. <i>hKey</i> must have been created as a migratable key and should have its usage and migrations secrets set using <code><a href="/docs/linux/man/3-tspi_policy_setsecret/">Tspi_Policy_SetSecret</a>(3)</code>. Also, <i>hKey</i> should have had its private key set to either RSA private component, p or q.</p>
<h2>Parameters</h2>
<h3>hKey</h3>
<p>The handle of the key object that is wrapped. </p>
<h3>hWrappingKey</h3>
<p>The handle to the key used to wrap the newly created key. </p>
<h3>hPcrComposite</h3>
<p>The handle to an object, if the value of the handle doesn&#8217;t equal NULL, the newly create key will be bound ot the PCR values described with this object. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_WrapKey</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hKey</i>, <i>hWrappingKey</i> or <i>hPcrComposite</i> are invalid handles.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_WrapKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_createkey/">Tspi_Key_CreateKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_certifykey/">Tspi_Key_CertifyKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_registerkey/">Tspi_Key_RegisterKey</a></code>(3).</p>
