---
title: "tspi_tpm_clearowner(3)"
name: "tspi_tpm_clearowner"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_clearowner/"
description: "Tspi_TPM_ClearOwner – clear TPM ownership"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_ClearOwner &#8211; clear TPM ownership </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_ClearOwner(TSS_HTPM </code><i>hTPM</i><code>, TSS_BOOL </code><i>fForcedClear</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_ClearOwner</code> wipes the TPM of everything but its endorsement key. It will wipe the SRK, so anything locked to the SRK will also disappear when this command is executed. This is the only way to be certain that keys are gone, as it is the only way to guarantee that nothing can keep a copy of the key. You must assert either physical presence or owner authorization in order to use this command. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>fForcedClear</h3>
<p>The <i>fForcedClear</i> parameter is used to tell whether this command is being executed with owner authorization or with physical presence. If FALSE, then TPM owner authorization is used. If TRUE, then physical presence is required to clear the TPM. </p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_ClearOwner</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_ClearOwner</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_takeownership/">Tspi_TPM_TakeOwnership</a></code>(3)</p>
