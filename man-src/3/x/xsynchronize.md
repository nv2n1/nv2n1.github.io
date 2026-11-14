---
title: "xsynchronize(3)"
name: "xsynchronize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsynchronize/"
description: "XSynchronize, XSetAfterFunction – enable or disable synchronization"
---

<p>XSynchronize, XSetAfterFunction &#8211; enable or disable synchronization </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int (*XSynchronize(Display *<i>display</i>, Bool <i>onoff</i>))();</p>
<dd>int (*XSetAfterFunction(Display *<i>display</i>, int (*<i>procedure</i>)()))();</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>procedure</i></p>
<dd>Specifies the procedure to be called.</p>
<dt><i>onoff</i></p>
<dd>Specifies a Boolean value that indicates whether to enable or disable synchronization.</dl>
<h2>Description</h2>
<p>The <code>XSynchronize</code> function returns the previous after function. If onoff is <code>True</code>, <code>XSynchronize</code> turns on synchronous behavior. If onoff is <code>False</code>, <code>XSynchronize</code> turns off synchronous behavior. </p>
<p> The specified procedure is called with only a display pointer. <code>XSetAfterFunction</code> returns the previous after function.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xseterrorhandler/">XSetErrorHandler</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
