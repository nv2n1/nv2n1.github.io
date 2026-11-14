---
title: "tk_idtowindow(3)"
name: "tk_idtowindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_idtowindow/"
description: "Tk_IdToWindow – Find Tk’s window information for an X window"
---

<p>Tk_IdToWindow &#8211; Find Tk&#8217;s window information for an X window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_IdToWindow</code>(<i>display, window</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) X display containing the window.</p>
<dd>Window <i>window</i> (in) X id for window. </p>
</dl>
<h2>Description</h2>
<p>Given an X window identifier and the X display it corresponds to, this procedure returns the corresponding Tk_Window handle. If there is no Tk_Window corresponding to <i>window</i> then NULL is returned. </p>
<h2>Keywords</h2>
<p>X window id</p>
