---
title: "tcl_initstubs(3)"
name: "tcl_initstubs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_initstubs/"
description: "Tcl_InitStubs – initialize the Tcl stubs mechanism"
---

<p>Tcl_InitStubs &#8211; initialize the Tcl stubs mechanism </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
const char *
<code>Tcl_InitStubs</code>(<i>interp, version, exact</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter handle.</p>
<dd>const char <i>*version</i> (in) A version string consisting of one or more decimal numbers separated by dots.</p>
<dd>int <i>exact</i> (in) Non-zero means that only the particular version specified by <i>version</i> is acceptable. Zero means that versions newer than <i>version</i> are also acceptable as long as they have the same major version number as <i>version</i>.
</dl>
<h2>Introduction</h2>
<p>The Tcl stubs mechanism defines a way to dynamically bind extensions to a particular Tcl implementation at run time. This provides two significant benefits to Tcl users:</p>
<dl COMPACT>
<dt>1)</p>
<dd>Extensions that use the stubs mechanism can be loaded into multiple versions of Tcl without being recompiled or relinked.</p>
<dt>2)</p>
<dd>Extensions that use the stubs mechanism can be dynamically loaded into statically-linked Tcl applications.</dl>
<p> The stubs mechanism accomplishes this by exporting function tables that define an interface to the Tcl API. The extension then accesses the Tcl API through offsets into the function table, so there are no direct references to any of the Tcl library&#8217;s symbols. This redirection is transparent to the extension, so an extension writer can continue to use all public Tcl functions as documented. </p>
<p> The stubs mechanism requires no changes to applications incorporating Tcl interpreters. Only developers creating C-based Tcl extensions need to take steps to use the stubs mechanism with their extensions. </p>
<p> Enabling the stubs mechanism for an extension requires the following steps:</p>
<dl COMPACT>
<dt>1)</p>
<dd>Call <code>Tcl_InitStubs</code> in the extension before calling any other Tcl functions.</p>
<dt>2)</p>
<dd>Define the <code>USE_TCL_STUBS</code> symbol. Typically, you would include the <code>-DUSE_TCL_STUBS</code> flag when compiling the extension.</p>
<dt>3)</p>
<dd>Link the extension with the Tcl stubs library instead of the standard Tcl library. On Unix platforms, the library name is <i>libtclstub8.1.a</i>; on Windows platforms, the library name is <i>tclstub81.lib</i>.</dl>
<p> If the extension also requires the Tk API, it must also call <code>Tk_InitStubs</code> to initialize the Tk stubs interface and link with the Tk stubs libraries. See the <code>Tk_InitStubs</code> page for more information.</p>
<h2>Description</h2>
<p><code>Tcl_InitStubs</code> attempts to initialize the stub table pointers and ensure that the correct version of Tcl is loaded. In addition to an interpreter handle, it accepts as arguments a version number and a Boolean flag indicating whether the extension requires an exact version match or not. If <i>exact</i> is 0, then the extension is indicating that newer versions of Tcl are acceptable as long as they have the same major version number as <i>version</i>; non-zero means that only the specified <i>version</i> is acceptable. <code>Tcl_InitStubs</code> returns a string containing the actual version of Tcl satisfying the request, or NULL if the Tcl version is not acceptable, does not support stubs, or any other error condition occurred.</p>
<h2>See Also</h2>
<p>Tk_InitStubs</p>
<h2>Keywords</h2>
<p>stubs</p>
