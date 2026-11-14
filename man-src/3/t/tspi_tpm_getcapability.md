---
title: "tspi_tpm_getcapability(3)"
name: "tspi_tpm_getcapability"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_getcapability/"
description: "Tspi_TPM_GetCapability – get information on the capabilities of the TPM"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_GetCapability &#8211; get information on the capabilities of the TPM </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_GetCapability(TSS_HTPM </code><i>hTPM</i><code>, TSS_FLAG </code><i>capArea</i><code>,</code>
<code> UINT32 </code><i>ulSubCapLength</i><code>, BYTE* </code><i>rgbSubCap</i><code>, </code>
<code> UINT32* </code><i>pulRespDataLength</i><code>, BYTE** </code><i>prgbRespData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_GetCapability</code> gets information on various capabilities of the TPM. This command can be used to learn how many PCRs the TPM supports, etc. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>capArea</h3>
<p>The <i>capArea</i> parameter is the flag indicating the attribute to query. Possible values are:</p>
<h3>ulSubCapLength</h3>
<p>The <i>ulSubCapLength</i> parameter is the length in bytes of the <i>rgbSubCap</i> parameter.</p>
<h3>rgbSubCap</h3>
<p>The <i>rgbSubCap</i> parameter is the data indicating the attribute to query. Possible values are:</p>
<h3>pulRespDataLength</h3>
<p>The <i>pulRespDataLength</i> parameter is the length in bytes of the <i>prgbRespData</i> parameter.</p>
<h3>prgbRespData</h3>
<p>The <i>prgbRespData</i> parameter receives a pointer to the actual data of the specified attribute. </p>
<h2>Notes</h2>
<p>The following Capability Areas and Sub-Capability Areas are supported by 1.1 TSS&#8217;s: </p>
<p> <code>TSS_TPMCAP_ORD</code> &#8211; query whether an ordinal is supported by the TPM.<br />
&nbsp;<wbr>&nbsp;<wbr>subCaps: TPM_ORD_*&nbsp;<wbr>(see tcpa_literals.h) </p>
<p> <code>TSS_TPMCAP_FLAG</code> &#8211; query for the volatile and non-volatile flags inside the TPM. (Must be owner authorized). In this case, the 2 UINT32 values will be returned concatenated together in prgbRespData.<br />
&nbsp;<wbr>&nbsp;<wbr>subCaps: ignored. </p>
<p> <code>TSS_TPMCAP_ALG</code> &#8211; query whether an algorithm is supported by the TPM.<br />
&nbsp;<wbr>&nbsp;<wbr>subCaps: TSS_ALG_RSA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_ALG_DES<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_ALG_3DES<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_ALG_SHA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_ALG_HMAC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_ALG_AES </p>
<p> <code>TSS_TPMCAP_PROPERTY</code> &#8211; query a property of the TPM.<br />
&nbsp;<wbr>&nbsp;<wbr>subCaps: TSS_TPMCAP_PROP_PCR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_TPMCAP_PROP_DIR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_TPMCAP_PROP_MANUFACTURER<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TSS_TPMCAP_PROP_SLOTS </p>
<p> <code>TSS_TPMCAP_VERSION</code> &#8211; get the TSS_VERSION structure tha identifies the TPM.<br />
&nbsp;<wbr>&nbsp;<wbr>subCaps: ignored. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_GetCapability</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_GetCapability</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_getcapabilitysigned/">Tspi_TPM_GetCapabilitySigned</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_getevent/">Tspi_TPM_GetEvent</a></code>(3).</p>
