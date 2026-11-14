---
title: "tspi_policy_flushsecret(3)"
name: "tspi_policy_flushsecret"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_policy_flushsecret/"
description: "Tspi_Policy_FlushSecret – flush a cached secret"
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Policy_FlushSecret &#8211; flush a cached secret </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Policy_FlushSecret(TSS_HPOLICY </code><i>hPolicy</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Policy_FlushSecret</code> tells the TSS to flush a secret that it had cached for a user. </p>
<h2>Parameters</h2>
<h3>hPolicy</h3>
<p>The <i>hPolicy</i> parameter is the handle of the policy object to be flushed. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Policy_FlushSecret</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hPolicy</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Policy_FlushSecret</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_policy_setsecret/">Tspi_Policy_SetSecret</a></code>(3), <code><a href="/docs/linux/man/3-tspi_policy_assigntoobject/">Tspi_Policy_AssignToObject</a></code>(3).</p>
