---
title: "tspi_tpm_selftestfull(3)"
name: "tspi_tpm_selftestfull"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_selftestfull/"
description: "Tspi_TPM_SelfTestFull – perform a self-test of each internal TPM function"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_SelfTestFull &#8211; perform a self-test of each internal TPM function </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_SelfTestFull(TSS_HTPM </code><i>hTPM</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_SelfTestFull</code> assures that the TPM is functioning as designed. For FIPS certification, crypto modules are required to test themselves before they are used, and this command is used to fulfill that requirement. This command can also be used to check the TPM whenever such a check is desired. <code>This command is not currently implemented</code>. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object on which the self-tests will be run. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetStatus</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_SelfTestFull</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_certifyselftest/">Tspi_TPM_CertifySelfTest</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_gettestresults/">Tspi_TPM_GetTestResults</a></code>(3).</p>
