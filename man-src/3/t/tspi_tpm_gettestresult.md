---
title: "tspi_tpm_gettestresult(3)"
name: "tspi_tpm_gettestresult"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_gettestresult/"
description: "Tspi_TPM_GetTestResult- get manufacturer specific information regarding the results of a self test."
---

<p>Tspi_TPM_GetTestResult- get manufacturer specific information regarding the results of a self test.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetTestResult(TSS_HTPM </code><i>hTPM</i><code>, UINT32* </code><i>pulTestResultLength</i><code>, BYTE** </code><i>prgbTestResult</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetTestResult</code> is provided by a manufacturer of a TPM to provide manufacturer specific self test results.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object </p>
<h3>pulTestREsultLength</h3>
<p>Receives the length (in bytes) of the prgbTestResult parameter </p>
<h3>prgbTestResult</h3>
<p>Pointer to the memory block containing the TPM manufacturer specific information.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetTestResult</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><code>hTPM</code> is not a valid handle to the TPM object.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetTestResult</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_selftestfull/">Tspi_TPM_SelfTestFull</a></code>(3).</p>
