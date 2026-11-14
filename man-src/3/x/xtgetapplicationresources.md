---
title: "xtgetapplicationresources(3)"
name: "xtgetapplicationresources"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetapplicationresources/"
description: "XtGetApplicationResources, XtVaGetApplicationResources – obtain application resources"
---

<p>XtGetApplicationResources, XtVaGetApplicationResources &#8211; obtain application resources </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetApplicationResources(Widget <i>w</i>, XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaGetApplicationResources(Widget <i>w</i>, XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list to override resources obtained from the resource database.</p>
<dt><i>base</i></p>
<dd>Specifies the base address of the subpart data structure where the resources should be written.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</p>
<dt><i>num_resources</i></p>
<dd>Specifies the number of resources in the resource list.</p>
<dt><i>resources</i></p>
<dd>Specifies the resource list for the subpart.</p>
<dt><i>w</i></p>
<dd>Specifies the widget that wants resources for a subpart or that identifies the resource database to search.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable arguments to override resources obtained from the resource database.</dl>
<h2>Description</h2>
<p>The <code>XtGetApplicationResources</code> function first uses the passed widget, which is usually an application shell, to construct a resource name and class list, Then, it retrieves the resources from the argument list, the resource database, or the resource list default values. After adding base to each address, <code>XtGetApplicationResources</code> copies the resources into the address given in the resource list. If args is NULL, num_args must be zero. However, if num_args is zero, the argument list is not referenced. The portable way to specify application resources is to declare them as members of a structure and pass the address of the structure as the base argument.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
