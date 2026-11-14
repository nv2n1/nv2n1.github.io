---
title: "xtsetkeyboardfocus(3)"
name: "xtsetkeyboardfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetkeyboardfocus/"
description: "XtSetKeyboardFocus – focus events on a child widget"
---

<p>XtSetKeyboardFocus &#8211; focus events on a child widget </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetKeyboardFocus(Widget <i>subtree</i>, Widget <i>descendant</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>subtree</i></p>
<dd>Specifies either the widget in the subtree structure which is to receive the keyboard event, or <code>None</code>. Note that it is not an error to specify <code>None</code> when no input focus was previously set.</p>
<dt><i>descendant</i></p>
<dd>Specifies the widget for which the keyboard focus is to be set.</dl>
<h2>Description</h2>
<p>If a future <code>KeyPress</code> or <code>KeyRelease</code> event occurs within the specified subtree, <code>XtSetKeyboardFocus</code> causes <code>XtDispatchEvent</code> to remap and send the event to the specified descendant widget. </p>
<p> When there is no modal cascade, keyboard events can occur within a widget W in one of three ways:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>W has the X input focus.</p>
<dt>&bull;</p>
<dd>W has the keyboard focus of one of its ancestors, and the event occurs within the ancestor or one of the ancestor&#8217;s descendants.</p>
<dt>&bull;</p>
<dd>No ancestor of W has a descendant within the keyboard focus, and the pointer is within W.</dl>
<p> When there is a modal cascade, a widget W receives keyboard events if an ancestor of W is in the active subset of the modal cascade and one or more of the previous conditions is <code>True</code>. </p>
<p> When subtree or one of its descendants acquires the X input focus or the pointer moves into the subtree such that keyboard events would now be delivered to subtree, a <code>FocusIn</code> event is generated for the descendant if <code>FocusNotify</code> events have been selected by the descendant. Similarly, when W loses the X input focus or the keyboard focus for one of its ancestors, a <code>FocusOut</code> event is generated for descendant if <code>FocusNotify</code> events have been selected by the descendant.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcallacceptfocus/">XtCallAcceptFocus</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
