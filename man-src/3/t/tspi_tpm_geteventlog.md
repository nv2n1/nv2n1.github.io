---
title: "tspi_tpm_geteventlog(3)"
name: "tspi_tpm_geteventlog"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_geteventlog/"
description: "Tspi_TPM_GetEventLog- get the entire PCR event log."
---

<p>Tspi_TPM_GetEventLog- get the entire PCR event log.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetEventLog(TSS_HTPM </code><i>hTPM</i><code>, UINT32* </code><i>pulEventNumber</i><code>,</code>
<code> TSS_PCR_EVENT** </code><i>prgPcrEvents</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetEventLog</code> provides the whole event log that was used to create all of the PCRs.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object. </p>
<h3>pulEventNumber</h3>
<p>Receives number of returned event data structures in prgPcrEvents parameter. </p>
<h3>prgPcrEvents</h3>
<p>Receives a pointer to an array of PCR event data. If NULL, only the numberof elements is returned in pulEventNumber parameter.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetEventLog</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><code>hTPM</code> is not a valid handle to the TPM object.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetEventLog</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getevent/">Tspi_TPM_GetEvent</a></code>(3) <code><a href="/docs/linux/man/3-tspi_tpm_getevents/">Tspi_TPM_GetEvents</a></code>(3).</p>
