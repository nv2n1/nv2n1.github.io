---
title: "tspi_policy_assigntoobject(3)"
name: "tspi_policy_assigntoobject"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_policy_assigntoobject/"
description: "Tspi_Policy_AssignToObject – assign a policy to an object"
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_Policy_AssignToObject &#8211; assign a policy to an object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Policy_AssignToObject(TSS_HPOLICY </code><i>hPolicy</i><code>, TSS_HOBJECT </code><i>hObject</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Policy_AssignToObject</code> assigns a given object to a certain policy. The object then uses its assigned policy to process an authorized TPM command. When each new object is initialized, it is assigned to the default policy, which is created when a context object is created. When an object is assigned to a policy, a reference is added to the list of assigned objects stored in the policy, and a reference to the policy is stored in the object by internal object functions. </p>
<h2>Parameters</h2>
<h3>hPolicy</h3>
<p>The <i>hPolicy</i> parameter is the handle of the policy object to be assigned to.</p>
<h3>hObject</h3>
<p>The <i>hObject</i> parameter is the object that will be assigned to <i>hPolicy</i>. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Policy_AssignToObject</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hPolicy</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_Policy_AssignToObject</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_policy_setsecret/">Tspi_Policy_SetSecret</a></code>(3), <code><a href="/docs/linux/man/3-tspi_policy_flushsecret/">Tspi_Policy_FlushSecret</a></code>(3).</p>
