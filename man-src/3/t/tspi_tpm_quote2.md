---
title: "tspi_tpm_quote2(3)"
name: "tspi_tpm_quote2"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_quote2/"
description: "Tspi_TPM_Quote2 – retreive a signed set of PCR values with a more complete view than Tspi_TPM_Quote."
---

<p>Tspi_TPM_Quote2 &#8211; retreive a signed set of PCR values with a more complete view than Tspi_TPM_Quote.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_Quote2(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hIdentKey</i><code>,</code>
<code> TSS_BOOL </code><i>fAddVersion</i><code>, TSS_HPCRS </code><i>hPcrComposite</i><code>,</code>
<code> TSS_VALIDATION* </code><i>pValidationData</i><code>, UINT32* </code><i>versionInfoSize</i><code>,</code>
<code> BYTE** </code><i>versionInfo</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_Quote2</code> quotes a TCG system, providing the requestor with a more complete view of the current platform configuration, than <code>Tspi_TPM_Quote</code>. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object. </p>
<h3>hIdentKey</h3>
<p>Handle of the signature key object. </p>
<h3>fAddVersion</h3>
<p>If TRUE, the TPM version is added to the output. If FALSE, the TPM version isn&#8217;t added to the output. </p>
<h3>hPcrComposite</h3>
<p>Handle of the PCR composite object, which contains the PCRs to be quoted. </p>
<h3>pValidationData</h3>
<p>Validation data structure [IN] Provide externalData information required to compute the signature. [OUT] On successful completion of the command, the structure provides a buffer containing the validation data and a buffer containing the data the validation data was computed form. </p>
<h3>versionInfoSize</h3>
<p>The size of the bytestream returned by versionInfo. If the <i>fAddVersion</i> is False this is zero. </p>
<h3>versionInfo</h3>
<p>The version information returned as a byte stream reflecting the data in TSS_CAP_VERSION_INFO if the fAddVersion is TRUE. Else it&#8217;s NULL. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_Quote</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hTPM</i>, <i>hIdentKey</i> or <i>hPcrComposite</i> is not a valid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_Quote2</code> conforms to the Trusted Computing Group Software Specification version 1.2</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_quote/">Tspi_TPM_Quote</a></code>(3).</p>
