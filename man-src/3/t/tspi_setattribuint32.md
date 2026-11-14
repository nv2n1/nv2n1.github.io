---
title: "tspi_setattribuint32(3)"
name: "tspi_setattribuint32"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_setattribuint32/"
description: "Tspi_SetAttribUint32 – set a 32bit attribute associated with a given class or object"
---

<p>TCG Software Stack Developers Reference<br />
 </center></p>
<h2>Name</h2>
<p>Tspi_SetAttribUint32 &#8211; set a 32bit attribute associated with a given class or object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_SetAttribUint32(TSS_HOBJECT </code><i>hObject</i><code>, TSS_FLAG </code><i>attribFlag</i><code>,</code>
<code> TSS_FLAG </code><i>subFlag</i><code>, UINT32 </code><i>ulAttrib</i><code>); </code></pre>
<h2>Description</h2>
<p><code>Tspi_SetAttribUint32</code> sets a uint32 attribute associated with a given class or object. In order to use this command, you must first create an object and then find the attributes you wish to set. </p>
<h2>Parameters</h2>
<h3>hObject</h3>
<p>The <i>hObject</i> parameter is the handle of the object or class whose attributes are being set. Note that this is any object handler &#8211; context, policy, TPM, key, hash, etc.</p>
<h3>attribFlag</h3>
<p>The <i>attribFlag</i> parameter indicates the specific attribute to be set.</p>
<h3>subFlag</h3>
<p>The <i>subFlag</i> parameter also indicates the specific attribute to be set.</p>
<h3>ulAttrib</h3>
<p>The <i>ulAttrib</i> parameter is the value that the specified attribute will be set to. </p>
<h2>Return Codes</h2>
<p><code>Tspi_SetAttribUint32</code> returns TSS_SUCCESS on success, otherwise one of the following values is returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE</font></p>
<dd><i>hObject</i> is not a valid handle. </p>
<dt><font SIZE="-1">TSS_E_INVALID_ATTRIB_FLAG</font></p>
<dd><i>attribFlag</i> is incorrect. </p>
<dt><font SIZE="-1">TSS_E_INVALID_ATTRIB_SUBFLAG</font></p>
<dd><i>subFlag</i> is incorrect. </p>
<dt><font SIZE="-1">TSS_E_INVALID_ATTRIB_DATA</font></p>
<dd><i>ulAttrib</i> is incorrect. </p>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR</font></p>
<dd>An internal SW error has been detected. </p>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>One or more parameters is bad. </p>
</dl>
<h2>Conforming To</h2>
<p><code>Tspi_SetAttribUint32</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_getattribuint32/">Tspi_GetAttribUint32</a></code>(3), <code><a href="/docs/linux/man/3-tspi_setattribdata/">Tspi_SetAttribData</a></code>(3), <code><a href="/docs/linux/man/3-tspi_getattribdata/">Tspi_GetAttribData</a></code>(3).</p>
