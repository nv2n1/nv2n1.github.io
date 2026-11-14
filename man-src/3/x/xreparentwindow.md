---
title: "xreparentwindow(3)"
name: "xreparentwindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xreparentwindow/"
description: "XReparentWindow – reparent windows"
---

<p>XReparentWindow &#8211; reparent windows </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XReparentWindow(Display *<i>display</i>, Window <i>w</i>, Window <i>parent</i>, int <i>x</i>, int <i>y</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>parent</i></p>
<dd>Specifies the parent window.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates of the position in the new parent window.</dl>
<h2>Description</h2>
<p>If the specified window is mapped, <code>XReparentWindow</code> automatically performs an <code>UnmapWindow</code> request on it, removes it from its current position in the hierarchy, and inserts it as the child of the specified parent. The window is placed in the stacking order on top with respect to sibling windows. </p>
<p> After reparenting the specified window, <code>XReparentWindow</code> causes the X server to generate a <code>ReparentNotify</code> event. The override_redirect member returned in this event is set to the window&#8217;s corresponding attribute. Window manager clients usually should ignore this window if this member is set to <code>True</code>. Finally, if the specified window was originally mapped, the X server automatically performs a <code>MapWindow</code> request on it. </p>
<p> The X server performs normal exposure processing on formerly obscured windows. The X server might not generate <code>Expose</code> events for regions from the initial <code>UnmapWindow</code> request that are immediately obscured by the final <code>MapWindow</code> request. A <code>BadMatch</code> error results if:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The new parent window is not on the same screen as the old parent window.</p>
<dt>&bull;</p>
<dd>The new parent window is the specified window or an inferior of the specified window.</p>
<dt>&bull;</p>
<dd>The new parent is <code>InputOnly</code>, and the window is not.</p>
<dt>&bull;</p>
<dd>The specified window has a <code>ParentRelative</code> background, and the new parent window is not the same depth as the specified window.</dl>
<p> <code>XReparentWindow</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangesaveset/">XChangeSaveSet</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
