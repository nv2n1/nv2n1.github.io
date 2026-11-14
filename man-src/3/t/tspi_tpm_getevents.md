---
title: "tspi_tpm_getevents(3)"
name: "tspi_tpm_getevents"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getevents/"
description: "Tspi_TPM_GetEvents- get a specific number of PCR events for a given index."
---

<p>Tspi_TPM_GetEvents- get a specific number of PCR events for a given index.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetEvents(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulPcrIndex</i><code>, </code>
<code> UINT32 </code><i>ulStartNumber</i><code>, UINT32* </code><i>pulEventNumber</i><code>, </code>
<code> TSS_PCR_EVENT* </code><i>prgbPcrEvents</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetEvents</code> provides a specific number of PCR events for a given index.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object. </p>
<h3>ulPcrIndex</h3>
<p>Index of the PCR to request. </p>
<h3>ulStartNumber</h3>
<p>Indext of the first event to request </p>
<h3>pulEventNumber</h3>
<p>[IN] Number of elements to request. [OUT] Receives number of returned event data structures in prgbPcrEvents parameter. </p>
<h3>prgbPcrEvents</h3>
<p>Receives a pointer to an array of PCR event data. If NULL, only the number of elements is returned in pulEventNumber parameter.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetEvents</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><code>hTPM</code> is not a valid handle to the TPM object.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetEvents</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getevent/">Tspi_TPM_GetEvent</a></code>(3) <code><a href="/docs/linux/man/3-tspi_tpm_geteventlog/">Tspi_TPM_GetEventLog</a></code>(3).</p>
