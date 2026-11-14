---
title: "tspi_tpm_pcrextend(3)"
name: "tspi_tpm_pcrextend"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_pcrextend/"
description: "Tspi_TPM_PcrExtend – extend a PCR register and optionally write the PCR event log."
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_PcrExtend &#8211; extend a PCR register and optionally write the PCR event log. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_PcrExtend(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulPcrIndex</i><code>,</code>
<code> UINT32 </code><i>ulPcrDataLength</i><code>, BYTE* </code><i>pbPcrData</i><code>,</code>
<code> TSS_PCR_EVENT* </code><i>pPcrEvent</i><code>,</code>
<code> UINT32* </code><i>pulPcrValueLength</i><code>, BYTE** </code><i>prgbPcrValue</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_PcrExtend</code> extends a PCR register and writes the PCR event log if one is supplied by the user. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object. The command to get the TPM to test itself will be sent here.</p>
<h3>ulPcrIndex</h3>
<p>The <i>ulPcrIndex</i> parameter is the index of the PCR to extend.</p>
<h3>ulPcrDataLength</h3>
<p>The <i>ulPcrDataLength</i> parameter is the length in bytes of the <i>pbPcrData</i> parameter.</p>
<h3>pbPcrData</h3>
<p>The <i>pbPcrData</i> parameter is a pointer to data to be hashed by the TSS, which will be used in the extend operation.</p>
<h3>pPcrEvent</h3>
<p>The <i>pPcrEvent</i> parameter is the TSS_PCR_EVENT structure to be passed to the TCS to record the extend event. If <i>pPcrEvent</i> is not NULL, the application should fill out the members of the structure that it cares about.</p>
<h3>pulPcrValueLength</h3>
<p>The <i>pulPcrValueLength</i> parameter receives the length in bytes of the <i>prgbPcrValue</i> parameter.</p>
<h3>prgbPcrValue</h3>
<p>The <i>prgbPcrValue</i> receives a pointer to the memory block containing the PCR data after the extend operation. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_PcrExtend</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_PcrExtend</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_pcrread/">Tspi_TPM_PcrRead</a></code>(3).</p>
