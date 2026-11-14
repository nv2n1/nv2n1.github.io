---
title: "tspi_tpm_getevent(3)"
name: "tspi_tpm_getevent"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getevent/"
description: "Tspi_TPM_GetEvent- get a PCR event for a given PCR index and event number."
---

<p>Tspi_TPM_GetEvent- get a PCR event for a given PCR index and event number.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetEvent(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulPcrIndex</i><code>,</code>
<code> UINT32 </code><i>ulEventNumber</i><code>, TSS_PCR_EVENT* </code><i>pPcrEvent</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetEvent</code> provides a PCR event for a given PCR index and event number.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object. </p>
<h3>ulPcrIndex</h3>
<p>Index of the PCR to request. </p>
<h3>ulEventNumber</h3>
<p>Index of the event to request. </p>
<h3>pPcrEvent</h3>
<p>Receives the PCR event data.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetEvent</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><code>hTPM</code> is not a valid handle to the TPM object.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetEvent</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getevents/">Tspi_TPM_GetEvents</a></code>(3) <code><a href="/docs/linux/man/3-tspi_tpm_geteventlog/">Tspi_TPM_GetEventLog</a></code>(3).</p>
