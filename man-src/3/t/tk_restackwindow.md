---
title: "tk_restackwindow(3)"
name: "tk_restackwindow"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_restackwindow/"
description: "Tk_RestackWindow – Change a window’s position in the stacking order"
---

<p>Tk_RestackWindow &#8211; Change a window&#8217;s position in the stacking order </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_RestackWindow</code>(<i>tkwin, aboveBelow, other</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window to restack.</p>
<dd>int <i>aboveBelow</i> (in) Indicates new position of <i>tkwin</i> relative to <i>other</i>; must be <code>Above</code> or <code>Below</code>.</p>
<dd>Tk_Window <i>other</i> (in) <i>Tkwin</i> will be repositioned just above or below this window. Must be a sibling of <i>tkwin</i> or a descendant of a sibling. If NULL then <i>tkwin</i> is restacked above or below all siblings. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_RestackWindow</code> changes the stacking order of <i>window</i> relative to its siblings. If <i>other</i> is specified as NULL then <i>window</i> is repositioned at the top or bottom of its stacking order, depending on whether <i>aboveBelow</i> is <code>Above</code> or <code>Below</code>. If <i>other</i> has a non-NULL value then <i>window</i> is repositioned just above or below <i>other</i>. </p>
<p> The <i>aboveBelow</i> argument must have one of the symbolic values <code>Above</code> or <code>Below</code>. Both of these values are defined by the include file &lt;X11/Xlib.h&gt;. </p>
<h2>Keywords</h2>
<p>above, below, obscure, stacking order</p>
