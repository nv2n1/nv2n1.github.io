---
title: "tk_mapwindow(3)"
name: "tk_mapwindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_mapwindow/"
description: "Tk_MapWindow, Tk_UnmapWindow – map or unmap a window"
---

<p>Tk_MapWindow, Tk_UnmapWindow &#8211; map or unmap a window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_MapWindow</code>(<i>tkwin</i>)
<code>Tk_UnmapWindow</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window. </p>
</dl>
<h2>Description</h2>
<p>These procedures may be used to map and unmap windows managed by Tk. <code>Tk_MapWindow</code> maps the window given by <i>tkwin</i>, and also creates an X window corresponding to <i>tkwin</i> if it does not already exist. See the <code>Tk_CreateWindow</code> manual entry for information on deferred window creation. <code>Tk_UnmapWindow</code> unmaps <i>tkwin</i>&#8216;s window from the screen. </p>
<p> If <i>tkwin</i> is a child window (i.e. <code>Tk_CreateWindow</code> was used to create a child window), then event handlers interested in map and unmap events are invoked immediately. If <i>tkwin</i> is not an internal window, then the event handlers will be invoked later, after X has seen the request and returned an event for it. </p>
<p> These procedures should be used in place of the X procedures <code>XMapWindow</code> and <code>XUnmapWindow</code>, since they update Tk&#8217;s local data structure for <i>tkwin</i>. Applications using Tk should not invoke <code>XMapWindow</code> and <code>XUnmapWindow</code> directly. </p>
<h2>Keywords</h2>
<p>map, unmap, window</p>
