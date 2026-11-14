---
title: "tcl_pkgprovide(3)"
name: "tcl_pkgprovide"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_pkgprovide/"
description: "Tcl_PkgRequire, Tcl_PkgRequireEx, Tcl_PkgRequireProc, Tcl_PkgPresent, Tcl_PkgPresentEx, Tcl_PkgProvide, Tcl_PkgProvideEx – package version control"
---

<p>Tcl_PkgRequire, Tcl_PkgRequireEx, Tcl_PkgRequireProc, Tcl_PkgPresent, Tcl_PkgPresentEx, Tcl_PkgProvide, Tcl_PkgProvideEx &#8211; package version control </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
const char *
<code>Tcl_PkgRequire</code>(<i>interp, name, version, exact</i>)
const char *
<code>Tcl_PkgRequireEx</code>(<i>interp, name, version, exact, clientDataPtr</i>)
int
<code>Tcl_PkgRequireProc</code>(<i>interp, name, objc, objv, clientDataPtr</i>)
const char *
<code>Tcl_PkgPresent</code>(<i>interp, name, version, exact</i>)
const char *
<code>Tcl_PkgPresentEx</code>(<i>interp, name, version, exact, clientDataPtr</i>)
int
<code>Tcl_PkgProvide</code>(<i>interp, name, version</i>)
int
<code>Tcl_PkgProvideEx</code>(<i>interp, name, version, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter where package is needed or available.</p>
<dd>const char <i>*name</i> (in) Name of package.</p>
<dd>const char <i>*version</i> (in) A version string consisting of one or more decimal numbers separated by dots.</p>
<dd>int <i>exact</i> (in) Non-zero means that only the particular version specified by <i>version</i> is acceptable. Zero means that newer versions than <i>version</i> are also acceptable as long as they have the same major version number as <i>version</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary value to be associated with the package.</p>
<dd>ClientData <i>*clientDataPtr</i> (out) Pointer to place to store the value associated with the matching package. It is only changed if the pointer is not NULL and the function completed successfully.</p>
<dd>int <i>objc</i> (in) Number of requirements.</p>
<dd>Tcl_Obj* <i>objv[]</i> (in) Array of requirements. </p>
</dl>
<h2>Description</h2>
<p>These procedures provide C-level interfaces to Tcl&#8217;s package and version management facilities. </p>
<p> <code>Tcl_PkgRequire</code> is equivalent to the <code>package require</code> command, <code>Tcl_PkgPresent</code> is equivalent to the <code>package present</code> command, and <code>Tcl_PkgProvide</code> is equivalent to the <code>package provide</code> command. </p>
<p> See the documentation for the Tcl commands for details on what these procedures do. </p>
<p> If <code>Tcl_PkgPresent</code> or <code>Tcl_PkgRequire</code> complete successfully they return a pointer to the version string for the version of the package that is provided in the interpreter (which may be different than <i>version</i>); if an error occurs they return NULL and leave an error message in the interpreter&#8217;s result. </p>
<p> <code>Tcl_PkgProvide</code> returns <code>TCL_OK</code> if it completes successfully; if an error occurs it returns <code>TCL_ERROR</code> and leaves an error message in the interpreter&#8217;s result. </p>
<p> <code>Tcl_PkgProvideEx</code>, <code>Tcl_PkgPresentEx</code> and <code>Tcl_PkgRequireEx</code> allow the setting and retrieving of the client data associated with the package. In all other respects they are equivalent to the matching functions. </p>
<p> <code>Tcl_PkgRequireProc</code> is the form of <code>package require</code> handling multiple requirements. The other forms are present for backward compatibility and translate their invocations to this form. </p>
<h2>Keywords</h2>
<p>package, present, provide, require, version</p>
