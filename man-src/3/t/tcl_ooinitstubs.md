---
title: "tcl_ooinitstubs(3)"
name: "tcl_ooinitstubs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_ooinitstubs/"
description: "Tcl_OOInitStubs – initialize library access to TclOO functionality"
---

<p>Tcl_OOInitStubs &#8211; initialize library access to TclOO functionality </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tclOO.h&gt;</code>
const char *
<code>Tcl_OOInitStubs</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) The Tcl interpreter that the TclOO API is integrated with and whose C interface is going to be used.
</dl>
<h2>Description</h2>
<p>When an extension library is going to use the C interface exposed by TclOO, it should use <code>Tcl_OOInitStubs</code> to initialize its access to that interface from within its <i>*</i><code>_Init</code> (or <i>*</i><code>_SafeInit</code>) function, passing in the <i>interp</i> that was passed into that routine as context. If the result of calling <code>Tcl_OOInitStubs</code> is NULL, the initialization failed and an error message will have been left in the interpreter&#8217;s result. Otherwise, the initialization succeeded and the TclOO API may thereafter be used; the version of the TclOO API is returned. </p>
<p> When using this function, either the C #define symbol <code>USE_TCLOO_STUBS</code> should be defined and your library code linked against the Tcl stub library, or that #define symbol should <i>not</i> be defined and your library code linked against the Tcl main library directly.</p>
<h2>Backward Compatibility Note</h2>
<p>If you are linking against the Tcl 8.5 forward compatibility package for TclOO, <i>only</i> the stub-enabled configuration is supported and you should also link against the TclOO independent stub library; that library is an integrated part of the main Tcl stub library in Tcl 8.6.</p>
<h2>Keywords</h2>
<p>stubs</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_initstubs/">Tcl_InitStubs</a>(3)</p>
