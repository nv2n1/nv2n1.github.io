---
title: "xmpanedgetpanes(3)"
name: "xmpanedgetpanes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmpanedgetpanes/"
description: "XmPanedGetPanes — A Paned function that returns the number of panes in the paned widget"
---

<p><code>XmPanedGetPanes</code> &#8212; A Paned function that returns the number of panes in the paned widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Paned.h&gt;
<code>int XmPanedGetPanes</code>(
<code>Widget widget</code>,
<code>WidgetList *panes</code>,
<code>int *num</code>);</pre>
<h2>Description</h2>
<p><code>XmPanedGetPanes</code> Returns the number of panes in the paned widget.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Paned widget ID</dd></dl>
<h2>Return</h2>
<dl COMPACT>
<dt><i>panes</i></dt>
<dd>Specifies the list of all panes contained in this widget</dd>
<dt><i>num</i></dt>
<dd>Specifies the number of panes in the paned widget</dd></dl>
<p> Returns the number of panes in the paned widget.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmpaned/">XmPaned</a></code>(3).</p>
