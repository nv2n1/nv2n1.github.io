---
title: "xgetinputfocus(3)"
name: "xgetinputfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetinputfocus/"
description: "XSetInputFocus, XGetInputFocus – control input focus"
---

<p>XSetInputFocus, XGetInputFocus &#8211; control input focus </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetInputFocus(Display *<i>display</i>, Window <i>focus</i>, int <i>revert_to</i>, Time <i>time</i>);</p>
<dd>int XGetInputFocus(Display *<i>display</i>, Window *<i>focus_return</i>, int *<i>revert_to_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>focus</i></p>
<dd>Specifies the window, <code>PointerRoot</code>, or <code>None</code>.</p>
<dt><i>focus_return</i></p>
<dd>Returns the focus window, <code>PointerRoot</code>, or <code>None</code>.</p>
<dt><i>revert_to</i></p>
<dd>Specifies where the input focus reverts to if the window becomes not viewable. You can pass <code>RevertToParent</code>, <code>RevertToPointerRoot</code>, or <code>RevertToNone</code>.</p>
<dt><i>revert_to_return</i></p>
<dd>Returns the current focus state <code>RevertToPointerRoot</code>, or <code>RevertToNone</code>).</p>
<dt><i>time</i></p>
<dd>Specifies the time. You can pass either a timestamp or <code>CurrentTime</code>.</dl>
<h2>Description</h2>
<p>The <code>XSetInputFocus</code> function changes the input focus and the last-focus-change time. It has no effect if the specified time is earlier than the current last-focus-change time or is later than the current X server time. Otherwise, the last-focus-change time is set to the specified time is replaced by the current X server time). <code>XSetInputFocus</code> causes the X server to generate <code>FocusIn</code> and <code>FocusOut</code> events. </p>
<p> Depending on the focus argument, the following occurs:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If focus is <code>None</code>, all keyboard events are discarded until a new focus window is set, and the revert_to argument is ignored.</p>
<dt>&bull;</p>
<dd>If focus is a window, it becomes the keyboard&#8217;s focus window. If a generated keyboard event would normally be reported to this window or one of its inferiors, the event is reported as usual. Otherwise, the event is reported relative to the focus window.</p>
<dt>&bull;</p>
<dd>If focus is <code>PointerRoot</code>, the focus window is dynamically taken to be the root window of whatever screen the pointer is on at each keyboard event. In this case, the revert_to argument is ignored.</dl>
<p> The specified focus window must be viewable at the time <code>XSetInputFocus</code> is called, or a <code>BadMatch</code> error results. If the focus window later becomes not viewable, the X server evaluates the revert_to argument to determine the new focus window as follows:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If revert_to is <code>RevertToParent</code>, the focus reverts to the parent (or the closest viewable ancestor), and the new revert_to value is taken to be <code>RevertToNone</code>.</p>
<dt>&bull;</p>
<dd>If revert_to is <code>RevertToPointerRoot</code> or <code>RevertToNone</code>, the focus reverts to <code>PointerRoot</code> or <code>None</code>, respectively. When the focus reverts, the X server generates <code>FocusIn</code> and <code>FocusOut</code> events, but the last-focus-change time is not affected.</dl>
<p> <code>XSetInputFocus</code> can generate <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XGetInputFocus</code> function returns the focus window and the current focus state.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xwarppointer/">XWarpPointer</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
