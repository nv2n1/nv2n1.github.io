---
title: "xttranslatecoords(3)"
name: "xttranslatecoords"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xttranslatecoords/"
description: "XtTranslateCoords – translate widget coordinates"
---

<p>XtTranslateCoords &#8211; translate widget coordinates </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtTranslateCoords(Widget <i>w</i>, Position <i>x</i>, Position <i>y</i>, Position *<i>rootx_return</i>, Position *<i>rooty_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>rootx_return</i></p>
<dd>
<dt><i>rooty_return</i></p>
<dd>Returns the root-relative x and y coordinates.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the widget-relative x and y coordinates.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>While <code>XtTranslateCoords</code> is similar to the Xlib <code>XTranslateCoordinates</code> function, it does not generate a server request because all the required information already is in the widget&#8217;s data structures.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
