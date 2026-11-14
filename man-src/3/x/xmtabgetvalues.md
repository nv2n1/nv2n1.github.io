---
title: "xmtabgetvalues(3)"
name: "xmtabgetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabgetvalues/"
description: "XmTabGetValues — A convenience function that returns tab values"
---

<p><code>XmTabGetValues</code> &#8212; A convenience function that returns tab values</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>float XmTabGetValues</code>(
<code>XmTab tab</code>,
<code>unsigned char *units</code>,
<code>XmOffsetModel *offset</code>,
<code>unsigned char *alignment</code>,
<code>char **decimal</code>);</pre>
<h2>Description</h2>
<p><code>XmTabGetValues</code> takes an <code>XmTab</code> structure, returns the floating point number that is set as the value of the tab, and then sets values for the <i>units</i>, <i>offset</i>, <i>alignment</i>, and <i>decimal</i> arguments where they are not NULL. The returned floating point number represents the distance that the rendering of the <code>XmString</code> segment associated with <i>tab</i> will be offset. The offset is from either the beginning of the rendering or from the previous tab stop, depending on the setting for the <i>offset</i> model. The distance will use the unit type pointed at by <i>unit</i>.</p>
<dl COMPACT>
<dt><i>tab</i></p>
<dd>Specifies the tab to get the value from.</p>
<dt><i>units</i></p>
<dd>Specifies a pointer to the unit type.</p>
<dt><i>offset</i></p>
<dd>Specifies a pointer to the offset model.</p>
<dt><i>alignment</i></p>
<dd>Specifies a pointer to the alignment type.</p>
<dt><i>decimal</i></p>
<dd>Specifies a pointer to the multibyte character used as the decimal point.</dl>
<h2>Return</h2>
<p>Returns a floating point number that is set as the value of the tab.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtab/">XmTab</a></code>(3).</p>
