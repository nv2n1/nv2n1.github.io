---
title: "xtisrealized(3)"
name: "xtisrealized"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtisrealized/"
description: "XtRealizeWidget, XtIsRealized, XtUnrealizeWidget – realize and unrealize widgets"
---

<p>XtRealizeWidget, XtIsRealized, XtUnrealizeWidget &#8211; realize and unrealize widgets </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtRealizeWidget(Widget <i>w</i>);</p>
<dd>Boolean XtIsRealized(Widget <i>w</i>);</p>
<dd>void XtUnrealizeWidget(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>If the widget is already realized, <code>XtRealizeWidget</code> simply returns. Otherwise, it performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Binds all action names in the widget&#8217;s translation table to procedures (see Section 10.1.2).</p>
<dt>&bull;</p>
<dd>Makes a post-order traversal of the widget tree rooted at the specified widget and calls the change_managed procedure of each composite widget that has one or more managed children.</p>
<dt>&bull;</p>
<dd>Constructs an <code>XSetWindowAttributes</code> structure filled in with information derived from the <code>Core</code> widget fields and calls the realize procedure for the widget, which adds any widget-specific attributes and creates the X window.</p>
<dt>&bull;</p>
<dd>If the widget is not a subclass of <code>compositeWidgetClass</code>, <code>XtRealizeWidget</code> returns; otherwise, it continues and performs the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Descends recursively to each of the widget&#8217;s managed children and calls the realize procedures. Primitive widgets that instantiate children are responsible for realizing those children themselves.</p>
<dt>&#8211;</p>
<dd>Maps all of the managed children windows that have mapped_when_managed <code>True</code>. (If a widget is managed but mapped_when_managed is <code>False</code>, the widget is allocated visual space but is not displayed. Some people seem to like this to indicate certain states.)</dl>
</dl>
</dl>
<p> If the widget is a top-level shell widget (that is, it has no parent), and mapped_when_managed is <code>True</code>, <code>XtRealizeWidget</code> maps the widget window. </p>
<p> The <code>XtIsRealized</code> function returns <code>True</code> if the widget has been realized, that is, if the widget has a nonzero X window ID. </p>
<p> Some widget procedures (for example, set_values) might wish to operate differently after the widget has been realized. </p>
<p> The <code>XtUnrealizeWidget</code> function destroys the windows of an existing widget and all of its children (recursively down the widget tree). To recreate the windows at a later time, call <code>XtRealizeWidget</code> again. If the widget was managed, it will be unmanaged automatically before its window is freed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtmanagechildren/">XtManageChildren</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
