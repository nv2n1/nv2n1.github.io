---
title: "tspi_pcrcomposite_setpcrvalue(3)"
name: "tspi_pcrcomposite_setpcrvalue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_pcrcomposite_setpcrvalue/"
description: "Tspi_PcrComposite_SetPcrValue- set the digest for a given PCR index inside a PCR composite object."
---

<p>Tspi_PcrComposite_SetPcrValue- set the digest for a given PCR index inside a PCR composite object.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_PcrComposite_SetPcrValue(TSS_HPCRS </code><i>hPcrComposite</i><code>, UINT32 </code><i>ulPcrIndex</i><code>,</code>
<code> UINT32 </code><i>ulPcrValueLength</i><code>, BYTE* </code><i>rgbPcrValue</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_PcrComposite_SetPcrValue</code> sets the digest for a given PCR index inside the PCR composite object.</p>
<h2>Parameters</h2>
<h3>hPcrComposite</h3>
<p>Handle of the PCR composite object instance where a PCR value should be set. </p>
<h3>ulPcrIndex</h3>
<p>This parameter indicates the index of the PCR to set. </p>
<h3>ulPcrValueLength</h3>
<p>The length (in bytes) of the rgbPcrValue parameter. </p>
<h3>rgbPcrValue</h3>
<p>Pointer to memory containing the actual value which should be set for the PCR indicated by ulPcrIndex.</p>
<h2>Return Codes</h2>
<p><code>Tspi_PcrComposite_SetPcrValue</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hPcrComposite</i> or <i>ulPcrIndex</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_PcrComposite_SetPcrValue</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_pcrcomposite_selectpcrindex/">Tspi_PcrComposite_SelectPcrIndex</a></code>(3), <code><a href="/docs/linux/man/3-tspi_pcrcomposite_getpcrvalue/">Tspi_PcrComposite_GetPcrValue</a></code>(3).</p>
