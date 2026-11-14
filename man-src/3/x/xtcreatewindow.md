---
title: "xtcreatewindow(3)"
name: "xtcreatewindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcreatewindow/"
description: "XtCreateWindow – window creation convenience function"
---

<p>XtCreateWindow &#8211; window creation convenience function </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtCreateWindow(Widget <i>w</i>, unsigned int <i>window_class</i>, Visual *<i>visual</i>, XtValueMask <i>value_mask</i>, XSetWindowAttributes *<i>attributes</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>attributes</i></p>
<dd>Specifies the window attributes to use in the <code>XCreateWindow</code> call.</p>
<dt><i>value_mask</i></p>
<dd>Specifies which attribute fields to use.</p>
<dt><i>visual</i></p>
<dd>Specifies the visual type (usually <code>CopyFromParent</code>).</p>
<dt><i>w</i></p>
<dd>Specifies the widget that is used to set the x,y coordinates and so on.</p>
<dt><i>window_class</i></p>
<dd>Specifies the Xlib window class (for example, <code>InputOutput</code>, <code>InputOnly</code>, or <code>CopyFromParent</code>).</dl>
<h2>Description</h2>
<p>The <code>XtCreateWindow</code> function calls the Xlib <code>XCreateWindow</code> function with values from the widget structure and the passed parameters. Then, it assigns the created window to the widget&#8217;s window field. </p>
<p> <code>XtCreateWindow</code> evaluates the following fields of the <code>Core</code> widget structure:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>depth</p>
<dt>&bull;</p>
<dd>screen</p>
<dt>&bull;</p>
<dd>parent -&gt; core.window</p>
<dt>&bull;</p>
<dd>x</p>
<dt>&bull;</p>
<dd>y</p>
<dt>&bull;</p>
<dd>width</p>
<dt>&bull;</p>
<dd>height</p>
<dt>&bull;</p>
<dd>border_width</dl>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
