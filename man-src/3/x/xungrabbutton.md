---
title: "xungrabbutton(3)"
name: "xungrabbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xungrabbutton/"
description: "XGrabButton, XUngrabButton – grab pointer buttons"
---

<p>XGrabButton, XUngrabButton &#8211; grab pointer buttons </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGrabButton(Display *<i>display</i>, unsigned int <i>button</i>, unsigned int <i>modifiers</i>, Window <i>grab_window</i>, Bool <i>owner_events</i>, unsigned int <i>event_mask</i>, int <i>pointer_mode</i>, <i>keyboard_mode</i>, Window <i>confine_to</i>, Cursor <i>cursor</i>);</p>
<dd>int XUngrabButton(Display *<i>display</i>, unsigned int <i>button</i>, unsigned int <i>modifiers</i>, Window <i>grab_window</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>button</i></p>
<dd>Specifies the pointer button that is to be grabbed or released or <code>AnyButton</code>.</p>
<dt><i>confine_to</i></p>
<dd>Specifies the window to confine the pointer in or <code>None</code>.</p>
<dt><i>cursor</i></p>
<dd>Specifies the cursor that is to be displayed or <code>None</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_mask</i></p>
<dd>Specifies which pointer events are reported to the client. The mask is the bitwise inclusive OR of the valid pointer event mask bits.</p>
<dt><i>grab_window</i></p>
<dd>Specifies the grab window.</p>
<dt><i>keyboard_mode</i></p>
<dd>Specifies further processing of keyboard events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>modifiers</i></p>
<dd>Specifies the set of keymasks or <code>AnyModifier</code>. The mask is the bitwise inclusive OR of the valid keymask bits.</p>
<dt><i>owner_events</i></p>
<dd>Specifies a Boolean value that indicates whether the pointer events are to be reported as usual or reported with respect to the grab window if selected by the event mask.</p>
<dt><i>pointer_mode</i></p>
<dd>Specifies further processing of pointer events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</dl>
<h2>Description</h2>
<p>The <code>XGrabButton</code> function establishes a passive grab. In the future, the pointer is actively grabbed (as for <code>XGrabPointer</code>), the last-pointer-grab time is set to the time at which the button was pressed (as transmitted in the <code>ButtonPress</code> event), and the <code>ButtonPress</code> event is reported if all of the following conditions are true:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The pointer is not grabbed, and the specified button is logically pressed when the specified modifier keys are logically down, and no other buttons or modifier keys are logically down.</p>
<dt>&bull;</p>
<dd>The grab_window contains the pointer.</p>
<dt>&bull;</p>
<dd>The confine_to window (if any) is viewable.</p>
<dt>&bull;</p>
<dd>A passive grab on the same button/key combination does not exist on any ancestor of grab_window.</dl>
<p> The interpretation of the remaining arguments is as for <code>XGrabPointer</code>. The active grab is terminated automatically when the logical state of the pointer has all buttons released (independent of the state of the logical modifier keys), at which point a <code>ButtonRelease</code> event is reported to the grabbing window. </p>
<p> Note that the logical state of a device (as seen by client applications) may lag the physical state if device event processing is frozen. </p>
<p> This request overrides all previous grabs by the same client on the same button/key combinations on the same window. A modifiers of <code>AnyModifier</code> is equivalent to issuing the grab request for all possible modifier combinations (including the combination of no modifiers). It is not required that all modifiers specified have currently assigned KeyCodes. A button of <code>AnyButton</code> is equivalent to issuing the request for all possible buttons. Otherwise, it is not required that the specified button currently be assigned to a physical button. </p>
<p> If some other client has already issued a <code>XGrabButton</code> with the same button/key combination on the same window, a <code>BadAccess</code> error results. When using <code>AnyModifier</code> or <code>AnyButton</code>, the request fails completely, and a <code>BadAccess</code> error results (no grabs are established) if there is a conflicting grab for any combination. <code>XGrabButton</code> has no effect on an active grab. </p>
<p> <code>XGrabButton</code> can generate <code>BadCursor</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XUngrabButton</code> function releases the passive button/key combination on the specified window if it was grabbed by this client. A modifiers of <code>AnyModifier</code> is equivalent to issuing the ungrab request for all possible modifier combinations, including the combination of no modifiers. A button of <code>AnyButton</code> is equivalent to issuing the request for all possible buttons. <code>XUngrabButton</code> has no effect on an active grab. </p>
<p> <code>XUngrabButton</code> can generate <code>BadValue</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallowevents/">XAllowEvents</a>(3), <a href="/docs/linux/man/3-xgrabpointer/">XGrabPointer</a>(3), <a href="/docs/linux/man/3-xgrabkey/">XGrabKey</a>(3), <a href="/docs/linux/man/3-xgrabkeyboard/">XGrabKeyboard</a>(3),<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
