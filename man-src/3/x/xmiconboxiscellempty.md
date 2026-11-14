---
title: "xmiconboxiscellempty(3)"
name: "xmiconboxiscellempty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmiconboxiscellempty/"
description: "XmIconBoxIsCellEmpty — A function that determines whether a cell in the IconBox is empty"
---

<p><code>XmIconBoxIsCellEmpty</code> &#8212; A function that determines whether a cell in the IconBox is empty</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/IconBox.h&gt;
<code>Boolean XmIconBoxIsCellEmpty</code>(
<code>Position cell_x</code>,
<code>Position cell_y</code>,
<code>Widget ignore</code>);</pre>
<h2>Description</h2>
<p><code>XmIconBoxIsCellEmpty</code> returns <code>True</code> if specified cell contains no child and <code>False</code> otherwise.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the IconBox widget ID</p>
<dt><i>cell_x</i></p>
<dd>Specifies the X location of the cell to check</p>
<dt><i>cell_y</i></p>
<dd>Specifies the Y location of the cell to check</p>
<dt><i>ignore</i></p>
<dd>If the widget ID specified by <code>ignore</code> is present in the specified cell, it will be ignored and the function will return <code>True</code></dl>
<h2>Return</h2>
<p>Returns <code>True</code> if the specified cell contains no child, and <code>False</code> otherwide.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmiconbox/">XmIconBox</a></code>(3).</p>
