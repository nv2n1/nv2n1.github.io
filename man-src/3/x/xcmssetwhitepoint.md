---
title: "xcmssetwhitepoint(3)"
name: "xcmssetwhitepoint"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmssetwhitepoint/"
description: "XcmsSetWhitePoint, XcmsSetWhiteAdjustProc – modifying CCC attributes"
---

<p>XcmsSetWhitePoint, XcmsSetWhiteAdjustProc &#8211; modifying CCC attributes </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsSetWhitePoint(XcmsCCC <i>ccc</i>, XcmsColor *<i>color</i>);</p>
<dd>XcmsWhiteAdjustProc XcmsSetWhiteAdjustProc(XcmsCCC <i>ccc</i>, XcmsWhiteAdjustProc <i>white_adjust_proc</i>, XPointer <i>client_data</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC.</p>
<dt><i>client_data</i></p>
<dd>Specifies client data for the white point adjustment procedure or NULL.</p>
<dt><i>color</i></p>
<dd>Specifies the new Client White Point.</p>
<dt><i>white_adjust_proc</i></p>
<dd>Specifies the white point adjustment procedure.</dl>
<h2>Description</h2>
<p>The <code>XcmsSetWhitePoint</code> function changes the Client White Point in the specified CCC. Note that the pixel member is ignored and that the color specification is left unchanged upon return. The format for the new white point must be <code>XcmsCIEXYZFormat</code>, <code>XcmsCIEuvYFormat</code>, <code>XcmsCIExyYFormat</code>, or <code>XcmsUndefinedFormat</code>. If the color argument is NULL, this function sets the format component of the Client White Point specification to <code>XcmsUndefinedFormat</code>, indicating that the Client White Point is assumed to be the same as the Screen White Point. </p>
<p> This function returns nonzero status if the format for the new white point is valid; otherwise, it returns zero. </p>
<p> The <code>XcmsSetWhiteAdjustProc</code> function first sets the white point adjustment procedure and client data in the specified CCC with the newly specified procedure and client data and then returns the old procedure.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-displayofccc/">DisplayOfCCC</a>(3), <a href="/docs/linux/man/3-xcmscccofcolormap/">XcmsCCCOfColormap</a>(3), <a href="/docs/linux/man/3-xcmsconvertcolors/">XcmsConvertColors</a>(3), <a href="/docs/linux/man/3-xcmscreateccc/">XcmsCreateCCC</a>(3), <a href="/docs/linux/man/3-xcmsdefaultccc/">XcmsDefaultCCC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
