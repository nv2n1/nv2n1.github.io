---
title: "xmsetfontunits(3)"
name: "xmsetfontunits"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsetfontunits/"
description: "XmSetFontUnits — A function that sets the font unit value for a display"
---

<p><code>XmSetFontUnits</code> &#8212; A function that sets the font unit value for a display</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmSetFontUnits</code>(
<code>Display * display</code>,
<code>int h_value</code>,
<code>int v_value</code>);</pre>
<h2>Description</h2>
<p><code>XmSetFontUnits</code> provides an external function to initialize font unit values. Applications may want to specify resolution-independent data based on a global font size. This function must be called before any widgets with resolution-independent data are created. See the <code>XmNunitType</code> resource description in the reference pages for <code>XmGadget</code>, <code>XmManager</code>, and <code>XmPrimitive</code> for more information on resolution independence. </p>
<p> This function sets the font units for all screens on the display. </p>
<p> <code>NOTE:</code> <code>XmSetFontUnits</code> is obsolete and exists for compatibility with previous releases. Instead of using this function, provide initial values or call <code>XtSetValues</code> for the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Defines the display for which this font unit value is to be applied.</p>
<dt><i>h_value</i></p>
<dd>Specifies the value to be used for horizontal units in the conversion calculations.</p>
<dt><i>h_value</i></p>
<dd>Specifies the value to be used for vertical units in the conversion calculations.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmconvertunits/">XmConvertUnits</a></code>(3), <code><a href="/docs/linux/man/3-xmsetfontunit/">XmSetFontUnit</a></code>(3), <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
