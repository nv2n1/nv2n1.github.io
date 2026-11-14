---
title: "xmdropsiteunregister(3)"
name: "xmdropsiteunregister"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteunregister/"
description: "XmDropSiteUnregister — A Drag and Drop function that frees drop site information"
---

<p><code>XmDropSiteUnregister</code> &#8212; A Drag and Drop function that frees drop site information</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteUnregister</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteUnregister</code> informs the toolkit that the specified widget is no longer a registered drop site. The function frees all associated drop site information.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget, registered as a drop site, that is to be unregistered</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3) and <code><a href="/docs/linux/man/3-xmdropsiteregister/">XmDropSiteRegister</a></code>(3).</p>
