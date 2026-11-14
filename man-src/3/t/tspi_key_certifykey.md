---
title: "tspi_key_certifykey(3)"
name: "tspi_key_certifykey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_certifykey/"
description: "Tspi_Key_CertifyKey – sign a public key."
---

<p>Tspi_Key_CertifyKey &#8211; sign a public key.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_CertifyKey(TSS_HKEY </code><i>hKey</i><code>, TSS_HKEY </code><i>hCertifyingKey</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Key_CertifyKey</code> signs a public key.</p>
<h2>Parameters</h2>
<h3>hKey</h3>
<p>Handle of the key object to be loaded. </p>
<h3>hCertifyingKey</h3>
<p>Handle to the certifying key used to sign the addressed by hKey. </p>
<h3>pValidationData</h3>
<p>Pointer to a structure of the type TSS_VALIDATION. After successful completion of the call the member rgbValidationData of this structure contains the signature data of the command. The member prgbData of the structure points to a buffer containing a TCPA_CERTIFY_INFO data stream as specified within the TCPA 1.1b Main Specification.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_CertifyKey</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hKey</i> or <i>hCertifyingKey</i> are invalid handles.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_CertifyKey</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_createkey/">Tspi_Key_CreateKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_wrapkey/">Tspi_Key_WrapKey</a></code>(3).</p>
