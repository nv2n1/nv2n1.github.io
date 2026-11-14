---
title: "tspi_tpm_authorizemigrationticket(3)"
name: "tspi_tpm_authorizemigrationticket"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_tpm_authorizemigrationticket/"
description: "Tspi_TPM_AuthorizeMigrationTicket- create the migration ticket required for the migration process."
---

<p>Tspi_TPM_AuthorizeMigrationTicket- create the migration ticket required for the migration process.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_TPM_AuthorizeMigrationTicket(TSS_HTPM </code><i>hTPM</i><code>, TSS_HKEY </code><i>hMigrationKey</i><code>,</code>
<code> TSS_MIGRATE_SCHEME </code><i>migrationScheme</i><code>, UINT32* </code><i>pulMigTicketLength</i><code>,</code>
<code> BYTE** </code><i>prgbMigTicket</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_TPM_AuthorizeMigrationTicket</code> is used by the owner to authorize a target public key for migration. This mean sthat when a system is set up, the owner can decide that all archives should be done on a particular server. Then as keys are created, the user can pick one of these servers for the target of the migration of their keys, if they wish. This provides one of the two authorizations necessary to migrate a key.</p>
<h2>Parameters</h2>
<h3>hTPM</h3>
<p>Handle of the TPM object </p>
<h3>hMigrationKey</h3>
<p>Handle of the object representing the migration key. </p>
<h3>migrationScheme</h3>
<p>Flag indiating the migration scheme to be used. </p>
<h3>pulMigTicketLength</h3>
<p>Recieves the length (in bytes) of the prgbMigTicket parameter. </p>
<h3>prgbMigTicket</h3>
<p>Recieves a pointer to thememory block containing the migration ticket blob.</p>
<h2>Return Codes</h2>
<p><code>Tspi_TPM_AuthorizeMigrationTicket</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd>Either <code>hTPM</code> or <code>hMigrationKey</code> is not a valid handle.</p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An error occurred internal to the TSS. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_TPM_AuthorizeMigrationTicket</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code>(none)</code>.</p>
