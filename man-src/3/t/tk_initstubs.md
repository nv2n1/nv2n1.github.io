---
title: "tk_initstubs(3)"
name: "tk_initstubs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_initstubs/"
description: "Tk_InitStubs – initialize the Tk stubs mechanism"
---

<p>Tk_InitStubs &#8211; initialize the Tk stubs mechanism </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
const char *
<code>Tk_InitStubs</code>(<i>interp, version, exact</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter handle.</p>
<dd>char <i>*version</i> (in) A version string consisting of one or more decimal numbers separated by dots.</p>
<dd>int <i>exact</i> (in) Non-zero means that only the particular Tk version specified by <i>version</i> is acceptable. Zero means that versions newer than <i>version</i> are also acceptable as long as they have the same major version number as <i>version</i>.
</dl>
<h2>Introduction</h2>
<p>The Tcl stubs mechanism defines a way to dynamically bind extensions to a particular Tcl implementation at run time. the stubs mechanism requires no changes to applications incoporating Tcl/Tk interpreters. Only developers creating C-based Tcl/Tk extensions need to take steps to use the stubs mechanism with their extensions. See the <code>Tcl_InitStubs</code> page for more information. </p>
<p> Enabling the stubs mechanism for a Tcl/Tk extension requires the following steps:</p>
<dl COMPACT>
<dt>1)</p>
<dd>Call <code>Tcl_InitStubs</code> in the extension before calling any other Tcl functions.</p>
<dt>2)</p>
<dd>Call <code>Tk_InitStubs</code> if the extension before calling any other Tk functions.</p>
<dt>2)</p>
<dd>Define the <code>USE_TCL_STUBS</code> symbol. Typically, you would include the <code>-DUSE_TCL_STUBS</code> flag when compiling the extension.</p>
<dt>3)</p>
<dd>Link the extension with the Tcl and Tk stubs libraries instead of the standard Tcl and Tk libraries. On Unix platforms, the library names are <i>libtclstub8.4.a</i> and <i>libtkstub8.4.a</i>; on Windows platforms, the library names are <i>tclstub84.lib</i> and <i>tkstub84.lib</i> (adjust names with appropriate version number).</dl>
<h2>Description</h2>
<p><code>Tk_InitStubs</code> attempts to initialize the Tk stub table pointers and ensure that the correct version of Tk is loaded. In addition to an interpreter handle, it accepts as arguments a version number and a Boolean flag indicating whether the extension requires an exact version match or not. If <i>exact</i> is 0, then the extension is indicating that newer versions of Tk are acceptable as long as they have the same major version number as <i>version</i>; non-zero means that only the specified <i>version</i> is acceptable. <code>Tcl_InitStubs</code> returns a string containing the actual version of Tk satisfying the request, or NULL if the Tk version is not acceptable, does not support the stubs mechanism, or any other error condition occurred.</p>
<h2>See Also</h2>
<p><code>Tcl_InitStubs</code></p>
<h2>Keywords</h2>
<p>stubs</p>
