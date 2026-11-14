---
title: "tspi_tpm_getrandom(3)"
name: "tspi_tpm_getrandom"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getrandom/"
description: "Tspi_TPM_GetRandom – generate a random number on the TPM"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_GetRandom &#8211; generate a random number on the TPM </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetRandom(TSS_HTPM </code><i>hTPM</i><code>, UINT32 </code><i>size</i><code>, BYTE** </code><i>random</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetRandom</code> gets a good random number for the purpose of generating symmetric keys, nonces, or seeding a random number generator. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object. The command to get the TPM to test itself will be sent here.</p>
<h3>size</h3>
<p>The <i>size</i> parameter is the number of random bytes requested.</p>
<h3>random</h3>
<p>The <i>random</i> parameter is a pointer to memory containing the random data. This is where the generated number goes. Because this internally allocates memory, Tspi_Context_FreeMemory should also be used. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetRandom</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetRandom</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_freememory/">Tspi_Context_FreeMemory</a></code>(3).</p>
