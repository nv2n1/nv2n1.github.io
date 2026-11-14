---
title: "xmcontainerrelayout(3)"
name: "xmcontainerrelayout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainerrelayout/"
description: "XmContainerRelayout — Container widget relayout function"
---

<p><code>XmContainerRelayout</code> &#8212; Container widget relayout function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>void XmContainerRelayout</code>(
<code>Widget container</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerRelayout</code> forces a layout of all items in the Container using the <code>XmNpositionIndex</code> and <code>XmNentryParent</code> constraint resources associated with each item.</p>
<dl COMPACT>
<dt><i>container</i></p>
<dd>Specifies the Container widget ID.</dl>
<p> For a complete definition of Container and its associated resources, see <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
