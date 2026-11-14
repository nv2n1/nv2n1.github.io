---
title: "xmcascadebuttonhighlight(3)"
name: "xmcascadebuttonhighlight"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcascadebuttonhighlight/"
description: "XmCascadeButtonHighlight — A CascadeButton and CascadeButtonGadget function that sets the highlight state"
---

<p><code>XmCascadeButtonHighlight</code> &#8212; A CascadeButton and CascadeButtonGadget function that sets the highlight state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CascadeB.h&gt;
#include &lt;Xm/CascadeBG.h&gt;
<code>void XmCascadeButtonHighlight</code>(
<code>Widget cascadeButton</code>,
<code>Boolean highlight</code>);</pre>
<h2>Description</h2>
<p><code>XmCascadeButtonHighlight</code> either draws or erases the shadow highlight around the CascadeButton or the CascadeButtonGadget.</p>
<dl COMPACT>
<dt><i>cascadeButton</i></p>
<dd>Specifies the CascadeButton or CascadeButtonGadget to be highlighted or unhighlighted</p>
<dt><i>highlight</i></p>
<dd>Specifies whether to highlight (True) or to unhighlight (False)</dl>
<p> For a complete definition of CascadeButton or CascadeButtonGadget and their associated resources, see <code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3) or <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3) and <code><a href="/docs/linux/man/3-xmcascadebuttongadgethighlight/">XmCascadeButtonGadgetHighlight</a></code>(3).</p>
