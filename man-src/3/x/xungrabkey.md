---
title: "xungrabkey(3)"
name: "xungrabkey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xungrabkey/"
description: "XGrabKey, XUngrabKey – grab keyboard keys"
---

<p>XGrabKey, XUngrabKey &#8211; grab keyboard keys </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGrabKey(Display *<i>display</i>, int <i>keycode</i>, unsigned int <i>modifiers</i>, Window <i>grab_window</i>, Bool <i>owner_events</i>, int <i>pointer_mode</i>, int <i>keyboard_mode</i>);</p>
<dd>int XUngrabKey(Display *<i>display</i>, int <i>keycode</i>, unsigned int <i>modifiers</i>, Window <i>grab_window</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>grab_window</i></p>
<dd>Specifies the grab window.</p>
<dt><i>keyboard_mode</i></p>
<dd>Specifies further processing of keyboard events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</p>
<dt><i>keycode</i></p>
<dd>Specifies the KeyCode or <code>AnyKey</code>.</p>
<dt><i>modifiers</i></p>
<dd>Specifies the set of keymasks or <code>AnyModifier</code>. The mask is the bitwise inclusive OR of the valid keymask bits.</p>
<dt><i>owner_events</i></p>
<dd>Specifies a Boolean value that indicates whether the keyboard events are to be reported as usual.</p>
<dt><i>pointer_mode</i></p>
<dd>Specifies further processing of pointer events. You can pass <code>GrabModeSync</code> or <code>GrabModeAsync</code>.</dl>
<h2>Description</h2>
<p>The <code>XGrabKey</code> function establishes a passive grab on the keyboard. In the future, the keyboard is actively grabbed (as for <code>XGrabKeyboard</code>), the last-keyboard-grab time is set to the time at which the key was pressed (as transmitted in the <code>KeyPress</code> event), and the <code>KeyPress</code> event is reported if all of the following conditions are true:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The keyboard is not grabbed and the specified key (which can itself be a modifier key) is logically pressed when the specified modifier keys are logically down, and no other modifier keys are logically down.</p>
<dt>&bull;</p>
<dd>Either the grab_window is an ancestor of (or is) the focus window, or the grab_window is a descendant of the focus window and contains the pointer.</p>
<dt>&bull;</p>
<dd>A passive grab on the same key combination does not exist on any ancestor of grab_window.</dl>
<p> The interpretation of the remaining arguments is as for <code>XGrabKeyboard</code>. The active grab is terminated automatically when the logical state of the keyboard has the specified key released (independent of the logical state of the modifier keys), at which point a <code>KeyRelease</code> event is reported to the grabbing window. </p>
<p> Note that the logical state of a device (as seen by client applications) may lag the physical state if device event processing is frozen. </p>
<p> A modifiers argument of <code>AnyModifier</code> is equivalent to issuing the request for all possible modifier combinations (including the combination of no modifiers). It is not required that all modifiers specified have currently assigned KeyCodes. A keycode argument of <code>AnyKey</code> is equivalent to issuing the request for all possible KeyCodes. Otherwise, the specified keycode must be in the range specified by min_keycode and max_keycode in the connection setup, or a <code>BadValue</code> error results. </p>
<p> If some other client has issued a <code>XGrabKey</code> with the same key combination on the same window, a <code>BadAccess</code> error results. When using <code>AnyModifier</code> or <code>AnyKey</code>, the request fails completely, and a <code>BadAccess</code> error results (no grabs are established) if there is a conflicting grab for any combination. </p>
<p> <code>XGrabKey</code> can generate <code>BadAccess</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XUngrabKey</code> function releases the key combination on the specified window if it was grabbed by this client. It has no effect on an active grab. A modifiers of <code>AnyModifier</code> is equivalent to issuing the request for all possible modifier combinations (including the combination of no modifiers). A keycode argument of <code>AnyKey</code> is equivalent to issuing the request for all possible key codes. </p>
<p> <code>XUngrabKey</code> can generate <code>BadValue</code> and <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>A client attempted to grab a key/button combination already grabbed by another client.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xallowevents/">XAllowEvents</a>(3), <a href="/docs/linux/man/3-xgrabbutton/">XGrabButton</a>(3), <a href="/docs/linux/man/3-xgrabkeyboard/">XGrabKeyboard</a>(3), <a href="/docs/linux/man/3-xgrabpointer/">XGrabPointer</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
