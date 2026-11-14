---
title: "xmobjectatpoint(3)"
name: "xmobjectatpoint"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmobjectatpoint/"
description: "XmObjectAtPoint — A toolkit function that determines which child intersects or comes closest to a specified point"
---

<p><code>XmObjectAtPoint</code> &#8212; A toolkit function that determines which child intersects or comes closest to a specified point</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Widget XmObjectAtPoint</code>(
<code>Widget widget</code>,
<code>Position x</code>,
<code>Position y</code>);</pre>
<h2>Description</h2>
<p><code>XmObjectAtPoint</code> searches the child list of the specified manager <i>widget</i> and returns the child most closely associated with the specified <i>x</i>,<i>y</i> coordinate pair. </p>
<p> For the typical Motif manager <i>widget</i>, <code>XmObjectAtPoint</code> uses the following rules to determine the returned object:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If one child intersects <i>x,y</i>, <code>XmObjectAtPoint</code> returns the widget ID of that child.</p>
<dt> &bull;</p>
<dd>If more than one child intersects <i>x,y</i>, <code>XmObjectAtPoint</code> returns the widget ID of the visible child.</p>
<dt> &bull;</p>
<dd>If no child intersects <i>x</i>,<i>y</i>, <code>XmObjectAtPoint</code> returns NULL.</dl>
<p> The preceding rules are only general. In fact, each manager <i>widget</i> is free to define &quot;most closely associated&quot; as it desires. For example, if no child intersects <i>x,y</i>, a manager might return the child closest to <i>x,y</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies a manager widget.</p>
<dt><i>x</i></p>
<dd>Specifies the x-coordinate about which you are seeking child information. The x-coordinate must be specified in pixels, relative to the left side of <i>manager</i>.</p>
<dt><i>y</i></p>
<dd>Specifies the y-coordinate about which you are seeking child information. The y-coordinate must be specified in pixels, relative to the top side of <i>manager</i>.</dl>
<h2>Return</h2>
<p>Returns the child of <i>manager</i> most closely associated with <i>x,y</i>. If none of its children are sufficiently associated with <i>x,y</i>, returns NULL.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3).</p>
