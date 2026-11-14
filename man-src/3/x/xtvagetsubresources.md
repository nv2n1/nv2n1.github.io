---
title: "xtvagetsubresources(3)"
name: "xtvagetsubresources"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvagetsubresources/"
description: "XtGetSubresources, XtVaGetSubresources – obtain subresources"
---

<p>XtGetSubresources, XtVaGetSubresources &#8211; obtain subresources </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetSubresources(Widget <i>w</i>, XtPointer <i>base</i>, const char *<i>name</i>, const char * <i>class</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaGetSubresources(Widget <i>w</i>, XtPointer <i>base</i>, const char *<i>name</i>, const char *<i>class</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list to override resources obtained from the resource database.</p>
<dt><i>base</i></p>
<dd>Specifies the base address of the subpart data structure where the resources should be written.</p>
<dt><i>class</i></p>
<dd>Specifies the class of the subpart.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the subpart.</p>
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
<p>The <code>XtGetSubresources</code> function constructs a name/class list from the application name/class, the name/classes of all its ancestors, and the widget itself. Then, it appends to this list the name/class pair passed in. The resources are fetched from the argument list, the resource database, or the default values in the resource list. Then, they are copied into the subpart record. If args is NULL, num_args must be zero. However, if num_args is zero, the argument list is not referenced.</p>
<h2>See Also</h2>
<p>XtGetApplicationResources, XtVaGetApplicationResources<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
