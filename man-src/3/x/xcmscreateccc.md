---
title: "xcmscreateccc(3)"
name: "xcmscreateccc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmscreateccc/"
description: "XcmsCreateCCC, XcmsFreeCCC – creating and destroying CCCs"
---

<p>XcmsCreateCCC, XcmsFreeCCC &#8211; creating and destroying CCCs </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XcmsCCC XcmsCreateCCC(Display *<i>display</i>, int <i>screen_number</i>, Visual *<i>visual</i>, XcmsColor *<i>client_white_point</i>, XcmsCompressionProc <i>compression_proc</i>, XPointer <i>compression_client_data</i>, XcmsWhiteAdjustProc <i>white_adjust_proc</i>, XPointer <i>white_adjust_client_data</i>);</dl>
<p> void XcmsFreeCCC(XcmsCCC <i>ccc</i>);</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>ccc</i></p>
<dd>Specifies the CCC.</p>
<dt><i>client_white_point</i></p>
<dd>Specifies the Client White Point. If NULL is specified, the Client White Point is to be assumed to be the same as the Screen White Point. Note that the pixel member is ignored.</p>
<dt><i>compression_client_data</i></p>
<dd>Specifies client data for use by the gamut compression procedure or NULL.</p>
<dt><i>compression_proc</i></p>
<dd>Specifies the gamut compression procedure that is to be applied when a color lies outside the screen&#8217;s color gamut. If NULL is specified and a function using this CCC must convert a color specification to a device-dependent format and encounters a color that lies outside the screen&#8217;s color gamut, that function will return <code>XcmsFailure</code>.</p>
<dt><i>screen_number</i></p>
<dd>Specifies the appropriate screen number on the host server.</p>
<dt><i>visual</i></p>
<dd>Specifies the visual type.</p>
<dt><i>white_adjust_client_data</i></p>
<dd>Specifies client data for use with the white point adjustment procedure or NULL.</p>
<dt><i>white_adjust_proc</i></p>
<dd>Specifies the white adjustment procedure that is to be applied when the Client White Point differs from the Screen White Point. NULL indicates that no white point adjustment is desired.</dl>
<h2>Description</h2>
<p>The <code>XcmsCreateCCC</code> function creates a CCC for the specified display, screen, and visual. </p>
<p> The <code>XcmsFreeCCC</code> function frees the memory used for the specified CCC. Note that default CCCs and those currently associated with colormaps are ignored.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-displayofccc/">DisplayOfCCC</a>(3), <a href="/docs/linux/man/3-xcmscccofcolormap/">XcmsCCCOfColormap</a>(3), <a href="/docs/linux/man/3-xcmsconvertcolors/">XcmsConvertColors</a>(3), <a href="/docs/linux/man/3-xcmsdefaultccc/">XcmsDefaultCCC</a>(3), <a href="/docs/linux/man/3-xcmssetwhitepoint/">XcmsSetWhitePoint</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
