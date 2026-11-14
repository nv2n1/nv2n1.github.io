---
title: "tk_coordstowindow(3)"
name: "tk_coordstowindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_coordstowindow/"
description: "Tk_CoordsToWindow – Find window containing a point"
---

<p>Tk_CoordsToWindow &#8211; Find window containing a point </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_CoordsToWindow</code>(<i>rootX, rootY, tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>rootX</i> (in) X-coordinate (in root window coordinates).</p>
<dd>int <i>rootY</i> (in) Y-coordinate (in root window coordinates).</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window that identifies application. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CoordsToWindow</code> locates the window that contains a given point. The point is specified in root coordinates with <i>rootX</i> and <i>rootY</i> (if a virtual-root window manager is in use then <i>rootX</i> and <i>rootY</i> are in the coordinate system of the virtual root window). The return value from the procedure is a token for the window that contains the given point. If the point is not in any window, or if the containing window is not in the same application as <i>tkwin</i>, then NULL is returned. </p>
<p> The containing window is decided using the same rules that determine which window contains the mouse cursor: if a parent and a child both contain the point then the child gets preference, and if two siblings both contain the point then the highest one in the stacking order (i.e. the one that&#8217;s visible on the screen) gets preference. </p>
<h2>Keywords</h2>
<p>containing, coordinates, root window</p>
