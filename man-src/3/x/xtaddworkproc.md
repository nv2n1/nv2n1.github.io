---
title: "xtaddworkproc(3)"
name: "xtaddworkproc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddworkproc/"
description: "XtAddInput, XtAddTimeOut, XtAddWorkProc – register input, timeout, and workprocs"
---

<p>XtAddInput, XtAddTimeOut, XtAddWorkProc &#8211; register input, timeout, and workprocs </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtInputId XtAddInput(int <i>source</i>, XtPointer <i>condition</i>, XtInputCallbackProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>XtIntervalId XtAddTimeOut(unsigned long <i>interval</i>, XtTimerCallbackProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>XtWorkProcId XtAddWorkProc(XtWorkProc <i>proc</i>, XtPointer <i>client_data</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when input is available</p>
<dt><i>condition</i></p>
<dd>Specifies the mask that indicates a read, write, or exception condition or some operating system dependent condition.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called when input is available.</p>
<dt><i>source</i></p>
<dd>Specifies the source file descriptor on a UNIX-based system or other operating system dependent device specification.</dl>
<h2>Description</h2>
<p><code>XtAddInput</code> has been replaced by <code>XtAppAddInput.</code> </p>
<p> <code>XtAddTimeOut</code> has been replaced by <code>XtAppAddTimeOut.</code> </p>
<p> <code>XtAddWorkProc</code> has been replaced by <code>XtAppAddWorkProc</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddinput/">XtAppAddInput</a>(3), <a href="/docs/linux/man/3-xtappaddtimeout/">XtAppAddTimeOut</a>(3), <a href="/docs/linux/man/3-xtappaddworkproc/">XtAppAddWorkProc</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
