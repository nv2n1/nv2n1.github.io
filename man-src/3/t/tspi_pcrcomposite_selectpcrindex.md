---
title: "tspi_pcrcomposite_selectpcrindex(3)"
name: "tspi_pcrcomposite_selectpcrindex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_pcrcomposite_selectpcrindex/"
description: "Tspi_PcrComposite_SelectPcrIndex- select a PCR index inside a PCR composite object."
---

<p>Tspi_PcrComposite_SelectPcrIndex- select a PCR index inside a PCR composite object.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_PcrComposite_SelectPcrIndex(TSS_HPCRS </code><i>hPcrComposite</i><code>, UINT32 </code><i>ulPcrIndex</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_PcrComposite_SelectPcrIndex</code> selects a PCR index inside a PCR composite object. The PCR composite object must be created withthe function Tspi_Context_CreateObject(). An exampled for the usage is the selection of PCR registeres before calling Tspi_TPM_Quote().</p>
<h2>Parameters</h2>
<h3>hPcrComposite</h3>
<p>Handle of the PCR composite object instance where the index should be selected. </p>
<h3>ulPcrIndex</h3>
<p>This parameter indicates the index of the PCR to select.</p>
<h2>Return Codes</h2>
<p><code>Tspi_PcrComposite_SelectPcrIndex</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hPcrComposite</i> or <i>ulPcrIndex</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_PcrComposite_SelectPcrIndex</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_quote/">Tspi_TPM_Quote</a></code>(3), <code><a href="/docs/linux/man/3-tspi_pcrcomposite_setpcrvalue/">Tspi_PcrComposite_SetPcrValue</a></code>(3), <code><a href="/docs/linux/man/3-tspi_pcrcomposite_getpcrvalue/">Tspi_PcrComposite_GetPcrValue</a></code>(3).</p>
