---
title: "xtremoveinput(3)"
name: "xtremoveinput"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtremoveinput/"
description: "XtAppAddInput, XtRemoveInput – register and remove an input source"
---

<p>XtAppAddInput, XtRemoveInput &#8211; register and remove an input source </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtInputId XtAppAddInput(XtAppContext <i>app_context</i>, int <i>source</i>, XtPointer <i>condition</i>, XtInputCallbackProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveInput(XtInputId <i>id</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context that identifies the application.</p>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when input is available.</p>
<dt><i>condition</i></p>
<dd>Specifies the mask that indicates a read, write, or exception condition or some operating system dependent condition.</p>
<dt><i>id</i></p>
<dd>Specifies the ID returned from the corresponding <code>XtAppAddInput</code> call.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called when input is available.</p>
<dt><i>source</i></p>
<dd>Specifies the source file descriptor on a UNIX-based system or other operating system dependent device specification.</dl>
<h2>Description</h2>
<p>The <code>XtAppAddInput</code> function registers with the Intrinsics read routine a new source of events, which is usually file input but can also be file output. Note that file should be loosely interpreted to mean any sink or source of data. <code>XtAppAddInput</code> also specifies the conditions under which the source can generate events. When input is pending on this source, the callback procedure is called. </p>
<p> The legal values for the condition argument are operating-system dependent. On a UNIX-based system, the condition is some union of <code>XtInputReadMask</code>, <code>XtInputWriteMask</code>, and <code>XtInputExceptMask</code>. The <code>XtRemoveInput</code> function causes the Intrinsics read routine to stop watching for input from the input source.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddtimeout/">XtAppAddTimeOut</a>(3),<a href="/docs/linux/man/3-xtappaddsignal/">XtAppAddSignal</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i> </p>
<h2>Bugs</h2>
<p>In ANSI C it is necessary to cast the condition to an XtPointer, e.g.:</p>
<dl COMPACT>
<dd>XtAppAddInput(app_context,</p>
<dl COMPACT>
<dd>source,<br />
 <code>(XtPointer)</code> (XtInputReadMask | XtInputWriteMask),<br />
 proc,<br />
 client_data);</dl>
</dl>
