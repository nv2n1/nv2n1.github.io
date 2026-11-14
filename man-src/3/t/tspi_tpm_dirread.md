---
title: "tspi_tpm_dirread(3)"
name: "tspi_tpm_dirread"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_dirread/"
description: "Tspi_TPM_DirRead – Read a Data Integrity Register"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_DirRead &#8211; Read a Data Integrity Register </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_DirRead(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulDirIndex</i><code>,</code>
<code> UINT32* </code><i>pulDirDataLength</i><code>, BYTE** </code><i>prgbDirData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_DirRead</code> reads a data integrity register. DIRs are non-volatile (persistent across reboots) memory areas maintained by the TPM. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>ulDirIndex</h3>
<p>The <i>ulDirIndex</i> parameter is the index of the DIR to read. To query the TPM for the number of DIR registers it supports, use <code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3).</p>
<h3>pulDirDataLength</h3>
<p>The <i>pulDirDataLength</i> parameter receives the length in bytes of the <i>prgbDirData</i> parameter.</p>
<h3>prgbDirData</h3>
<p>The <i>prgbDirData</i> parameter receives a pointer to memory containing the DIR data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_DirRead</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_DirRead</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_dirwrite/">Tspi_TPM_DirWrite</a></code>(3).</p>
