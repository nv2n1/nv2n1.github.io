---
title: "tspi_tpm_stirrandom(3)"
name: "tspi_tpm_stirrandom"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_stirrandom/"
description: "Tspi_TPM_StirRandom – add entropy to the TPM random number generator"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_StirRandom &#8211; add entropy to the TPM random number generator </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_StirRandom(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>ulEntropyDataLength</i><code>, BYTE* </code><i>rgbEntropyData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_StirRandom</code> adds entropy to the TPM random number generator for the purpose of generating better random numbers. The <i>entropy</i> variable should assigned an appropriately seeded random number before this function is called. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object. The command to get the TPM to test itself will be sent here.</p>
<h3>ulEntropyDataLength</h3>
<p>The <i>ulEntropyDataLength</i> parameter is the length in bytes of the <i>rgbEntropyData</i> parameter.</p>
<h3>rgbEntropyData</h3>
<p>The <i>rgbEntropyData</i> parameter is a pointer to the entropy data. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_StirRandom</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_StirRandom</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getrandom/">Tspi_TPM_GetRandom</a></code>(3).</p>
