---
title: "tspi_tpm_cmksetrestrictions(3)"
name: "tspi_tpm_cmksetrestrictions"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_cmksetrestrictions/"
description: "Tspi_TPM_CMKSetRestrictions – set restrictions on use of delegated Certified Migratable Keys"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_TPM_CMKSetRestrictions &#8211; set restrictions on use of delegated Certified Migratable Keys </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_CMKSetRestrictions(TSS_HTPM </code><i>hTPM</i><code>, TSS_CMK_DELEGATE </code><i>CmkDelegate</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_CMKSetRestrictions</code> is used to set restrictions on the delegated use of Certified Migratable Keys (CMKs). Use of this command cannot itself be delegated. </p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>The <i>hTPM</i> parameter is used to specify the handle of the TPM object.</p>
<h3>CmkDelegate</h3>
<p>The <i>CmkDelegate</i> parameter is a bitmask describing the kinds of CMKs that can be used in a delegated auth session. Each bit represents a type of key. If the bit of a key type is set, then the CMK can be used in a delegated authorization session, otherwise use of that key will result in a TPM_E_INVALID_KEYUSAGE return code from the TPM. </p>
<p> The possible values of <i>CmkDelegate</i> are any combination of the following flags logically OR&#8217;d together: </p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_CMK_DELEGATE_SIGNING</font></p>
<dd>Allow use of signing keys. </p>
<dt><font SIZE="-1">TSS_CMK_DELEGATE_STORAGE</font></p>
<dd>Allow use of storage keys. </p>
<dt><font SIZE="-1">TSS_CMK_DELEGATE_BIND</font></p>
<dd>Allow use of binding keys. </p>
<dt><font SIZE="-1">TSS_CMK_DELEGATE_LEGACY</font></p>
<dd>Allow use of legacy keys. </p>
<dt><font SIZE="-1">TSS_CMK_DELEGATE_MIGRATE</font></p>
<dd>Allow use of migratable keys. </p>
</dl>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CMKSetRestrictions</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hTPM</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CMKSetRestrictions</code> conforms to the Trusted Computing Group Software Specification version 1.2 Errata A </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_tpm_cmkapprovema/">Tspi_TPM_CMKApproveMA</a></code>(3), <code><a href="/docs/linux/man/3-tspi_tpm_cmkcreateticket/">Tspi_TPM_CMKCreateTicket</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_cmkcreateblob/">Tspi_Key_CMKCreateBlob</a></code>(3)</p>
