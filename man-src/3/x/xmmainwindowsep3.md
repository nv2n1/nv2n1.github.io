---
title: "xmmainwindowsep3(3)"
name: "xmmainwindowsep3"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmainwindowsep3/"
description: "XmMainWindowSep3 — A MainWindow function that returns the widget ID of the third Separator widget"
---

<p><code>XmMainWindowSep3</code> &#8212; A MainWindow function that returns the widget ID of the third Separator widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MainW.h&gt;
<code>Widget XmMainWindowSep3</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmMainWindowSep3</code> returns the widget ID of the third Separator in the MainWindow. The third Separator is located between the message window and the widget above it. This Separator is visible only when <code>XmNshowSeparator</code> is True. </p>
<p> <code>NOTE:</code> <code>XmMainWindowSep3</code> is obsolete and exists for compatibility with previous releases. Use <code>XtNameToWidget</code> instead. Pass a MainWindow variable as the first argument to <code>XtNameToWidget</code> and pass <code>Separator3</code> as the second argument.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the MainWindow widget ID</dl>
<p> For a complete definition of MainWindow and its associated resources, see <code><a href="/docs/linux/man/3-xmmainwindow/">XmMainWindow</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the third Separator.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmainwindow/">XmMainWindow</a></code>(3).</p>
