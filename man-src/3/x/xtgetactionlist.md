---
title: "xtgetactionlist(3)"
name: "xtgetactionlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetactionlist/"
description: "XtGetActionList – obtain class action list"
---

<p>XtGetActionList &#8211; obtain class action list </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetActionList(WidgetClass <i>widget_class</i>, XtActionList* <i>actions_return</i>, Cardinal* <i>num_actions_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class whose actions are to be returned.</p>
<dt><i>actions_return</i></p>
<dd>Returns the action list.</p>
<dt><i>num_actions_return</i></p>
<dd>Returns the number of action procedures declared by the class.</dl>
<h2>Description</h2>
<p><code>XtGetActionList</code> returns the action table defined by the specified widget class. This table does not include actions defined by the superclasses. If <i>widget_class</i> is not initialized, or is not <code>coreWidgetClass</code> or a subclass thereof, or if the class does not define any actions, *<i>actions_return</i> will be NULL and *<i>num_actions_return</i> will be zero. If *<i>actions_return</i> is non-NULL the client is responsible for freeing the table using <code>XtFree</code> when it is no longer needed.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
