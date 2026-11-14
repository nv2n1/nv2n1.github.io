---
title: "xmtabcreate(3)"
name: "xmtabcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabcreate/"
description: "XmTabCreate — A convenience function that creates a tab stop"
---

<p><code>XmTabCreate</code> &#8212; A convenience function that creates a tab stop</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTab XmTabCreate</code>(
<code>float value</code>,
<code>unsigned char units</code>,
<code>XmOffsetModel offset_model</code>,
<code>unsigned char alignment</code>,
<code>char *decimal</code>);</pre>
<h2>Description</h2>
<p><code>XmTabCreate</code> creates a tab stop at a position defined by the <i>value</i> and <i>units</i> arguments.</p>
<dl COMPACT>
<dt><i>value</i></p>
<dd>Specifies the floating point value to be used in conjunction with <i>units</i> to calculate the location of the tab stop. Note that negative values are not permitted.</p>
<dt><i>units</i></p>
<dd>Specifies the unit type (for example, <code>XmMILLIMETERS</code>) to be used in conjunction with <i>value</i> to calculate the location of the tab stop. You can specify any unit described by the <code>XmConvertUnits</code> reference page. For resources of type, dimension, or position, you can specify units as described in the <code>XmNunitType</code> resource of the <code>XmGadget</code>, <code>XmManager</code>, or <code>XmPrimitive</code> reference page.</p>
<dt><i>offset_model</i></p>
<dd>Specifies whether the tab value represents an absolute position or a relative offset from the previous tab. Valid values are <code>XmABSOLUTE</code> and <code>XmRELATIVE</code>.</p>
<dt><i>alignment</i></p>
<dd>Specifies how the text should be aligned relative to this tab stop. Valid values are <code>XmALIGNMENT_BEGINNING</code>.</p>
<dt><i>decimal</i></p>
<dd>Specifies the multibyte character in the current language environment to be used as the decimal point for a decimal aligned tab stop. This is currently unused.</dl>
<h2>Return</h2>
<p>Returns a newly allocated <code>XmTab</code>. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XmTabFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtab/">XmTab</a></code>(3) and <code><a href="/docs/linux/man/3-xmtabfree/">XmTabFree</a></code>(3).</p>
