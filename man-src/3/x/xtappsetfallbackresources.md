---
title: "xtappsetfallbackresources(3)"
name: "xtappsetfallbackresources"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappsetfallbackresources/"
description: "XtAppSetFallbackResources – set fallback resources"
---

<p>XtAppSetFallbackResources &#8211; set fallback resources </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppSetFallbackResources(XtAppContext <i>app_context</i>, String* <i>specification_list</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>specification_list</i></p>
<dd>Specifies a NULL-terminated list of resource specifications to pre-load the database, or NULL.</dl>
<h2>Description</h2>
<p>Each entry in <i>specification_list</i> points to a string in the format <code>XrmPutLineResource</code>. following a call to <code>XtAppSetFallbackResources</code>, when a resource database is being created for a particular screen and the Intrinsics are not able to find or read an application-specific class resource file and if <i>specification_list</i> is not NULL the resource specification in <i>specification_list</i> will be merged into the screen resource database in place of the application-specific class resource file. <code>XtAppSetFallbackResources</code> is not required to copy <i>specification_list</i>; the caller must ensure that the contents of the list and the strings addressed by the list remain valid until all displays are initialized or until <code>XtAppSetFallbackResources</code> is called again. The value NULL for <i>specification_list</i> removes any previous fallback resource specification for the application context. The intended use for fallback resources is to provide a minimal number of resources that will make the application usable (or at least terminate with helpful diagnostic messages) when some problem exists in finding and loading the application defaults file.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
