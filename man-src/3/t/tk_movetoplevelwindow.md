---
title: "tk_movetoplevelwindow(3)"
name: "tk_movetoplevelwindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_movetoplevelwindow/"
description: "Tk_MoveToplevelWindow – Adjust the position of a top-level window"
---

<p>Tk_MoveToplevelWindow &#8211; Adjust the position of a top-level window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_MoveToplevelWindow(</code><i>tkwin, x, y</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for top-level window to move.</p>
<dd>int <i>x</i> (in) New x-coordinate for the top-left pixel of <i>tkwin</i>&#8216;s border, or the top-left pixel of the decorative border supplied for <i>tkwin</i> by the window manager, if there is one.</p>
<dd>int <i>y</i> (in) New y-coordinate for the top-left pixel of <i>tkwin</i>&#8216;s border, or the top-left pixel of the decorative border supplied for <i>tkwin</i> by the window manager, if there is one. </p>
</dl>
<h2>Description</h2>
<p>In general, a window should never set its own position; this should be done only by the geometry manger that is responsible for the window. For top-level windows the window manager is effectively the geometry manager; Tk provides interface code between the application and the window manager to convey the application&#8217;s desires to the geometry manager. The desired size for a top-level window is conveyed using the usual <code>Tk_GeometryRequest</code> mechanism. The procedure <code>Tk_MoveToplevelWindow</code> may be used by an application to request a particular position for a top-level window; this procedure is similar in function to the <code>wm geometry</code> Tcl command except that negative offsets cannot be specified. It is invoked by widgets such as menus that want to appear at a particular place on the screen. </p>
<p> When <code>Tk_MoveToplevelWindow</code> is called it does not immediately pass on the new desired location to the window manager; it defers this action until all other outstanding work has been completed, using the <code>Tk_DoWhenIdle</code> mechanism. </p>
<h2>Keywords</h2>
<p>position, top-level window, window manager</p>
