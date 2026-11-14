---
title: "tspi_tpm_certifyselftest(3)"
name: "tspi_tpm_certifyselftest"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_certifyselftest/"
description: "Tspi_TPM_CertifySelfTest- have the TPM sign its self test data"
---

<p>Tspi_TPM_CertifySelfTest- have the TPM sign its self test data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_CertifySelfTest(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hKey</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code> );</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_CertifySelfTest</code> performs a self-test of each internal TPM function and returns an authenticated value (signature) if the test has passed.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object </p>
<h3>hKey</h3>
<p>Handle of the signature key object </p>
<h3>pValidationData</h3>
<p>Validation data structure. [IN] Provide externalData information required to compute the signature. [OUT] On successful completion of the ocmmand, the structure provides a buffer containing the validation data and a buffer containing the data the validation data was computed from.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CertifySelfTest</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><code>hTPM</code> is not a valid handle to a TPM object.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CertifySelfTest</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_selftestfull/">Tspi_TPM_SelfTestFull</a></code>(3).</p>
