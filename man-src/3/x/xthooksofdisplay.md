---
title: "xthooksofdisplay(3)"
name: "xthooksofdisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xthooksofdisplay/"
---

XtHooksOfDisplay - external agent access points 

<h2>Syntax</h2>#include &lt;X11/Intrinsic.h&gt;
<dl COMPACT><dd>Widget XtHooksOfDisplay(Display* <i>display</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>display</i>
<dd>Specifies the desired display.</dl><h2>Description</h2>The class of this object is a private, implementation dependent, subclass of Object. The hook object has no parent. The resources of this object are the callback lists for hooks and the read-only resources for getting a list of parentless shells.
<h2>See Also</h2><i>X Toolkit Intrinsics - C Language Interface</i> 
 <i>Xlib - C Language X Interface</i>
