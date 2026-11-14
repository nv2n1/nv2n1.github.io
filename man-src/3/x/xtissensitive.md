---
title: "xtissensitive(3)"
name: "xtissensitive"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtissensitive/"
description: "XtSetSensitive, XtIsSensitive – set and check a widget’s sensitivity state"
---

<p>XtSetSensitive, XtIsSensitive &#8211; set and check a widget&#8217;s sensitivity state </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetSensitive(Widget <i>w</i>, Boolean <i>sensitive</i>);</p>
<dd>Boolean XtIsSensitive(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>sensitive</i></p>
<dd>Specifies a Boolean value that indicates whether the widget should receive keyboard and pointer events.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtSetSensitive</code> function first calls <code>XtSetValues</code> on the current widget with an argument list specifying that the sensitive field should change to the new value. It then recursively propagates the new value down the managed children tree by calling <code>XtSetValues</code> on each child to set the ancestor_sensitive to the new value if the new values for sensitive and the child&#8217;s ancestor_sensitive are not the same. </p>
<p> <code>XtSetSensitive</code> calls <code>XtSetValues</code> to change sensitive and ancestor_sensitive. Therefore, when one of these changes, the widget&#8217;s set_values procedure should take whatever display actions are needed (for example, greying out or stippling the widget). </p>
<p> <code>XtSetSensitive</code> maintains the invariant that if parent has either sensitive or ancestor_sensitive <code>False</code>, then all children have ancestor_sensitive <code>False</code>. </p>
<p> The <code>XtIsSensitive</code> function returns <code>True</code> or <code>False</code> to indicate whether or not user input events are being dispatched. If both core.sensitive and core.ancestor_sensitive are <code>True</code>, <code>XtIsSensitive</code> returns <code>True</code>; otherwise, it returns <code>False</code>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
