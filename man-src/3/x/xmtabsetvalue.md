---
title: "xmtabsetvalue(3)"
name: "xmtabsetvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabsetvalue/"
description: "XmTabSetValue — A convenience function that sets a tab stop"
---

<p><code>XmTabSetValue</code> &#8212; A convenience function that sets a tab stop</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmTabSetValue</code>(
<code>XmTab tab</code>,
<code>float value</code>);</pre>
<h2>Description</h2>
<p><code>XmTabSetValue</code> sets the <i>value</i> field of the <code>XmTab</code> structure associated with <i>tab</i>.</p>
<dl COMPACT>
<dt><i>tab</i></p>
<dd>Specifies the tab to set the value of.</p>
<dt><i>value</i></p>
<dd>Specifies the floating point number which represents the distance that the rendering of the <code>XmString</code> segment associated with <i>tab</i> will be offset. The offset is from either the beginning of the rendering or from the previous tab stop, depending on the setting for the <i>offset</i> model. The distance depends on the tab&#8217;s unit type. Note that negative values are not permitted, and that if a tab stop would cause text to overlap, the x position for the segment is set immediately after the end of the previous segment.</dl>
<h2>Related</h2>
<p>See also the <i>Motif Programmer&#8217;s Guide</i> for more information about tabs and tab lists. <code><a href="/docs/linux/man/3-xmtab/">XmTab</a></code>(3).</p>
