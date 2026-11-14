---
title: "xcmscieluvquerymaxl(3)"
name: "xcmscieluvquerymaxl"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmscieluvquerymaxl/"
description: "XcmsCIELuvQueryMaxC, XcmsCIELuvQueryMaxL, XcmsCIELuvQueryMaxLC, XcmsCIELuvQueryMinL – obtain the CIE L*u*v* coordinates"
---

<p>XcmsCIELuvQueryMaxC, XcmsCIELuvQueryMaxL, XcmsCIELuvQueryMaxLC, XcmsCIELuvQueryMinL &#8211; obtain the CIE L*u*v* coordinates </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XcmsCIELuvQueryMaxC(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue_angle</i>, XcmsFloat <i>L_star</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsCIELuvQueryMaxL(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue_angle</i>, XcmsFloat <i>chroma</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsCIELuvQueryMaxLC(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue_angle</i>, XcmsColor *<i>color_return</i>);</p>
<dd>Status XcmsCIELuvQueryMinL(XcmsCCC <i>ccc</i>, XcmsFloat <i>hue_angle</i>, XcmsFloat <i>chroma</i>, XcmsColor *<i>color_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC. Note that the CCC&#8217;s Client White Point and White Point Adjustment procedures are ignored.</p>
<dt><i>chroma</i></p>
<dd>Specifies the chroma at which to find maximum lightness (MaxL) or minimum lightness (MinL).</p>
<dt><i>color_return</i></p>
<dd>Returns the CIE L*u*v* coordinates of maximum chroma (MaxC and MaxLC), maximum lightness (MaxL), or minimum lightness (MinL) displayable by the screen for the given hue angle and lightness (MaxC), hue angle and chroma (MaxL and MinL), or hue angle (MaxLC). The white point associated with the returned color specification is the Screen White Point. The value returned in the pixel member is undefined.</p>
<dt><i>hue_angle</i></p>
<dd>Specifies the hue angle (in degrees) at which to find maximum chroma (MaxC and MaxLC), maximum lightness (MaxL), or minimum lightness (MinL).</p>
<dt><i>L_star</i></p>
<dd>Specifies the lightness (L*) at which to find maximum chroma (MaxC) or maximum lightness (MaxL).</dl>
<h2>Description</h2>
<p>The <code>XcmsCIELuvQueryMaxC</code> function, given a hue angle and lightness, finds the point of maximum chroma displayable by the screen. It returns this point in CIE L*u*v* coordinates. </p>
<p> The <code>XcmsCIELuvQueryMaxL</code> function, given a hue angle and chroma, finds the point in CIE L*u*v* color space of maximum lightness (L*) displayable by the screen. It returns this point in CIE L*u*v* coordinates. An <code>XcmsFailure</code> return value usually indicates that the given chroma is beyond maximum for the given hue angle. </p>
<p> The <code>XcmsCIELuvQueryMaxLC</code> function, given a hue angle, finds the point of maximum chroma displayable by the screen. It returns this point in CIE L*u*v* coordinates. </p>
<p> The <code>XcmsCIELuvQueryMinL</code> function, given a hue angle and chroma, finds the point of minimum lightness (L*) displayable by the screen. It returns this point in CIE L*u*v* coordinates. An <code>XcmsFailure</code> return value usually indicates that the given chroma is beyond maximum for the given hue angle.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmscielabquerymaxc/">XcmsCIELabQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmstekhvcquerymaxc/">XcmsTekHVCQueryMaxC</a>(3), <a href="/docs/linux/man/3-xcmsqueryblack/">XcmsQueryBlack</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
