---
title: "xmcascadebuttongadgethighlight(3)"
name: "xmcascadebuttongadgethighlight"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcascadebuttongadgethighlight/"
description: "XmCascadeButtonGadgetHighlight — A CascadeButtonGadget function that sets the highlight state"
---

<p><code>XmCascadeButtonGadgetHighlight</code> &#8212; A CascadeButtonGadget function that sets the highlight state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CascadeBG.h&gt;
<code>void XmCascadeButtonGadgetHighlight</code>(
<code>Widget cascadeButtonGadget</code>,
<code>Boolean highlight</code>);</pre>
<h2>Description</h2>
<p><code>XmCascadeButtonGadgetHighlight</code> either draws or erases the shadow highlight around the CascadeButtonGadget.</p>
<dl COMPACT>
<dt><i>cascadeButtonGadget</i></p>
<dd>Specifies the CascadeButtonGadget to be highlighted or unhighlighted</p>
<dt><i>highlight</i></p>
<dd>Specifies whether to highlight (True) or to unhighlight (False)</dl>
<p> For a complete definition of CascadeButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmcascadebuttonhighlight/">XmCascadeButtonHighlight</a></code>(3).</p>
