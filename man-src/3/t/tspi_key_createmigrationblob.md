---
title: "tspi_key_createmigrationblob(3)"
name: "tspi_key_createmigrationblob"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_createmigrationblob/"
description: "Tspi_Key_CreateMigrationBlob – create a key blob suitable for migrating to another TPM."
---

<p>Tspi_Key_CreateMigrationBlob &#8211; create a key blob suitable for migrating to another TPM.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_CreateMigrationBlob(TSS_HKEY </code><i>hKeyToMigrate</i><code>, TSS_HKEY </code><i>hParentKey</i><code>,</code>
<code> UINT32 </code><i>ulMigTicketLength</i><code>, BYTE* </code><i>rgbMigTicket</i><code>,</code>
<code> UINT32* </code><i>pulRandomLength</i><code>, BYTE** </code><i>prgbRandom</i><code>,</code>
<code> UINT32* </code><i>pulMigrationBlobLength</i><code>, BYTE** </code><i>prgbMigrationBlob</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Key_CreateMigrationBlob</code> returns a key blob containing an encrypted section, which will be different depending on the migration scheme indicated within the migration ticket previously created by the method Tspi_TPM_AuthorizeMigrationTicket().</p>
<h2>Parameters</h2>
<h3>hKeyToMigrate</h3>
<p>Handle of the key object to migrate. </p>
<h3>hParentKey</h3>
<p>Handle to the parent key related to the key addressed by hKeyToMigrate. </p>
<h3>ulMigTicketLength</h3>
<p>The length (in bytes) of the rgbMigTickey parameter. </p>
<h3>rgbMigTicket</h3>
<p>Pointer to memory containing the migration ticket (migration public key and its authorization digest). </p>
<h3>pulRandomLength</h3>
<p>On successful completion this parameter returns the random data length returned at the parameter prgbRandom. </p>
<h3>prgbRandom</h3>
<p>On successful completion this parameter returns the random data. </p>
<h3>pulMigrationBlobLength</h3>
<p>On successful completion this parameter returns the length of the migration blob data returned at the parameter prgbMigrationBlob. </p>
<h3>prgbMigrationBlob</h3>
<p>On successful completion this parameter returns the migration data blob. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_CreateMigrationBlob</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hKeyToMigrate</i>, <i>hParentKey</i> or <i>rgbMigTicket</i> are invalid parameters.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER &#8211; One of the passed parameters is wrong. </font></p>
<dd>
<dt><font SIZE="-1">TSS_E_KEY_NO_MIGRATION_POLICY &#8211; No migration policy picked.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_CreateMigrationBlob</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_createkey/">Tspi_Key_CreateKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_certifykey/">Tspi_Key_CertifyKey</a></code>(3).</p>
