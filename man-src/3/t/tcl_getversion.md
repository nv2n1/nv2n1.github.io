---
title: "tcl_getversion(3)"
name: "tcl_getversion"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getversion/"
description: "Tcl_GetVersion – get the version of the library at runtime"
---

<p>Tcl_GetVersion &#8211; get the version of the library at runtime </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_GetVersion</code>(<i>major, minor, patchLevel, type</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>*major</i> (out) Major version number of the Tcl library.</p>
<dd>int <i>*minor</i> (out) Minor version number of the Tcl library.</p>
<dd>int <i>*patchLevel</i> (out) The patch level of the Tcl library (or alpha or beta number).</p>
<dd>Tcl_ReleaseType <i>*type</i> (out) The type of release, also indicates the type of patch level. Can be one of <code>TCL_ALPHA_RELEASE</code>, <code>TCL_BETA_RELEASE</code>, or <code>TCL_FINAL_RELEASE</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_GetVersion</code> should be used to query the version number of the Tcl library at runtime. This is useful when using a dynamically loaded Tcl library or when writing a stubs-aware extension. For instance, if you write an extension that is linked against the Tcl stubs library, it could be loaded into a program linked to an older version of Tcl than you expected. Use <code>Tcl_GetVersion</code> to verify that fact, and possibly to change the behavior of your extension. </p>
<p> <code>Tcl_GetVersion</code> accepts NULL for any of the arguments. For instance if you do not care about the <i>patchLevel</i> of the library, pass a NULL for the <i>patchLevel</i> argument. </p>
<h2>Keywords</h2>
<p>version, patchlevel, major, minor, alpha, beta, release</p>
