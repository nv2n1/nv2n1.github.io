---
title: "tspi_getpolicyobject(3)"
name: "tspi_getpolicyobject"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_getpolicyobject/"
description: "Tspi_GetPolicyObject – get a policy object assigned to a working object"
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_GetPolicyObject &#8211; get a policy object assigned to a working object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_GetPolicyObject(TSS_HOBJECT </code><i>hObject</i><code>, TSS_FLAG </code><i>policyType</i><code>,</code>
<code> TSS_HPOLICY* </code><i>phPolicy</i><code>); </code></pre>
<h2>Description</h2>
<p><code>Tspi_GetPolicyObject</code> returns a policy object currently assigned to a working object. If you determine that the policy is different from what you require, you can change the policy by creating a new one and using Tspi_Policy_AssignToObject. </p>
<h2>Parameters</h2>
<h3>hObject</h3>
<p>The <i>hObject</i> parameter is the handle of the object.</p>
<h3>policyType</h3>
<p>The <i>policyType</i> parameter indicates the policy type of interest. Types are TSS_POLICY_USAGE and TSS_POLICY_MIGRATION.</p>
<h3>phPolicy</h3>
<p>The <i>phPolicy</i> parameter receives the handle to the assigned policy object. </p>
<h2>Return Codes</h2>
<p><code>Tspi_GetPolicyObject</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hContext</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_GetPolicyObject</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_gettpmobject/">Tspi_Context_GetTpmObject</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_loadkeybyuuid/">Tspi_Context_LoadKeyByUUID</a></code>(3), <code><a href="/docs/linux/man/3-tspi_setattribuint32/">Tspi_SetAttribUint32</a></code>(3), <code><a href="/docs/linux/man/3-tspi_policy_assigntoobject/">Tspi_Policy_AssignToObject</a></code>(3).</p>
