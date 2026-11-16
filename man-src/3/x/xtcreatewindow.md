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
<dd>void XtCreateWindow(Widget <i>w</i>, unsigned int <i>window_class</i>, Visual *<i>visual</i>, XtValueMask <i>value_mask</i>, XSetWindowAttributes *<i>attributes</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>attributes</i></dt>
<dd>Specifies the window attributes to use in the <code>XCreateWindow</code> call.</dd>
<dt><i>value_mask</i></dt>
<dd>Specifies which attribute fields to use.</dd>
<dt><i>visual</i></dt>
<dd>Specifies the visual type (usually <code>CopyFromParent</code>).</dd>
<dt><i>w</i></dt>
<dd>Specifies the widget that is used to set the x,y coordinates and so on.</dd>
<dt><i>window_class</i></dt>
<dd>Specifies the Xlib window class (for example, <code>InputOutput</code>, <code>InputOnly</code>, or <code>CopyFromParent</code>).</dd></dl>
<h2>Description</h2>
<p>The <code>XtCreateWindow</code> function calls the Xlib <code>XCreateWindow</code> function with values from the widget structure and the passed parameters. Then, it assigns the created window to the widget&#8217;s window field. </p>
<p> <code>XtCreateWindow</code> evaluates the following fields of the <code>Core</code> widget structure:</p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>depth</dd>
<dt>&bull;</dt>
<dd>screen</dd>
<dt>&bull;</dt>
<dd>parent -&gt; core.window</dd>
<dt>&bull;</dt>
<dd>x</dd>
<dt>&bull;</dt>
<dd>y</dd>
<dt>&bull;</dt>
<dd>width</dd>
<dt>&bull;</dt>
<dd>height</dd>
<dt>&bull;</dt>
<dd>border_width</dd></dl>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
