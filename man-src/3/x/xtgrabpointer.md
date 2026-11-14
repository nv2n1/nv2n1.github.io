---
title: "xtgrabpointer(3)"
name: "xtgrabpointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgrabpointer/"
description: "XtGrabKey, XtUngrabKey, XtGrabKeyboard, XtUngrabKeyboard, XtGrabButton, XtUngrabButton, XtGrabPointer, XtUngrabPointer – manage grabs"
---

<p>XtGrabKey, XtUngrabKey, XtGrabKeyboard, XtUngrabKeyboard, XtGrabButton, XtUngrabButton, XtGrabPointer, XtUngrabPointer &#8211; manage grabs </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGrabKey(Widget <i>widget</i>, KeyCode <i>keycode</i>, Modifiers <i>modifiers</i>, Boolean <i>owner_events</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>);</p>
<dd>void XtUngrabKey(Widget <i>widget</i>, KeyCode <i>keycode</i>, Modifiers <i>modifiers</i>);</p>
<dd>int XtGrabKeyboard(Widget <i>widget</i>, Boolean <i>owner_events</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>, Time <i>time</i>);</p>
<dd>void XtUngrabKeyboard(Widget <i>widget</i>, Time <i>time</i>);</p>
<dd>void XtGrabButton(Widget <i>widget</i>, int <i>button</i>, Modifiers <i>modifiers</i>, Boolean <i>owner_events</i>, unsigned int <i>event_mask</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>, Window <i>confine_to</i>, Cursor <i>cursor</i>);</p>
<dd>void XtUngrabButton(Widget <i>widget</i>, unsigned <i>button</i>, Modifiers <i>modifiers</i>);</p>
<dd>int XtGrabPointer(Widget <i>widget</i>, Boolean <i>owner_events</i>, unsigned int <i>event_mask</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>, Window <i>confine_to</i>, Cursor <i>cursor</i>, Time <i>time</i>);</p>
<dd>void XtUngrabPointer(Widget <i>widget</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget in whose window the grab will occur. Must be of class Core or a subclass thereof. </p>
<dt><i>keycode</i></p>
<dd>
<dt><i>modifiers</i></p>
<dd>
<dt><i>owner_events</i></p>
<dd>
<dt><i>pointer_mode</i></p>
<dd>
<dt><i>keyboard_mode</i></p>
<dd>
<dt><i>time</i></p>
<dd>
<dt><i>button</i></p>
<dd>
<dt><i>confine_to</i></p>
<dd>
<dt><i>cursor</i></p>
<dd>Specifies arguments to the associated Xlib function call.</dl>
<h2>Description</h2>
<p><code>XtGrabKey</code> calls <code>XGrabKey</code> specifying the widget&#8217;s window as the grab window if the widget is realized. The remaining arguments are exactly as for <code>XGrabKey</code>. If the widget is not realized, or is later unrealized, the call to <code>XGrabKey</code> will be performed (again) when the widget is realized and its window becomes mapped. In the future, if <code>XtDispatchEvent</code> is called with a <code>KeyPress</code> event matching the specified keycode and modifiers (which may be <code>AnyKey</code> or <code>AnyModifier</code>, respectively) for the widget&#8217;s window, the Intrinsics will call <code>XtUngrabKeyboard</code> with the timestamp from the <code>KeyPress</code> event if either of the following conditions is true:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>There is a modal cascade and the widget is not in the active subset of the cascade and the keyboard was not previously grabbed, or</p>
<dt>&bull;</p>
<dd><code>XFilterEvent</code> returns <code>True</code>.</dl>
<p> <code>XtUngrabKey</code> calls <code>XUngrabKey</code> specifying the widget&#8217;s window as the ungrab window if the widget is realized. The remaining arguments are exactly as for <code>XUngrabKey</code>. If the widget is not realized, <code>XtUngrabKey</code> removes a deferred <code>XtGrabKey</code> request, if any, for the specified widget, keycode, and modifiers. </p>
<p> If the specified widget is realized <code>XtGrabKeyboard</code> calls <code>XGrabKeyboard</code> specifying the widget&#8217;s window as the grab window. The remaining arguments and return value are exactly as for <code>XGrabKeyboard</code>. If the widget is not realized, <code>XtGrabKeyboard</code> immediately returns <code>GrabNotViewable</code>. No future ungrab is implied by <code>XtGrabKeyboard</code>. </p>
<p> <code>XtUngrabKeyboard</code> calls <code>XUngrabKeyboard</code> with the specified time. </p>
<p> <code>XtGrabButton</code> calls <code>XGrabButton</code> specifying the widget&#8217;s window as the grab window if the widget is realized. The remaining arguments are exactly as for <code>XGrabButton</code>. If the widget is not realized, or is later unrealized, the call to <code>XGrabButton</code> will be performed (again) when the widget is realized and its window becomes mapped. In the future, if <code>XtDispatchEvent</code> is called with a <code>ButtonPress</code> event matching the specified button and modifiers (which may be <code>AnyButton</code> or <code>AnyModifier</code>, respectively) for the widget&#8217;s window, the Intrinsics will call <code>XtUngrabPointer</code> with the timestamp from the <code>ButtonPress</code> event if either of the following conditions is true:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>There is a modal cascade and the widget is not in the active subset of the cascade and the pointer was not previously grabbed, or</p>
<dt>&bull;</p>
<dd><code>XFilterEvent</code> returns <code>True</code>.</dl>
<p> <code>XtUngrabButton</code> calls <code>XUngrabButton</code> specifying the widget&#8217;s window as the ungrab window if the widget is realized. The remaining arguments are exactly as for <code>XUngrabButton</code>. If the widget is not realized, <code>XtUngrabButton</code> removes a deferred <code>XtGrabButton</code> request, if any, for the specified widget, button, and modifiers. </p>
<p> <code>XtGrabPointer</code> calls <code>XGrabPointer</code> specifying the widget&#8217;s window as the grab window. The remaining arguments and return value are exactly as for <code>XGrabPointer</code>. If the widget is not realized, <code>XtGrabPointer</code> immediately returns <code>GrabNotViewable</code>. No future ungrab is implied by <code>XtGrabPointer</code>. </p>
<p> <code>XtUngrabPointer</code> calls <code>XUngrabPointer</code> with the specified time.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
