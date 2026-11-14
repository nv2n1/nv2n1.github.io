---
title: "xmdropsiteregistered(3)"
name: "xmdropsiteregistered"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteregistered/"
description: "XmDropSiteRegistered — A Drag and Drop function that determines if a drop site has been registered"
---

<p><code>XmDropSiteRegistered</code> &#8212; A Drag and Drop function that determines if a drop site has been registered</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>Boolean XmDropSiteRegistered</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteRegistered</code> determines if the specified widget has a drop site registered. If a drop site is registered, this function returns True.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget being queried.</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Return</h2>
<p>If the widget is not a registered drop site, this function returns False. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteendupdate/">XmDropSiteEndUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsitestartupdate/">XmDropSiteStartUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteupdate/">XmDropSiteUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteunregister/">XmDropSiteUnregister</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
