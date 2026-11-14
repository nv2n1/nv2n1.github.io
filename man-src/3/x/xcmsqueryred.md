---
title: "xcmsqueryred(3)"
name: "xcmsqueryred"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsqueryred/"
description: "XcmsQueryBlack, XcmsQueryBlue, XcmsQueryGreen, XcmsQueryRed, XcmsQueryWhite – obtain black, blue, green, red, and white CCC color specifications"
---

<p>XcmsQueryBlack, XcmsQueryBlue, XcmsQueryGreen, XcmsQueryRed, XcmsQueryWhite &#8211; obtain black, blue, green, red, and white CCC color specifications </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsQueryBlack(XcmsCCC <i>ccc</i>, XcmsColorFormat <i>target_format</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsQueryBlue(XcmsCCC <i>ccc</i>, XcmsColorFormat <i>target_format</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsQueryGreen(XcmsCCC <i>ccc</i>, XcmsColorFormat <i>target_format</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsQueryRed(XcmsCCC <i>ccc</i>, XcmsColorFormat <i>target_format</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsQueryWhite(XcmsCCC <i>ccc</i>, XcmsColorFormat <i>target_format</i>, XcmsColor *<i>color_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC. Note that the CCC&#8217;s Client White Point and White Point Adjustment procedures are ignored.</p>
<dt><i>color_return</i></p>
<dd>Returns the color specification in the specified target format. The white point associated with the returned color specification is the Screen White Point. The value returned in the pixel member is undefined.</p>
<dt><i>target_format</i></p>
<dd>Specifies the target color specification format.</dl>
<h2>Description</h2>
<p>The <code>XcmsQueryBlack</code> function returns the color specification in the specified target format for zero-intensity red, green, and blue. </p>
<p> The <code>XcmsQueryBlue</code> function returns the color specification in the specified target format for full-intensity blue while red and green are zero. </p>
<p> The <code>XcmsQueryGreen</code> function returns the color specification in the specified target format for full-intensity green while red and blue are zero. </p>
<p> The <code>XcmsQueryRed</code> function returns the color specification in the specified target format for full-intensity red while green and blue are zero. </p>
<p> The <code>XcmsQueryWhite</code> function returns the color specification in the specified target format for full-intensity red, green, and blue.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmscielabquerymaxc/">XcmsCIELabQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmscieluvquerymaxc/">XcmsCIELuvQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmstekhvcquerymaxc/">XcmsTekHVCQueryMaxC</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
