---
title: "tspi_context_connect(3)"
name: "tspi_context_connect"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_connect/"
---

<h2>Name.</h2>
<p>Tspi_Context_Connect- connect a TSP to a Core Services daemon</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_Connect(TSS_HCONTEXT </code><i>hLocalContext</i><code>, UNICODE* </code><i>wszDestination</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_Context_Connect</code> creates a connetion between the application and the local or remote TSS System.</p>
<h2>Parameters</h2>
<h3>hLocalContext</h3>
<p>The handle to the context to be connected. </p>
<h3>wszDestination</h3>
<p>A null terminated unicode string which specifies the local or remote system to which one will be connected. If <i>wszDestination</i> is NULL, the connection will be to a local TCS. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_Connect</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; <i>hLocalContext</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_Connect</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_create/">Tspi_Context_Create</a></code>(3), <code><a href="/docs/linux/man/3-tspi_context_close/">Tspi_Context_Close</a></code>(3).</p>
