---
title: "xtgetresourcelist(3)"
name: "xtgetresourcelist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetresourcelist/"
description: "XtGetResourceList, XtGetConstraintResourceList – obtain resource list"
---

<p>XtGetResourceList, XtGetConstraintResourceList &#8211; obtain resource list </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetResourceList(WidgetClass <i>class</i>, XtResourceList *<i>resources_return</i>, Cardinal *<i>num_resources_return</i>);</p>
<dd>void XtGetConstraintResourceList(WidgetClass <i>class</i>, XtResourceList *<i>resources_return</i>, Cardinal *<i>num_resources_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>num_resources_return</i></p>
<dd>Specifies a pointer to where to store the number of entries in the resource list.</p>
<dt><i>resources_return</i></p>
<dd>Specifies a pointer to where to store the returned resource list. The caller must free this storage using <code>XtFree</code> when done with it.</p>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class for which you want the list.</dl>
<h2>Description</h2>
<p>If <code>XtGetResourceList</code> is called before the widget class is initialized (that is, before the first widget of that class has been created), <code>XtGetResourceList</code> returns the resource list as specified in the widget class record. If it is called after the widget class has been initialized, <code>XtGetResourceList</code> returns a merged resource list that contains the resources for all superclasses. The list returned by <code>XtGetResourceList</code> should be freed using <code>XtFree</code> when it is no longer needed. </p>
<p> If <code>XtGetConstraintResourceList</code> is called before the widget class is initialized (that is, before the first widget of that class has been created), <code>XtGetConstraintResourceList</code> returns the resource list as specified in the widget class Constraint part record. If it is called after the widget class has been initialized, <code>XtGetConstraintResourceList</code> returns a merged resource list that contains the Constraint resources for all superclasses. If the specified class is not a subclass of <code>constraintWidgetClass</code>, <i>*resources_return</i> is set to NULL and <i>*num_resources_return</i> is set to zero. The list returned by <code>XtGetConstraintResourceList</code> should be freed using <code>XtFree</code> when it is no longer needed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtgetsubresources/">XtGetSubresources</a>(3), <a href="/docs/linux/man/3-xtoffset/">XtOffset</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
