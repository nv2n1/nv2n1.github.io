---
title: "tk_hwndtowindow(3)"
name: "tk_hwndtowindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_hwndtowindow/"
description: "Tk_HWNDToWindow – Find Tk’s window information for a Windows window"
---

<p>Tk_HWNDToWindow &#8211; Find Tk&#8217;s window information for a Windows window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tkPlatDecls.h&gt;</code>
Tk_Window
<code>Tk_HWNDToWindow</code>(<i>hwnd</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>HWND <i>hwnd</i> (in) Windows handle for the window. </p>
</dl>
<h2>Description</h2>
<p>Given a Windows HWND window identifier, this procedure returns the corresponding Tk_Window handle. If there is no Tk_Window corresponding to <i>hwnd</i> then NULL is returned. </p>
<h2>Keywords</h2>
<p>Windows window id</p>
