---
title: "xmscalesetticks(3)"
name: "xmscalesetticks"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscalesetticks/"
description: "XmScaleSetTicks — A Scale function that controls tick marks"
---

<p><code>XmScaleSetTicks</code> &#8212; A Scale function that controls tick marks</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Scale.h&gt;
<code>void XmScaleSetTicks</code>(
<code>Widget scale</code>,
<code>int big_every</code>,
<code>Cardinal num_medium</code>,
<code>Cardinal num_small</code>,
<code>Dimension size_big</code>,
<code>Dimension size_medium</code>,
<code>Dimension size_small</code>);</pre>
<h2>Description</h2>
<p><code>XmScaleSetTicks</code> controls the number, location, and size of the tick marks on a Scale. Each tick mark is a SeparatorGadget oriented perpendicular to the Scale&#8217;s orientation. For example, if the Scale is oriented horizontally, the tick marks will be oriented vertically. </p>
<p> If you specify tick marks for a Scale and then change the Scale&#8217;s orientation, you will have to do the following:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd>Remove all the tick marks. To remove tick marks from a Scale, you must destroy (with <code>XtDestroyChildren</code>) the SeparatorGadget tick marks. The first two children of a Scale are its title and scroll bar, and all additional children are tick marks.</dd>
<dt> &bull;</dt>
<dd>Recreate the tick marks by calling <code>XmScaleSetTicks</code>.</dd>
<dt><i>scale</i></dt>
<dd>Specifies the Scale widget ID that is getting the tick marks.</dd>
<dt><i>big_every</i></dt>
<dd>Specifies the number of scale values between big ticks.</dd>
<dt><i>num_medium</i></dt>
<dd>Specifies the number of medium ticks between big values.</dd>
<dt><i>num_small</i></dt>
<dd>Specifies the number of small ticks between medium values.</dd>
<dt><i>size_big</i></dt>
<dd>Specifies the size (either width or height) of the big ticks.</dd>
<dt><i>size_medium</i></dt>
<dd>Specifies the size (either width or height) of the medium ticks.</dd>
<dt><i>size_small</i></dt>
<dd>Specifies the size (either width or height) of the small ticks.</dd></dl>
<p> For a complete definition of Scale and its associated resources, see <code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
