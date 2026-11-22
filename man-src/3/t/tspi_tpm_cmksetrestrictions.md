---
title: "tspi_tpm_cmksetrestrictions(3)"
name: "tspi_tpm_cmksetrestrictions"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_cmksetrestrictions/"
description: "Tspi_TPM_CMKSetRestrictions – set restrictions on use of delegated Certified Migratable Keys"
---

<p>TCG Software Stack Developer&#8217;s Reference<br/>
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
<dt>TSS_CMK_DELEGATE_SIGNING</dt>
<dd>Allow use of signing keys. </dd>
<dt>TSS_CMK_DELEGATE_STORAGE</dt>
<dd>Allow use of storage keys. </dd>
<dt>TSS_CMK_DELEGATE_BIND</dt>
<dd>Allow use of binding keys. </dd>
<dt>TSS_CMK_DELEGATE_LEGACY</dt>
<dd>Allow use of legacy keys. </dd>
<dt>TSS_CMK_DELEGATE_MIGRATE</dt>
<dd>Allow use of migratable keys. </dd>
</dl>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_CMKSetRestrictions</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt>TSS_E_INVALID_HANDLE</dt>
<dd><i>hTPM</i> is not a valid handle. </dd>
<dt>TSS_E_INTERNAL_ERROR</dt>
<dd>An internal SW error has been detected. </dd>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_CMKSetRestrictions</code> conforms to the Trusted Computing Group Software Specification version 1.2 Errata A </p>
<h2>See Also</h2>
<p><code>Tspi_TPM_CMKApproveMA</code>(3), <code>Tspi_TPM_CMKCreateTicket</code>(3), <code>Tspi_Key_CMKCreateBlob</code>(3)</p>
