---
title: "xmdropsiteupdate(3)"
name: "xmdropsiteupdate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteupdate/"
description: "XmDropSiteUpdate — A Drag and Drop function that sets resource values for a drop site"
---

<p><code>XmDropSiteUpdate</code> &#8212; A Drag and Drop function that sets resource values for a drop site</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteUpdate</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteUpdate</code> modifies drop site resources associated with the specified widget. This routine updates the drop site resources specified in the <i>arglist</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered as a drop site</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteendupdate/">XmDropSiteEndUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteregister/">XmDropSiteRegister</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsitestartupdate/">XmDropSiteStartUpdate</a></code>(3), and <code><a href="/docs/linux/man/3-xmdropsiteunregister/">XmDropSiteUnregister</a></code>(3).</p>
