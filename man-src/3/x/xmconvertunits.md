---
title: "xmconvertunits(3)"
name: "xmconvertunits"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmconvertunits/"
description: "XmConvertUnits — A function that converts a value in one unit type to another unit type"
---

<p><code>XmConvertUnits</code> &#8212; A function that converts a value in one unit type to another unit type</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>int XmConvertUnits</code>(
<code>Widget widget</code>,
<code>int orientation</code>,
<code>int from_unit_type</code>,
<code>int from_value</code>,
<code>int to_unit_type</code>);</pre>
<h2>Description</h2>
<p><code>XmConvertUnits</code> converts the value and returns it as the return value from the function. For resources of type, dimension, or position, you can specify units using the syntax described in the <code>XmNunitType</code> resource of the <code>XmPrimitive</code> reference page.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget for which the data is to be converted.</p>
<dt><i>orientation</i></p>
<dd>Specifies whether the converter uses the horizontal or vertical screen resolution when performing the conversions. The <i>orientation</i> parameter can have values of <code>XmHORIZONTAL</code> or <code>XmVERTICAL</code>.</p>
<dt><i>from_unit_type</i></p>
<dd>Specifies the current unit type of the supplied value</p>
<dt><i>from_value</i></p>
<dd>Specifies the value to be converted</p>
<dt><i>to_unit_type</i></p>
<dd>Converts the value to the unit type specified</dl>
<p> The parameters <i>from_unit_type</i> and <i>to_unit_type</i> can have the following values:</p>
<dl COMPACT>
<dt><code>XmPIXELS</code></p>
<dd>All values provided to the widget are treated as pixel values. This is the default for the resource.</p>
<dt><code>XmMILLIMETERS</code></p>
<dd>All values provided to the widget are treated as millimeter values.</p>
<dt><code>Xm100TH_MILLIMETERS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a millimeter.</p>
<dt><code>XmCENTIMETERS</code></p>
<dd>All values provided to the widget are treated as centimeter values.</p>
<dt><code>XmINCHES</code></p>
<dd>All values provided to the widget are treated as inch values.</p>
<dt><code>Xm1000TH_INCHES</code></p>
<dd>All values provided to the widget are treated as 1/1000 of an inch.</p>
<dt><code>XmPOINTS</code></p>
<dd>All values provided to the widget are treated as point values. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>Xm100TH_POINTS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a point. A point is a unit typically used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>XmFONT_UNITS</code></p>
<dd>All values provided to the widget are treated as normal font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</p>
<dt><code>Xm100TH_FONT_UNITS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dl>
<h2>Return</h2>
<p>Returns the converted value. If a NULL widget, incorrect <i>orientation</i>, or incorrect <i>unit_type</i> is supplied as parameter data, 0 (zero) is returned.</p>
<h2>Related</h2>
<p><code>XmPrimitive</code>, <code><a href="/docs/linux/man/3-xmsetfontunits/">XmSetFontUnits</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
