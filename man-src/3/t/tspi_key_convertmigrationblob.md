---
title: "tspi_key_convertmigrationblob(3)"
name: "tspi_key_convertmigrationblob"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_key_convertmigrationblob/"
description: "Tspi_Key_ConvertMigrationBlob – create a wrapped key from a migration blob"
---

<p>TCG Software Stack Developer&#8217;s Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Key_ConvertMigrationBlob &#8211; create a wrapped key from a migration blob </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Key_ConvertMigrationBlob(TSS_HKEY </code><i>hKeyToMigrate</i><code>, TSS_HKEY </code><i>hParentKey</i><code>,</code>
<code> UINT32 </code><i>ulRandomLength</i><code>, BYTE* </code><i>rgbRandom</i><code>,</code>
<code> UINT32 </code><i>ulMigrationBlobLength</i><code>, BYTE* </code><i>rgbMigrationBlob</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Key_ConvertMigrationBlob</code> takes the migration blob built by <code>Tspi_Key_CreateMigrationBlob</code> using the migration scheme TSS_MS_MIGRATE and creates a normal wrapped key. The resulting normal wrapped key blob is stored in the instance associated with hKeyToMigrate and may be retrieved from that instance by <code>Tspi_GetAttribData</code>. </p>
<h2>Parameters</h2>
<h3>hKeyToMigrate</h3>
<p>The handle of the key object to convert.</p>
<h3>hParentKey</h3>
<p>Handle to the parent key related to the key addressed by <i>hKeyToMigrate</i>.</p>
<h3>ulRandomLength</h3>
<p>Length of random data provided at the parameter <i>rgbRandom</i>.</p>
<h3>rgbRandom</h3>
<p>Random data as returned together with the migration blob by the method <code>Tspi_Key_CreateMigrationBlob</code>.</p>
<h3>ulMigrationBlobLength</h3>
<p>Length of the migration blob data provided at the parameter <i>rgbMigrationBlob</i>.</p>
<h3>rgbMigrationBlob</h3>
<p>Migration blob data as returned by a previously called method <code>Tspi_Key_CreateMigrationBlob</code>. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Key_ConvertMigrationBlob</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hKeyToMigrate</i> or <i>hParentKey</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Key_ConvertMigrationBlob</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_key_loadkey/">Tspi_Key_LoadKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_unloadkey/">Tspi_Key_UnloadKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_certifykey/">Tspi_Key_CertifyKey</a></code>(3), <code><a href="/docs/linux/man/3-tspi_key_createmigrationblob/">Tspi_Key_CreateMigrationBlob</a></code>(3).</p>
