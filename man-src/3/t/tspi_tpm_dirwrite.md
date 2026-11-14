---
title: "tspi_tpm_dirwrite(3)"
name: "tspi_tpm_dirwrite"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_dirwrite/"
description: "Tspi_TPM_DirWrite – write to a Data Integrity Register"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_DirWrite &#8211; write to a Data Integrity Register </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_DirWrite(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulDirIndex</i><code>,</code>
<code> UINT32 </code><i>ulDirDataLength</i><code>, BYTE* </code><i>rgbDirData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_DirWrite</code> writes a data integrity register. You need to know the DIR index and data you wish to write to the DIR prior to using this command. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>ulDirIndex</h3>
<p>The <i>ulDirIndex</i> parameter is the index of the DIR to write. To query the TPM for the number of DIR registers it supports, use <code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3).</p>
<h3>ulDirDataLength</h3>
<p>The <i>ulDirDataLength</i> parameter is the length in bytes of the <i>rgbDirData</i> parameter.</p>
<h3>rgbDirData</h3>
<p>The <i>rgbDirData</i> parameter is a pointer to memory containing the data to be written to the DIR. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_DirWrite</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_DirWrite</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getcapability/">Tspi_TPM_GetCapability</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_dirread/">Tspi_TPM_DirRead</a></code>(3).</p>
