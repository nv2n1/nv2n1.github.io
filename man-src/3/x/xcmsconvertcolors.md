---
title: "xcmsconvertcolors(3)"
name: "xcmsconvertcolors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsconvertcolors/"
description: "XcmsConvertColors – convert CCC color specifications"
---

<p>XcmsConvertColors &#8211; convert CCC color specifications </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsConvertColors(XcmsCCC <i>ccc</i>, XcmsColor <i>colors_in_out</i>[], unsigned int <i>ncolors</i>, XcmsColorFormat <i>target_format</i>, Bool <i>compression_flags_return</i>[]);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC. If Conversion is between device-independent color spaces only (for example, TekHVC to CIELuv), the CCC is necessary only to specify the Client White Point.</p>
<dt><i>colors_in_out</i></p>
<dd>Specifies an array of color specifications. Pixel members are ignored and remain unchanged upon return.</p>
<dt><i>compression_flags_return</i></p>
<dd>Returns an array of Boolean values indicating compression status. If a non-NULL pointer is supplied, each element of the array is set to <code>True</code> if the corresponding color was compressed and <code>False</code> otherwise. Pass NULL if the compression status is not useful.</p>
<dt><i>ncolors</i></p>
<dd>Specifies the number of <code>XcmsColor</code> structures in the color-specification array.</p>
<dt><i>target_format</i></p>
<dd>Specifies the target color specification format.</dl>
<h2>Description</h2>
<p>The <code>XcmsConvertColors</code> function converts the color specifications in the specified array of <code>XcmsColor</code> structures from their current format to a single target format, using the specified CCC. When the return value is <code>XcmsFailure</code>, the contents of the color specification array are left unchanged. </p>
<p> The array may contain a mixture of color specification formats (for example, 3 CIE XYZ, 2 CIE Luv, and so on). When the array contains both device-independent and device-dependent color specifications and the target_format argument specifies a device-dependent format (for example, <code>XcmsRGBiFormat</code>, <code>XcmsRGBFormat</code>), all specifications are converted to CIE XYZ format and then to the target device-dependent format.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-displayofccc/">DisplayOfCCC</a>(3), <a href="/docs/linux/man/3-xcmscccofcolormap/">XcmsCCCOfColormap</a>(3), <a href="/docs/linux/man/3-xcmscreateccc/">XcmsCreateCCC</a>(3), <a href="/docs/linux/man/3-xcmsdefaultccc/">XcmsDefaultCCC</a>(3), <a href="/docs/linux/man/3-xcmssetwhitepoint/">XcmsSetWhitePoint</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
