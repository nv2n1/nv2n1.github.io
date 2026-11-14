---
title: "tcl_staticpackage(3)"
name: "tcl_staticpackage"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_staticpackage/"
description: "Tcl_StaticPackage – make a statically linked package available via the ‘load’ command"
---

<p>Tcl_StaticPackage &#8211; make a statically linked package available via the &#8216;load&#8217; command </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_StaticPackage</code>(<i>interp, pkgName, initProc, safeInitProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) If not NULL, points to an interpreter into which the package has already been loaded (i.e., the caller has already invoked the appropriate initialization procedure). NULL means the package has not yet been incorporated into any interpreter.</p>
<dd>const char <i>*pkgName</i> (in) Name of the package; should be properly capitalized (first letter upper-case, all others lower-case).</p>
<dd>Tcl_PackageInitProc <i>*initProc</i> (in) Procedure to invoke to incorporate this package into a trusted interpreter.</p>
<dd>Tcl_PackageInitProc <i>*safeInitProc</i> (in) Procedure to call to incorporate this package into a safe interpreter (one that will execute untrusted scripts). NULL means the package cannot be used in safe interpreters. </p>
</dl>
<h2>Description</h2>
<p>This procedure may be invoked to announce that a package has been linked statically with a Tcl application and, optionally, that it has already been loaded into an interpreter. Once <code>Tcl_StaticPackage</code> has been invoked for a package, it may be loaded into interpreters using the <code>load</code> command. <code>Tcl_StaticPackage</code> is normally invoked only by the <code>Tcl_AppInit</code> procedure for the application, not by packages for themselves (<code>Tcl_StaticPackage</code> should only be invoked for statically loaded packages, and code in the package itself should not need to know whether the package is dynamically or statically loaded). </p>
<p> When the <code>load</code> command is used later to load the package into an interpreter, one of <i>initProc</i> and <i>safeInitProc</i> will be invoked, depending on whether the target interpreter is safe or not. <i>initProc</i> and <i>safeInitProc</i> must both match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_PackageInitProc(Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>interp</i> argument identifies the interpreter in which the package is to be loaded. The initialization procedure must return <code>TCL_OK</code> or <code>TCL_ERROR</code> to indicate whether or not it completed successfully; in the event of an error it should set the interpreter&#8217;s result to point to an error message. The result or error from the initialization procedure will be returned as the result of the <code>load</code> command that caused the initialization procedure to be invoked. </p>
<h2>Keywords</h2>
<p>initialization procedure, package, static linking</p>
