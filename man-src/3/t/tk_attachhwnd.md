---
title: "tk_attachhwnd(3)"
name: "tk_attachhwnd"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_attachhwnd/"
description: "Tk_GetHWND, Tk_AttachHWND – manage interactions between the Windows handle and an X window"
---

<p>Tk_GetHWND, Tk_AttachHWND &#8211; manage interactions between the Windows handle and an X window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tkPlatDecls.h&gt;</code>
HWND
<code>Tk_GetHWND</code>(<i>window</i>)
Window
<code>Tk_AttachHWND</code>(<i>tkwin, hwnd</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Window <i>window</i> (in) X token for window.</p>
<dd>Tk_Window <i>tkwin</i> (in) Tk window for window.</p>
<dd>HWND <i>hwnd</i> (in) Windows HWND for window.
</dl>
<h2>Description</h2>
<p><code>Tk_GetHWND</code> returns the Windows HWND identifier for X Windows window given by <i>window</i>. </p>
<p> <code>Tk_AttachHWND</code> binds the Windows HWND identifier to the specified Tk_Window given by <i>tkwin</i>. It returns an X Windows window that encapsulates the HWND. </p>
<h2>Keywords</h2>
<p>identifier, window</p>
