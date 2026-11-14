---
title: "tspi_getattribdata(3)"
name: "tspi_getattribdata"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_getattribdata/"
description: "Tspi_GetAttribData – get a non 32bit attribute of the object."
---

<p>Tspi_GetAttribData &#8211; get a non 32bit attribute of the object.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_GetAttribData(TSS_HOBJECT </code><i>hObject</i><code>, TSS_FLAG </code><i>attribFlag</i><code>,</code>
<code> TSS_FLAG </code><i>subFlag</i><code>, UINT32* </code><i>pulAttribDataSize</i><code>,</code>
<code> BYTE** </code><i>prgbAttribData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_GetAttribData</code> is used to get the value of a particular attribute associated iwth a particular object where that attribute does not happen to be a UINT32. The structure and size of the attribute data depends on the attribute.</p>
<h2>Parameters</h2>
<h3>hObject</h3>
<p>Handle of the object where to retrieve the attribute. </p>
<h3>attribFlag</h3>
<p>Flag indicating the attribute to query. </p>
<h3>subFlag</h3>
<p>Sub flag indicating the attribute to query. </p>
<h3>pulAttribDataSize</h3>
<p>Recieves the length (in bytes) of the prgbAttribData parameter. </p>
<h3>prgbAttribData</h3>
<p>On successful completion of the command, this parameter points to a buffer containing the actual data of the specified attribute.</p>
<h2>Return Codes</h2>
<p><code>Tspi_GetAttribData</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hObject</i>, <i>attribFlag</i>, or <i>subFlag</i> are invalid.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_FLAG</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_SUBFLAG</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_DATA</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_GetAttribData</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_setattribdata/">Tspi_SetAttribData</a></code>(3).</p>
