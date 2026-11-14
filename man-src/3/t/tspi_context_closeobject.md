---
title: "tspi_context_closeobject(3)"
name: "tspi_context_closeobject"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_closeobject/"
description: "Tspi_Context_CloseObject – destroy resources associated with an object handle."
---

<p>Tspi_Context_CloseObject &#8211; destroy resources associated with an object handle.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code> TSS_RESULT Tspi_Context_CloseObject(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_HOBJECT </code><i>hObject</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_CloseObject</code> destroys the object associated with the object handle. All allocated resources associated within the object are also released.</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>hObject</h3>
<p>The handle of the object to be destroyed.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_CloseObject</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hContext</i> or <i>hObject</i> are invalid handles.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_CloseObject</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_createobject/">Tspi_Context_CreateObject</a></code>(3).</p>
