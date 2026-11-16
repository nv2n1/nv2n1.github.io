---
title: "xmconvertstringtounits(3)"
name: "xmconvertstringtounits"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmconvertstringtounits/"
description: "XmConvertStringToUnits — A function that converts a string specification to a unit value"
---

<p><code>XmConvertStringToUnits</code> &#8212; A function that converts a string specification to a unit value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>int XmConvertStringToUnits</code>(
<code>Screen *screen</code>,
<code>String spec</code>,
<code>int orientation</code>,
<code>int to_type</code>,
<code>XtEnum *parse_error</code>);</pre>
<h2>Description</h2>
<p><code>XmConvertStringToUnits</code> converts a string specification value and returns the converted value as the return value from the function. This function uses the specified screen&#8217;s resolution to compute the number of units for the string specification.</p>
<dl COMPACT>
<dt><i>screen</i></dt>
<dd>Specifies the screen whose resolution is to be used for the computation.</dd>
<dt><i>spec</i></dt>
<dd>Specifies the string, in <i>&lt;floating value&gt;&lt;unit&gt;</i> format, to be converted.</dd>
<dt><i>orientation</i></dt>
<dd>Specifies whether the converter uses the horizontal or vertical screen resolution when performing the conversion. The <i>orientation</i> parameter can have values of <code>XmHORIZONTAL</code> or <code>XmVERTICAL</code>.</dd>
<dt><i>to_type</i></dt>
<dd>Converts the value to the unit type specified. Refer to the <code>XmNunitType</code> resource of the <code>XmGadget</code>, <code>XmManager</code>, or <code>XmPrimitive</code> reference page. This parameter can have one of the following values:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmPIXELS</code></dt>
<dd>The returned value will be the number of pixels.</dd>
<dt><code>XmMILLIMETERS</code></dt>
<dd>The returned value will be the number of millimeters.</dd>
<dt><code>Xm100TH_MILLIMETERS</code></dt>
<dd>The returned values will be the number of 1/100 millimeters.</dd>
<dt><code>XmCENTIMETERS</code></dt>
<dd>The returned values will be the number of centimeters.</dd>
<dt><code>XmINCHES</code></dt>
<dd>The returned values will be the number of inches.</dd>
<dt><code>Xm1000TH_INCHES</code></dt>
<dd>The returned values will be the number of 1/100 inches.</dd>
<dt><code>XmPOINTS</code></dt>
<dd>The returned values will be the number of points. A point is a text processing unit defined as 1/72 of an inch.</dd>
<dt><code>Xm100TH_POINTS</code></dt>
<dd>The returned values will be the number of 1/100 points.</dd>
<dt><code>XmFONT_UNITS</code></dt>
<dd>All values provided to the widget are treated as font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dd>
<dt><code>Xm100TH_FONT_UNITS</code></dt>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dd></dl>
</dl>
<dt><i>parse_error</i></dt>
<dd>Specifies if a parsing error occurred. This is set to a value of True indicates that an error occurred, a value of False to indicate no error.</dd></dl>
<h2>Return</h2>
<p>Returns the converted value. If a NULL screen, incorrect <i>orientation</i>, or incorrect <i>unit_type</i> is supplied as parameter data, or if a parsing error occurred, 0 (zero) is returned.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmconvertunits/">XmConvertUnits</a></code>(3), <code><a href="/docs/linux/man/3-xmsetfontunits/">XmSetFontUnits</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
