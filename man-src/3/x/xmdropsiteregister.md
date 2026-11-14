---
title: "xmdropsiteregister(3)"
name: "xmdropsiteregister"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteregister/"
description: "XmDropSiteRegister — A Drag and Drop function that identifies a drop site and assigns resources that specify its behavior"
---

<p><code>XmDropSiteRegister</code> &#8212; A Drag and Drop function that identifies a drop site and assigns resources that specify its behavior</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteRegister</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteRegister</code> identifies the specified widget or gadget as a drop site and sets resource values that define the drop site&#8217;s behavior. The routine assigns default values to any resources that are not specified in the argument list. The toolkit generates a warning message if a drop site is registered with <code>XmNdropSiteActivity</code> set to <code>XmDROP_SITE_ACTIVE</code> and the <code>XmNdropProc</code> resource is NULL. </p>
<p> If the drop site is a descendant of a widget that is registered as a drop site, the <code>XmNdropSiteType</code> resource of the ancestor drop site must be specified as <code>XmDROP_SITE_COMPOSITE</code>. The ancestor must be registered before the descendant. The drop site is stacked above all other sibling drop sites already registered.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget to be registered.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteendupdate/">XmDropSiteEndUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsitestartupdate/">XmDropSiteStartUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteupdate/">XmDropSiteUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteunregister/">XmDropSiteUnregister</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
