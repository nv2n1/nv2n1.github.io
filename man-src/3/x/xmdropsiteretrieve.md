---
title: "xmdropsiteretrieve(3)"
name: "xmdropsiteretrieve"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteretrieve/"
description: "XmDropSiteRetrieve — A Drag and Drop function that retrieves resource values set on a drop site"
---

<p><code>XmDropSiteRetrieve</code> &#8212; A Drag and Drop function that retrieves resource values set on a drop site</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteRetrieve</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteRetrieve</code> extracts values for the given resources from the drop site specified by <i>widget</i>. An initiator can also obtain information about the current drop site by passing the associated DragContext widget as the <i>widget</i> parameter to this routine. The initiator can retrieve all of the drop site resources except <code>XmNdragProc</code> and <code>XmNdropProc</code> using this method.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget that encloses the drop site.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3) and <code><a href="/docs/linux/man/3-xmdropsiteupdate/">XmDropSiteUpdate</a></code>(3).</p>
