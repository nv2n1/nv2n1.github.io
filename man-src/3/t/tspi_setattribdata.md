---
title: "tspi_setattribdata(3)"
name: "tspi_setattribdata"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_setattribdata/"
description: "Tspi_SetAttribData – set a non 32bit attribute of an object."
---

<p>Tspi_SetAttribData &#8211; set a non 32bit attribute of an object.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_SetAttribData(TSS_HOBJECT </code><i>hObject</i><code>, TSS_FLAG </code><i>attribFlag</i><code>,</code>
<code> TSS_FLAG </code><i>subFlag</i><code>, UINT32 </code><i>ulAttribDataSize</i><code>,</code>
<code> BYTE* </code><i>rgbAttribData</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_SetAttribData</code> sets the attributes associated with a given class of object that aren&#8217;t UINT32. The structure and size of hte attribute data depends on the attribute.</p>
<h2>Parameters</h2>
<h3>hObject</h3>
<p>Handle of the object where the attribute is to be set. </p>
<h3>attribFlag</h3>
<p>Flag indicating the attribute to set. </p>
<h3>subFlag</h3>
<p>Sub flag indicating the attribute to set </p>
<h3>ulAttribDataSize</h3>
<p>Supplies the length (in bytes) of the rgbAttribData. </p>
<h3>rgbAttribData</h3>
<p>Pointer to the actual data which is to be set for the specified attribute.</p>
<h2>Return Codes</h2>
<p><code>Tspi_SetAttribData</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hObject</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_FLAG &#8211; <i>attribFlag</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_SUBFLAG &#8211; <i>subFlag</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_ATTRIB_DATA &#8211; <i>rgbAttribData</i> is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_BAD_PARAMETER</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_SetAttribData</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_getattribdata/">Tspi_GetAttribData</a></code>(3).</p>
