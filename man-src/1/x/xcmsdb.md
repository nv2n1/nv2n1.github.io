---
title: "xcmsdb(1)"
name: "xcmsdb"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcmsdb/"
description: "xcmsdb – Device Color Characterization utility for X Color Management System"
---

<h2 class="name">NAME</h2>
<p> xcmsdb &#8211; Device Color Characterization utility for X Color Management System </p>
<h2>SYNOPSIS</h2>
<p> <code>xcmsdb</code> [ <code>-query</code> ] [ <code>-remove</code> ] [ <code>-format 32</code>|<code>16</code>|<code>8</code> ] [ <code>-help</code> ] [ <code>-version</code> ] [ <i>filename</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>xcmsdb</i> is used to load, query, or remove Device Color Characterization data stored in properties on the root window of the screen as specified in section 7, Device Color Characterization, of the ICCCM. Device Color Characterization data (also called the Device Profile) is an integral part of Xlib&#8217;s X Color Management System (Xcms), necessary for proper conversion of color specification between device-independent and device-dependent forms. Xcms uses 3&#215;3 matrices stored in the XDCCC_LINEAR_RGB_MATRICES property to convert color specifications between CIEXYZ and RGB Intensity (XcmsRGBi, also referred to as linear RGB). Xcms then uses display gamma information stored in the XDCCC_LINEAR_RGB_CORRECTION property to convert color specifications between RGBi and RGB device (XcmsRGB, also referred to as device RGB). </p>
<p> Note that Xcms allows clients to register <i>function sets</i> in addition to its built-in function set for CRT color monitors. Additional function sets may store their device profile information in other properties in function set specific format. This utility is unaware of these non-standard properties. </p>
<p> The ASCII readable contents of <i>filename</i> (or the standard input if no input file is given) are appropriately transformed for storage in properties, provided the <code>-query</code> or <code>-remove</code> options are not specified.</p>
<h2>OPTIONS</h2>
<p> <i>xcmsdb</i> program accepts the following options:</p>
<dl>
<dt><code>-query</code></p>
<dd> This option attempts to read the XDCCC properties off the screen&#8217;s root window. If successful, it transforms the data into a more readable format, then sends the data to standard out.</p>
<dt><code>-remove</code></p>
<dd> This option attempts to remove the XDCCC properties on the screen&#8217;s root window.</p>
<dt><code>-format 32</code>|<code>16</code>|<code>8</code></p>
<dd> Specifies the property format (32, 16, or 8 bits per entry) for the XDCCC_LINEAR_RGB_CORRECTION property. Precision of encoded floating point values increases with the increase in bits per entry. The default is 32 bits per entry.</p>
<dt><code>-help</code></p>
<dd> This option prints a summary of the available options and exits.</p>
<dt><code>-version</code></p>
<dd> This option prints the program version and exits.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xprop/">xprop</a>(1), Xlib documentation</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to figure out which display and screen to use.</dl>
<h2>AUTHOR</h2>
<p> Chuck Adams, Tektronix Inc. Al Tabayoyon, SynChromatics Inc. (added multi-visual support) </p>
<h2>Index</h2>
